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

import pytest

from rosidl_runtime_py import utilities
from rosidl_runtime_py.import_message import import_message_from_namespaced_type

import test_msgs.action
import test_msgs.msg
import test_msgs.srv


class TestConfig:

    def __init__(self, *, path, object_type, to_namespaced_type_method, is_method):
        self.path = path
        self.object_type = object_type
        self.to_namespaced_type_method = to_namespaced_type_method
        self.is_method = is_method


@pytest.mark.parametrize('config', (
    TestConfig(
        path='test_msgs/msg/Empty',
        object_type=test_msgs.msg.Empty,
        to_namespaced_type_method=utilities.full_msg_type_to_namespaced_type,
        is_method=utilities.is_msg
    ),
    TestConfig(
        path='test_msgs/Empty',
        object_type=test_msgs.msg.Empty,
        to_namespaced_type_method=utilities.full_msg_type_to_namespaced_type,
        is_method=utilities.is_msg
    ),
    TestConfig(
        path='test_msgs/srv/Empty',
        object_type=test_msgs.srv.Empty,
        to_namespaced_type_method=utilities.full_srv_type_to_namespaced_type,
        is_method=utilities.is_srv
    ),
    TestConfig(
        path='test_msgs/Empty',
        object_type=test_msgs.srv.Empty,
        to_namespaced_type_method=utilities.full_srv_type_to_namespaced_type,
        is_method=utilities.is_srv
    ),
    TestConfig(
        path='test_msgs/action/Fibonacci',
        object_type=test_msgs.action.Fibonacci,
        to_namespaced_type_method=utilities.full_action_type_to_namespaced_type,
        is_method=utilities.is_action
    ),
    TestConfig(
        path='test_msgs/Fibonacci',
        object_type=test_msgs.action.Fibonacci,
        to_namespaced_type_method=utilities.full_action_type_to_namespaced_type,
        is_method=utilities.is_action
    ),
))
def test_utilities(config):
    message = import_message_from_namespaced_type(config.to_namespaced_type_method(config.path))
    assert message is config.object_type
    assert config.is_method(message)
