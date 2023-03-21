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
from rosidl_pycommon import convert_camel_case_to_lower_case_underscore
from rosidl_parser.definition import Message

include_directives = set()
register_functions = []
}@
#include <Python.h>
@
@[for message in content.get_elements_of_type(Message)]@

@{
TEMPLATE(
    '_msg_pkg_typesupport_entry_point.c.em',
    package_name=package_name, idl_type=message.structure.namespaced_type, message=message,
    typesupport_impl=typesupport_impl, include_directives=include_directives,
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
    '_srv_pkg_typesupport_entry_point.c.em',
    package_name=package_name, idl_type=service.namespaced_type,
    service=service, typesupport_impl=typesupport_impl,
    include_directives=include_directives,
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
    '_action_pkg_typesupport_entry_point.c.em',
    package_name=package_name, idl_type=action.namespaced_type,
    action=action, typesupport_impl=typesupport_impl,
    include_directives=include_directives,
    register_functions=register_functions)
}@
@[end for]@

#include "./_@(package_name)_decl.h"

static PyMethodDef @(package_name)__methods[] = {
  {NULL, NULL, 0, NULL}  /* sentinel */
};

static int
_@(package_name)_clear(PyObject * module)
{
  (void)module;
  @(package_name)__lazy_import_release();
  return 0;
}

static void
_@(package_name)_free(void * module)
{
  _@(package_name)_clear((PyObject *)module);
}


static struct PyModuleDef @(package_name)__module = {
  PyModuleDef_HEAD_INIT,
  "_@(package_name)_support",
  "_@(package_name)_doc",
  -1,  /* -1 means that the module keeps state in global variables */
  @(package_name)__methods,
  NULL,
  NULL,
  _@(package_name)_clear,
  _@(package_name)_free,
};


PyMODINIT_FUNC
PyInit_@(package_name)_s__@(typesupport_impl)(void)
{
  PyObject * pymodule = NULL;
  pymodule = PyModule_Create(&@(package_name)__module);
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

  @(package_name)__lazy_import_acquire();
  return pymodule;
}
