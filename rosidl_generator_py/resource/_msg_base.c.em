@# Included from rosidl_generator_py/resource/_idl_pkg_bases.c.em
@{
from rosidl_generator_py.generate_py_impl import SPECIAL_NESTED_BASIC_TYPES
from rosidl_parser.definition import AbstractNestedType
from rosidl_parser.definition import AbstractSequence
from rosidl_parser.definition import AbstractString
from rosidl_parser.definition import AbstractWString
from rosidl_parser.definition import Array
from rosidl_parser.definition import BasicType
from rosidl_parser.definition import EMPTY_STRUCTURE_REQUIRED_MEMBER_NAME
from rosidl_parser.definition import NamespacedType
from rosidl_pycommon import convert_camel_case_to_lower_case_underscore


def primitive_msg_type_to_c(type_):
    from rosidl_generator_c import BASIC_IDL_TYPES_TO_C
    from rosidl_parser.definition import AbstractString
    from rosidl_parser.definition import AbstractWString
    from rosidl_parser.definition import BasicType
    if isinstance(type_, AbstractString):
        return 'rosidl_runtime_c__String'
    if isinstance(type_, AbstractWString):
        return 'rosidl_runtime_c__U16String'
    assert isinstance(type_, BasicType)
    return BASIC_IDL_TYPES_TO_C[type_.typename]


def primitive_msg_type_to_pymember_type(type_):
    BASIC_IDL_TYPES_TO_PYMEMBER_TYPE = {
        'float': 'T_DOUBLE',
        'double': 'T_DOUBLE',
        'long double': 'T_DOUBLE',
        'char': 'T_CHAR',
        'wchar': 'T_USHORT',
        'boolean': 'T_BOOL',
        'octet': 'T_UBYTE',
        'uint8': 'T_UBYTE',
        'int8': 'T_BYTE',
        'uint16': 'T_USHORT',
        'int16': 'T_SHORT',
        'uint32': 'T_UINT',
        'int32': 'T_INT',
        'uint64': 'T_ULONGLONG',
        'int64': 'T_LONGLONG',
    }
    return BASIC_IDL_TYPES_TO_PYMEMBER_TYPE[type_.typename]


header_files = [
    'Python.h',
    'stdbool.h',
    'structmember.h',
    './_%s_decl.h' % package_name
]
}@
@[for header_file in header_files]@
@{
repeated_header_file = header_file in include_directives
}@
@[    if repeated_header_file]@
// already included above
// @
@[    else]@
@{include_directives.add(header_file)}@
@[    end if]@
@[    if '/' not in header_file]@
#include <@(header_file)>
@[    else]@
#include "@(header_file)"
@[    end if]@
@[end for]@


static struct PyMemberDef @(message.structure.namespaced_type.name)Base_members[] = {
@[for member in message.structure.members]@
@[  if len(message.structure.members) == 1 and member.name == EMPTY_STRUCTURE_REQUIRED_MEMBER_NAME]@
@[    continue]@
@[  end if]@
  {"_@(member.name)", @
@[  if isinstance(member.type, BasicType)]@
@(primitive_msg_type_to_pymember_type(member.type)), @
@[  else isinstance(member.type, AbstractGenericString)]@
T_OBJECT, @
@[  end if]@
offsetof(@(message.structure.namespaced_type.name)Base, _@(member.name)), 0, NULL},
@[end for]@
  {NULL}  /* Sentinel */
};

static void @(message.structure.namespaced_type.name)Base_dealloc(@(message.structure.namespaced_type.name)Base * self)
{
@[for member in message.structure.members]@
@[  if not isinstance(member.type, BasicType)]@
  Py_XDECREF(self->_@(member.name));
@[  end if]@
@[end for]@
  Py_TYPE(self)->tp_free((PyObject *)self);
}


static PyTypeObject @(message.structure.namespaced_type.name)BaseType = {
  PyVarObject_HEAD_INIT(NULL, 0)
  .tp_name = "@(message.structure.namespaced_type.name)Base",
  .tp_doc = "Base for @(message.structure.namespaced_type.name) python class",
  .tp_basicsize = sizeof(@(message.structure.namespaced_type.name)Base),
  .tp_itemsize = 0,
  .tp_flags = Py_TPFLAGS_DEFAULT | Py_TPFLAGS_BASETYPE,
  .tp_new = PyType_GenericNew,
  .tp_dealloc = (destructor)@(message.structure.namespaced_type.name)Base_dealloc,
  .tp_members = @(message.structure.namespaced_type.name)Base_members,
};


@{
type_name = convert_camel_case_to_lower_case_underscore(message.structure.namespaced_type.name)
register_function = '_register_base_msg_type__' + '__'.join(message.structure.namespaced_type.namespaces[1:] + [type_name])
register_functions.append(register_function)
}@
static int8_t @(register_function)(PyObject * module)
{
  if (PyType_Ready(&@(message.structure.namespaced_type.name)BaseType) < 0) {
    return 1;
  }

  Py_INCREF(&@(message.structure.namespaced_type.name)BaseType);
  if (PyModule_AddObject(module, "@(message.structure.namespaced_type.name)Base", (PyObject *) &@(message.structure.namespaced_type.name)BaseType) < 0) {
    Py_DECREF(&@(message.structure.namespaced_type.name)BaseType);
    return 1;
  }
  return 0;
}
