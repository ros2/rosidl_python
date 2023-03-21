# generated from rosidl_generator_py/resource/_idl.py.em
# with input from example_msgs:srv/CustomCall.idl
# generated code does not contain a copyright notice


# Import statements for member types

import builtins  # noqa: E402, I100

import example_msgs._example_msgs_bases as _bases  # noqa: E402, I100

import rosidl_parser.definition  # noqa: E402, I100


class Metaclass_CustomCall_Request(type):
    """Metaclass of message 'CustomCall_Request'."""

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
            '_my_param',
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
                'example_msgs.srv.CustomCall_Request')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._CREATE_ROS_MESSAGE = module.create_ros_message_msg__srv__custom_call__request
            cls._CONVERT_FROM_PY = module.convert_from_py_msg__srv__custom_call__request
            cls._CONVERT_TO_PY = module.convert_to_py_msg__srv__custom_call__request
            cls._TYPE_SUPPORT = module.type_support_msg__srv__custom_call__request
            cls._DESTROY_ROS_MESSAGE = module.destroy_ros_message_msg__srv__custom_call__request

    @classmethod
    def __prepare__(cls, name, bases, **kwargs):
        # list constant names here so that they appear in the help text of
        # the message class under "Data and other attributes defined here:"
        # as well as populate each message instance
        return {
        }


class CustomCall_Request(_bases.CustomCall_RequestBase, metaclass=Metaclass_CustomCall_Request):
    """Message class 'CustomCall_Request'."""

    # This field is modified after class creation.
    # See the comment to Metaclass_CustomCall_Request.__new__
    __slots__ = []

    _fields_and_field_types = {
        'my_param': 'int32',
    }

    SLOT_TYPES = (
        rosidl_parser.definition.BasicType('int32'),  # noqa: E501
    )

    def __init__(self, **kwargs):
        assert all('_' + key in self.__slots__ for key in kwargs.keys()), \
            'Invalid arguments passed to constructor: %s' % \
            ', '.join(sorted(k for k in kwargs.keys() if '_' + k not in self.__slots__))
        self.my_param = kwargs.get('my_param', int())

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
        if self.my_param != other.my_param:
            return False
        return True

    @classmethod
    def get_fields_and_field_types(cls):
        from copy import copy
        return copy(cls._fields_and_field_types)

    @builtins.property
    def my_param(self):
        """Message field 'my_param'."""
        return self._my_param

    @my_param.setter
    def my_param(self, value):
        if __debug__:
            assert \
                isinstance(value, int), \
                "The 'my_param' field must be of type 'int'"
            assert value >= -2147483648 and value < 2147483648, \
                "The 'my_param' field must be an integer in [-2147483648, 2147483647]"
        self._my_param = value


# Import statements for member types

# already imported above
# import builtins

# already imported above
# import example_msgs._example_msgs_bases as _bases

# already imported above
# import rosidl_parser.definition


class Metaclass_CustomCall_Response(type):
    """Metaclass of message 'CustomCall_Response'."""

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
            '_my_result',
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
                'example_msgs.srv.CustomCall_Response')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._CREATE_ROS_MESSAGE = module.create_ros_message_msg__srv__custom_call__response
            cls._CONVERT_FROM_PY = module.convert_from_py_msg__srv__custom_call__response
            cls._CONVERT_TO_PY = module.convert_to_py_msg__srv__custom_call__response
            cls._TYPE_SUPPORT = module.type_support_msg__srv__custom_call__response
            cls._DESTROY_ROS_MESSAGE = module.destroy_ros_message_msg__srv__custom_call__response

    @classmethod
    def __prepare__(cls, name, bases, **kwargs):
        # list constant names here so that they appear in the help text of
        # the message class under "Data and other attributes defined here:"
        # as well as populate each message instance
        return {
        }


class CustomCall_Response(_bases.CustomCall_ResponseBase, metaclass=Metaclass_CustomCall_Response):
    """Message class 'CustomCall_Response'."""

    # This field is modified after class creation.
    # See the comment to Metaclass_CustomCall_Response.__new__
    __slots__ = []

    _fields_and_field_types = {
        'my_result': 'int32',
    }

    SLOT_TYPES = (
        rosidl_parser.definition.BasicType('int32'),  # noqa: E501
    )

    def __init__(self, **kwargs):
        assert all('_' + key in self.__slots__ for key in kwargs.keys()), \
            'Invalid arguments passed to constructor: %s' % \
            ', '.join(sorted(k for k in kwargs.keys() if '_' + k not in self.__slots__))
        self.my_result = kwargs.get('my_result', int())

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
        if self.my_result != other.my_result:
            return False
        return True

    @classmethod
    def get_fields_and_field_types(cls):
        from copy import copy
        return copy(cls._fields_and_field_types)

    @builtins.property
    def my_result(self):
        """Message field 'my_result'."""
        return self._my_result

    @my_result.setter
    def my_result(self, value):
        if __debug__:
            assert \
                isinstance(value, int), \
                "The 'my_result' field must be of type 'int'"
            assert value >= -2147483648 and value < 2147483648, \
                "The 'my_result' field must be an integer in [-2147483648, 2147483647]"
        self._my_result = value


# Import statements for member types

# already imported above
# import builtins

# already imported above
# import example_msgs._example_msgs_bases as _bases

# already imported above
# import rosidl_parser.definition


