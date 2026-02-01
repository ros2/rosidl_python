# generated from rosidl_generator_py/resource/_idl.py.em
# with input from rosidl_generator_py:msg/BoundedSequences.idl
# generated code does not contain a copyright notice

from __future__ import annotations

import collections.abc
from os import getenv
import typing

import rosidl_pycommon.interface_base_classes

# This is being done at the module level and not on the instance level to avoid looking
# for the same variable multiple times on each instance. This variable is not supposed to
# change during runtime so it makes sense to only look for it once.
ros_python_check_fields = getenv('ROS_PYTHON_CHECK_FIELDS', default='')


if typing.TYPE_CHECKING:
    from rosidl_generator_py.msg import Constants
    from ctypes import Structure

    class PyCapsule(Structure):
        pass  # don't need to define the full structure
    from rosidl_generator_py.msg import BasicTypes
    from rosidl_generator_py.msg import Defaults


# Import statements for member types

# Member 'char_values'
# Member 'float32_values'
# Member 'float64_values'
# Member 'int8_values'
# Member 'uint8_values'
# Member 'int16_values'
# Member 'uint16_values'
# Member 'int32_values'
# Member 'uint32_values'
# Member 'int64_values'
# Member 'uint64_values'
# Member 'char_values_default'
# Member 'float32_values_default'
# Member 'float64_values_default'
# Member 'int8_values_default'
# Member 'uint8_values_default'
# Member 'int16_values_default'
# Member 'uint16_values_default'
# Member 'int32_values_default'
# Member 'uint32_values_default'
# Member 'int64_values_default'
# Member 'uint64_values_default'
import array  # noqa: E402, I100

import builtins  # noqa: E402, I100

import math  # noqa: E402, I100

import rosidl_parser.definition  # noqa: E402, I100


class Metaclass_BoundedSequences(rosidl_pycommon.interface_base_classes.MessageTypeSupportMeta):
    """Metaclass of message 'BoundedSequences'."""

    _CREATE_ROS_MESSAGE: typing.ClassVar[typing.Optional[PyCapsule]] = None
    _CONVERT_FROM_PY: typing.ClassVar[typing.Optional[PyCapsule]] = None
    _CONVERT_TO_PY: typing.ClassVar[typing.Optional[PyCapsule]] = None
    _DESTROY_ROS_MESSAGE: typing.ClassVar[typing.Optional[PyCapsule]] = None
    _TYPE_SUPPORT: typing.ClassVar[typing.Optional[PyCapsule]] = None

    class BoundedSequencesConstants(typing.TypedDict):
        pass

    __constants: BoundedSequencesConstants = {
    }

    @classmethod
    def __import_type_support__(cls) -> None:
        try:
            from rosidl_generator_py import import_type_support  # type: ignore[attr-defined]
            module = import_type_support('rosidl_generator_py')
        except ImportError:
            import logging
            import traceback
            logger = logging.getLogger(
                'rosidl_generator_py.msg.BoundedSequences')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._CREATE_ROS_MESSAGE = module.create_ros_message_msg__msg__bounded_sequences
            cls._CONVERT_FROM_PY = module.convert_from_py_msg__msg__bounded_sequences
            cls._CONVERT_TO_PY = module.convert_to_py_msg__msg__bounded_sequences
            cls._TYPE_SUPPORT = module.type_support_msg__msg__bounded_sequences
            cls._DESTROY_ROS_MESSAGE = module.destroy_ros_message_msg__msg__bounded_sequences

            from rosidl_generator_py.msg import BasicTypes
            if BasicTypes._TYPE_SUPPORT is None:
                BasicTypes.__import_type_support__()

            from rosidl_generator_py.msg import Constants
            if Constants._TYPE_SUPPORT is None:
                Constants.__import_type_support__()

            from rosidl_generator_py.msg import Defaults
            if Defaults._TYPE_SUPPORT is None:
                Defaults.__import_type_support__()

    @classmethod
    def __prepare__(metacls, name: str, bases: tuple[type[typing.Any], ...], /, **kwds: typing.Any) -> collections.abc.MutableMapping[str, object]:
        # list constant names here so that they appear in the help text of
        # the message class under "Data and other attributes defined here:"
        # as well as populate each message instance
        return {
            'BOOL_VALUES_DEFAULT__DEFAULT': [False, True, False],
            'BYTE_VALUES_DEFAULT__DEFAULT': [b'\x00', b'\x01', b'\xff'],
            'CHAR_VALUES_DEFAULT__DEFAULT': array.array('B', (0, 1, 127, )),
            'FLOAT32_VALUES_DEFAULT__DEFAULT': array.array('f', (1.125, 0.0, -1.125, )),
            'FLOAT64_VALUES_DEFAULT__DEFAULT': array.array('d', (3.1415, 0.0, -3.1415, )),
            'INT8_VALUES_DEFAULT__DEFAULT': array.array('b', (0, 127, -128, )),
            'UINT8_VALUES_DEFAULT__DEFAULT': array.array('B', (0, 1, 255, )),
            'INT16_VALUES_DEFAULT__DEFAULT': array.array('h', (0, 32767, -32768, )),
            'UINT16_VALUES_DEFAULT__DEFAULT': array.array('H', (0, 1, 65535, )),
            'INT32_VALUES_DEFAULT__DEFAULT': array.array('i', (0, 2147483647, -2147483648, )),
            'UINT32_VALUES_DEFAULT__DEFAULT': array.array('I', (0, 1, 4294967295, )),
            'INT64_VALUES_DEFAULT__DEFAULT': array.array('q', (0, 9223372036854775807, -9223372036854775808, )),
            'UINT64_VALUES_DEFAULT__DEFAULT': array.array('Q', (0, 1, 18446744073709551615, )),
            'STRING_VALUES_DEFAULT__DEFAULT': ['', 'max value', 'min value'],
        }

    @property
    def BOOL_VALUES_DEFAULT__DEFAULT(cls) -> list[bool]:
        """Return default value for message field 'bool_values_default'."""
        return [False, True, False]

    @property
    def BYTE_VALUES_DEFAULT__DEFAULT(cls) -> list[bytes]:
        """Return default value for message field 'byte_values_default'."""
        return [b'\x00', b'\x01', b'\xff']

    @property
    def CHAR_VALUES_DEFAULT__DEFAULT(cls) -> array.array[int]:
        """Return default value for message field 'char_values_default'."""
        return array.array('B', (0, 1, 127, ))

    @property
    def FLOAT32_VALUES_DEFAULT__DEFAULT(cls) -> array.array[float]:
        """Return default value for message field 'float32_values_default'."""
        return array.array('f', (1.125, 0.0, -1.125, ))

    @property
    def FLOAT64_VALUES_DEFAULT__DEFAULT(cls) -> array.array[float]:
        """Return default value for message field 'float64_values_default'."""
        return array.array('d', (3.1415, 0.0, -3.1415, ))

    @property
    def INT8_VALUES_DEFAULT__DEFAULT(cls) -> array.array[int]:
        """Return default value for message field 'int8_values_default'."""
        return array.array('b', (0, 127, -128, ))

    @property
    def UINT8_VALUES_DEFAULT__DEFAULT(cls) -> array.array[int]:
        """Return default value for message field 'uint8_values_default'."""
        return array.array('B', (0, 1, 255, ))

    @property
    def INT16_VALUES_DEFAULT__DEFAULT(cls) -> array.array[int]:
        """Return default value for message field 'int16_values_default'."""
        return array.array('h', (0, 32767, -32768, ))

    @property
    def UINT16_VALUES_DEFAULT__DEFAULT(cls) -> array.array[int]:
        """Return default value for message field 'uint16_values_default'."""
        return array.array('H', (0, 1, 65535, ))

    @property
    def INT32_VALUES_DEFAULT__DEFAULT(cls) -> array.array[int]:
        """Return default value for message field 'int32_values_default'."""
        return array.array('i', (0, 2147483647, -2147483648, ))

    @property
    def UINT32_VALUES_DEFAULT__DEFAULT(cls) -> array.array[int]:
        """Return default value for message field 'uint32_values_default'."""
        return array.array('I', (0, 1, 4294967295, ))

    @property
    def INT64_VALUES_DEFAULT__DEFAULT(cls) -> array.array[int]:
        """Return default value for message field 'int64_values_default'."""
        return array.array('q', (0, 9223372036854775807, -9223372036854775808, ))

    @property
    def UINT64_VALUES_DEFAULT__DEFAULT(cls) -> array.array[int]:
        """Return default value for message field 'uint64_values_default'."""
        return array.array('Q', (0, 1, 18446744073709551615, ))

    @property
    def STRING_VALUES_DEFAULT__DEFAULT(cls) -> list[str]:
        """Return default value for message field 'string_values_default'."""
        return ['', 'max value', 'min value']


