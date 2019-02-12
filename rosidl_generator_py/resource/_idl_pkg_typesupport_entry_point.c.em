// generated from rosidl_generator_py/resource/_idl_pkg_typesupport_entry_point.c.em
// generated code does not contain a copyright notice
@
@#######################################################################
@# EmPy template for generating _<pkg>_s.ep.<ts>.c files
@#
@# Context:
@#  - package_name (string)
@#  - content (IdlContent, combined list of elements across all interface files
@#  - typesupport_impl (string identifying the typesupport used)
@#######################################################################
@
@#######################################################################
@# Handle messages
@#######################################################################
@{
from rosidl_cmake import convert_camel_case_to_lower_case_underscore
from rosidl_parser.definition import Message

include_directives = set()
}@
#include <Python.h>

static PyMethodDef @(package_name)__methods[] = {
  {NULL, NULL, 0, NULL}  /* sentinel */
};

static struct PyModuleDef @(package_name)__module = {
  PyModuleDef_HEAD_INIT,
  "_@(package_name)_support",
  "_@(package_name)_doc",
  -1,  /* -1 means that the module keeps state in global variables */
  @(package_name)__methods,
  NULL,
  NULL,
  NULL,
  NULL,
};
@
@[for message in content.get_elements_of_type(Message)]@

@{
TEMPLATE(
    '_msg_pkg_typesupport_entry_point.c.em',
    package_name=package_name, idl_type=message.structure.type, message=message,
    typesupport_impl=typesupport_impl, include_directives=include_directives)
}@
@[end for]@
@
@#######################################################################
@# Handle services
@#######################################################################
@{
from rosidl_parser.definition import Service
}@
@[for service in content.get_elements_of_type(Service)]@

@{
TEMPLATE(
    '_srv_pkg_typesupport_entry_point.c.em',
    package_name=package_name, idl_type=service.structure_type,
    service=service, typesupport_impl=typesupport_impl,
    include_directives=include_directives)
}@
@[end for]@
@
@#######################################################################
@# Handle actions
@#######################################################################
@{
from rosidl_parser.definition import Action
}@
@[for action in content.get_elements_of_type(Action)]@

@{
TEMPLATE(
    '_msg_pkg_typesupport_entry_point.c.em',
    package_name=package_name, idl_type=action.structure_type,
    message=action.goal, typesupport_impl=typesupport_impl,
    include_directives=include_directives)
}@

@{
TEMPLATE(
    '_msg_pkg_typesupport_entry_point.c.em',
    package_name=package_name, idl_type=action.structure_type,
    message=action.result, typesupport_impl=typesupport_impl,
    include_directives=include_directives)
}@

@{
TEMPLATE(
    '_msg_pkg_typesupport_entry_point.c.em',
    package_name=package_name, idl_type=action.structure_type,
    message=action.feedback, typesupport_impl=typesupport_impl,
    include_directives=include_directives)
}@

@{
TEMPLATE(
    '_srv_pkg_typesupport_entry_point.c.em',
    package_name=package_name, idl_type=action.structure_type,
    service=action.send_goal_service, typesupport_impl=typesupport_impl,
    include_directives=include_directives)
}@

@{
TEMPLATE(
    '_srv_pkg_typesupport_entry_point.c.em',
    package_name=package_name, idl_type=action.structure_type,
    service=action.get_result_service, typesupport_impl=typesupport_impl,
    include_directives=include_directives)
}@

@{
TEMPLATE(
    '_msg_pkg_typesupport_entry_point.c.em',
    package_name=package_name, idl_type=action.structure_type,
    message=action.feedback_message, typesupport_impl=typesupport_impl,
    include_directives=include_directives)
}@
@[end for]@

PyMODINIT_FUNC
PyInit_@(package_name)_s__@(typesupport_impl)(void)
{
  PyObject * pymodule = NULL;
  pymodule = PyModule_Create(&@(package_name)__module);
  if (!pymodule) {
    return NULL;
  }
  int8_t err;
@[for message in content.get_elements_of_type(Message)]@

  err = _register_msg_type__@('__'.join(message.structure.type.namespaces[1:]))__@(convert_camel_case_to_lower_case_underscore(message.structure.type.name))(pymodule);
  if (err) {
    Py_XDECREF(pymodule);
    return NULL;
  }
@[end for]@
@[for service in content.get_elements_of_type(Service)]@

  err = _register_msg_type__@('__'.join(service.request_message.structure.type.namespaces[1:]))__@(convert_camel_case_to_lower_case_underscore(service.request_message.structure.type.name))(pymodule);
  if (err) {
    Py_XDECREF(pymodule);
    return NULL;
  }

  err = _register_msg_type__@('__'.join(service.response_message.structure.type.namespaces[1:]))__@(convert_camel_case_to_lower_case_underscore(service.response_message.structure.type.name))(pymodule);
  if (err) {
    Py_XDECREF(pymodule);
    return NULL;
  }

  err = _register_srv_type__@('__'.join(service.structure_type.namespaces[1:]))__@(convert_camel_case_to_lower_case_underscore(service.structure_type.name))(pymodule);
  if (err) {
    Py_XDECREF(pymodule);
    return NULL;
  }
@[end for]@
@[for action in content.get_elements_of_type(Action)]@

  err = _register_msg_type__@('__'.join(action.goal.structure.type.namespaces[1:]))__@(convert_camel_case_to_lower_case_underscore(action.goal.structure.type.name))(pymodule);
  if (err) {
    Py_XDECREF(pymodule);
    return NULL;
  }

  err = _register_msg_type__@('__'.join(action.result.structure.type.namespaces[1:]))__@(convert_camel_case_to_lower_case_underscore(action.result.structure.type.name))(pymodule);
  if (err) {
    Py_XDECREF(pymodule);
    return NULL;
  }

  err = _register_msg_type__@('__'.join(action.feedback.structure.type.namespaces[1:]))__@(convert_camel_case_to_lower_case_underscore(action.feedback.structure.type.name))(pymodule);
  if (err) {
    Py_XDECREF(pymodule);
    return NULL;
  }

  err = _register_srv_type__@('__'.join(action.send_goal_service.structure_type.namespaces[1:]))__@(convert_camel_case_to_lower_case_underscore(action.send_goal_service.structure_type.name))(pymodule);
  if (err) {
    Py_XDECREF(pymodule);
    return NULL;
  }

  err = _register_srv_type__@('__'.join(action.get_result_service.structure_type.namespaces[1:]))__@(convert_camel_case_to_lower_case_underscore(action.get_result_service.structure_type.name))(pymodule);
  if (err) {
    Py_XDECREF(pymodule);
    return NULL;
  }

  err = _register_msg_type__@('__'.join(action.feedback_message.structure.type.namespaces[1:]))__@(convert_camel_case_to_lower_case_underscore(action.feedback_message.structure.type.name))(pymodule);
  if (err) {
    Py_XDECREF(pymodule);
    return NULL;
  }
@[end for]@

  return pymodule;
}
