# Copyright 2017-2019 Open Source Robotics Foundation, Inc.
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

from typing import Any
from typing import Dict

from rosidl_runtime_py.import_message import import_message_type


def set_message_fields(msg: Any, values: Dict[str, str]) -> None:
    """
    Set the fields of a ROS message.

    :param msg: The ROS message to populate.
    :param values: The values to set in the ROS message. The keys of the dictionary represent
        fields of the message.
    :raises AttributeError: If the message does not have a field provided in the input dictionary.
    :raises ValueError: If a message value does not match its field type.
    """
    for field_name, field_value in values.items():
        field_type = type(getattr(msg, field_name))
        try:
            value = field_type(field_value)
        except TypeError:
            value = field_type()
            set_message_fields(value, field_value)
        f_type = msg.get_fields_and_field_types()[field_name]
        # Check if field is an array of ROS message types
        if f_type.find('/') != -1:
            if isinstance(field_type(), list):
                # strip the 'sequence<' prefix if it is a sequence
                if f_type.startswith('sequence'):
                    f_type = f_type[len('sequence') + 1:]
                f_type = f_type[:f_type.rfind('[')]
                field_elem_type = import_message_type('', f_type)
                for n in range(len(value)):
                    submsg = field_elem_type()
                    set_message_fields(submsg, value[n])
                    value[n] = submsg
        setattr(msg, field_name, value)
