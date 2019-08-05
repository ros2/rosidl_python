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

from typing import Text

from rosidl_parser.definition import NamespacedType


def __full_type_to_namespaced_type(path: Text, default_namespace):
    namespace = path.split(sep='/')
    name = namespace[-1]
    namespace = namespace[0:-1]
    if len(namespace) == 1:
        namespace.append(default_namespace)
    return NamespacedType(namespace, name)


def full_action_type_to_namespaced_type(path: Text):
    """Create a `NamespacedType` object from the full name of an action."""
    return __full_type_to_namespaced_type(path, 'action')


def full_msg_type_to_namespaced_type(path: Text):
    """Create a `NamespacedType` object from the full name of a message."""
    return __full_type_to_namespaced_type(path, 'msg')


def full_srv_type_to_namespaced_type(path: Text):
    """Create a `NamespacedType` object from the full name of a service."""
    return __full_type_to_namespaced_type(path, 'srv')


def is_action(action):
    """Return `True` if `action` is an action."""
    return hasattr(action, 'Goal')


def is_srv(srv):
    """Return `True` if `srv` is a service."""
    return hasattr(srv, 'Request')


def is_msg(msg):
    """Return `True` if `msg` is a message."""
    return hasattr(msg, 'get_fields_and_field_types')
