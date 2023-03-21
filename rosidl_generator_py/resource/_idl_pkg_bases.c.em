// generated from rosidl_generator_py/resource/_idl_pkg_bases.c.em
// generated code does not contain a copyright notice
@
@#######################################################################
@# EmPy template for generating _<idl>_bases.c files
@#
@# Context:
@#  - package_name (string)
@#  - content (IdlContent, list of elements, e.g. Messages or Services)
@#######################################################################
@
@#######################################################################
@# Handle messages
@#######################################################################
@{
from rosidl_parser.definition import Message
from rosidl_pycommon import convert_camel_case_to_lower_case_underscore

include_directives = set()
register_functions = []

}@
@[for message in content.get_elements_of_type(Message)]@
@{

TEMPLATE(
    '_msg_base.c.em',
    package_name=package_name,
    message=message, include_directives=include_directives,
    register_functions=register_functions)
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
    '_msg_base.c.em',
    package_name=package_name,
    message=service.request_message, include_directives=include_directives,
    register_functions=register_functions)
}@

@{
TEMPLATE(
    '_msg_base.c.em',
    package_name=package_name,
    message=service.response_message, include_directives=include_directives,
    register_functions=register_functions)
}@

@{
TEMPLATE(
    '_msg_base.c.em',
    package_name=package_name,
    message=service.event_message, include_directives=include_directives,
    register_functions=register_functions)
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
    '_msg_base.c.em',
    package_name=package_name,
    message=action.goal, include_directives=include_directives,
    register_functions=register_functions)
}@

@{
TEMPLATE(
    '_msg_base.c.em',
    package_name=package_name,
    message=action.result, include_directives=include_directives,
    register_functions=register_functions)
}@

@{
TEMPLATE(
    '_msg_base.c.em',
    package_name=package_name,
    message=action.feedback, include_directives=include_directives,
    register_functions=register_functions)
}@

@{
TEMPLATE(
    '_msg_base.c.em',
    package_name=package_name,
    message=action.send_goal_service.request_message,
    include_directives=include_directives,
    register_functions=register_functions)
}@

@{
TEMPLATE(
    '_msg_base.c.em',
    package_name=package_name,
    message=action.send_goal_service.response_message,
    include_directives=include_directives,
    register_functions=register_functions)
}@

@{
TEMPLATE(
    '_msg_base.c.em',
    package_name=package_name,
    message=action.send_goal_service.event_message,
    include_directives=include_directives,
    register_functions=register_functions)
}@

@{
TEMPLATE(
    '_msg_base.c.em',
    package_name=package_name,
    message=action.get_result_service.request_message,
    include_directives=include_directives,
    register_functions=register_functions)
}@

@{
TEMPLATE(
    '_msg_base.c.em',
    package_name=package_name,
    message=action.get_result_service.response_message,
    include_directives=include_directives,
    register_functions=register_functions)
}@

@{
TEMPLATE(
    '_msg_base.c.em',
    package_name=package_name,
    message=action.get_result_service.event_message,
    include_directives=include_directives,
    register_functions=register_functions)
}@

@{
TEMPLATE(
    '_msg_base.c.em',
    package_name=package_name,
    message=action.feedback_message, include_directives=include_directives,
    register_functions=register_functions)
}@
@[end for]@


static PyModuleDef _module = {
  PyModuleDef_HEAD_INIT,
  .m_name = "_@(package_name)_bases",
  .m_doc = "Extention module for @(package_name) messages",
  .m_size = -1,
};


PyMODINIT_FUNC
PyInit__@(package_name)_bases(void)
{
  PyObject * pymodule = NULL;
  pymodule = PyModule_Create(&_module);
  if (!pymodule) {
    return NULL;
  }
  int8_t err;
@[for register_function in register_functions]@

  err = @(register_function)(pymodule);
  if (err) {
    Py_XDECREF(pymodule);
    return NULL;
  }
@[end for]@

  return pymodule;
}
