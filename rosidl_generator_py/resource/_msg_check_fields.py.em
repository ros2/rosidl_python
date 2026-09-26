@{
from rosidl_parser.definition import AbstractGenericString
from rosidl_parser.definition import AbstractNestedType
from rosidl_parser.definition import AbstractSequence
from rosidl_parser.definition import Array
from rosidl_parser.definition import ACTION_FEEDBACK_SUFFIX
from rosidl_parser.definition import ACTION_GOAL_SUFFIX
from rosidl_parser.definition import ACTION_RESULT_SUFFIX
from rosidl_parser.definition import BasicType
from rosidl_parser.definition import BOOLEAN_TYPE
from rosidl_parser.definition import INTEGER_TYPES
from rosidl_parser.definition import BoundedSequence
from rosidl_parser.definition import FLOATING_POINT_TYPES
from rosidl_parser.definition import SIGNED_INTEGER_TYPES
from rosidl_parser.definition import UNSIGNED_INTEGER_TYPES
from rosidl_parser.definition import NamespacedType
from rosidl_pycommon import convert_camel_case_to_lower_case_underscore
from rosidl_generator_py.generate_py_impl import get_python_type
from rosidl_generator_py.generate_py_impl import SPECIAL_NESTED_BASIC_TYPES


def get_importable_namespaced_type(
    type_: NamespacedType,
    action_goal_suffix: str = ACTION_GOAL_SUFFIX,
    action_result_suffix: str = ACTION_RESULT_SUFFIX,
    action_feedback_suffix: str = ACTION_FEEDBACK_SUFFIX,
    camel_to_snake=convert_camel_case_to_lower_case_underscore,
) -> tuple[str, str]:
    joined_type_namespaces = '.'.join(type_.namespaces)
    if (
        type_.name.endswith(action_goal_suffix) or
        type_.name.endswith(action_result_suffix) or
        type_.name.endswith(action_feedback_suffix)
    ):
        action_name, _ = type_.name.rsplit('_', 1)
        lower_case_name = camel_to_snake(action_name)
        module_name = f'{joined_type_namespaces}._{lower_case_name}'
    else:
        module_name = joined_type_namespaces
    return module_name, f'{module_name}.{type_.name}'
}@
@{
python_type = get_python_type(type_)
if isinstance(type_, NamespacedType):
    _, python_type = get_importable_namespaced_type(type_)
}@
        if self._check_fields:
@[  if isinstance(member.type, AbstractNestedType)]@
@[    if isinstance(member.type.value_type, BasicType) and member.type.value_type.typename in SPECIAL_NESTED_BASIC_TYPES]@
@[      if isinstance(member.type, Array)]@
            if isinstance(value, numpy.ndarray):
                assert value.dtype == @(SPECIAL_NESTED_BASIC_TYPES[member.type.value_type.typename]['dtype']), \
                    "The '@(member.name)' numpy.ndarray() must have the dtype of '@(SPECIAL_NESTED_BASIC_TYPES[member.type.value_type.typename]['dtype'])'"
                assert value.size == @(member.type.size), \
                    "The '@(member.name)' numpy.ndarray() must have a size of @(member.type.size)"
@[      elif isinstance(member.type, AbstractSequence)]@
            if isinstance(value, array.array):
                assert value.typecode == '@(SPECIAL_NESTED_BASIC_TYPES[member.type.value_type.typename]['type_code'])', \
                    "The '@(member.name)' array.array() must have the type code of '@(SPECIAL_NESTED_BASIC_TYPES[member.type.value_type.typename]['type_code'])'"
@[        if isinstance(member.type, BoundedSequence)]@
                assert len(value) <= @(member.type.maximum_size), \
                    "The '@(member.name)' array.array() must have a size <= @(member.type.maximum_size)"
@[        end if]@
@[      end if]@
@[    else]@
            if False:  # Done for templating alignment
                pass
@[    end if]@
@[  else]@
            if False:  # Done for templating alignment
                pass
@[  end if]@
            else:
                assert \
@[  if isinstance(member.type, AbstractNestedType)]@
                    ((isinstance(value, collections.abc.Sequence) or
                     isinstance(value, collections.abc.Set)) and
                     not isinstance(value, str) and
                     not isinstance(value, collections.UserString) and
@{assert_msg_suffixes = ['sequence']}@
@[      if isinstance(type_, AbstractGenericString) and type_.has_maximum_size()]@
                     all(len(val) <= @(type_.maximum_size) for val in value) and
@{assert_msg_suffixes.append('and each string value not longer than %d' % type_.maximum_size)}@
@[      end if]@
@[      if isinstance(member.type, (Array, BoundedSequence))]@
@[        if isinstance(member.type, BoundedSequence)]@
                     len(value) <= @(member.type.maximum_size) and
@{assert_msg_suffixes.insert(1, 'with length <= %d' % member.type.maximum_size)}@
@[        else]@
                     len(value) == @(member.type.size) and
@{assert_msg_suffixes.insert(1, 'with length %d' % member.type.size)}@
@[        end if]@
@[      end if]@
                     all(isinstance(v, @(python_type)) for v in value) and
@{assert_msg_suffixes.append("and each value of type '%s'" % python_type)}@
@[      if isinstance(type_, BasicType) and type_.typename in SIGNED_INTEGER_TYPES]@
@{
nbits = int(type_.typename[3:])
bound = 2**(nbits - 1)
}@
                     all(val >= -@(bound) and val < @(bound) for val in value)), \
