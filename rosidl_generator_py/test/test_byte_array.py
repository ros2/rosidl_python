# Copyright 2022 Open Source Robotics Foundation, Inc.
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
from rosidl_generator_py.msg import ByteArray


def test_msg_bytearray():
    msg = ByteArray()

    # types
    assert isinstance(msg.data, list)

    # default values
    assert [] == msg.data

    # set values
    l1 = [1, 2, 3]
    msg.data = l1
    # get values
    assert bytes(l1) == msg.data

    # set values
    l2 = {1, 2, 3}
    msg.data = l2
    # get values
    assert bytes(l2) == msg.data

    from collections import UserList
    # set values
    l3 = UserList(l1)
    msg.data = l3
    # get values
    assert bytes(l3) == msg.data

    # set values
    l4 = bytes('123', 'utf-8')
    msg.data = l4
    # get values
    assert l4 == msg.data

    # set values
    l5 = [b'1', b'2', b'3']
    msg.data = l5
    # get values
    assert l5 == msg.data


def test_msg_bytearray_exception():
    msg = ByteArray()

    with pytest.raises(ValueError):
        l1 = [1, 2, 256]
        msg.data = l1

    with pytest.raises(AssertionError):
        l2 = ['a', 'b']
        msg.data = l2

    with pytest.raises(AssertionError):
        l3 = [1, b'2', b'3']
        msg.data = l3
