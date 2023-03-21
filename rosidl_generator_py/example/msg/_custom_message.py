# generated from rosidl_generator_py/resource/_idl.py.em
# with input from example_msgs:msg/CustomMessage.idl
# generated code does not contain a copyright notice


# Import statements for member types

# Member 'limited_seq'
# Member 'unlimited_seq'
import array  # noqa: E402, I100

import builtins  # noqa: E402, I100

import example_msgs._example_msgs_bases as _bases  # noqa: E402, I100

# Member 'fixed_seq'
import numpy  # noqa: E402, I100

import rosidl_parser.definition  # noqa: E402, I100


class Metaclass_CustomMessage(type):
    """Metaclass of message 'CustomMessage'."""

    _CREATE_ROS_MESSAGE = None
    _CONVERT_FROM_PY = None
    _CONVERT_TO_PY = None
    _DESTROY_ROS_MESSAGE = None
    _TYPE_SUPPORT = None

    __constants = {
    }

    def __new__(cls, *args):
        new_type = super().__new__(cls, *args)

        # Ugly hack here.
        # There are two purposes for __slots__ field of message class:
        #   1) __slots__ field is used in ROS as a list of message members.
        #      Number of ROS packages rely on its value.
        #   2) defining __slots__ in Python class prevents adding __dict__
        #      to class instances. This behvior is desirable.
        # If #1 defined in message class body, then base class member descriptors are
        # overriden and no longer can be used. On the other side, any __slots__ value
        # should be defined to guaratee #2.
        # So we define empty list in message class body and modify it after type object
        # constructed. This is neither prohibited, nor encouraged by CPython documentation.
        new_type.__slots__ += [
            '_x',
            '_ts',
            '_fixed_seq',
            '_limited_seq',
            '_unlimited_seq',
        ]
        return new_type

    @classmethod
    def __import_type_support__(cls):
        try:
            from rosidl_generator_py import import_type_support
            module = import_type_support('example_msgs')
        except ImportError:
            import logging
            import traceback
            logger = logging.getLogger(
                'example_msgs.msg.CustomMessage')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._CREATE_ROS_MESSAGE = module.create_ros_message_msg__msg__custom_message
            cls._CONVERT_FROM_PY = module.convert_from_py_msg__msg__custom_message
            cls._CONVERT_TO_PY = module.convert_to_py_msg__msg__custom_message
            cls._TYPE_SUPPORT = module.type_support_msg__msg__custom_message
            cls._DESTROY_ROS_MESSAGE = module.destroy_ros_message_msg__msg__custom_message

            from builtin_interfaces.msg import Time
            if Time.__class__._TYPE_SUPPORT is None:
                Time.__class__.__import_type_support__()

    @classmethod
    def __prepare__(cls, name, bases, **kwargs):
        # list constant names here so that they appear in the help text of
        # the message class under "Data and other attributes defined here:"
        # as well as populate each message instance
        return {
        }


