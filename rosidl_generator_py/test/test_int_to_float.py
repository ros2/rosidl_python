# Copyright 2021 Open Source Robotics Foundation, Inc.
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

from rosidl_generator_py.msg import Float


def test_int_to_float():
    msg1 = Float(check_types=True, float_value=float(1))

    assert isinstance(msg1.float_value, float)
    assert 1 == msg1.float_value

    msg2 = Float(check_types=True, float_value=int(1))
    assert isinstance(msg2.float_value, float)
    assert 1 == msg2.float_value
