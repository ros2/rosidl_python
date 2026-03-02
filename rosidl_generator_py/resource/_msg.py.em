@# Included from rosidl_generator_py/resource/_idl.py.em
@{
from rosidl_pycommon import convert_camel_case_to_lower_case_underscore
from rosidl_generator_py.generate_py_impl import constant_value_to_py
from rosidl_generator_py.generate_py_impl import get_python_type
from rosidl_generator_py.generate_py_impl import get_type_annotation_constant
from rosidl_generator_py.generate_py_impl import get_type_annotation_default
from rosidl_generator_py.generate_py_impl import get_setter_and_getter_type
from rosidl_generator_py.generate_py_impl import SPECIAL_NESTED_BASIC_TYPES
from rosidl_generator_py.generate_py_impl import value_to_py
from rosidl_parser.definition import AbstractGenericString
from rosidl_parser.definition import AbstractNestedType
from rosidl_parser.definition import AbstractSequence
from rosidl_parser.definition import AbstractWString
from rosidl_parser.definition import ACTION_FEEDBACK_SUFFIX
from rosidl_parser.definition import ACTION_GOAL_SUFFIX
from rosidl_parser.definition import ACTION_RESULT_SUFFIX
from rosidl_parser.definition import SERVICE_EVENT_MESSAGE_SUFFIX
from rosidl_parser.definition import SERVICE_REQUEST_MESSAGE_SUFFIX
from rosidl_parser.definition import SERVICE_RESPONSE_MESSAGE_SUFFIX
from rosidl_parser.definition import Array
from rosidl_parser.definition import BasicType
from rosidl_parser.definition import BOOLEAN_TYPE
from rosidl_parser.definition import BoundedSequence
from rosidl_parser.definition import CHARACTER_TYPES
from rosidl_parser.definition import EMPTY_STRUCTURE_REQUIRED_MEMBER_NAME
from rosidl_parser.definition import FLOATING_POINT_TYPES
from rosidl_parser.definition import INTEGER_TYPES
from rosidl_parser.definition import NamespacedType
from rosidl_parser.definition import SIGNED_INTEGER_TYPES
from rosidl_parser.definition import UnboundedSequence
from rosidl_parser.definition import UNSIGNED_INTEGER_TYPES
}@
@{
import_type_checking = False
type_annotations_setter: dict[str, str] = {}
type_annotations_getter: dict[str, str] = {}
type_imports: set[str] = set()

for member in message.structure.members:
    setter_type, getter_type = get_setter_and_getter_type(member, type_imports)
    type_annotations_setter[member.name] = setter_type
    type_annotations_getter[member.name] = getter_type

custom_type_annotations = {}

for constant in message.constants:
    custom_type_annotations[constant.name] = get_type_annotation_constant(constant)

default_type_annotations = {}

for member in message.structure.members:
    if member.has_annotation('default'):
        default_type_annotations[member.name] = get_type_annotation_default(member)
}@
@{
suffix = '__'.join(message.structure.namespaced_type.namespaces[1:]) + '__' + convert_camel_case_to_lower_case_underscore(message.structure.namespaced_type.name)
new_typing_imports = sorted(type_imports - type_annotations_import_statements)
}@
@[if new_typing_imports]@


if typing.TYPE_CHECKING:
@[  for type_import in new_typing_imports]@
    @(type_import)  # noqa: E402, I100, I201, I300
@{
type_annotations_import_statements.add(type_import)
}@
@[  end for]@
@[end if]@
@#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
@# Collect necessary import statements for all members
@{
from collections import OrderedDict
imports = OrderedDict()
if message.structure.members:
    imports.setdefault(
        'import rosidl_parser.definition', [])  # used for SLOT_TYPES
for member in message.structure.members:
    type_ = member.type
    if isinstance(type_, AbstractNestedType):
        type_ = type_.value_type
    if member.name != EMPTY_STRUCTURE_REQUIRED_MEMBER_NAME:
        imports.setdefault(
            'import builtins', [])  # used for @builtins.property
    if isinstance(type_, BasicType) and type_.typename in FLOATING_POINT_TYPES:
        imports.setdefault(
            'import math', [])  # used for math.isinf
    if (
        isinstance(member.type, AbstractNestedType) and
        isinstance(member.type.value_type, BasicType) and
        member.type.value_type.typename in SPECIAL_NESTED_BASIC_TYPES
    ):
        if isinstance(member.type, Array):
            member_names = imports.setdefault(
                'import numpy', [])
        elif isinstance(member.type, AbstractSequence):
            member_names = imports.setdefault(
                'import array', [])
        else:
            assert False
        member_names.append(member.name)
}@
@#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
@
@#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
@[if imports]@


