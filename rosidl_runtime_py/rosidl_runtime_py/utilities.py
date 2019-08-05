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
from rosidl_runtime_py.import_message import import_message_from_namespaced_type


def get_interface(path: Text):
    """Get an interface from its full name."""
    return import_message_from_namespaced_type(get_namespaced_type(path))


def get_message(path: Text):
    """Get a message from its full name."""
    interface = import_message_from_namespaced_type(get_message_namespaced_type(path))
    if not is_message(interface):
        raise RuntimeError('Expected the full name of a message')
    return interface


def get_service(path: Text):
    """Get a service from its full name."""
    interface = import_message_from_namespaced_type(get_service_namespaced_type(path))
    if not is_service(interface):
        raise RuntimeError('Expected the full name of a service')
    return interface


def get_action(path: Text):
    """Get a message from its full name."""
    interface = import_message_from_namespaced_type(get_action_namespaced_type(path))
    if not is_action(interface):
        raise RuntimeError('Expected the full name of an action')
    return interface


def get_namespaced_type(path: Text):
    """Create a `NamespacedType` object from the full name of an interface."""
    return _get_namespaced_type(path)


def get_message_namespaced_type(path: Text):
    """Create a `NamespacedType` object from the full name of a message."""
    return _get_namespaced_type(path, 'msg')


def get_service_namespaced_type(path: Text):
    """Create a `NamespacedType` object from the full name of a service."""
    return _get_namespaced_type(path, 'srv')


def get_action_namespaced_type(path: Text):
    """Create a `NamespacedType` object from the full name of an action."""
    return _get_namespaced_type(path, 'action')


def is_message(interface):
    """Return `True` if `interface` is a message."""
    return hasattr(interface, 'SLOT_TYPES')


def is_service(interface):
    """Return `True` if `interface` is a service."""
    return hasattr(interface, 'Request') and hasattr(interface, 'Response')


def is_action(interface):
    """Return `True` if `interface` is an action."""
    return (
        hasattr(interface, 'Goal') and
        hasattr(interface, 'Result') and
        hasattr(interface, 'Feedback')
    )


def _get_namespaced_type(path: Text, default_namespace=None):
    namespace = path.split(sep='/')
    name = namespace[-1]
    namespace = namespace[0:-1]
    if len(namespace) == 1 and default_namespace is not None:
        namespace.append(default_namespace)
    return NamespacedType(namespace, name)