class Metaclass_CustomCall_Event(type):
    """Metaclass of message 'CustomCall_Event'."""

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
            '_info',
            '_request',
            '_response',
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
                'example_msgs.srv.CustomCall_Event')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._CREATE_ROS_MESSAGE = module.create_ros_message_msg__srv__custom_call__event
            cls._CONVERT_FROM_PY = module.convert_from_py_msg__srv__custom_call__event
            cls._CONVERT_TO_PY = module.convert_to_py_msg__srv__custom_call__event
            cls._TYPE_SUPPORT = module.type_support_msg__srv__custom_call__event
            cls._DESTROY_ROS_MESSAGE = module.destroy_ros_message_msg__srv__custom_call__event

            from service_msgs.msg import ServiceEventInfo
            if ServiceEventInfo.__class__._TYPE_SUPPORT is None:
                ServiceEventInfo.__class__.__import_type_support__()

    @classmethod
    def __prepare__(cls, name, bases, **kwargs):
        # list constant names here so that they appear in the help text of
        # the message class under "Data and other attributes defined here:"
        # as well as populate each message instance
        return {
        }


class CustomCall_Event(_bases.CustomCall_EventBase, metaclass=Metaclass_CustomCall_Event):
    """Message class 'CustomCall_Event'."""

    # This field is modified after class creation.
    # See the comment to Metaclass_CustomCall_Event.__new__
    __slots__ = []

    _fields_and_field_types = {
        'info': 'service_msgs/ServiceEventInfo',
        'request': 'sequence<example_msgs/CustomCall_Request, 1>',
        'response': 'sequence<example_msgs/CustomCall_Response, 1>',
    }

    SLOT_TYPES = (
        rosidl_parser.definition.NamespacedType(['service_msgs', 'msg'], 'ServiceEventInfo'),  # noqa: E501
        rosidl_parser.definition.BoundedSequence(rosidl_parser.definition.NamespacedType(['example_msgs', 'srv'], 'CustomCall_Request'), 1),  # noqa: E501
        rosidl_parser.definition.BoundedSequence(rosidl_parser.definition.NamespacedType(['example_msgs', 'srv'], 'CustomCall_Response'), 1),  # noqa: E501
    )

    def __init__(self, **kwargs):
        assert all('_' + key in self.__slots__ for key in kwargs.keys()), \
            'Invalid arguments passed to constructor: %s' % \
            ', '.join(sorted(k for k in kwargs.keys() if '_' + k not in self.__slots__))
        from service_msgs.msg import ServiceEventInfo
        self.info = kwargs.get('info', ServiceEventInfo())
        self.request = kwargs.get('request', [])
        self.response = kwargs.get('response', [])

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
        if self.info != other.info:
            return False
        if self.request != other.request:
            return False
        if self.response != other.response:
            return False
        return True

    @classmethod
    def get_fields_and_field_types(cls):
        from copy import copy
        return copy(cls._fields_and_field_types)

    @builtins.property
    def info(self):
        """Message field 'info'."""
        return self._info

    @info.setter
    def info(self, value):
        if __debug__:
            from service_msgs.msg import ServiceEventInfo
            assert \
                isinstance(value, ServiceEventInfo), \
                "The 'info' field must be a sub message of type 'ServiceEventInfo'"
        self._info = value

    @builtins.property
    def request(self):
        """Message field 'request'."""
        return self._request

    @request.setter
    def request(self, value):
        if __debug__:
            from example_msgs.srv import CustomCall_Request
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
                 len(value) <= 1 and
                 all(isinstance(v, CustomCall_Request) for v in value) and
                 True), \
                "The 'request' field must be a set or sequence with length <= 1 and each value of type 'CustomCall_Request'"
        self._request = value

    @builtins.property
    def response(self):
        """Message field 'response'."""
        return self._response

    @response.setter
    def response(self, value):
        if __debug__:
            from example_msgs.srv import CustomCall_Response
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
                 len(value) <= 1 and
                 all(isinstance(v, CustomCall_Response) for v in value) and
                 True), \
                "The 'response' field must be a set or sequence with length <= 1 and each value of type 'CustomCall_Response'"
        self._response = value


class Metaclass_CustomCall(type):
    """Metaclass of service 'CustomCall'."""

    _TYPE_SUPPORT = None

    @classmethod
    def __import_type_support__(cls):
        try:
            from rosidl_generator_py import import_type_support
            module = import_type_support('example_msgs')
        except ImportError:
            import logging
            import traceback
            logger = logging.getLogger(
                'example_msgs.srv.CustomCall')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._TYPE_SUPPORT = module.type_support_srv__srv__custom_call

            from example_msgs.srv import _custom_call
            if _custom_call.Metaclass_CustomCall_Request._TYPE_SUPPORT is None:
                _custom_call.Metaclass_CustomCall_Request.__import_type_support__()
            if _custom_call.Metaclass_CustomCall_Response._TYPE_SUPPORT is None:
                _custom_call.Metaclass_CustomCall_Response.__import_type_support__()
            if _custom_call.Metaclass_CustomCall_Event._TYPE_SUPPORT is None:
                _custom_call.Metaclass_CustomCall_Event.__import_type_support__()


class CustomCall(metaclass=Metaclass_CustomCall):
    from example_msgs.srv._custom_call import CustomCall_Request as Request
    from example_msgs.srv._custom_call import CustomCall_Response as Response
    from example_msgs.srv._custom_call import CustomCall_Event as Event

    def __init__(self):
        raise NotImplementedError('Service classes can not be instantiated')