# Import statements for member types
@[    for import_statement, member_names in sorted(imports.items())]@

@[        for member_name in member_names]@
# Member '@(member_name)'
@[        end for]@
@[        if import_statement in import_statements]@
# already imported above
# @
@[        end if]@
@(import_statement)@
@[        if import_statement not in import_statements]@
@{import_statements.add(import_statement)}@
  # noqa: E402, I100@
@[        end if]
@[    end for]@
@[end if]@
@#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>


class Metaclass_@(message.structure.namespaced_type.name)(rosidl_pycommon.interface_base_classes.MessageTypeSupportMeta):
    """Metaclass of message '@(message.structure.namespaced_type.name)'."""

    _CREATE_ROS_MESSAGE: typing.ClassVar[typing.Optional[PyCapsule]] = None
    _CONVERT_FROM_PY: typing.ClassVar[typing.Optional[PyCapsule]] = None
    _CONVERT_TO_PY: typing.ClassVar[typing.Optional[PyCapsule]] = None
    _DESTROY_ROS_MESSAGE: typing.ClassVar[typing.Optional[PyCapsule]] = None
    _TYPE_SUPPORT: typing.ClassVar[typing.Optional[PyCapsule]] = None

    class @(message.structure.namespaced_type.name)Constants(typing.TypedDict):
@[if not custom_type_annotations]@
        pass
@[else]@
@[for constant in message.constants]@
        @(constant.name): @(custom_type_annotations[constant.name])
@[     end for]@
@[end if]@

    __constants: @(message.structure.namespaced_type.name)Constants = {
@[for constant in message.constants]@
        '@(constant.name)': @constant_value_to_py(constant.type, constant.value),
@[end for]@
    }

    @@classmethod
    def __import_type_support__(cls) -> None:
        try:
            from rosidl_generator_py import import_type_support  # type: ignore[attr-defined]
            module = import_type_support('@(package_name)')
        except ImportError:
            import logging
            import traceback
            logger = logging.getLogger(
                '@('.'.join(message.structure.namespaced_type.namespaced_name()))')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._CREATE_ROS_MESSAGE = module.create_ros_message_msg__@(suffix)
            cls._CONVERT_FROM_PY = module.convert_from_py_msg__@(suffix)
            cls._CONVERT_TO_PY = module.convert_to_py_msg__@(suffix)
            cls._TYPE_SUPPORT = module.type_support_msg__@(suffix)
            cls._DESTROY_ROS_MESSAGE = module.destroy_ros_message_msg__@(suffix)
@{
importable_typesupports = set()
for member in message.structure.members:
    type_ = member.type
    if isinstance(type_, AbstractNestedType):
        type_ = type_.value_type
    if isinstance(type_, NamespacedType):
        if (
            type_.name.endswith(SERVICE_RESPONSE_MESSAGE_SUFFIX) or
            type_.name.endswith(SERVICE_REQUEST_MESSAGE_SUFFIX)
        ):
            continue
        if (
            type_.name.endswith(ACTION_GOAL_SUFFIX) or
            type_.name.endswith(ACTION_RESULT_SUFFIX) or
            type_.name.endswith(ACTION_FEEDBACK_SUFFIX)
        ):
            action_name, suffix = type_.name.rsplit('_', 1)
            typename = (*type_.namespaces, action_name, action_name + '.' + suffix)
        else:
            typename = (*type_.namespaces, type_.name, type_.name)
        importable_typesupports.add(typename)
}@
@[for typename in sorted(importable_typesupports)]@

            from @('.'.join(typename[:-2])) import @(typename[-2])
            if @(typename[-1])._TYPE_SUPPORT is None:
                @(typename[-1]).__import_type_support__()
@[end for]@

    @@classmethod
    def __prepare__(metacls, name: str, bases: tuple[type[typing.Any], ...], /, **kwds: typing.Any) -> collections.abc.MutableMapping[str, object]:
        # list constant names here so that they appear in the help text of
        # the message class under "Data and other attributes defined here:"
        # as well as populate each message instance
        return {
@[for constant in message.constants]@
            '@(constant.name)': metacls.__constants['@(constant.name)'],
@[end for]@
@[for member in message.structure.members]@
@[  if member.has_annotation('default')]@
            '@(member.name.upper())__DEFAULT': @(value_to_py(member.type, member.get_annotation_value('default')['value'])),
@[  end if]@
@[end for]@
        }
