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

"""
Convert OMG IDL 4.2 field-type strings to ROS 2 .msg-syntax field-type strings.

Generated message classes store field types as OMG IDL 4.2 strings in
``_fields_and_field_types`` (e.g. ``sequence<string<256>, 32>``). Some
tooling -- such as consumers of the MCAP ``ros2msg`` schema encoding --
expects ROS 2 ``.msg`` syntax instead (e.g. ``string<=256[<=32]``). This
module implements that conversion so it can be requested on demand via
``get_fields_and_field_types(syntax='ros')`` without changing the stored
IDL representation.
"""

import re

_BOUNDED_STRING_RE = re.compile(r'(w?string)<(\d+)>')
_BOUNDED_SEQUENCE_RE = re.compile(r'^sequence<(.+), (\d+)>$')
_UNBOUNDED_SEQUENCE_RE = re.compile(r'^sequence<(.+)>$')


def omg_to_ros_syntax(omg_type: str) -> str:
    """
    Convert a single OMG IDL 4.2 field-type string to ROS 2 .msg syntax.

    :param omg_type: A field-type string as stored in a generated message
        class's ``_fields_and_field_types`` dict, e.g.
        ``sequence<string<256>, 32>``.
    :return: The equivalent ROS 2 .msg-syntax string, e.g.
        ``string<=256[<=32]``.
    """
    match = _BOUNDED_SEQUENCE_RE.match(omg_type)
    if match:
        value_type, max_size = match.groups()
        return f'{omg_to_ros_syntax(value_type)}[<={max_size}]'

    match = _UNBOUNDED_SEQUENCE_RE.match(omg_type)
    if match:
        value_type = match.group(1)
        return f'{omg_to_ros_syntax(value_type)}[]'

    return _BOUNDED_STRING_RE.sub(r'\1<=\2', omg_type)