class CustomMessage(_bases.CustomMessageBase, metaclass=Metaclass_CustomMessage):
    """Message class 'CustomMessage'."""

    # This field is modified after class creation.
    # See the comment to Metaclass_CustomMessage.__new__
    __slots__ = []

    _fields_and_field_types = {
        'x': 'uint16',
        'ts': 'builtin_interfaces/Time',
        'fixed_seq': 'int16[3]',
        'limited_seq': 'sequence<int16, 3>',
        'unlimited_seq': 'sequence<int16>',
    }

    SLOT_TYPES = (
        rosidl_parser.definition.BasicType('uint16'),  # noqa: E501
        rosidl_parser.definition.NamespacedType(['builtin_interfaces', 'msg'], 'Time'),  # noqa: E501
        rosidl_parser.definition.Array(rosidl_parser.definition.BasicType('int16'), 3),  # noqa: E501
        rosidl_parser.definition.BoundedSequence(rosidl_parser.definition.BasicType('int16'), 3),  # noqa: E501
        rosidl_parser.definition.UnboundedSequence(rosidl_parser.definition.BasicType('int16')),  # noqa: E501
    )

    def __init__(self, **kwargs):
        assert all('_' + key in self.__slots__ for key in kwargs.keys()), \
            'Invalid arguments passed to constructor: %s' % \
            ', '.join(sorted(k for k in kwargs.keys() if '_' + k not in self.__slots__))
        self.x = kwargs.get('x', int())
        from builtin_interfaces.msg import Time
        self.ts = kwargs.get('ts', Time())
        if 'fixed_seq' not in kwargs:
            self.fixed_seq = numpy.zeros(3, dtype=numpy.int16)
        else:
            self.fixed_seq = numpy.array(kwargs.get('fixed_seq'), dtype=numpy.int16)
            assert self.fixed_seq.shape == (3, )
        self.limited_seq = array.array('h', kwargs.get('limited_seq', []))
        self.unlimited_seq = array.array('h', kwargs.get('unlimited_seq', []))

    def __repr__(self):
        typename = self.__class__.__module__.split('.')
        typename.pop()
        typename.append(self.__class__.__name__)
        args = []
        for s, t in zip(self.__slots__, self.SLOT_TYPES):
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
                    assert fieldstr.startswith('array(')
                    prefix = "array('X', "
                    suffix = ')'
                    fieldstr = fieldstr[len(prefix):-len(suffix)]
            args.append(s[1:] + '=' + fieldstr)
        return '%s(%s)' % ('.'.join(typename), ', '.join(args))

    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return False
        if self.x != other.x:
            return False
        if self.ts != other.ts:
            return False
        if all(self.fixed_seq != other.fixed_seq):
            return False
        if self.limited_seq != other.limited_seq:
            return False
        if self.unlimited_seq != other.unlimited_seq:
            return False
        return True

    @classmethod
    def get_fields_and_field_types(cls):
        from copy import copy
        return copy(cls._fields_and_field_types)

    @builtins.property
    def x(self):
        """Message field 'x'."""
        return self._x

    @x.setter
    def x(self, value):
        if __debug__:
            assert \
                isinstance(value, int), \
                "The 'x' field must be of type 'int'"
            assert value >= 0 and value < 65536, \
                "The 'x' field must be an unsigned integer in [0, 65535]"
        self._x = value

    @builtins.property
    def ts(self):
        """Message field 'ts'."""
        return self._ts

    @ts.setter
    def ts(self, value):
        if __debug__:
            from builtin_interfaces.msg import Time
            assert \
                isinstance(value, Time), \
                "The 'ts' field must be a sub message of type 'Time'"
        self._ts = value

    @builtins.property
    def fixed_seq(self):
        """Message field 'fixed_seq'."""
        return self._fixed_seq

    @fixed_seq.setter
    def fixed_seq(self, value):
        if isinstance(value, numpy.ndarray):
            assert value.dtype == numpy.int16, \
                "The 'fixed_seq' numpy.ndarray() must have the dtype of 'numpy.int16'"
            assert value.size == 3, \
                "The 'fixed_seq' numpy.ndarray() must have a size of 3"
            self._fixed_seq = value
            return
        if __debug__:
            from collections.abc import Sequence
            from collections.abc import Set
            from collections import UserList
            from collections import UserString
            assert \
                ((isinstance(value, Sequence) or
                  isinstance(value, Set) or
                  isinstance(value, UserList)) and
                 not isinstance(value, str) and
                 not isinstance(value, UserString) and
                 len(value) == 3 and
                 all(isinstance(v, int) for v in value) and
                 all(val >= -32768 and val < 32768 for val in value)), \
                "The 'fixed_seq' field must be a set or sequence with length 3 and each value of type 'int' and each integer in [-32768, 32767]"
        self._fixed_seq = numpy.array(value, dtype=numpy.int16)

    @builtins.property
    def limited_seq(self):
        """Message field 'limited_seq'."""
        return self._limited_seq

    @limited_seq.setter
    def limited_seq(self, value):
        if isinstance(value, array.array):
            assert value.typecode == 'h', \
                "The 'limited_seq' array.array() must have the type code of 'h'"
            assert len(value) <= 3, \
                "The 'limited_seq' array.array() must have a size <= 3"
            self._limited_seq = value
            return
        if __debug__:
            from collections.abc import Sequence
            from collections.abc import Set
            from collections import UserList
            from collections import UserString
            assert \
                ((isinstance(value, Sequence) or
                  isinstance(value, Set) or
                  isinstance(value, UserList)) and
                 not isinstance(value, str) and
                 not isinstance(value, UserString) and
                 len(value) <= 3 and
                 all(isinstance(v, int) for v in value) and
                 all(val >= -32768 and val < 32768 for val in value)), \
                "The 'limited_seq' field must be a set or sequence with length <= 3 and each value of type 'int' and each integer in [-32768, 32767]"
        self._limited_seq = array.array('h', value)

    @builtins.property
    def unlimited_seq(self):
        """Message field 'unlimited_seq'."""
        return self._unlimited_seq

    @unlimited_seq.setter
    def unlimited_seq(self, value):
        if isinstance(value, array.array):
            assert value.typecode == 'h', \
                "The 'unlimited_seq' array.array() must have the type code of 'h'"
            self._unlimited_seq = value
            return
        if __debug__:
            from collections.abc import Sequence
            from collections.abc import Set
            from collections import UserList
            from collections import UserString
            assert \
                ((isinstance(value, Sequence) or
                  isinstance(value, Set) or
                  isinstance(value, UserList)) and
                 not isinstance(value, str) and
                 not isinstance(value, UserString) and
                 all(isinstance(v, int) for v in value) and
                 all(val >= -32768 and val < 32768 for val in value)), \
                "The 'unlimited_seq' field must be a set or sequence and each value of type 'int' and each integer in [-32768, 32767]"
        self._unlimited_seq = array.array('h', value)