@[for constant in message.constants]@

    @@property
    def @(constant.name)(self) -> @(custom_type_annotations[constant.name]):
        """Message constant '@(constant.name)'."""
        return Metaclass_@(message.structure.namespaced_type.name).__constants['@(constant.name)']
@[end for]@
@[for member in message.structure.members]@
@[  if member.has_annotation('default')]@

    @@property
    def @(member.name.upper())__DEFAULT(cls) -> @(default_type_annotations[member.name]):
        """Return default value for message field '@(member.name)'."""
        return @(value_to_py(member.type, member.get_annotation_value('default')['value']))
@[  end if]@
@[end for]@


class @(message.structure.namespaced_type.name)(rosidl_pycommon.interface_base_classes.BaseMessage, metaclass=Metaclass_@(message.structure.namespaced_type.name)):
@[if not message.constants]@
    """Message class '@(message.structure.namespaced_type.name)'."""
@[else]@
    """
    Message class '@(message.structure.namespaced_type.name)'.

    Constants:
@[  for constant_name in [c.name for c in message.constants]]@
      @(constant_name)
@[  end for]@
    """
@[end if]@

    __slots__ = [
@[for member in message.structure.members]@
@[  if len(message.structure.members) == 1 and member.name == EMPTY_STRUCTURE_REQUIRED_MEMBER_NAME]@
@[    continue]@
@[  end if]@
        '_@(member.name)',
@[end for]@
        '_check_fields',
    ]

    _fields_and_field_types: dict[str, str] = {
@[for member in message.structure.members]@
@[  if len(message.structure.members) == 1 and member.name == EMPTY_STRUCTURE_REQUIRED_MEMBER_NAME]@
@[    continue]@
@[  end if]@
@{
type_ = member.type
if isinstance(type_, AbstractNestedType):
    type_ = type_.value_type
}@
        '@(member.name)': '@
@# the prefix for nested types
@[  if isinstance(member.type, AbstractSequence)]@
sequence<@
@[  end if]@
@# the typename of the non-nested type or the nested basetype
@[  if isinstance(type_, BasicType)]@
@(type_.typename)@
@[  elif isinstance(type_, AbstractGenericString)]@
@
@[    if isinstance(type_, AbstractWString)]@
w@
@[    end if]@
string@
@[    if type_.has_maximum_size()]@
<@(type_.maximum_size)>@
@[    end if]@
@[  elif isinstance(type_, NamespacedType)]@
@('/'.join([type_.namespaces[0], type_.name]))@
@[  end if]@
@# the suffix for nested types
@[  if isinstance(member.type, AbstractSequence)]@
@[    if isinstance(member.type, BoundedSequence)]@
, @(member.type.maximum_size)@
@[    end if]@
>@
@[  elif isinstance(member.type, Array)]@
[@(member.type.size)]@
@[  end if]@
',
@[end for]@
    }

    # This attribute is used to store an rosidl_parser.definition variable
    # related to the data type of each of the components the message.
    SLOT_TYPES: tuple[rosidl_parser.definition.AbstractType, ...] = (
@[for member in message.structure.members]@
@[  if len(message.structure.members) == 1 and member.name == EMPTY_STRUCTURE_REQUIRED_MEMBER_NAME]@
@[    continue]@
@[  end if]@
@{
type_ = member.type
if isinstance(type_, AbstractNestedType):
    type_ = type_.value_type
}@
        @
@[  if isinstance(member.type, AbstractNestedType)]@
@(member.type.__class__.__module__).@(member.type.__class__.__name__)(@
@[  end if]@
@# the typename of the non-nested type or the nested value_type
@(type_.__class__.__module__).@(type_.__class__.__name__)(@
@[  if isinstance(type_, BasicType)]@
'@(type_.typename)'@
@[  elif isinstance(type_, AbstractGenericString) and type_.has_maximum_size()]@
@(type_.maximum_size)@
@[  elif isinstance(type_, NamespacedType)]@
[@(', '.join("'%s'" % n for n in type_.namespaces))], '@(type_.name)'@
@[  end if]@
)@
@[  if isinstance(member.type, Array)]@
, @(member.type.size)@
@[  elif isinstance(member.type, BoundedSequence)]@
, @(member.type.maximum_size)@
@[  end if]@
@[  if isinstance(member.type, AbstractNestedType)]@
)@
@[  end if]@
,  # noqa: E501
@[end for]@
    )

    def __init__(self, *,
@[for member in message.structure.members]@
@[  if len(message.structure.members) == 1 and member.name == EMPTY_STRUCTURE_REQUIRED_MEMBER_NAME]@
@[    continue]@
@[  end if]@
@{
import inspect
import builtins
noqa_string = ''
if member.name in dict(inspect.getmembers(builtins)).keys():
    noqa_string = ', A002'
}@
                 @(member.name): typing.Optional[@(type_annotations_setter[member.name])] = None,  # noqa: E501@(noqa_string)
@[end for]@
                 check_fields: typing.Optional[bool] = None) -> None:
        if check_fields is not None:
            self._check_fields = check_fields
        else:
            self._check_fields = ros_python_check_fields == '1'
