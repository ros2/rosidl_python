# generated from rosidl_generator_py/resource/_idl.py.em
# with input from rosidl_generator_py:msg/Constants.idl
# generated code does not contain a copyright notice

# This is being done at the module level and not on the instance level to avoid looking
# for the same variable multiple times on each instance. This variable is not supposed to
# change during runtime so it makes sense to only look for it once.
from os import getenv
import sys
from typing import Any, Callable, Dict, Literal, Optional, Tuple, TYPE_CHECKING, TypedDict

ros_python_check_fields = getenv('ROS_PYTHON_CHECK_FIELDS', default='')

if sys.version_info >= (3, 12):
    from typing import override
else:
    # Definition taking from typing_extension.
    def override(func: Callable[..., Any]) -> Callable[..., Any]:
        return func

if TYPE_CHECKING:
    from ctypes import Structure

    class PyCapsule(Structure):
        pass  # don't need to define the full structure


# Import statements for member types

import rosidl_parser.definition  # noqa: E402, I100


class Metaclass_Constants(type):
    """Metaclass of message 'Constants'."""

    _CREATE_ROS_MESSAGE: Optional['PyCapsule'] = None
    _CONVERT_FROM_PY: Optional['PyCapsule'] = None
    _CONVERT_TO_PY: Optional['PyCapsule'] = None
    _DESTROY_ROS_MESSAGE: Optional['PyCapsule'] = None
    _TYPE_SUPPORT: Optional['PyCapsule'] = None

    class ConstantsConstants(TypedDict):
        BOOL_CONST: Literal[True]
        BYTE_CONST: Literal[b'2']
        CHAR_CONST: Literal[100]
        FLOAT32_CONST: Literal[1.125]
        FLOAT64_CONST: Literal[1.125]
        INT8_CONST: Literal[-50]
        UINT8_CONST: Literal[200]
        INT16_CONST: Literal[-1000]
        UINT16_CONST: Literal[2000]
        INT32_CONST: Literal[-30000]
        UINT32_CONST: Literal[60000]
        INT64_CONST: Literal[-40000000]
        UINT64_CONST: Literal[50000000]

    __constants: ConstantsConstants = {
        'BOOL_CONST': True,
        'BYTE_CONST': b'2',
        'CHAR_CONST': 100,
        'FLOAT32_CONST': 1.125,
        'FLOAT64_CONST': 1.125,
        'INT8_CONST': -50,
        'UINT8_CONST': 200,
        'INT16_CONST': -1000,
        'UINT16_CONST': 2000,
        'INT32_CONST': -30000,
        'UINT32_CONST': 60000,
        'INT64_CONST': -40000000,
        'UINT64_CONST': 50000000,
    }

    class ConstantsDefault(ConstantsConstants):
        pass

    @classmethod
    def __import_type_support__(cls) -> None:
        try:
            from rosidl_generator_py import import_type_support
            module = import_type_support('rosidl_generator_py')
        except ImportError:
            import logging
            import traceback
            logger = logging.getLogger(
                'rosidl_generator_py.msg.Constants')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._CREATE_ROS_MESSAGE = module.create_ros_message_msg__msg__constants
            cls._CONVERT_FROM_PY = module.convert_from_py_msg__msg__constants
            cls._CONVERT_TO_PY = module.convert_to_py_msg__msg__constants
            cls._TYPE_SUPPORT = module.type_support_msg__msg__constants
            cls._DESTROY_ROS_MESSAGE = module.destroy_ros_message_msg__msg__constants

    @override
    @classmethod
    def __prepare__(cls, name: Literal['Constants'], bases: Tuple[()], **kwargs: Any) -> ConstantsDefault:
        # list constant names here so that they appear in the help text of
        # the message class under "Data and other attributes defined here:"
        # as well as populate each message instance
        return {
            'BOOL_CONST': cls.__constants['BOOL_CONST'],
            'BYTE_CONST': cls.__constants['BYTE_CONST'],
            'CHAR_CONST': cls.__constants['CHAR_CONST'],
            'FLOAT32_CONST': cls.__constants['FLOAT32_CONST'],
            'FLOAT64_CONST': cls.__constants['FLOAT64_CONST'],
            'INT8_CONST': cls.__constants['INT8_CONST'],
            'UINT8_CONST': cls.__constants['UINT8_CONST'],
            'INT16_CONST': cls.__constants['INT16_CONST'],
            'UINT16_CONST': cls.__constants['UINT16_CONST'],
            'INT32_CONST': cls.__constants['INT32_CONST'],
            'UINT32_CONST': cls.__constants['UINT32_CONST'],
            'INT64_CONST': cls.__constants['INT64_CONST'],
            'UINT64_CONST': cls.__constants['UINT64_CONST'],
        }

    @property
    def BOOL_CONST(self) -> Literal[True]:
        """Message constant 'BOOL_CONST'."""
        return Metaclass_Constants.__constants['BOOL_CONST']

    @property
    def BYTE_CONST(self) -> Literal[50]:
        """Message constant 'BYTE_CONST'."""
        return Metaclass_Constants.__constants['BYTE_CONST']

    @property
    def CHAR_CONST(self) -> Literal[100]:
        """Message constant 'CHAR_CONST'."""
        return Metaclass_Constants.__constants['CHAR_CONST']

    @property
    def FLOAT32_CONST(self) -> Literal[1.125]:
        """Message constant 'FLOAT32_CONST'."""
        return Metaclass_Constants.__constants['FLOAT32_CONST']

    @property
    def FLOAT64_CONST(self) -> Literal[1.125]:
        """Message constant 'FLOAT64_CONST'."""
        return Metaclass_Constants.__constants['FLOAT64_CONST']

    @property
    def INT8_CONST(self) -> Literal[-50]:
        """Message constant 'INT8_CONST'."""
        return Metaclass_Constants.__constants['INT8_CONST']

    @property
    def UINT8_CONST(self) -> Literal[200]:
        """Message constant 'UINT8_CONST'."""
        return Metaclass_Constants.__constants['UINT8_CONST']

    @property
    def INT16_CONST(self) -> Literal[-1000]:
        """Message constant 'INT16_CONST'."""
        return Metaclass_Constants.__constants['INT16_CONST']

    @property
    def UINT16_CONST(self) -> Literal[2000]:
        """Message constant 'UINT16_CONST'."""
        return Metaclass_Constants.__constants['UINT16_CONST']

    @property
    def INT32_CONST(self) -> Literal[-30000]:
        """Message constant 'INT32_CONST'."""
        return Metaclass_Constants.__constants['INT32_CONST']

    @property
    def UINT32_CONST(self) -> Literal[60000]:
        """Message constant 'UINT32_CONST'."""
        return Metaclass_Constants.__constants['UINT32_CONST']

    @property
    def INT64_CONST(self) -> Literal[-40000000]:
        """Message constant 'INT64_CONST'."""
        return Metaclass_Constants.__constants['INT64_CONST']

    @property
    def UINT64_CONST(self) -> Literal[50000000]:
        """Message constant 'UINT64_CONST'."""
        return Metaclass_Constants.__constants['UINT64_CONST']


