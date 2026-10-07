# Copyright 2026 Open Source Robotics Foundation, Inc.
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

import contextlib
import pathlib
import sys
from types import ModuleType

from pytest import CaptureFixture
from rosidl_parser.definition import Array
from rosidl_parser.definition import IdlContent
from rosidl_parser.definition import Member
from rosidl_parser.definition import Message
from rosidl_parser.definition import NamespacedType
from rosidl_parser.definition import Structure
from rosidl_parser.definition import UnboundedSequence
from rosidl_pycommon import convert_camel_case_to_lower_case_underscore
from rosidl_pycommon import expand_template

PACKAGE_NAME = 'rosidl_generator_py'
RESOURCE_DIR = pathlib.Path(__file__).parents[1] / 'resource'


try:
    import rpyutils  # noqa: F401
except ImportError:
    rpyutils = ModuleType('rpyutils')

    def _add_dll_directories_from_env(
        _: str,
    ) -> contextlib.AbstractContextManager[None]:
        return contextlib.nullcontext()

    rpyutils.add_dll_directories_from_env = _add_dll_directories_from_env
    sys.modules['rpyutils'] = rpyutils


def _render_message(
    tmp_path: pathlib.Path,
    capsys: CaptureFixture[str],
    message_name: str,
    members: list[Member],
) -> str:
    content = IdlContent()
    content.elements.append(Message(
        Structure(NamespacedType([PACKAGE_NAME, 'msg'], message_name), members)
    ))

    output_filename = (
        f'_{convert_camel_case_to_lower_case_underscore(message_name)}.py'
    )
    output_path = tmp_path / output_filename
    with capsys.disabled():
        expand_template(
            str(RESOURCE_DIR / '_idl.py.em'),
            {
                'package_name': PACKAGE_NAME,
                'interface_path': pathlib.Path('msg') / f'{message_name}.msg',
                'content': content,
            },
            str(output_path),
        )
    return output_path.read_text(encoding='utf-8')


def test_namespaced_field_imports_are_absolute(
    tmp_path: pathlib.Path,
    capsys: CaptureFixture[str],
) -> None:
    duration_type = NamespacedType(['builtin_interfaces', 'msg'], 'Duration')
    source = _render_message(
        tmp_path,
        capsys,
        'Duration',
        [Member(duration_type, 'data')],
    )

    assert 'from builtin_interfaces.msg import Duration' not in source
    assert 'import builtin_interfaces.msg' in source
    assert (
        'if builtin_interfaces.msg.Duration._TYPE_SUPPORT is None:'
    ) in source
    assert (
        'self.data = data if data is not None else '
        'builtin_interfaces.msg.Duration()'
    ) in source
    assert 'isinstance(value, builtin_interfaces.msg.Duration)' in source


def test_namespaced_array_and_sequence_imports_are_absolute(
    tmp_path: pathlib.Path,
    capsys: CaptureFixture[str],
) -> None:
    duration_type = NamespacedType(['builtin_interfaces', 'msg'], 'Duration')
    source = _render_message(
        tmp_path,
        capsys,
        'DurationArraySequence',
        [
            Member(Array(duration_type, 2), 'array_data'),
            Member(UnboundedSequence(duration_type), 'sequence_data'),
        ],
    )

    assert 'from builtin_interfaces.msg import Duration' not in source
    assert 'import builtin_interfaces.msg' in source
    assert (
        '[builtin_interfaces.msg.Duration() for x in range(2)]'
    ) in source
    assert (
        'all(isinstance(v, builtin_interfaces.msg.Duration) for v in value)'
    ) in source
