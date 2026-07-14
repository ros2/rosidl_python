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

import pytest

from rosidl_generator_py.field_type_syntax import omg_to_ros_syntax


@pytest.mark.parametrize(
    'omg_type,expected_ros_type',
    [
        ('string<5>', 'string<=5'),
        ('wstring<5>', 'wstring<=5'),
        ('string', 'string'),
        ('char', 'char'),
        ('sequence<char>', 'char[]'),
        ('sequence<string>', 'string[]'),
        ('sequence<string, 10>', 'string[<=10]'),
        ('sequence<string<5>>', 'string<=5[]'),
        ('sequence<string<5>, 10>', 'string<=5[<=10]'),
    ],
)
def test_omg_to_ros_syntax(omg_type: str, expected_ros_type: str) -> None:
    assert omg_to_ros_syntax(omg_type) == expected_ros_type
