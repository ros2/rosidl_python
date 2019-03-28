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

class SetFieldError(Exception):

    def __init__(self, field_name, exception):
        super(SetFieldError, self).__init__()
        self.field_name = field_name
        self.exception = exception


def set_msg_fields(msg, values):
    for field_name, field_value in values.items():
        field_type = type(getattr(msg, field_name))
        try:
            value = field_type(field_value)
        except TypeError:
            value = field_type()
            try:
                set_msg_fields(value, field_value)
            except SetFieldError as e:
                raise SetFieldError(
                    '{field_name}.{e.field_name}'.format_map(locals()),
                    e.exception)
        except ValueError as e:
            raise SetFieldError(field_name, e)
        try:
            setattr(msg, field_name, value)
        except Exception as e:
            raise SetFieldError(field_name, e)