class Constants(metaclass=Metaclass_Constants):
    """
    Message class 'Constants'.

    Constants:
      BOOL_CONST
      BYTE_CONST
      CHAR_CONST
      FLOAT32_CONST
      FLOAT64_CONST
      INT8_CONST
      UINT8_CONST
      INT16_CONST
      UINT16_CONST
      INT32_CONST
      UINT32_CONST
      INT64_CONST
      UINT64_CONST
    """

    __slots__ = [
        '_check_fields',
    ]

    _fields_and_field_types: Dict[str, str] = {
    }

    # This attribute is used to store an rosidl_parser.definition variable
    # related to the data type of each of the components the message.
    SLOT_TYPES: Tuple[rosidl_parser.definition.AbstractType, ...] = (
    )

    def __init__(self,
                 check_fields: Optional[bool] = None) -> None:
        if check_fields is not None:
            self._check_fields = check_fields
        else:
            self._check_fields = ros_python_check_fields == '1'

    def __repr__(self) -> str:
        typename = self.__class__.__module__.split('.')
        typename.pop()
        typename.append(self.__class__.__name__)
        args = []
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
        if not isinstance(other, self.__class__):
            return False
        return True

    @classmethod
    def get_fields_and_field_types(cls) -> Dict[str, str]:
        from copy import copy
        return copy(cls._fields_and_field_types)
