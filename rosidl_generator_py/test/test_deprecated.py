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

import warnings

import pytest

from rosidl_generator_py.msg import TestDeprecated


def test_deprecated_field_getter_emits_warning():
    """Test that accessing a deprecated field emits a DeprecationWarning."""
    msg = TestDeprecated()

    with pytest.warns(DeprecationWarning, match='Use distance_meters instead'):
        _ = msg.distance_cm


def test_deprecated_field_setter_emits_warning():
    """Test that setting a deprecated field emits a DeprecationWarning."""
    msg = TestDeprecated()

    with pytest.warns(DeprecationWarning, match='Use distance_meters instead'):
        msg.distance_cm = 42


def test_non_deprecated_field_no_warning():
    """Test that accessing non-deprecated fields does not emit a warning."""
    msg = TestDeprecated()

    with warnings.catch_warnings():
        warnings.simplefilter('error', DeprecationWarning)
        # Should not raise - distance_meters is not deprecated
        _ = msg.distance_meters


def test_deprecated_field_values():
    """Test that deprecated fields still work correctly for values."""
    msg = TestDeprecated()

    # Suppress the deprecation warnings for value testing
    with warnings.catch_warnings():
        warnings.simplefilter('ignore', DeprecationWarning)

        # Default value
        assert msg.distance_cm == 0
        assert msg.distance_meters == 0.0

        # Set and get
        msg.distance_cm = 10
        msg.distance_meters = 1.5
        assert msg.distance_cm == 10
        assert msg.distance_meters == 1.5