@[for member in message.structure.members]@
@[  if len(message.structure.members) == 1 and member.name == EMPTY_STRUCTURE_REQUIRED_MEMBER_NAME]@
@[    continue]@
@[  end if]@
@{
type_ = member.type
if isinstance(type_, AbstractNestedType):
    type_ = type_.value_type
}@
@[  if member.has_annotation('default')]@
        self.@(member.name) = @(member.name) if @(member.name) is not None else @(message.structure.namespaced_type.name).@(member.name.upper())__DEFAULT
@[  else]@
@[    if isinstance(type_, NamespacedType) and not isinstance(member.type, AbstractSequence)]@
@[      if (
            type_.name.endswith(ACTION_GOAL_SUFFIX) or
            type_.name.endswith(ACTION_RESULT_SUFFIX) or
            type_.name.endswith(ACTION_FEEDBACK_SUFFIX)
        )]@
        from @('.'.join(type_.namespaces))._@(convert_camel_case_to_lower_case_underscore(type_.name.rsplit('_', 1)[0])) import @(type_.name)
@[      else]@
        from @('.'.join(type_.namespaces)) import @(type_.name)
@[      end if]@
@[    end if]@
@[    if isinstance(member.type, Array)]@
@[      if isinstance(type_, BasicType) and type_.typename == 'octet']@
        self.@(member.name) = @(member.name) if @(member.name) is not None else [bytes([0]) for x in range(@(member.type.size))]
@[      elif isinstance(type_, BasicType) and type_.typename in CHARACTER_TYPES]@
        self.@(member.name) = @(member.name) if @(member.name) is not None else [chr(0) for x in range(@(member.type.size))]
@[      else]@
@[        if isinstance(member.type.value_type, BasicType) and member.type.value_type.typename in SPECIAL_NESTED_BASIC_TYPES]@
        if @(member.name) is None:
            self.@(member.name) = numpy.zeros(@(member.type.size), dtype=@(SPECIAL_NESTED_BASIC_TYPES[member.type.value_type.typename]['dtype']))
        else:
            self.@(member.name) = @(member.name)
@[        else]@
        self.@(member.name) = @(member.name) if @(member.name) is not None else [@(get_python_type(type_))() for x in range(@(member.type.size))]
@[        end if]@
@[      end if]@
@[    elif isinstance(member.type, AbstractSequence)]@
@[      if isinstance(member.type.value_type, BasicType) and member.type.value_type.typename in SPECIAL_NESTED_BASIC_TYPES]@
        self.@(member.name) = @(member.name) if @(member.name) is not None else array.array('@(SPECIAL_NESTED_BASIC_TYPES[member.type.value_type.typename]['type_code'])', [])
@[      else]@
        self.@(member.name) = @(member.name) if @(member.name) is not None else []
@[      end if]@
@[    elif isinstance(type_, BasicType) and type_.typename == 'octet']@
        self.@(member.name) = @(member.name) if @(member.name) is not None else bytes([0])
@[    elif isinstance(type_, BasicType) and type_.typename in CHARACTER_TYPES]@
        self.@(member.name) = @(member.name) if @(member.name) is not None else chr(0)
@[    else]@
        self.@(member.name) = @(member.name) if @(member.name) is not None else @(get_python_type(type_))()
