@{
from rosidl_parser.definition import AbstractGenericString
from rosidl_parser.definition import Array
from rosidl_parser.definition import BasicType
from rosidl_parser.definition import BoundedSequence
from rosidl_parser.definition import FLOATING_POINT_TYPES
from rosidl_parser.definition import SIGNED_INTEGER_TYPES
from rosidl_parser.definition import UNSIGNED_INTEGER_TYPES
from rosidl_generator_py.generate_py_impl import get_python_type
}@
@(indent)((isinstance(value, collections.abc.Sequence) or
@(indent)  isinstance(value, collections.abc.Set)) and
@(indent) not isinstance(value, str) and
@(indent) not isinstance(value, collections.UserString) and
@{assert_msg_suffixes = ['sequence']}@
@[    if isinstance(type_, AbstractGenericString) and type_.has_maximum_size()]@
@(indent) all(len(val) <= @(type_.maximum_size) for val in value) and
@{assert_msg_suffixes.append('and each string value not longer than %d' % type_.maximum_size)}@
@[    end if]@
@[    if isinstance(member.type, (Array, BoundedSequence))]@
@[      if isinstance(member.type, BoundedSequence)]@
@(indent) len(value) <= @(member.type.maximum_size) and
@{assert_msg_suffixes.insert(1, 'with length <= %d' % member.type.maximum_size)}@
@[      else]@
@(indent) len(value) == @(member.type.size) and
@{assert_msg_suffixes.insert(1, 'with length %d' % member.type.size)}@
@[      end if]@
@[    end if]@
@(indent) all(isinstance(v, @(get_python_type(type_))) for v in value) and
@{assert_msg_suffixes.append("and each value of type '%s'" % get_python_type(type_))}@
@[    if isinstance(type_, BasicType) and type_.typename in SIGNED_INTEGER_TYPES]@
@{
nbits = int(type_.typename[3:])
bound = 2**(nbits - 1)
}@
@(indent) all(val >= -@(bound) and val < @(bound) for val in value)), \
@{assert_msg_suffixes.append('and each integer in [%d, %d]' % (-bound, bound - 1))}@
@[    elif isinstance(type_, BasicType) and type_.typename in UNSIGNED_INTEGER_TYPES]@
@{
nbits = int(type_.typename[4:])
bound = 2**nbits
}@
@(indent) all(val >= 0 and val < @(bound) for val in value)), \
@{assert_msg_suffixes.append('and each unsigned integer in [0, %d]' % (bound - 1))}@
@[    elif isinstance(type_, BasicType) and type_.typename == 'char']@
@(indent) all(ord(val) >= 0 and ord(val) < 256 for val in value)), \
@{assert_msg_suffixes.append('and each char in [0, 255]')}@
@[    elif isinstance(type_, BasicType) and type_.typename in FLOATING_POINT_TYPES]@
@[      if type_.typename == "float"]@
@{
name = "float"
bound = 3.402823466e+38
}@
@(indent) all(not (val < -@(bound) or val > @(bound)) or math.isinf(val) for val in value)), \
@{assert_msg_suffixes.append('and each float in [%f, %f]' % (-bound, bound))}@
@[      elif type_.typename == "double"]@
@{
name = "double"
bound = 1.7976931348623157e+308
}@
@(indent) all(not (val < -@(bound) or val > @(bound)) or math.isinf(val) for val in value)), \
@{assert_msg_suffixes.append('and each double in [%f, %f]' % (-bound, bound))}@
@[      end if]@
@[    else]@
@(indent) True), \
@[    end if]@
@(indent)"The '@(member.name)' field must be @(' '.join(assert_msg_suffixes))"
