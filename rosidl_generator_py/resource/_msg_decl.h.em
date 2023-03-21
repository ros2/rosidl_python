@# Included from rosidl_generator_py/resource/_idl_pkg_decl.h.em
@{
from rosidl_generator_py.generate_py_impl import SPECIAL_NESTED_BASIC_TYPES
from rosidl_parser.definition import AbstractNestedType
from rosidl_parser.definition import AbstractSequence
from rosidl_parser.definition import AbstractString
from rosidl_parser.definition import AbstractWString
from rosidl_parser.definition import Array
from rosidl_parser.definition import BasicType
from rosidl_parser.definition import EMPTY_STRUCTURE_REQUIRED_MEMBER_NAME
from rosidl_parser.definition import NamespacedType
from rosidl_pycommon import convert_camel_case_to_lower_case_underscore


def primitive_msg_type_to_c(type_):
    from rosidl_generator_c import BASIC_IDL_TYPES_TO_C
    from rosidl_parser.definition import AbstractString
    from rosidl_parser.definition import AbstractWString
    from rosidl_parser.definition import BasicType
    if isinstance(type_, AbstractString):
        return 'rosidl_runtime_c__String'
    if isinstance(type_, AbstractWString):
        return 'rosidl_runtime_c__U16String'
    assert isinstance(type_, BasicType)
    return BASIC_IDL_TYPES_TO_C[type_.typename]


header_files = [
    'Python.h',
    'stdbool.h',
    'structmember.h'
]
}@
@[for header_file in header_files]@
@{
repeated_header_file = header_file in include_directives
}@
@[    if repeated_header_file]@
// already included above
// @
@[    else]@
@{include_directives.add(header_file)}@
@[    end if]@
@[    if '/' not in header_file]@
#include <@(header_file)>
@[    else]@
#include "@(header_file)"
@[    end if]@
@[end for]@


typedef struct
{
  PyObject_HEAD
  /* Type-specific fields go here. */
@[for member in message.structure.members]@
@[  if len(message.structure.members) == 1 and member.name == EMPTY_STRUCTURE_REQUIRED_MEMBER_NAME]@
@[    continue]@
@[  end if]@
@[  if isinstance(member.type, BasicType)]@
@[    if member.type.typename == 'float']@
  double _@(member.name);
@[    else]@
  @(primitive_msg_type_to_c(member.type)) _@(member.name);
@[    end if]@
@[  else isinstance(member.type, AbstractGenericString)]@
  PyObject * _@(member.name);
@[  end if]@
@[end for]@
} @(message.structure.namespaced_type.name)Base;

// Import-support constants for @(message.structure.namespaced_type.name)Base type
@{
locally_declared = set()
}@
@[for member in message.structure.members]@
@[  if isinstance(member.type, AbstractNestedType) and isinstance(member.type.value_type, BasicType) and member.type.value_type.typename in SPECIAL_NESTED_BASIC_TYPES]@
@[    if isinstance(member.type, Array)]@
@[      if 'numpy.ndarray' not in required_py_modules]@
#define NUMPY__NDARRAY__IMPORT_INDEX @(len(required_py_modules))
@{        required_py_modules.append('numpy.ndarray')}@
@[      elif 'numpy.ndarray' not in locally_declared]@
//      NUMPY__NDARRAY__IMPORT_INDEX defined above
@[      end if]@
@{      locally_declared.add('numpy.ndarray')}@
@{      dtype = SPECIAL_NESTED_BASIC_TYPES[member.type.value_type.typename]['dtype']}@
@{      const_name = dtype.replace('.', '__').upper()}@
@[      if dtype not in required_py_modules]@
#define @(const_name)__IMPORT_INDEX @(len(required_py_modules))
@{          required_py_modules.append(dtype)}@
@[      elif dtype not in locally_declared]@
//      @(const_name)__IMPORT_INDEX defined above
@[      end if]@
@{      locally_declared.add(dtype)}@
@[    elif isinstance(member.type, AbstractSequence)]@
@[      if 'array.array' not in required_py_modules]@
#define ARRAY__ARRAY__IMPORT_INDEX @(len(required_py_modules))
@{        required_py_modules.append('array.array')}@
@[      elif 'array.array' not in locally_declared]@
//      ARRAY__ARRAY__IMPORT_INDEX defined above
@[      end if]@
@{      locally_declared.add('array.array')}@
@[    end if]@
@[  end if]@
@[end for]@
@
@{
type_ = message.structure.namespaced_type
const_name = '__'.join(type_.namespaces + [convert_camel_case_to_lower_case_underscore(type_.name)]).upper()
# const_name = '__'.join(type_.namespaced_name()).upper()
assert const_name not in required_py_modules, "Const name collision"
const_value = len(required_py_modules)
required_py_modules.append(const_name)
}@
#define @(const_name)__IMPORT_INDEX @(const_value)