@{assert_msg_suffixes.append('and each integer in [%d, %d]' % (-bound, bound - 1))}@
@[      elif isinstance(type_, BasicType) and type_.typename in UNSIGNED_INTEGER_TYPES]@
@{
nbits = int(type_.typename[4:])
bound = 2**nbits
}@
                     all(val >= 0 and val < @(bound) for val in value)), \
@{assert_msg_suffixes.append('and each unsigned integer in [0, %d]' % (bound - 1))}@
@[      elif isinstance(type_, BasicType) and type_.typename == 'char']@
                     all(ord(val) >= 0 and ord(val) < 256 for val in value)), \
@{assert_msg_suffixes.append('and each char in [0, 255]')}@
@[      elif isinstance(type_, BasicType) and type_.typename in FLOATING_POINT_TYPES]@
@[        if type_.typename == "float"]@
@{
name = "float"
bound = 3.402823466e+38
}@
                     all(not (val < -@(bound) or val > @(bound)) or math.isinf(val) for val in value)), \
@{assert_msg_suffixes.append('and each float in [%f, %f]' % (-bound, bound))}@
@[      elif type_.typename == "double"]@
@{
name = "double"
bound = 1.7976931348623157e+308
}@
                     all(not (val < -@(bound) or val > @(bound)) or math.isinf(val) for val in value)), \
@{assert_msg_suffixes.append('and each double in [%f, %f]' % (-bound, bound))}@
@[        end if]@
@[      else]@
                     True), \
@[      end if]@
                    "The '@(member.name)' field must be @(' '.join(assert_msg_suffixes))"
@[  elif isinstance(member.type, AbstractGenericString) and member.type.has_maximum_size()]@
                    (isinstance(value, (str, collections.UserString)) and
                     len(value) <= @(member.type.maximum_size)), \
                    "The '@(member.name)' field must be string value " \
                    'not longer than @(type_.maximum_size)'
@[  elif isinstance(type_, NamespacedType)]@
                    isinstance(value, @(python_type)), \
                    "The '@(member.name)' field must be a sub message of type '@(type_.name)'"
@[  elif isinstance(type_, BasicType) and type_.typename == 'octet']@
                    (isinstance(value, (bytes, bytearray, memoryview)) and
                     len(value) == 1), \
                    "The '@(member.name)' field must be of type 'bytes' or 'ByteString' with length 1"
@[  elif isinstance(type_, BasicType) and type_.typename == 'char']@
                    (isinstance(value, (str, collections.UserString)) and
                     len(value) == 1 and ord(value) >= -128 and ord(value) < 128), \
                    "The '@(member.name)' field must be of type 'str' or 'collections.UserString' " \
                    'with length 1 and the character ord() in [-128, 127]'
@[  elif isinstance(type_, AbstractGenericString)]@
                    isinstance(value, str), \
                    "The '@(member.name)' field must be of type '@(get_python_type(type_))'"
@[  elif isinstance(type_, BasicType) and type_.typename in (BOOLEAN_TYPE, *FLOATING_POINT_TYPES, *INTEGER_TYPES)]@
                    isinstance(value, @(get_python_type(type_))), \
                    "The '@(member.name)' field must be of type '@(get_python_type(type_))'"
@[    if type_.typename in SIGNED_INTEGER_TYPES]@
@{
nbits = int(type_.typename[3:])
bound = 2**(nbits - 1)
}@
                assert value >= -@(bound) and value < @(bound), \
                    "The '@(member.name)' field must be an integer in [@(-bound), @(bound - 1)]"
@[    elif type_.typename in UNSIGNED_INTEGER_TYPES]@
@{
nbits = int(type_.typename[4:])
bound = 2**nbits
}@
                assert value >= 0 and value < @(bound), \
                    "The '@(member.name)' field must be an unsigned integer in [0, @(bound - 1)]"
@[    elif type_.typename in FLOATING_POINT_TYPES]@
@[      if type_.typename == "float"]@
@{
name = "float"
bound = 3.402823466e+38
}@
@[      elif type_.typename == "double"]@
@{
name = "double"
bound = 1.7976931348623157e+308
}@
@[      end if]@
                assert not (value < -@(bound) or value > @(bound)) or math.isinf(value), \
                    "The '@(member.name)' field must be a @(name) in [@(-bound), @(bound)]"
@[    end if]@
@[  else]@
                    False
@[  end if]@
