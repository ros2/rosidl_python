# Copyright 2016-2019 Open Source Robotics Foundation, Inc.
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


from rosidl_generator_py.generate_py_impl import floating_point_to_py


def test_floating_point_to_py():

    # normal floating point values
    assert floating_point_to_py("1.0") == "1.0"
    assert floating_point_to_py("-42.0") == "-42.0"

    # NaN's
    assert floating_point_to_py("NaN") == "math.nan"
    assert floating_point_to_py("nan") == "math.nan"
    assert floating_point_to_py("NAN") == "math.nan"