class BoundedSequences(rosidl_pycommon.interface_base_classes.BaseMessage, metaclass=Metaclass_BoundedSequences):
    """Message class 'BoundedSequences'."""

    __slots__ = [
        '_bool_values',
        '_byte_values',
        '_char_values',
        '_float32_values',
        '_float64_values',
        '_int8_values',
        '_uint8_values',
        '_int16_values',
        '_uint16_values',
        '_int32_values',
        '_uint32_values',
        '_int64_values',
        '_uint64_values',
        '_string_values',
        '_basic_types_values',
        '_constants_values',
        '_defaults_values',
        '_bool_values_default',
        '_byte_values_default',
        '_char_values_default',
        '_float32_values_default',
        '_float64_values_default',
        '_int8_values_default',
        '_uint8_values_default',
        '_int16_values_default',
        '_uint16_values_default',
        '_int32_values_default',
        '_uint32_values_default',
        '_int64_values_default',
        '_uint64_values_default',
        '_string_values_default',
        '_alignment_check',
        '_check_fields',
    ]

    _fields_and_field_types: dict[str, str] = {
        'bool_values': 'sequence<boolean, 3>',
        'byte_values': 'sequence<octet, 3>',
        'char_values': 'sequence<uint8, 3>',
        'float32_values': 'sequence<float, 3>',
        'float64_values': 'sequence<double, 3>',
        'int8_values': 'sequence<int8, 3>',
        'uint8_values': 'sequence<uint8, 3>',
        'int16_values': 'sequence<int16, 3>',
        'uint16_values': 'sequence<uint16, 3>',
        'int32_values': 'sequence<int32, 3>',
        'uint32_values': 'sequence<uint32, 3>',
        'int64_values': 'sequence<int64, 3>',
        'uint64_values': 'sequence<uint64, 3>',
        'string_values': 'sequence<string, 3>',
        'basic_types_values': 'sequence<rosidl_generator_py/BasicTypes, 3>',
        'constants_values': 'sequence<rosidl_generator_py/Constants, 3>',
        'defaults_values': 'sequence<rosidl_generator_py/Defaults, 3>',
        'bool_values_default': 'sequence<boolean, 3>',
        'byte_values_default': 'sequence<octet, 3>',
        'char_values_default': 'sequence<uint8, 3>',
        'float32_values_default': 'sequence<float, 3>',
        'float64_values_default': 'sequence<double, 3>',
        'int8_values_default': 'sequence<int8, 3>',
        'uint8_values_default': 'sequence<uint8, 3>',
        'int16_values_default': 'sequence<int16, 3>',
        'uint16_values_default': 'sequence<uint16, 3>',
        'int32_values_default': 'sequence<int32, 3>',
        'uint32_values_default': 'sequence<uint32, 3>',
        'int64_values_default': 'sequence<int64, 3>',
        'uint64_values_default': 'sequence<uint64, 3>',
        'string_values_default': 'sequence<string, 3>',
        'alignment_check': 'int32',
    }

    # This attribute is used to store an rosidl_parser.definition variable
    # related to the data type of each of the components the message.
    SLOT_TYPES: tuple[rosidl_parser.definition.AbstractType, ...] = (
        rosidl_parser.definition.BoundedSequence(rosidl_parser.definition.BasicType('boolean'), 3),  # noqa: E501
        rosidl_parser.definition.BoundedSequence(rosidl_parser.definition.BasicType('octet'), 3),  # noqa: E501
        rosidl_parser.definition.BoundedSequence(rosidl_parser.definition.BasicType('uint8'), 3),  # noqa: E501
        rosidl_parser.definition.BoundedSequence(rosidl_parser.definition.BasicType('float'), 3),  # noqa: E501
        rosidl_parser.definition.BoundedSequence(rosidl_parser.definition.BasicType('double'), 3),  # noqa: E501
        rosidl_parser.definition.BoundedSequence(rosidl_parser.definition.BasicType('int8'), 3),  # noqa: E501
        rosidl_parser.definition.BoundedSequence(rosidl_parser.definition.BasicType('uint8'), 3),  # noqa: E501
        rosidl_parser.definition.BoundedSequence(rosidl_parser.definition.BasicType('int16'), 3),  # noqa: E501
        rosidl_parser.definition.BoundedSequence(rosidl_parser.definition.BasicType('uint16'), 3),  # noqa: E501
        rosidl_parser.definition.BoundedSequence(rosidl_parser.definition.BasicType('int32'), 3),  # noqa: E501
        rosidl_parser.definition.BoundedSequence(rosidl_parser.definition.BasicType('uint32'), 3),  # noqa: E501
        rosidl_parser.definition.BoundedSequence(rosidl_parser.definition.BasicType('int64'), 3),  # noqa: E501
        rosidl_parser.definition.BoundedSequence(rosidl_parser.definition.BasicType('uint64'), 3),  # noqa: E501
        rosidl_parser.definition.BoundedSequence(rosidl_parser.definition.UnboundedString(), 3),  # noqa: E501
        rosidl_parser.definition.BoundedSequence(rosidl_parser.definition.NamespacedType(['rosidl_generator_py', 'msg'], 'BasicTypes'), 3),  # noqa: E501
        rosidl_parser.definition.BoundedSequence(rosidl_parser.definition.NamespacedType(['rosidl_generator_py', 'msg'], 'Constants'), 3),  # noqa: E501
        rosidl_parser.definition.BoundedSequence(rosidl_parser.definition.NamespacedType(['rosidl_generator_py', 'msg'], 'Defaults'), 3),  # noqa: E501
        rosidl_parser.definition.BoundedSequence(rosidl_parser.definition.BasicType('boolean'), 3),  # noqa: E501
        rosidl_parser.definition.BoundedSequence(rosidl_parser.definition.BasicType('octet'), 3),  # noqa: E501
        rosidl_parser.definition.BoundedSequence(rosidl_parser.definition.BasicType('uint8'), 3),  # noqa: E501
        rosidl_parser.definition.BoundedSequence(rosidl_parser.definition.BasicType('float'), 3),  # noqa: E501
        rosidl_parser.definition.BoundedSequence(rosidl_parser.definition.BasicType('double'), 3),  # noqa: E501
        rosidl_parser.definition.BoundedSequence(rosidl_parser.definition.BasicType('int8'), 3),  # noqa: E501
        rosidl_parser.definition.BoundedSequence(rosidl_parser.definition.BasicType('uint8'), 3),  # noqa: E501
        rosidl_parser.definition.BoundedSequence(rosidl_parser.definition.BasicType('int16'), 3),  # noqa: E501
        rosidl_parser.definition.BoundedSequence(rosidl_parser.definition.BasicType('uint16'), 3),  # noqa: E501
        rosidl_parser.definition.BoundedSequence(rosidl_parser.definition.BasicType('int32'), 3),  # noqa: E501
        rosidl_parser.definition.BoundedSequence(rosidl_parser.definition.BasicType('uint32'), 3),  # noqa: E501
        rosidl_parser.definition.BoundedSequence(rosidl_parser.definition.BasicType('int64'), 3),  # noqa: E501
        rosidl_parser.definition.BoundedSequence(rosidl_parser.definition.BasicType('uint64'), 3),  # noqa: E501
        rosidl_parser.definition.BoundedSequence(rosidl_parser.definition.UnboundedString(), 3),  # noqa: E501
        rosidl_parser.definition.BasicType('int32'),  # noqa: E501
    )

    def __init__(self, *,
                 bool_values: typing.Optional[collections.abc.Sequence[bool]] = None,  # noqa: E501
                 byte_values: typing.Optional[collections.abc.Sequence[bytes]] = None,  # noqa: E501
                 char_values: typing.Optional[typing.Union[array.array[int], collections.abc.Sequence[int]]] = None,  # noqa: E501
                 float32_values: typing.Optional[typing.Union[array.array[float], collections.abc.Sequence[float]]] = None,  # noqa: E501
                 float64_values: typing.Optional[typing.Union[array.array[float], collections.abc.Sequence[float]]] = None,  # noqa: E501
                 int8_values: typing.Optional[typing.Union[array.array[int], collections.abc.Sequence[int]]] = None,  # noqa: E501
                 uint8_values: typing.Optional[typing.Union[array.array[int], collections.abc.Sequence[int]]] = None,  # noqa: E501
                 int16_values: typing.Optional[typing.Union[array.array[int], collections.abc.Sequence[int]]] = None,  # noqa: E501
                 uint16_values: typing.Optional[typing.Union[array.array[int], collections.abc.Sequence[int]]] = None,  # noqa: E501
                 int32_values: typing.Optional[typing.Union[array.array[int], collections.abc.Sequence[int]]] = None,  # noqa: E501
                 uint32_values: typing.Optional[typing.Union[array.array[int], collections.abc.Sequence[int]]] = None,  # noqa: E501
                 int64_values: typing.Optional[typing.Union[array.array[int], collections.abc.Sequence[int]]] = None,  # noqa: E501
                 uint64_values: typing.Optional[typing.Union[array.array[int], collections.abc.Sequence[int]]] = None,  # noqa: E501
                 string_values: typing.Optional[collections.abc.Sequence[str]] = None,  # noqa: E501
                 basic_types_values: typing.Optional[collections.abc.Sequence[BasicTypes]] = None,  # noqa: E501
                 constants_values: typing.Optional[collections.abc.Sequence[Constants]] = None,  # noqa: E501
                 defaults_values: typing.Optional[collections.abc.Sequence[Defaults]] = None,  # noqa: E501
                 bool_values_default: typing.Optional[collections.abc.Sequence[bool]] = None,  # noqa: E501
                 byte_values_default: typing.Optional[collections.abc.Sequence[bytes]] = None,  # noqa: E501
                 char_values_default: typing.Optional[typing.Union[array.array[int], collections.abc.Sequence[int]]] = None,  # noqa: E501
                 float32_values_default: typing.Optional[typing.Union[array.array[float], collections.abc.Sequence[float]]] = None,  # noqa: E501
                 float64_values_default: typing.Optional[typing.Union[array.array[float], collections.abc.Sequence[float]]] = None,  # noqa: E501
                 int8_values_default: typing.Optional[typing.Union[array.array[int], collections.abc.Sequence[int]]] = None,  # noqa: E501
                 uint8_values_default: typing.Optional[typing.Union[array.array[int], collections.abc.Sequence[int]]] = None,  # noqa: E501
                 int16_values_default: typing.Optional[typing.Union[array.array[int], collections.abc.Sequence[int]]] = None,  # noqa: E501
                 uint16_values_default: typing.Optional[typing.Union[array.array[int], collections.abc.Sequence[int]]] = None,  # noqa: E501
                 int32_values_default: typing.Optional[typing.Union[array.array[int], collections.abc.Sequence[int]]] = None,  # noqa: E501
                 uint32_values_default: typing.Optional[typing.Union[array.array[int], collections.abc.Sequence[int]]] = None,  # noqa: E501
                 int64_values_default: typing.Optional[typing.Union[array.array[int], collections.abc.Sequence[int]]] = None,  # noqa: E501
                 uint64_values_default: typing.Optional[typing.Union[array.array[int], collections.abc.Sequence[int]]] = None,  # noqa: E501
                 string_values_default: typing.Optional[collections.abc.Sequence[str]] = None,  # noqa: E501
                 alignment_check: typing.Optional[int] = None,  # noqa: E501
                 check_fields: typing.Optional[bool] = None) -> None:
        if check_fields is not None:
            self._check_fields = check_fields
        else:
            self._check_fields = ros_python_check_fields == '1'
        self.bool_values = bool_values if bool_values is not None else []
        self.byte_values = byte_values if byte_values is not None else []
        self.char_values = char_values if char_values is not None else array.array('B', [])
        self.float32_values = float32_values if float32_values is not None else array.array('f', [])
        self.float64_values = float64_values if float64_values is not None else array.array('d', [])
        self.int8_values = int8_values if int8_values is not None else array.array('b', [])
        self.uint8_values = uint8_values if uint8_values is not None else array.array('B', [])
        self.int16_values = int16_values if int16_values is not None else array.array('h', [])
        self.uint16_values = uint16_values if uint16_values is not None else array.array('H', [])
        self.int32_values = int32_values if int32_values is not None else array.array('i', [])
        self.uint32_values = uint32_values if uint32_values is not None else array.array('I', [])
        self.int64_values = int64_values if int64_values is not None else array.array('q', [])
        self.uint64_values = uint64_values if uint64_values is not None else array.array('Q', [])
        self.string_values = string_values if string_values is not None else []
        self.basic_types_values = basic_types_values if basic_types_values is not None else []
        self.constants_values = constants_values if constants_values is not None else []
        self.defaults_values = defaults_values if defaults_values is not None else []
        self.bool_values_default = bool_values_default if bool_values_default is not None else BoundedSequences.BOOL_VALUES_DEFAULT__DEFAULT
        self.byte_values_default = byte_values_default if byte_values_default is not None else BoundedSequences.BYTE_VALUES_DEFAULT__DEFAULT
        self.char_values_default = char_values_default if char_values_default is not None else BoundedSequences.CHAR_VALUES_DEFAULT__DEFAULT
        self.float32_values_default = float32_values_default if float32_values_default is not None else BoundedSequences.FLOAT32_VALUES_DEFAULT__DEFAULT
        self.float64_values_default = float64_values_default if float64_values_default is not None else BoundedSequences.FLOAT64_VALUES_DEFAULT__DEFAULT
        self.int8_values_default = int8_values_default if int8_values_default is not None else BoundedSequences.INT8_VALUES_DEFAULT__DEFAULT
        self.uint8_values_default = uint8_values_default if uint8_values_default is not None else BoundedSequences.UINT8_VALUES_DEFAULT__DEFAULT
        self.int16_values_default = int16_values_default if int16_values_default is not None else BoundedSequences.INT16_VALUES_DEFAULT__DEFAULT
        self.uint16_values_default = uint16_values_default if uint16_values_default is not None else BoundedSequences.UINT16_VALUES_DEFAULT__DEFAULT
        self.int32_values_default = int32_values_default if int32_values_default is not None else BoundedSequences.INT32_VALUES_DEFAULT__DEFAULT
        self.uint32_values_default = uint32_values_default if uint32_values_default is not None else BoundedSequences.UINT32_VALUES_DEFAULT__DEFAULT
        self.int64_values_default = int64_values_default if int64_values_default is not None else BoundedSequences.INT64_VALUES_DEFAULT__DEFAULT
        self.uint64_values_default = uint64_values_default if uint64_values_default is not None else BoundedSequences.UINT64_VALUES_DEFAULT__DEFAULT
        self.string_values_default = string_values_default if string_values_default is not None else BoundedSequences.STRING_VALUES_DEFAULT__DEFAULT
        self.alignment_check = alignment_check if alignment_check is not None else int()

    def __repr__(self) -> str:
        typename = self.__class__.__module__.split('.')
        typename.pop()
        typename.append(self.__class__.__name__)
        args: list[str] = []
        for s, t in zip(self.get_fields_and_field_types().keys(), self.SLOT_TYPES):
            field = getattr(self, s)
            fieldstr = repr(field)
            # We use Python array type for fields that can be directly stored
            # in them, and "normal" sequences for everything else.  If it is
            # a type that we store in an array, strip off the 'array' portion.
            if (
                isinstance(t, rosidl_parser.definition.AbstractSequence) and
                isinstance(t.value_type, rosidl_parser.definition.BasicType) and
                t.value_type.typename in ['float', 'double', 'int8', 'uint8', 'int16', 'uint16', 'int32', 'uint32', 'int64', 'uint64']
            ):
                if len(field) == 0:
                    fieldstr = '[]'
                else:
                    if self._check_fields:
                        assert fieldstr.startswith('array(')
                    prefix = "array('X', "
                    suffix = ')'
                    fieldstr = fieldstr[len(prefix):-len(suffix)]
            args.append(s + '=' + fieldstr)
        return '%s(%s)' % ('.'.join(typename), ', '.join(args))

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, BoundedSequences):
            return False
        if self.bool_values != other.bool_values:
            return False
        if self.byte_values != other.byte_values:
            return False
        if self.char_values != other.char_values:
            return False
        if self.float32_values != other.float32_values:
            return False
        if self.float64_values != other.float64_values:
            return False
        if self.int8_values != other.int8_values:
            return False
        if self.uint8_values != other.uint8_values:
            return False
        if self.int16_values != other.int16_values:
            return False
        if self.uint16_values != other.uint16_values:
            return False
        if self.int32_values != other.int32_values:
            return False
        if self.uint32_values != other.uint32_values:
            return False
        if self.int64_values != other.int64_values:
            return False
        if self.uint64_values != other.uint64_values:
            return False
        if self.string_values != other.string_values:
            return False
        if self.basic_types_values != other.basic_types_values:
            return False
        if self.constants_values != other.constants_values:
            return False
        if self.defaults_values != other.defaults_values:
            return False
        if self.bool_values_default != other.bool_values_default:
            return False
        if self.byte_values_default != other.byte_values_default:
            return False
        if self.char_values_default != other.char_values_default:
            return False
        if self.float32_values_default != other.float32_values_default:
            return False
        if self.float64_values_default != other.float64_values_default:
            return False
        if self.int8_values_default != other.int8_values_default:
            return False
        if self.uint8_values_default != other.uint8_values_default:
            return False
        if self.int16_values_default != other.int16_values_default:
            return False
        if self.uint16_values_default != other.uint16_values_default:
            return False
        if self.int32_values_default != other.int32_values_default:
            return False
        if self.uint32_values_default != other.uint32_values_default:
            return False
        if self.int64_values_default != other.int64_values_default:
            return False
        if self.uint64_values_default != other.uint64_values_default:
            return False
        if self.string_values_default != other.string_values_default:
            return False
        if self.alignment_check != other.alignment_check:
            return False
        return True

    @classmethod
    def get_fields_and_field_types(cls) -> dict[str, str]:
        from copy import copy
        return copy(cls._fields_and_field_types)

    @builtins.property
    def bool_values(self) -> collections.abc.Sequence[bool]:   # typing.Annotated can be remove after mypy 1.16+ see mypy#3004
        """Message field 'bool_values'."""
        return self._bool_values

    @bool_values.setter
    def bool_values(self, value: collections.abc.Sequence[bool]) -> None:

        from collections.abc import Set
        if isinstance(value, Set):
            import warnings
            warnings.warn(
                'Using set or subclass of set is deprecated,'
                ' please use a subclass of collections.abc.Sequence like list',
                DeprecationWarning)
        if self._check_fields:
            from collections.abc import Sequence
            from collections import UserString
            assert \
                ((isinstance(value, Sequence) or
                  isinstance(value, Set)) and
                 not isinstance(value, str) and
                 not isinstance(value, UserString) and
                 len(value) <= 3 and
                 all(isinstance(v, bool) for v in value) and
                 True), \
                "The 'bool_values' field must be sequence with length <= 3 and each value of type bool"
        self._bool_values = value

    @builtins.property
    def byte_values(self) -> collections.abc.Sequence[bytes]:   # typing.Annotated can be remove after mypy 1.16+ see mypy#3004
        """Message field 'byte_values'."""
        return self._byte_values

    @byte_values.setter
    def byte_values(self, value: collections.abc.Sequence[bytes]) -> None:

        from collections.abc import Set
        if isinstance(value, Set):
            import warnings
            warnings.warn(
                'Using set or subclass of set is deprecated,'
                ' please use a subclass of collections.abc.Sequence like list',
                DeprecationWarning)
        if self._check_fields:
            from collections.abc import Sequence
            from collections import UserString
            assert \
                ((isinstance(value, Sequence) or
                  isinstance(value, Set)) and
                 not isinstance(value, str) and
                 not isinstance(value, UserString) and
                 len(value) <= 3 and
                 all(isinstance(v, bytes) for v in value) and
                 True), \
                "The 'byte_values' field must be sequence with length <= 3 and each value of type bytes"
        self._byte_values = value

    @builtins.property
    def char_values(self) -> typing.Annotated[typing.Any, array.array[int]]:   # typing.Annotated can be remove after mypy 1.16+ see mypy#3004
        """Message field 'char_values'."""
        return self._char_values

    @char_values.setter
    def char_values(self, value: typing.Union[array.array[int], collections.abc.Sequence[int]]) -> None:

        from collections.abc import Set
        if isinstance(value, Set):
            import warnings
            warnings.warn(
                'Using set or subclass of set is deprecated,'
                ' please use a subclass of collections.abc.Sequence like list',
                DeprecationWarning)
        if self._check_fields:
            if isinstance(value, array.array):
                assert value.typecode == 'B', \
                    "The 'char_values' array.array() must have the type code of 'B'"
                assert len(value) <= 3, \
                    "The 'char_values' array.array() must have a size <= 3"
            self._char_values = value
            return
        from collections.abc import Sequence
        from collections import UserString
        assert \
            ((isinstance(value, Sequence) or
              isinstance(value, Set)) and
             not isinstance(value, str) and
             not isinstance(value, UserString) and
             len(value) <= 3 and
             all(isinstance(v, int) for v in value) and
             all(val >= 0 and val < 256 for val in value)), \
            "The 'char_values' field must be sequence with length <= 3 and each value of type int and each unsigned integer in [0, 255]"
        # type ignore below fixed in mypy 1.17+ see mypy#19421
        self._char_values = array.array('B', value)  # type: ignore[assignment]

    @builtins.property
    def float32_values(self) -> typing.Annotated[typing.Any, array.array[float]]:   # typing.Annotated can be remove after mypy 1.16+ see mypy#3004
        """Message field 'float32_values'."""
        return self._float32_values

    @float32_values.setter
    def float32_values(self, value: typing.Union[array.array[float], collections.abc.Sequence[float]]) -> None:

        from collections.abc import Set
        if isinstance(value, Set):
            import warnings
            warnings.warn(
                'Using set or subclass of set is deprecated,'
                ' please use a subclass of collections.abc.Sequence like list',
                DeprecationWarning)
        if self._check_fields:
            if isinstance(value, array.array):
                assert value.typecode == 'f', \
                    "The 'float32_values' array.array() must have the type code of 'f'"
                assert len(value) <= 3, \
                    "The 'float32_values' array.array() must have a size <= 3"
            self._float32_values = value
            return
        from collections.abc import Sequence
        from collections import UserString
        assert \
            ((isinstance(value, Sequence) or
              isinstance(value, Set)) and
             not isinstance(value, str) and
             not isinstance(value, UserString) and
             len(value) <= 3 and
             all(isinstance(v, float) for v in value) and
             all(not (val < -3.402823466e+38 or val > 3.402823466e+38) or math.isinf(val) for val in value)), \
            "The 'float32_values' field must be sequence with length <= 3 and each value of type float 'and each float in [-3.402823466e+38, 3.402823466e+38]'"
        # type ignore below fixed in mypy 1.17+ see mypy#19421
        self._float32_values = array.array('f', value)  # type: ignore[assignment]

    @builtins.property
    def float64_values(self) -> typing.Annotated[typing.Any, array.array[float]]:   # typing.Annotated can be remove after mypy 1.16+ see mypy#3004
        """Message field 'float64_values'."""
        return self._float64_values

    @float64_values.setter
    def float64_values(self, value: typing.Union[array.array[float], collections.abc.Sequence[float]]) -> None:

        from collections.abc import Set
        if isinstance(value, Set):
            import warnings
            warnings.warn(
                'Using set or subclass of set is deprecated,'
                ' please use a subclass of collections.abc.Sequence like list',
                DeprecationWarning)
        if self._check_fields:
            if isinstance(value, array.array):
                assert value.typecode == 'd', \
                    "The 'float64_values' array.array() must have the type code of 'd'"
                assert len(value) <= 3, \
                    "The 'float64_values' array.array() must have a size <= 3"
            self._float64_values = value
            return
        from collections.abc import Sequence
        from collections import UserString
        assert \
            ((isinstance(value, Sequence) or
              isinstance(value, Set)) and
             not isinstance(value, str) and
             not isinstance(value, UserString) and
             len(value) <= 3 and
             all(isinstance(v, float) for v in value) and
             all(not (val < -1.7976931348623157e+308 or val > 1.7976931348623157e+308) or math.isinf(val) for val in value)), \
            "The 'float64_values' field must be sequence with length <= 3 and each value of type float 'and each double in [-1.7976931348623157e+308, 1.7976931348623157e+308]'"
        # type ignore below fixed in mypy 1.17+ see mypy#19421
        self._float64_values = array.array('d', value)  # type: ignore[assignment]

    @builtins.property
    def int8_values(self) -> typing.Annotated[typing.Any, array.array[int]]:   # typing.Annotated can be remove after mypy 1.16+ see mypy#3004
        """Message field 'int8_values'."""
        return self._int8_values

    @int8_values.setter
    def int8_values(self, value: typing.Union[array.array[int], collections.abc.Sequence[int]]) -> None:

        from collections.abc import Set
        if isinstance(value, Set):
            import warnings
            warnings.warn(
                'Using set or subclass of set is deprecated,'
                ' please use a subclass of collections.abc.Sequence like list',
                DeprecationWarning)
        if self._check_fields:
            if isinstance(value, array.array):
                assert value.typecode == 'b', \
                    "The 'int8_values' array.array() must have the type code of 'b'"
                assert len(value) <= 3, \
                    "The 'int8_values' array.array() must have a size <= 3"
            self._int8_values = value
            return
        from collections.abc import Sequence
        from collections import UserString
        assert \
            ((isinstance(value, Sequence) or
              isinstance(value, Set)) and
             not isinstance(value, str) and
             not isinstance(value, UserString) and
             len(value) <= 3 and
             all(isinstance(v, int) for v in value) and
             all(val >= -128 and val < 128 for val in value)), \
            "The 'int8_values' field must be sequence with length <= 3 and each value of type int and each integer in [-128, 127]"
        # type ignore below fixed in mypy 1.17+ see mypy#19421
        self._int8_values = array.array('b', value)  # type: ignore[assignment]

    @builtins.property
    def uint8_values(self) -> typing.Annotated[typing.Any, array.array[int]]:   # typing.Annotated can be remove after mypy 1.16+ see mypy#3004
        """Message field 'uint8_values'."""
        return self._uint8_values

    @uint8_values.setter
    def uint8_values(self, value: typing.Union[array.array[int], collections.abc.Sequence[int]]) -> None:

        from collections.abc import Set
        if isinstance(value, Set):
            import warnings
            warnings.warn(
                'Using set or subclass of set is deprecated,'
                ' please use a subclass of collections.abc.Sequence like list',
                DeprecationWarning)
        if self._check_fields:
            if isinstance(value, array.array):
                assert value.typecode == 'B', \
                    "The 'uint8_values' array.array() must have the type code of 'B'"
                assert len(value) <= 3, \
                    "The 'uint8_values' array.array() must have a size <= 3"
            self._uint8_values = value
            return
        from collections.abc import Sequence
        from collections import UserString
        assert \
            ((isinstance(value, Sequence) or
              isinstance(value, Set)) and
             not isinstance(value, str) and
             not isinstance(value, UserString) and
             len(value) <= 3 and
             all(isinstance(v, int) for v in value) and
             all(val >= 0 and val < 256 for val in value)), \
            "The 'uint8_values' field must be sequence with length <= 3 and each value of type int and each unsigned integer in [0, 255]"
        # type ignore below fixed in mypy 1.17+ see mypy#19421
        self._uint8_values = array.array('B', value)  # type: ignore[assignment]

    @builtins.property
    def int16_values(self) -> typing.Annotated[typing.Any, array.array[int]]:   # typing.Annotated can be remove after mypy 1.16+ see mypy#3004
        """Message field 'int16_values'."""
        return self._int16_values

    @int16_values.setter
    def int16_values(self, value: typing.Union[array.array[int], collections.abc.Sequence[int]]) -> None:

        from collections.abc import Set
        if isinstance(value, Set):
            import warnings
            warnings.warn(
                'Using set or subclass of set is deprecated,'
                ' please use a subclass of collections.abc.Sequence like list',
                DeprecationWarning)
        if self._check_fields:
            if isinstance(value, array.array):
                assert value.typecode == 'h', \
                    "The 'int16_values' array.array() must have the type code of 'h'"
                assert len(value) <= 3, \
                    "The 'int16_values' array.array() must have a size <= 3"
            self._int16_values = value
            return
        from collections.abc import Sequence
        from collections import UserString
        assert \
            ((isinstance(value, Sequence) or
              isinstance(value, Set)) and
             not isinstance(value, str) and
             not isinstance(value, UserString) and
             len(value) <= 3 and
             all(isinstance(v, int) for v in value) and
             all(val >= -32768 and val < 32768 for val in value)), \
            "The 'int16_values' field must be sequence with length <= 3 and each value of type int and each integer in [-32768, 32767]"
        # type ignore below fixed in mypy 1.17+ see mypy#19421
        self._int16_values = array.array('h', value)  # type: ignore[assignment]

    @builtins.property
    def uint16_values(self) -> typing.Annotated[typing.Any, array.array[int]]:   # typing.Annotated can be remove after mypy 1.16+ see mypy#3004
        """Message field 'uint16_values'."""
        return self._uint16_values

    @uint16_values.setter
    def uint16_values(self, value: typing.Union[array.array[int], collections.abc.Sequence[int]]) -> None:

        from collections.abc import Set
        if isinstance(value, Set):
            import warnings
            warnings.warn(
                'Using set or subclass of set is deprecated,'
                ' please use a subclass of collections.abc.Sequence like list',
                DeprecationWarning)
        if self._check_fields:
            if isinstance(value, array.array):
                assert value.typecode == 'H', \
                    "The 'uint16_values' array.array() must have the type code of 'H'"
                assert len(value) <= 3, \
                    "The 'uint16_values' array.array() must have a size <= 3"
            self._uint16_values = value
            return
        from collections.abc import Sequence
        from collections import UserString
        assert \
            ((isinstance(value, Sequence) or
              isinstance(value, Set)) and
             not isinstance(value, str) and
             not isinstance(value, UserString) and
             len(value) <= 3 and
             all(isinstance(v, int) for v in value) and
             all(val >= 0 and val < 65536 for val in value)), \
            "The 'uint16_values' field must be sequence with length <= 3 and each value of type int and each unsigned integer in [0, 65535]"
        # type ignore below fixed in mypy 1.17+ see mypy#19421
        self._uint16_values = array.array('H', value)  # type: ignore[assignment]

    @builtins.property
    def int32_values(self) -> typing.Annotated[typing.Any, array.array[int]]:   # typing.Annotated can be remove after mypy 1.16+ see mypy#3004
        """Message field 'int32_values'."""
        return self._int32_values

    @int32_values.setter
    def int32_values(self, value: typing.Union[array.array[int], collections.abc.Sequence[int]]) -> None:

        from collections.abc import Set
        if isinstance(value, Set):
            import warnings
            warnings.warn(
                'Using set or subclass of set is deprecated,'
                ' please use a subclass of collections.abc.Sequence like list',
                DeprecationWarning)
        if self._check_fields:
            if isinstance(value, array.array):
                assert value.typecode == 'i', \
                    "The 'int32_values' array.array() must have the type code of 'i'"
                assert len(value) <= 3, \
                    "The 'int32_values' array.array() must have a size <= 3"
            self._int32_values = value
            return
        from collections.abc import Sequence
        from collections import UserString
        assert \
            ((isinstance(value, Sequence) or
              isinstance(value, Set)) and
             not isinstance(value, str) and
             not isinstance(value, UserString) and
             len(value) <= 3 and
             all(isinstance(v, int) for v in value) and
             all(val >= -2147483648 and val < 2147483648 for val in value)), \
            "The 'int32_values' field must be sequence with length <= 3 and each value of type int and each integer in [-2147483648, 2147483647]"
        # type ignore below fixed in mypy 1.17+ see mypy#19421
        self._int32_values = array.array('i', value)  # type: ignore[assignment]

    @builtins.property
    def uint32_values(self) -> typing.Annotated[typing.Any, array.array[int]]:   # typing.Annotated can be remove after mypy 1.16+ see mypy#3004
        """Message field 'uint32_values'."""
        return self._uint32_values

    @uint32_values.setter
    def uint32_values(self, value: typing.Union[array.array[int], collections.abc.Sequence[int]]) -> None:

        from collections.abc import Set
        if isinstance(value, Set):
            import warnings
            warnings.warn(
                'Using set or subclass of set is deprecated,'
                ' please use a subclass of collections.abc.Sequence like list',
                DeprecationWarning)
        if self._check_fields:
            if isinstance(value, array.array):
                assert value.typecode == 'I', \
                    "The 'uint32_values' array.array() must have the type code of 'I'"
                assert len(value) <= 3, \
                    "The 'uint32_values' array.array() must have a size <= 3"
            self._uint32_values = value
            return
        from collections.abc import Sequence
        from collections import UserString
        assert \
            ((isinstance(value, Sequence) or
              isinstance(value, Set)) and
             not isinstance(value, str) and
             not isinstance(value, UserString) and
             len(value) <= 3 and
             all(isinstance(v, int) for v in value) and
             all(val >= 0 and val < 4294967296 for val in value)), \
            "The 'uint32_values' field must be sequence with length <= 3 and each value of type int and each unsigned integer in [0, 4294967295]"
        # type ignore below fixed in mypy 1.17+ see mypy#19421
        self._uint32_values = array.array('I', value)  # type: ignore[assignment]

    @builtins.property
    def int64_values(self) -> typing.Annotated[typing.Any, array.array[int]]:   # typing.Annotated can be remove after mypy 1.16+ see mypy#3004
        """Message field 'int64_values'."""
        return self._int64_values

    @int64_values.setter
    def int64_values(self, value: typing.Union[array.array[int], collections.abc.Sequence[int]]) -> None:

        from collections.abc import Set
        if isinstance(value, Set):
            import warnings
            warnings.warn(
                'Using set or subclass of set is deprecated,'
                ' please use a subclass of collections.abc.Sequence like list',
                DeprecationWarning)
        if self._check_fields:
            if isinstance(value, array.array):
                assert value.typecode == 'q', \
                    "The 'int64_values' array.array() must have the type code of 'q'"
                assert len(value) <= 3, \
                    "The 'int64_values' array.array() must have a size <= 3"
            self._int64_values = value
            return
        from collections.abc import Sequence
        from collections import UserString
        assert \
            ((isinstance(value, Sequence) or
              isinstance(value, Set)) and
             not isinstance(value, str) and
             not isinstance(value, UserString) and
             len(value) <= 3 and
             all(isinstance(v, int) for v in value) and
             all(val >= -9223372036854775808 and val < 9223372036854775808 for val in value)), \
            "The 'int64_values' field must be sequence with length <= 3 and each value of type int and each integer in [-9223372036854775808, 9223372036854775807]"
        # type ignore below fixed in mypy 1.17+ see mypy#19421
        self._int64_values = array.array('q', value)  # type: ignore[assignment]

    @builtins.property
    def uint64_values(self) -> typing.Annotated[typing.Any, array.array[int]]:   # typing.Annotated can be remove after mypy 1.16+ see mypy#3004
        """Message field 'uint64_values'."""
        return self._uint64_values

    @uint64_values.setter
    def uint64_values(self, value: typing.Union[array.array[int], collections.abc.Sequence[int]]) -> None:

        from collections.abc import Set
        if isinstance(value, Set):
            import warnings
            warnings.warn(
                'Using set or subclass of set is deprecated,'
                ' please use a subclass of collections.abc.Sequence like list',
                DeprecationWarning)
        if self._check_fields:
            if isinstance(value, array.array):
                assert value.typecode == 'Q', \
                    "The 'uint64_values' array.array() must have the type code of 'Q'"
                assert len(value) <= 3, \
                    "The 'uint64_values' array.array() must have a size <= 3"
            self._uint64_values = value
            return
        from collections.abc import Sequence
        from collections import UserString
        assert \
            ((isinstance(value, Sequence) or
              isinstance(value, Set)) and
             not isinstance(value, str) and
             not isinstance(value, UserString) and
             len(value) <= 3 and
             all(isinstance(v, int) for v in value) and
             all(val >= 0 and val < 18446744073709551616 for val in value)), \
            "The 'uint64_values' field must be sequence with length <= 3 and each value of type int and each unsigned integer in [0, 18446744073709551615]"
        # type ignore below fixed in mypy 1.17+ see mypy#19421
        self._uint64_values = array.array('Q', value)  # type: ignore[assignment]

    @builtins.property
    def string_values(self) -> collections.abc.Sequence[str]:   # typing.Annotated can be remove after mypy 1.16+ see mypy#3004
        """Message field 'string_values'."""
        return self._string_values

    @string_values.setter
    def string_values(self, value: collections.abc.Sequence[str]) -> None:

        from collections.abc import Set
        if isinstance(value, Set):
            import warnings
            warnings.warn(
                'Using set or subclass of set is deprecated,'
                ' please use a subclass of collections.abc.Sequence like list',
                DeprecationWarning)
        if self._check_fields:
            from collections.abc import Sequence
            from collections import UserString
            assert \
                ((isinstance(value, Sequence) or
                  isinstance(value, Set)) and
                 not isinstance(value, str) and
                 not isinstance(value, UserString) and
                 len(value) <= 3 and
                 all(isinstance(v, str) for v in value) and
                 True), \
                "The 'string_values' field must be sequence with length <= 3 and each value of type str"
        self._string_values = value

    @builtins.property
    def basic_types_values(self) -> collections.abc.Sequence[BasicTypes]:   # typing.Annotated can be remove after mypy 1.16+ see mypy#3004
        """Message field 'basic_types_values'."""
        return self._basic_types_values

    @basic_types_values.setter
    def basic_types_values(self, value: collections.abc.Sequence[BasicTypes]) -> None:

        from collections.abc import Set
        if isinstance(value, Set):
            import warnings
            warnings.warn(
                'Using set or subclass of set is deprecated,'
                ' please use a subclass of collections.abc.Sequence like list',
                DeprecationWarning)
        if self._check_fields:
            from rosidl_generator_py.msg import BasicTypes
            from collections.abc import Sequence
            from collections import UserString
            assert \
                ((isinstance(value, Sequence) or
                  isinstance(value, Set)) and
                 not isinstance(value, str) and
                 not isinstance(value, UserString) and
                 len(value) <= 3 and
                 all(isinstance(v, BasicTypes) for v in value) and
                 True), \
                "The 'basic_types_values' field must be sequence with length <= 3 and each value of type BasicTypes"
        self._basic_types_values = value

    @builtins.property
    def constants_values(self) -> collections.abc.Sequence[Constants]:   # typing.Annotated can be remove after mypy 1.16+ see mypy#3004
        """Message field 'constants_values'."""
        return self._constants_values

    @constants_values.setter
    def constants_values(self, value: collections.abc.Sequence[Constants]) -> None:

        from collections.abc import Set
        if isinstance(value, Set):
            import warnings
            warnings.warn(
                'Using set or subclass of set is deprecated,'
                ' please use a subclass of collections.abc.Sequence like list',
                DeprecationWarning)
        if self._check_fields:
            from rosidl_generator_py.msg import Constants
            from collections.abc import Sequence
            from collections import UserString
            assert \
                ((isinstance(value, Sequence) or
                  isinstance(value, Set)) and
                 not isinstance(value, str) and
                 not isinstance(value, UserString) and
                 len(value) <= 3 and
                 all(isinstance(v, Constants) for v in value) and
                 True), \
                "The 'constants_values' field must be sequence with length <= 3 and each value of type Constants"
        self._constants_values = value

    @builtins.property
    def defaults_values(self) -> collections.abc.Sequence[Defaults]:   # typing.Annotated can be remove after mypy 1.16+ see mypy#3004
        """Message field 'defaults_values'."""
        return self._defaults_values

    @defaults_values.setter
    def defaults_values(self, value: collections.abc.Sequence[Defaults]) -> None:

        from collections.abc import Set
        if isinstance(value, Set):
            import warnings
            warnings.warn(
                'Using set or subclass of set is deprecated,'
                ' please use a subclass of collections.abc.Sequence like list',
                DeprecationWarning)
        if self._check_fields:
            from rosidl_generator_py.msg import Defaults
            from collections.abc import Sequence
            from collections import UserString
            assert \
                ((isinstance(value, Sequence) or
                  isinstance(value, Set)) and
                 not isinstance(value, str) and
                 not isinstance(value, UserString) and
                 len(value) <= 3 and
                 all(isinstance(v, Defaults) for v in value) and
                 True), \
                "The 'defaults_values' field must be sequence with length <= 3 and each value of type Defaults"
        self._defaults_values = value

    @builtins.property
    def bool_values_default(self) -> collections.abc.Sequence[bool]:   # typing.Annotated can be remove after mypy 1.16+ see mypy#3004
        """Message field 'bool_values_default'."""
        return self._bool_values_default

    @bool_values_default.setter
    def bool_values_default(self, value: collections.abc.Sequence[bool]) -> None:

        from collections.abc import Set
        if isinstance(value, Set):
            import warnings
            warnings.warn(
                'Using set or subclass of set is deprecated,'
                ' please use a subclass of collections.abc.Sequence like list',
                DeprecationWarning)
        if self._check_fields:
            from collections.abc import Sequence
            from collections import UserString
            assert \
                ((isinstance(value, Sequence) or
                  isinstance(value, Set)) and
                 not isinstance(value, str) and
                 not isinstance(value, UserString) and
                 len(value) <= 3 and
                 all(isinstance(v, bool) for v in value) and
                 True), \
                "The 'bool_values_default' field must be sequence with length <= 3 and each value of type bool"
        self._bool_values_default = value

    @builtins.property
    def byte_values_default(self) -> collections.abc.Sequence[bytes]:   # typing.Annotated can be remove after mypy 1.16+ see mypy#3004
        """Message field 'byte_values_default'."""
        return self._byte_values_default

    @byte_values_default.setter
    def byte_values_default(self, value: collections.abc.Sequence[bytes]) -> None:

        from collections.abc import Set
        if isinstance(value, Set):
            import warnings
            warnings.warn(
                'Using set or subclass of set is deprecated,'
                ' please use a subclass of collections.abc.Sequence like list',
                DeprecationWarning)
        if self._check_fields:
            from collections.abc import Sequence
            from collections import UserString
            assert \
                ((isinstance(value, Sequence) or
                  isinstance(value, Set)) and
                 not isinstance(value, str) and
                 not isinstance(value, UserString) and
                 len(value) <= 3 and
                 all(isinstance(v, bytes) for v in value) and
                 True), \
                "The 'byte_values_default' field must be sequence with length <= 3 and each value of type bytes"
        self._byte_values_default = value

    @builtins.property
    def char_values_default(self) -> typing.Annotated[typing.Any, array.array[int]]:   # typing.Annotated can be remove after mypy 1.16+ see mypy#3004
        """Message field 'char_values_default'."""
        return self._char_values_default

    @char_values_default.setter
    def char_values_default(self, value: typing.Union[array.array[int], collections.abc.Sequence[int]]) -> None:

        from collections.abc import Set
        if isinstance(value, Set):
            import warnings
            warnings.warn(
                'Using set or subclass of set is deprecated,'
                ' please use a subclass of collections.abc.Sequence like list',
                DeprecationWarning)
        if self._check_fields:
            if isinstance(value, array.array):
                assert value.typecode == 'B', \
                    "The 'char_values_default' array.array() must have the type code of 'B'"
                assert len(value) <= 3, \
                    "The 'char_values_default' array.array() must have a size <= 3"
            self._char_values_default = value
            return
        from collections.abc import Sequence
        from collections import UserString
        assert \
            ((isinstance(value, Sequence) or
              isinstance(value, Set)) and
             not isinstance(value, str) and
             not isinstance(value, UserString) and
             len(value) <= 3 and
             all(isinstance(v, int) for v in value) and
             all(val >= 0 and val < 256 for val in value)), \
            "The 'char_values_default' field must be sequence with length <= 3 and each value of type int and each unsigned integer in [0, 255]"
        # type ignore below fixed in mypy 1.17+ see mypy#19421
        self._char_values_default = array.array('B', value)  # type: ignore[assignment]

    @builtins.property
    def float32_values_default(self) -> typing.Annotated[typing.Any, array.array[float]]:   # typing.Annotated can be remove after mypy 1.16+ see mypy#3004
        """Message field 'float32_values_default'."""
        return self._float32_values_default

    @float32_values_default.setter
    def float32_values_default(self, value: typing.Union[array.array[float], collections.abc.Sequence[float]]) -> None:

        from collections.abc import Set
        if isinstance(value, Set):
            import warnings
            warnings.warn(
                'Using set or subclass of set is deprecated,'
                ' please use a subclass of collections.abc.Sequence like list',
                DeprecationWarning)
        if self._check_fields:
            if isinstance(value, array.array):
                assert value.typecode == 'f', \
                    "The 'float32_values_default' array.array() must have the type code of 'f'"
                assert len(value) <= 3, \
                    "The 'float32_values_default' array.array() must have a size <= 3"
            self._float32_values_default = value
            return
        from collections.abc import Sequence
        from collections import UserString
        assert \
            ((isinstance(value, Sequence) or
              isinstance(value, Set)) and
             not isinstance(value, str) and
             not isinstance(value, UserString) and
             len(value) <= 3 and
             all(isinstance(v, float) for v in value) and
             all(not (val < -3.402823466e+38 or val > 3.402823466e+38) or math.isinf(val) for val in value)), \
            "The 'float32_values_default' field must be sequence with length <= 3 and each value of type float 'and each float in [-3.402823466e+38, 3.402823466e+38]'"
        # type ignore below fixed in mypy 1.17+ see mypy#19421
        self._float32_values_default = array.array('f', value)  # type: ignore[assignment]

    @builtins.property
    def float64_values_default(self) -> typing.Annotated[typing.Any, array.array[float]]:   # typing.Annotated can be remove after mypy 1.16+ see mypy#3004
        """Message field 'float64_values_default'."""
        return self._float64_values_default

    @float64_values_default.setter
    def float64_values_default(self, value: typing.Union[array.array[float], collections.abc.Sequence[float]]) -> None:

        from collections.abc import Set
        if isinstance(value, Set):
            import warnings
            warnings.warn(
                'Using set or subclass of set is deprecated,'
                ' please use a subclass of collections.abc.Sequence like list',
                DeprecationWarning)
        if self._check_fields:
            if isinstance(value, array.array):
                assert value.typecode == 'd', \
                    "The 'float64_values_default' array.array() must have the type code of 'd'"
                assert len(value) <= 3, \
                    "The 'float64_values_default' array.array() must have a size <= 3"
            self._float64_values_default = value
            return
        from collections.abc import Sequence
        from collections import UserString
        assert \
            ((isinstance(value, Sequence) or
              isinstance(value, Set)) and
             not isinstance(value, str) and
             not isinstance(value, UserString) and
             len(value) <= 3 and
             all(isinstance(v, float) for v in value) and
             all(not (val < -1.7976931348623157e+308 or val > 1.7976931348623157e+308) or math.isinf(val) for val in value)), \
            "The 'float64_values_default' field must be sequence with length <= 3 and each value of type float 'and each double in [-1.7976931348623157e+308, 1.7976931348623157e+308]'"
        # type ignore below fixed in mypy 1.17+ see mypy#19421
        self._float64_values_default = array.array('d', value)  # type: ignore[assignment]

    @builtins.property
    def int8_values_default(self) -> typing.Annotated[typing.Any, array.array[int]]:   # typing.Annotated can be remove after mypy 1.16+ see mypy#3004
        """Message field 'int8_values_default'."""
        return self._int8_values_default

    @int8_values_default.setter
    def int8_values_default(self, value: typing.Union[array.array[int], collections.abc.Sequence[int]]) -> None:

        from collections.abc import Set
        if isinstance(value, Set):
            import warnings
            warnings.warn(
                'Using set or subclass of set is deprecated,'
                ' please use a subclass of collections.abc.Sequence like list',
                DeprecationWarning)
        if self._check_fields:
            if isinstance(value, array.array):
                assert value.typecode == 'b', \
                    "The 'int8_values_default' array.array() must have the type code of 'b'"
                assert len(value) <= 3, \
                    "The 'int8_values_default' array.array() must have a size <= 3"
            self._int8_values_default = value
            return
        from collections.abc import Sequence
        from collections import UserString
        assert \
            ((isinstance(value, Sequence) or
              isinstance(value, Set)) and
             not isinstance(value, str) and
             not isinstance(value, UserString) and
             len(value) <= 3 and
             all(isinstance(v, int) for v in value) and
             all(val >= -128 and val < 128 for val in value)), \
            "The 'int8_values_default' field must be sequence with length <= 3 and each value of type int and each integer in [-128, 127]"
        # type ignore below fixed in mypy 1.17+ see mypy#19421
        self._int8_values_default = array.array('b', value)  # type: ignore[assignment]

    @builtins.property
    def uint8_values_default(self) -> typing.Annotated[typing.Any, array.array[int]]:   # typing.Annotated can be remove after mypy 1.16+ see mypy#3004
        """Message field 'uint8_values_default'."""
        return self._uint8_values_default

    @uint8_values_default.setter
    def uint8_values_default(self, value: typing.Union[array.array[int], collections.abc.Sequence[int]]) -> None:

        from collections.abc import Set
        if isinstance(value, Set):
            import warnings
            warnings.warn(
                'Using set or subclass of set is deprecated,'
                ' please use a subclass of collections.abc.Sequence like list',
                DeprecationWarning)
        if self._check_fields:
            if isinstance(value, array.array):
                assert value.typecode == 'B', \
                    "The 'uint8_values_default' array.array() must have the type code of 'B'"
                assert len(value) <= 3, \
                    "The 'uint8_values_default' array.array() must have a size <= 3"
            self._uint8_values_default = value
            return
        from collections.abc import Sequence
        from collections import UserString
        assert \
            ((isinstance(value, Sequence) or
              isinstance(value, Set)) and
             not isinstance(value, str) and
             not isinstance(value, UserString) and
             len(value) <= 3 and
             all(isinstance(v, int) for v in value) and
             all(val >= 0 and val < 256 for val in value)), \
            "The 'uint8_values_default' field must be sequence with length <= 3 and each value of type int and each unsigned integer in [0, 255]"
        # type ignore below fixed in mypy 1.17+ see mypy#19421
        self._uint8_values_default = array.array('B', value)  # type: ignore[assignment]

    @builtins.property
    def int16_values_default(self) -> typing.Annotated[typing.Any, array.array[int]]:   # typing.Annotated can be remove after mypy 1.16+ see mypy#3004
        """Message field 'int16_values_default'."""
        return self._int16_values_default

    @int16_values_default.setter
    def int16_values_default(self, value: typing.Union[array.array[int], collections.abc.Sequence[int]]) -> None:

        from collections.abc import Set
        if isinstance(value, Set):
            import warnings
            warnings.warn(
                'Using set or subclass of set is deprecated,'
                ' please use a subclass of collections.abc.Sequence like list',
                DeprecationWarning)
        if self._check_fields:
            if isinstance(value, array.array):
                assert value.typecode == 'h', \
                    "The 'int16_values_default' array.array() must have the type code of 'h'"
                assert len(value) <= 3, \
                    "The 'int16_values_default' array.array() must have a size <= 3"
            self._int16_values_default = value
            return
        from collections.abc import Sequence
        from collections import UserString
        assert \
            ((isinstance(value, Sequence) or
              isinstance(value, Set)) and
             not isinstance(value, str) and
             not isinstance(value, UserString) and
             len(value) <= 3 and
             all(isinstance(v, int) for v in value) and
             all(val >= -32768 and val < 32768 for val in value)), \
            "The 'int16_values_default' field must be sequence with length <= 3 and each value of type int and each integer in [-32768, 32767]"
        # type ignore below fixed in mypy 1.17+ see mypy#19421
        self._int16_values_default = array.array('h', value)  # type: ignore[assignment]

    @builtins.property
    def uint16_values_default(self) -> typing.Annotated[typing.Any, array.array[int]]:   # typing.Annotated can be remove after mypy 1.16+ see mypy#3004
        """Message field 'uint16_values_default'."""
        return self._uint16_values_default

    @uint16_values_default.setter
    def uint16_values_default(self, value: typing.Union[array.array[int], collections.abc.Sequence[int]]) -> None:

        from collections.abc import Set
        if isinstance(value, Set):
            import warnings
            warnings.warn(
                'Using set or subclass of set is deprecated,'
                ' please use a subclass of collections.abc.Sequence like list',
                DeprecationWarning)
        if self._check_fields:
            if isinstance(value, array.array):
                assert value.typecode == 'H', \
                    "The 'uint16_values_default' array.array() must have the type code of 'H'"
                assert len(value) <= 3, \
                    "The 'uint16_values_default' array.array() must have a size <= 3"
            self._uint16_values_default = value
            return
        from collections.abc import Sequence
        from collections import UserString
        assert \
            ((isinstance(value, Sequence) or
              isinstance(value, Set)) and
             not isinstance(value, str) and
             not isinstance(value, UserString) and
             len(value) <= 3 and
             all(isinstance(v, int) for v in value) and
             all(val >= 0 and val < 65536 for val in value)), \
            "The 'uint16_values_default' field must be sequence with length <= 3 and each value of type int and each unsigned integer in [0, 65535]"
        # type ignore below fixed in mypy 1.17+ see mypy#19421
        self._uint16_values_default = array.array('H', value)  # type: ignore[assignment]

    @builtins.property
    def int32_values_default(self) -> typing.Annotated[typing.Any, array.array[int]]:   # typing.Annotated can be remove after mypy 1.16+ see mypy#3004
        """Message field 'int32_values_default'."""
        return self._int32_values_default

    @int32_values_default.setter
    def int32_values_default(self, value: typing.Union[array.array[int], collections.abc.Sequence[int]]) -> None:

        from collections.abc import Set
        if isinstance(value, Set):
            import warnings
            warnings.warn(
                'Using set or subclass of set is deprecated,'
                ' please use a subclass of collections.abc.Sequence like list',
                DeprecationWarning)
        if self._check_fields:
            if isinstance(value, array.array):
                assert value.typecode == 'i', \
                    "The 'int32_values_default' array.array() must have the type code of 'i'"
                assert len(value) <= 3, \
                    "The 'int32_values_default' array.array() must have a size <= 3"
            self._int32_values_default = value
            return
        from collections.abc import Sequence
        from collections import UserString
        assert \
            ((isinstance(value, Sequence) or
              isinstance(value, Set)) and
             not isinstance(value, str) and
             not isinstance(value, UserString) and
             len(value) <= 3 and
             all(isinstance(v, int) for v in value) and
             all(val >= -2147483648 and val < 2147483648 for val in value)), \
            "The 'int32_values_default' field must be sequence with length <= 3 and each value of type int and each integer in [-2147483648, 2147483647]"
        # type ignore below fixed in mypy 1.17+ see mypy#19421
        self._int32_values_default = array.array('i', value)  # type: ignore[assignment]

    @builtins.property
    def uint32_values_default(self) -> typing.Annotated[typing.Any, array.array[int]]:   # typing.Annotated can be remove after mypy 1.16+ see mypy#3004
        """Message field 'uint32_values_default'."""
        return self._uint32_values_default

    @uint32_values_default.setter
    def uint32_values_default(self, value: typing.Union[array.array[int], collections.abc.Sequence[int]]) -> None:

        from collections.abc import Set
        if isinstance(value, Set):
            import warnings
            warnings.warn(
                'Using set or subclass of set is deprecated,'
                ' please use a subclass of collections.abc.Sequence like list',
                DeprecationWarning)
        if self._check_fields:
            if isinstance(value, array.array):
                assert value.typecode == 'I', \
                    "The 'uint32_values_default' array.array() must have the type code of 'I'"
                assert len(value) <= 3, \
                    "The 'uint32_values_default' array.array() must have a size <= 3"
            self._uint32_values_default = value
            return
        from collections.abc import Sequence
        from collections import UserString
        assert \
            ((isinstance(value, Sequence) or
              isinstance(value, Set)) and
             not isinstance(value, str) and
             not isinstance(value, UserString) and
             len(value) <= 3 and
             all(isinstance(v, int) for v in value) and
             all(val >= 0 and val < 4294967296 for val in value)), \
            "The 'uint32_values_default' field must be sequence with length <= 3 and each value of type int and each unsigned integer in [0, 4294967295]"
        # type ignore below fixed in mypy 1.17+ see mypy#19421
        self._uint32_values_default = array.array('I', value)  # type: ignore[assignment]

    @builtins.property
    def int64_values_default(self) -> typing.Annotated[typing.Any, array.array[int]]:   # typing.Annotated can be remove after mypy 1.16+ see mypy#3004
        """Message field 'int64_values_default'."""
        return self._int64_values_default

    @int64_values_default.setter
    def int64_values_default(self, value: typing.Union[array.array[int], collections.abc.Sequence[int]]) -> None:

        from collections.abc import Set
        if isinstance(value, Set):
            import warnings
            warnings.warn(
                'Using set or subclass of set is deprecated,'
                ' please use a subclass of collections.abc.Sequence like list',
                DeprecationWarning)
        if self._check_fields:
            if isinstance(value, array.array):
                assert value.typecode == 'q', \
                    "The 'int64_values_default' array.array() must have the type code of 'q'"
                assert len(value) <= 3, \
                    "The 'int64_values_default' array.array() must have a size <= 3"
            self._int64_values_default = value
            return
        from collections.abc import Sequence
        from collections import UserString
        assert \
            ((isinstance(value, Sequence) or
              isinstance(value, Set)) and
             not isinstance(value, str) and
             not isinstance(value, UserString) and
             len(value) <= 3 and
             all(isinstance(v, int) for v in value) and
             all(val >= -9223372036854775808 and val < 9223372036854775808 for val in value)), \
            "The 'int64_values_default' field must be sequence with length <= 3 and each value of type int and each integer in [-9223372036854775808, 9223372036854775807]"
        # type ignore below fixed in mypy 1.17+ see mypy#19421
        self._int64_values_default = array.array('q', value)  # type: ignore[assignment]

    @builtins.property
    def uint64_values_default(self) -> typing.Annotated[typing.Any, array.array[int]]:   # typing.Annotated can be remove after mypy 1.16+ see mypy#3004
        """Message field 'uint64_values_default'."""
        return self._uint64_values_default

    @uint64_values_default.setter
    def uint64_values_default(self, value: typing.Union[array.array[int], collections.abc.Sequence[int]]) -> None:

        from collections.abc import Set
        if isinstance(value, Set):
            import warnings
            warnings.warn(
                'Using set or subclass of set is deprecated,'
                ' please use a subclass of collections.abc.Sequence like list',
                DeprecationWarning)
        if self._check_fields:
            if isinstance(value, array.array):
                assert value.typecode == 'Q', \
                    "The 'uint64_values_default' array.array() must have the type code of 'Q'"
                assert len(value) <= 3, \
                    "The 'uint64_values_default' array.array() must have a size <= 3"
            self._uint64_values_default = value
            return
        from collections.abc import Sequence
        from collections import UserString
        assert \
            ((isinstance(value, Sequence) or
              isinstance(value, Set)) and
             not isinstance(value, str) and
             not isinstance(value, UserString) and
             len(value) <= 3 and
             all(isinstance(v, int) for v in value) and
             all(val >= 0 and val < 18446744073709551616 for val in value)), \
            "The 'uint64_values_default' field must be sequence with length <= 3 and each value of type int and each unsigned integer in [0, 18446744073709551615]"
        # type ignore below fixed in mypy 1.17+ see mypy#19421
        self._uint64_values_default = array.array('Q', value)  # type: ignore[assignment]

    @builtins.property
    def string_values_default(self) -> collections.abc.Sequence[str]:   # typing.Annotated can be remove after mypy 1.16+ see mypy#3004
        """Message field 'string_values_default'."""
        return self._string_values_default

    @string_values_default.setter
    def string_values_default(self, value: collections.abc.Sequence[str]) -> None:

        from collections.abc import Set
        if isinstance(value, Set):
            import warnings
            warnings.warn(
                'Using set or subclass of set is deprecated,'
                ' please use a subclass of collections.abc.Sequence like list',
                DeprecationWarning)
        if self._check_fields:
            from collections.abc import Sequence
            from collections import UserString
            assert \
                ((isinstance(value, Sequence) or
                  isinstance(value, Set)) and
                 not isinstance(value, str) and
                 not isinstance(value, UserString) and
                 len(value) <= 3 and
                 all(isinstance(v, str) for v in value) and
                 True), \
                "The 'string_values_default' field must be sequence with length <= 3 and each value of type str"
        self._string_values_default = value

    @builtins.property
    def alignment_check(self) -> int:
        """Message field 'alignment_check'."""
        return self._alignment_check

    @alignment_check.setter
    def alignment_check(self, value: int) -> None:

        if self._check_fields:
            assert \
                isinstance(value, int), \
                "The 'alignment_check' field must be of type 'int'"
            assert value >= -2147483648 and value < 2147483648, \
                "The 'alignment_check' field must be an unsigned integer in [-2147483648, 2147483647]"
        self._alignment_check = value
