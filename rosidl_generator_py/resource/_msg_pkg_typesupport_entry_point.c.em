@# Included from rosidl_generator_py/resource/_idl_pkg_typesupport_entry_point.c.em
@{
from rosidl_cmake import convert_camel_case_to_lower_case_underscore
module_name = convert_camel_case_to_lower_case_underscore(message.structure.type.name)

header_filename = module_name
if header_filename.endswith('__request'):
    header_filename = header_filename[:-9]
elif header_filename.endswith('__response'):
    header_filename = header_filename[:-10]
if header_filename.endswith('__goal'):
    header_filename = header_filename[:-6]
elif header_filename.endswith('__result'):
    header_filename = header_filename[:-8]
elif header_filename.endswith('__feedback'):
    header_filename = header_filename[:-10]
if header_filename.endswith('__action'):
    header_filename = header_filename[:-8]

include_parts = message.structure.type.namespaces + [header_filename]
include_base = '/'.join(include_parts)

header_files = [
    'stdbool.h',
    'stdint.h',
    'rosidl_generator_c/visibility_control.h',
    'rosidl_generator_c/message_type_support_struct.h',
    'rosidl_generator_c/service_type_support_struct.h',
    'rosidl_generator_c/action_type_support_struct.h',
    include_base + '__type_support.h',
    include_base + '__struct.h',
    include_base + '__functions.h',
]
}@
@[for header_file in header_files]@
@[    if header_file in include_directives]@
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
@
@{
msg_typename = '__'.join(message.structure.type.namespaces + [message.structure.type.name])
}@

static void * @('__'.join(message.structure.type.namespaces + [module_name]))__create_ros_message(void)
{
  return @(msg_typename)__create();
}

static void @('__'.join(message.structure.type.namespaces + [module_name]))__destroy_ros_message(void * raw_ros_message)
{
  @(msg_typename) * ros_message = (@(msg_typename) *)raw_ros_message;
  @(msg_typename)__destroy(ros_message);
}

ROSIDL_GENERATOR_C_IMPORT
bool @('__'.join(message.structure.type.namespaces + [module_name]))__convert_from_py(PyObject * _pymsg, void * ros_message);
ROSIDL_GENERATOR_C_IMPORT
PyObject * @('__'.join(message.structure.type.namespaces + [module_name]))__convert_to_py(void * raw_ros_message);


ROSIDL_GENERATOR_C_IMPORT
const rosidl_message_type_support_t *
ROSIDL_GET_MSG_TYPE_SUPPORT(@(', '.join(message.structure.type.namespaces + [message.structure.type.name])));

int8_t
_register_msg_type__@('__'.join(message.structure.type.namespaces[1:] + [module_name]))(PyObject * pymodule)
{
  int8_t err;
@{
function_names = ['create_ros_message', 'destroy_ros_message', 'convert_from_py', 'convert_to_py', 'type_support']
}@
@[for function_name in function_names]@

  PyObject * pyobject_@(function_name) = NULL;
  pyobject_@(function_name) = PyCapsule_New(
@[    if function_name != 'type_support']@
    (void *)&@('__'.join(message.structure.type.namespaces + [module_name]))__@(function_name),
@[    else]@
    (void *)ROSIDL_GET_MSG_TYPE_SUPPORT(@(', '.join(message.structure.type.namespaces + [message.structure.type.name]))),
@[    end if]@
    NULL, NULL);
  if (!pyobject_@(function_name)) {
    // previously added objects will be removed when the module is destroyed
    return -1;
  }
  err = PyModule_AddObject(
    pymodule,
    "@(function_name)_msg__@('__'.join(message.structure.type.namespaces[1:] + [module_name]))",
    pyobject_@(function_name));
  if (err) {
    // the created capsule needs to be decremented
    Py_XDECREF(pyobject_@(function_name));
    // previously added objects will be removed when the module is destroyed
    return err;
  }
@[end for]@
  return 0;
}