@[    end if]@
@[  end if]@
@[end for]@

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
                t.value_type.typename in @([*SPECIAL_NESTED_BASIC_TYPES])
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
        if not isinstance(other, @(message.structure.namespaced_type.name)):
            return False
@[for member in message.structure.members]@
@[  if len(message.structure.members) == 1 and member.name == EMPTY_STRUCTURE_REQUIRED_MEMBER_NAME]@
@[    continue]@
@[  end if]@
@[  if isinstance(member.type, Array) and isinstance(member.type.value_type, BasicType) and member.type.value_type.typename in SPECIAL_NESTED_BASIC_TYPES]@
        if any(self.@(member.name) != other.@(member.name)):
@[  else]@
        if self.@(member.name) != other.@(member.name):
@[  end if]@
            return False
@[end for]@
        return True

    @@classmethod
    def get_fields_and_field_types(cls) -> dict[str, str]:
        from copy import copy
        return copy(cls._fields_and_field_types)
@[for member in message.structure.members]@
@[  if len(message.structure.members) == 1 and member.name == EMPTY_STRUCTURE_REQUIRED_MEMBER_NAME]@
@[    continue]@
@[  end if]@

@{
type_ = member.type
if isinstance(type_, AbstractNestedType):
    type_ = type_.value_type

noqa_string = ''
if member.name in dict(inspect.getmembers(builtins)).keys():
    noqa_string = '  # noqa: A003'

array_type_commment = ''
if isinstance(member.type, (Array, AbstractSequence)):
    array_type_commment = '   # typing.Annotated can be remove after mypy 1.16+ see mypy#3004'
}@
    @@builtins.property@(noqa_string)
    def @(member.name)(self) -> @(type_annotations_getter[member.name]):@(noqa_string)@(array_type_commment)
        """Message field '@(member.name)'."""
        return self._@(member.name)

    @@@(member.name).setter@(noqa_string)
    def @(member.name)(self, value: @(type_annotations_setter[member.name])) -> None:@(noqa_string)
@[  if isinstance(member.type, AbstractNestedType)]@
        if isinstance(value, collections.abc.Set):
            import warnings
            warnings.warn(
                'Using set or subclass of set is deprecated,'
                ' please use a subclass of collections.abc.Sequence like list',
                DeprecationWarning)
@[  end if]@
@[  if isinstance(type_, NamespacedType)]@
@[      if (
            type_.name.endswith(ACTION_GOAL_SUFFIX) or
            type_.name.endswith(ACTION_RESULT_SUFFIX) or
            type_.name.endswith(ACTION_FEEDBACK_SUFFIX)
        )]@
        from @('.'.join(type_.namespaces))._@(convert_camel_case_to_lower_case_underscore(type_.name.rsplit('_', 1)[0])) import @(type_.name)
@[      else]@
        from @('.'.join(type_.namespaces)) import @(type_.name)
@[      end if]@
@[  end if]@

@{
TEMPLATE(
    '_msg_check_fields.py.em',
    member=member,
    type_=type_,
)
}@

@[  if isinstance(member.type, AbstractNestedType)]@
@[    if isinstance(member.type.value_type, BasicType) and member.type.value_type.typename in SPECIAL_NESTED_BASIC_TYPES]@
@[      if isinstance(member.type, Array)]@
        if isinstance(value, numpy.ndarray):
@[      elif isinstance(member.type, AbstractSequence)]@
        if isinstance(value, array.array):
@[      end if]@
@[    else]@
        if isinstance(value, list):
@[    end if]@
            self._@(member.name) = value
            return
@[  end if]@
@[  if isinstance(member.type, AbstractNestedType)]@
@[    if isinstance(member.type.value_type, BasicType) and member.type.value_type.typename in SPECIAL_NESTED_BASIC_TYPES]@
@[      if isinstance(member.type, Array)]@
        self._@(member.name) = numpy.array(value, dtype=@(SPECIAL_NESTED_BASIC_TYPES[member.type.value_type.typename]['dtype']))
@[      elif isinstance(member.type, AbstractSequence)]@
        # type ignore below fixed in mypy 1.17+ see mypy#19421
        self._@(member.name) = array.array('@(SPECIAL_NESTED_BASIC_TYPES[member.type.value_type.typename]['type_code'])', value)  # type: ignore[assignment]
@[      end if]@
@[    else]@
        self._@(member.name) = list(value)
@[    end if]@
@[  else]@
        self._@(member.name) = value
@[  end if]@
@[end for]@
