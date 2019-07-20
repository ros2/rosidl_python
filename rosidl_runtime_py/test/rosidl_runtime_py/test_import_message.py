# Copyright 2019 Mikael Arguedas
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

import pytest

from rosidl_parser.definition import NamespacedType
from rosidl_parser.definition import UnboundedSequence

from rosidl_runtime_py.import_message import import_message_from_namespaced_type

from test_msgs.msg import Empty


def test_import_namespaced_type():
    fixture_namespaced_type = NamespacedType(['test_msgs', 'msg'], 'Empty')
    imported_message = import_message_from_namespaced_type(fixture_namespaced_type)
    assert type(imported_message) == type(Empty)
    not_namespaced_type = UnboundedSequence(fixture_namespaced_type)
    assert not isinstance(not_namespaced_type, NamespacedType)
    with pytest.raises(AttributeError):
        import_message_from_namespaced_type(not_namespaced_type)
    imported_message2 = import_message_from_namespaced_type(
        not_namespaced_type.value_type)
    assert type(imported_message2) == type(Empty)
