# Copyright 2026 Cellumation GmbH
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
Round trip tests for the generated convert_from_py / convert_to_py functions.

convert_to_py allocates the Python message with tp_alloc and writes straight to the
``_field`` slots instead of calling ``__init__`` and going through the property
setters. That makes it responsible for producing every slot, and for producing the
exact container types (``list`` / ``array.array`` / ``numpy.ndarray``) that
``__init__`` used to create. These tests exercise the full matrix of field kinds
against those two properties.

The conversion functions are reached the same way rclpy reaches them, by unwrapping
the PyCapsules on the message metaclass. ``PYFUNCTYPE`` is required rather than
``CFUNCTYPE`` because the latter releases the GIL, which crashes immediately.
"""

import array
import ctypes
import importlib
import os
from typing import Any, List, Optional

import numpy
import pytest

from rosidl_generator_py.msg import Arrays
from rosidl_generator_py.msg import BasicTypes
from rosidl_generator_py.msg import BoundedPlainSequences
from rosidl_generator_py.msg import BoundedSequences
from rosidl_generator_py.msg import BuiltinTypeSequencesIdl
from rosidl_generator_py.msg import Constants
from rosidl_generator_py.msg import Defaults
from rosidl_generator_py.msg import Empty
from rosidl_generator_py.msg import MultiNested
from rosidl_generator_py.msg import Nested
from rosidl_generator_py.msg import StringArrays
from rosidl_generator_py.msg import Strings
from rosidl_generator_py.msg import UnboundedSequences
from rosidl_generator_py.msg import WStrings

from rosidl_parser.definition import AbstractSequence
from rosidl_parser.definition import AbstractString
from rosidl_parser.definition import AbstractWString
from rosidl_parser.definition import Array
from rosidl_parser.definition import BasicType
from rosidl_parser.definition import BoundedSequence
from rosidl_parser.definition import NamespacedType

MESSAGE_TYPES = [
    Arrays,
    BasicTypes,
    BoundedPlainSequences,
    BoundedSequences,
    BuiltinTypeSequencesIdl,
    Constants,
    Defaults,
    Empty,
    MultiNested,
    Nested,
    StringArrays,
    Strings,
    UnboundedSequences,
    WStrings,
]

# Kept small so that it fits the tightest bound used by the test interfaces.
SEQUENCE_LENGTH = 2

# Basic types that are stored in an array.array when in a sequence and in a
# numpy.ndarray when in a fixed size array, mapped to the typecode and dtype the
# generated code has to produce.
#
# Spelled out here rather than imported from generate_py_impl on purpose. It makes
# the test an independent oracle for the container types instead of comparing the
# generator against itself, and the generated test interfaces shadow the generator
# package on sys.path anyway.
SPECIAL_NESTED_BASIC_TYPES = {
    'float': ('f', numpy.float32),
    'double': ('d', numpy.float64),
    'int8': ('b', numpy.int8),
    'uint8': ('B', numpy.uint8),
    'int16': ('h', numpy.int16),
    'uint16': ('H', numpy.uint16),
    'int32': ('i', numpy.int32),
    'uint32': ('I', numpy.uint32),
    'int64': ('q', numpy.int64),
    'uint64': ('Q', numpy.uint64),
}

# What __init__ would store in the _check_fields slot.
EXPECTED_CHECK_FIELDS = os.getenv('ROS_PYTHON_CHECK_FIELDS', default='') == '1'

_PyCapsule_GetPointer = ctypes.pythonapi.PyCapsule_GetPointer
_PyCapsule_GetPointer.restype = ctypes.c_void_p
_PyCapsule_GetPointer.argtypes = [ctypes.py_object, ctypes.c_char_p]


def _capsule(message_type: type, function: str) -> Any:
    """
    Look up one of the conversion capsules of a message type.

    ``__import_type_support__()`` cannot be used here. It runs
    ``from rosidl_generator_py import import_type_support``, but the test interfaces
    of this package are generated into a Python package that is *also* called
    ``rosidl_generator_py`` and shadows the generator package on ``sys.path``. The
    generated helper swallows the resulting ImportError and leaves the capsules
    unset, so the typesupport extension module is imported directly instead, the
    same way ``rosidl_generator_py.import_type_support`` would.
    """
    package, *middle, module = message_type.__module__.split('.')
    suffix = '__'.join(middle + [module[1:]])
    typesupport = importlib.import_module(
        '.{}_s__rosidl_typesupport_c'.format(package), package=package)
    return getattr(typesupport, '{}_msg__{}'.format(function, suffix))


def _round_trip(message: Any) -> Any:
    """Send a message through convert_from_py and convert_to_py and back."""
    message_type = type(message)

    def pointer(name: str) -> int:
        return _PyCapsule_GetPointer(_capsule(message_type, name), None)

    # PYFUNCTYPE keeps the GIL held, which the conversion functions require.
    create = ctypes.PYFUNCTYPE(ctypes.c_void_p)(pointer('create_ros_message'))
    destroy = ctypes.PYFUNCTYPE(None, ctypes.c_void_p)(pointer('destroy_ros_message'))
    convert_from_py = ctypes.PYFUNCTYPE(
        ctypes.c_bool, ctypes.py_object, ctypes.c_void_p)(pointer('convert_from_py'))
    convert_to_py = ctypes.PYFUNCTYPE(
        ctypes.py_object, ctypes.c_void_p)(pointer('convert_to_py'))

    ros_message = create()
    assert ros_message, 'failed to allocate the ROS message'
    try:
        assert convert_from_py(message, ros_message), 'convert_from_py failed'
        return convert_to_py(ros_message)
    finally:
        destroy(ros_message)


def _scalar_value(type_: Any, seed: int) -> Any:
    """Build a value for a single element, small enough to fit every basic type."""
    if isinstance(type_, NamespacedType):
        module = __import__('.'.join(type_.namespaces), fromlist=[type_.name])
        return _populate(getattr(module, type_.name)())
    if isinstance(type_, (AbstractString, AbstractWString)):
        # Short enough for the bounded string fields of the test interfaces.
        return 'v%d' % seed
    assert isinstance(type_, BasicType), type_
    if type_.typename == 'boolean':
        return bool(seed % 2)
    if type_.typename == 'octet':
        return bytes([seed])
    if type_.typename == 'char':
        # Only reachable from a .idl file. 'char' in a .msg interface is mapped to
        # uint8 before it reaches the generator, but a real IDL char is a str.
        return chr(seed)
    if type_.typename in ('float', 'double'):
        # Exactly representable as float32, so float32 fields survive the round trip.
        return seed + 0.5
    # Fits in int8, the narrowest signed integer type.
    return seed


def _field_value(slot_type: Any, seed: int) -> Any:
    """Build a field value using the same container type that __init__ would."""
    if not isinstance(slot_type, (Array, AbstractSequence)):
        return _scalar_value(slot_type, seed)

    if isinstance(slot_type, Array):
        length = slot_type.size
    elif isinstance(slot_type, BoundedSequence):
        length = min(SEQUENCE_LENGTH, slot_type.maximum_size)
    else:
        length = SEQUENCE_LENGTH
    value_type = slot_type.value_type
    values = [_scalar_value(value_type, seed + i) for i in range(length)]

    if isinstance(value_type, BasicType) and \
            value_type.typename in SPECIAL_NESTED_BASIC_TYPES:
        type_code, dtype = SPECIAL_NESTED_BASIC_TYPES[value_type.typename]
        if isinstance(slot_type, Array):
            return numpy.array(values, dtype=dtype)
        return array.array(type_code, values)
    return values


def _populate(message: Any) -> Any:
    """Assign a deterministic value to every field of a message."""
    for seed, (name, slot_type) in enumerate(
            zip(message.get_fields_and_field_types(), message.SLOT_TYPES)):
        setattr(message, name, _field_value(slot_type, seed + 1))
    return message


def _assert_same_shape(original: Any, converted: Any, path: str) -> None:
    """Assert the converted value has exactly the container types of the original."""
    assert type(original) is type(converted), \
        '%s: expected %s, got %s' % (path, type(original), type(converted))
    if isinstance(original, array.array):
        assert original.typecode == converted.typecode, \
            '%s: typecode %s != %s' % (path, original.typecode, converted.typecode)
    elif isinstance(original, numpy.ndarray):
        assert original.dtype == converted.dtype, \
            '%s: dtype %s != %s' % (path, original.dtype, converted.dtype)
    elif isinstance(original, list):
        assert len(original) == len(converted), '%s: length differs' % path
        for index, (left, right) in enumerate(zip(original, converted)):
            _assert_same_shape(left, right, '%s[%d]' % (path, index))
    elif hasattr(original, 'get_fields_and_field_types'):
        _assert_message_invariants(original, converted, path)


def _assert_message_invariants(original: Any, converted: Any, path: str) -> None:
    """Check the slots of a converted message, recursively."""
    # tp_alloc leaves every slot NULL, so a slot the C code forgets to assign only
    # shows up as an AttributeError at the point of use. Reading them all here turns
    # that into a test failure instead.
    assert converted._check_fields == EXPECTED_CHECK_FIELDS, \
        '%s: _check_fields was not set the way __init__ would set it' % path
    for name in original.get_fields_and_field_types():
        _assert_same_shape(
            getattr(original, name), getattr(converted, name), '%s.%s' % (path, name))


@pytest.mark.parametrize(
    'message_type', MESSAGE_TYPES, ids=[t.__name__ for t in MESSAGE_TYPES])
def test_round_trip_populated(message_type: type) -> None:
    """A fully populated message survives a round trip unchanged."""
    original = _populate(message_type())
    converted = _round_trip(original)

    assert converted == original
    assert type(converted) is message_type
    _assert_message_invariants(original, converted, message_type.__name__)
    # Touches every slot through the public properties, so a slot left unset by the
    # C code raises AttributeError here rather than in user code later on.
    assert repr(converted) == repr(original)


@pytest.mark.parametrize(
    'message_type', MESSAGE_TYPES, ids=[t.__name__ for t in MESSAGE_TYPES])
def test_round_trip_default(message_type: type) -> None:
    """A default constructed message survives a round trip unchanged."""
    original = message_type()
    converted = _round_trip(original)

    assert converted == original
    _assert_message_invariants(original, converted, message_type.__name__)
    assert repr(converted) == repr(original)


def test_round_trip_empty_sequences() -> None:
    """Empty sequences round trip, covering the zero length array.array path."""
    original = UnboundedSequences()
    converted = _round_trip(original)

    assert converted == original
    assert converted.uint8_values == array.array('B', [])
    assert converted.string_values == []


def test_converted_message_is_usable() -> None:
    """A converted message behaves like a normally constructed one."""
    original = _populate(Nested())
    converted = _round_trip(original)

    # Assignment still runs the property setters, including their validation.
    converted.basic_types_value.int32_value = 42
    assert converted.basic_types_value.int32_value == 42
    with pytest.raises(AssertionError):
        converted.basic_types_value._check_fields = True
        converted.basic_types_value.int32_value = 'not an int'


def test_no_reference_leak() -> None:
    """Repeated conversions do not accumulate references to the message class."""
    import sys
    original = _populate(Arrays())
    _round_trip(original)
    before = sys.getrefcount(Arrays)
    for _ in range(100):
        _round_trip(original)
    assert sys.getrefcount(Arrays) == before


def _unset_slots(message: Any) -> Optional[List[str]]:
    return [name for name in message.__slots__ if not hasattr(message, name)]


@pytest.mark.parametrize(
    'message_type', MESSAGE_TYPES, ids=[t.__name__ for t in MESSAGE_TYPES])
def test_every_slot_is_assigned(message_type: type) -> None:
    """Every declared slot is populated, including _check_fields."""
    converted = _round_trip(_populate(message_type()))
    assert _unset_slots(converted) == []
