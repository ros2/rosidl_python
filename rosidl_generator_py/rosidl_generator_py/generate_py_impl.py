# Copyright 2014-2018 Open Source Robotics Foundation, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from ast import literal_eval
import os
import pathlib

from rosidl_cmake import convert_camel_case_to_lower_case_underscore
from rosidl_cmake import expand_template
from rosidl_cmake import generate_files
from rosidl_cmake import get_newest_modification_time
from rosidl_cmake import read_generator_arguments
from rosidl_parser.definition import BasicType
from rosidl_parser.definition import IdlContent
from rosidl_parser.definition import IdlLocator
from rosidl_parser.definition import NamespacedType
from rosidl_parser.definition import NestedType
from rosidl_parser.definition import String
from rosidl_parser.parser import parse_idl_file


def generate_py(generator_arguments_file, typesupport_impls):
    mapping = {
        '_idl.py.em': '_%s.py',
        '_idl_support.c.em': '_%s_s.c',
    }
    generate_files(generator_arguments_file, mapping)

    args = read_generator_arguments(generator_arguments_file)
    package_name = args['package_name']

    # expand init modules for each directory
    modules = {}
    idl_content = IdlContent()
    for idl_tuple in args.get('idl_tuples', []):
        idl_parts = idl_tuple.rsplit(':', 1)
        assert len(idl_parts) == 2

        idl_rel_path = pathlib.Path(idl_parts[1])
        idl_stems = modules.setdefault(str(idl_rel_path.parent), set())
        idl_stems.add(idl_rel_path.stem)

        locator = IdlLocator(*idl_parts)
        idl_file = parse_idl_file(locator)
        idl_content.elements += idl_file.content.elements

    for subfolder in modules.keys():
        with open(os.path.join(args['output_dir'], subfolder, '__init__.py'), 'w') as f:
            for idl_stem in sorted(modules[subfolder]):
                module_name = '_' + \
                    convert_camel_case_to_lower_case_underscore(idl_stem)
                f.write(
                    'from {package_name}.{subfolder}.{module_name} import '
                    '{idl_stem}  # noqa: F401\n'.format_map(locals()))

    # expand templates per available typesupport implementation
    template_dir = args['template_dir']
    type_support_impl_by_filename = {
        '_%s_s.ep.{0}.c'.format(impl): impl for impl in typesupport_impls
    }
    mapping_msg_pkg_extension = {
        os.path.join(template_dir, '_idl_pkg_typesupport_entry_point.c.em'):
        type_support_impl_by_filename.keys(),
    }

    for template_file in mapping_msg_pkg_extension.keys():
        assert os.path.exists(template_file), 'Could not find template: ' + template_file

    latest_target_timestamp = get_newest_modification_time(args['target_dependencies'])

    for template_file, generated_filenames in mapping_msg_pkg_extension.items():
        for generated_filename in generated_filenames:
            package_name = args['package_name']
            if action_specs:
                package_name += '_action'
            data = {
                'package_name': args['package_name'],
                'content': idl_content,
                'typesupport_impl': type_support_impl_by_filename.get(generated_filename, ''),
            }
            generated_file = os.path.join(
                args['output_dir'], generated_filename % package_name
            )
            expand_template(
                template_file, data, generated_file,
                minimum_timestamp=latest_target_timestamp)

    return 0


def value_to_py(type_, value, array_as_tuple=False):
    assert value is not None

    if not isinstance(type_, NestedType):
        return primitive_value_to_py(type_, value)

    py_values = []
    for single_value in literal_eval(value):
        py_value = primitive_value_to_py(type_.basetype, single_value)
        py_values.append(py_value)
    if array_as_tuple:
        return '(%s)' % ', '.join(py_values)
    else:
        return '[%s]' % ', '.join(py_values)


def primitive_value_to_py(type_, value):
    assert value is not None

    if isinstance(type_, String):
        return "'%s'" % escape_string(value)

    assert isinstance(type_, BasicType)

    if type_.type == 'boolean':
        return 'True' if value else 'False'

    if type_.type in (
        'int8', 'uint8',
        'int16', 'uint16',
        'int32', 'uint32',
        'int64', 'uint64',
    ):
        return str(value)

    if type_.type == 'char':
        return repr('%c' % value)

    if type_.type == 'octet':
        return repr(bytes([value]))

    if type_.type in ('float', 'double'):
        return '%s' % value

    assert False, "unknown primitive type '%s'" % type_.type


def constant_value_to_py(type_, value):
    assert value is not None

    if isinstance(type_, BasicType):
        if type_.type == 'bool':
            return 'True' if value else 'False'

        if type_.type in (
            'int8', 'uint8',
            'int16', 'uint16',
            'int32', 'uint32',
            'int64', 'uint64',
        ):
            return str(value)

        if type_.type == 'char':
            return repr('%c' % value)

        if type_.type == 'octet':
            return repr(bytes([value]))

        if type_.type in ('float', 'double'):
            return '%s' % value

    if isinstance(type_, String):
        return "'%s'" % escape_string(value)

    assert False, "unknown constant type '%s'" % type_


def escape_string(s):
    s = s.replace('\\', '\\\\')
    s = s.replace("'", "\\'")
    return s


def get_python_type(type_):
    if isinstance(type_, NamespacedType):
        return type_.name

    if isinstance(type_, String):
        return 'str'

    if isinstance(type_, NestedType):
        if isinstance(type_.basetype, BasicType) and type_.basetype.type == 'octet':
            return 'bytes'

        if isinstance(type_.basetype, BasicType) and type_.basetype.type in ('char', 'wchar'):
            return 'str'

    if isinstance(type_, BasicType) and type_.type == 'boolean':
        return 'bool'

    if isinstance(type_, BasicType) and type_.type == 'octet':
        return 'bytes'

    if isinstance(type_, BasicType) and type_.type in (
        'int8', 'uint8',
        'int16', 'uint16',
        'int32', 'uint32',
        'int64', 'uint64',
    ):
        return 'int'

    if isinstance(type_, BasicType) and type_.type in (
        'float', 'double',
    ):
        return 'float'

    if isinstance(type_, BasicType) and type_.type in (
        'char', 'wchar',
    ):
        return 'str'

    assert False, "unknown type '%s'" % type_
