# Copyright 2019 Open Source Robotics Foundation, Inc.
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

import copy

import pytest

from rosidl_runtime_py import set_message_fields
from test_msgs import message_fixtures


def test_set_message_fields_none():
    # Smoke-test on a bunch of messages
    msgs = []
    msgs.extend(message_fixtures.get_msg_arrays())
    msgs.extend(message_fixtures.get_msg_basic_types())
    msgs.extend(message_fixtures.get_msg_bounded_sequences())
    msgs.extend(message_fixtures.get_msg_builtins())
    msgs.extend(message_fixtures.get_msg_constants())
    msgs.extend(message_fixtures.get_msg_defaults())
    msgs.extend(message_fixtures.get_msg_empty())
    msgs.extend(message_fixtures.get_msg_multi_nested())
    msgs.extend(message_fixtures.get_msg_nested())
    msgs.extend(message_fixtures.get_msg_strings())
    msgs.extend(message_fixtures.get_msg_unbounded_sequences())

    for m in msgs:
        original_m = copy.copy(m)
        set_message_fields(m, {})
        # Assert message is not modified when setting no fields
        assert original_m == m


def test_set_message_fields_partial():
    original_msg = message_fixtures.get_msg_basic_types()[0]
    original_msg.bool_value = False
    original_msg.char_value = 3
    original_msg.int32_value = 42

    modified_msg = copy.copy(original_msg)
    values = {}
    values['bool_value'] = True
    values['char_value'] = 1
    values['int32_value'] = 24
    set_message_fields(modified_msg, values)

    for _attr in original_msg.__slots__:
        # Remove underscore prefix
        attr = _attr[1:]
        if attr in values:
            assert getattr(modified_msg, attr) == values[attr]
        else:
            assert getattr(modified_msg, attr) == getattr(original_msg, attr)


def test_set_message_fields_full():
    msg_list = message_fixtures.get_msg_basic_types()
    msg0 = msg_list[0]
    msg1 = msg_list[1]

    # Set msg0 values to the values of msg1
    values = {}
    for _attr in msg1.__slots__:
        # Remove underscore prefix
        attr = _attr[1:]
        values[attr] = getattr(msg1, attr)
    set_message_fields(msg0, values)

    assert msg0 == msg1


def test_set_message_fields_invalid():
    msg = message_fixtures.get_msg_basic_types()[0]
    invalid_field = {}
    invalid_field['test_invalid_field'] = 42
    with pytest.raises(AttributeError):
        set_message_fields(msg, invalid_field)

    invalid_type = {}
    invalid_type['int32_value'] = 'this is not an integer'
    with pytest.raises(ValueError):
        set_message_fields(msg, invalid_type)


def test_set_nested_namespaced_fields():
    msg = message_fixtures.get_msg_dynamic_array_nested()[0]
    test_values = {
        'primitive_values': [
            {'string_value': 'foo', 'int8_value': 42},
            {'string_value': 'bar', 'int8_value': 11}
        ]
    }
    set_message_fields(msg, test_values)
    assert msg.primitive_values[0].string_value == 'foo'
    assert msg.primitive_values[0].int8_value == 42
    assert msg.primitive_values[0].uint8_value == 0
    assert msg.primitive_values[1].string_value == 'bar'
    assert msg.primitive_values[1].int8_value == 11
    assert msg.primitive_values[1].uint8_value == 0

    static_array_msg = message_fixtures.get_msg_static_array_nested()[0]
    test_values = {
        'primitive_values': [
            {'string_value': 'foo', 'int8_value': 42},
            {'string_value': 'bar', 'int8_value': 11},
            {'string_value': 'baz', 'int8_value': 22},
            {'string_value': 'foobar', 'int8_value': 33}
        ]
    }
    set_message_fields(static_array_msg, test_values)
    assert static_array_msg.primitive_values[0].string_value == 'foo'
    assert static_array_msg.primitive_values[0].int8_value == 42
    assert static_array_msg.primitive_values[0].uint8_value == 0
    assert static_array_msg.primitive_values[1].string_value == 'bar'
    assert static_array_msg.primitive_values[1].int8_value == 11
    assert static_array_msg.primitive_values[1].uint8_value == 0
    assert static_array_msg.primitive_values[2].string_value == 'baz'
    assert static_array_msg.primitive_values[2].int8_value == 22
    assert static_array_msg.primitive_values[2].uint8_value == 0
    assert static_array_msg.primitive_values[3].string_value == 'foobar'
    assert static_array_msg.primitive_values[3].int8_value == 33
    assert static_array_msg.primitive_values[3].uint8_value == 0
