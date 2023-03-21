// generated from rosidl_generator_py/resource/_idl_pkg_decl.c.em
// generated code does not contain a copyright notice
#pragma once
@
@#######################################################################
@# EmPy template for generating _<idl>_decl.h files
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
required_py_modules = []

}@
@[for message in content.get_elements_of_type(Message)]@
@{

TEMPLATE(
    '_msg_decl.h.em',
    package_name=package_name,
    message=message, include_directives=include_directives,
    required_py_modules=required_py_modules)
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
    '_msg_decl.h.em',
    package_name=package_name,
    message=service.request_message, include_directives=include_directives,
    required_py_modules=required_py_modules)
}@

@{
TEMPLATE(
    '_msg_decl.h.em',
    package_name=package_name,
    message=service.response_message, include_directives=include_directives,
    required_py_modules=required_py_modules)
}@

@{
TEMPLATE(
    '_msg_decl.h.em',
    package_name=package_name,
    message=service.event_message, include_directives=include_directives,
    required_py_modules=required_py_modules)
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
    '_msg_decl.h.em',
    package_name=package_name,
    message=action.goal, include_directives=include_directives,
    required_py_modules=required_py_modules)
}@

@{
TEMPLATE(
    '_msg_decl.h.em',
    package_name=package_name,
    message=action.result, include_directives=include_directives,
    required_py_modules=required_py_modules)
}@

@{
TEMPLATE(
    '_msg_decl.h.em',
    package_name=package_name,
    message=action.feedback, include_directives=include_directives,
    required_py_modules=required_py_modules)
}@

@{
TEMPLATE(
    '_msg_decl.h.em',
    package_name=package_name,
    message=action.send_goal_service.request_message,
    include_directives=include_directives,
    required_py_modules=required_py_modules)
}@

@{
TEMPLATE(
    '_msg_decl.h.em',
    package_name=package_name,
    message=action.send_goal_service.response_message,
    include_directives=include_directives,
    required_py_modules=required_py_modules)
}@

@{
TEMPLATE(
    '_msg_decl.h.em',
    package_name=package_name,
    message=action.send_goal_service.event_message,
    include_directives=include_directives,
    required_py_modules=required_py_modules)
}@

@{
TEMPLATE(
    '_msg_decl.h.em',
    package_name=package_name,
    message=action.get_result_service.request_message,
    include_directives=include_directives,
    required_py_modules=required_py_modules)
}@

@{
TEMPLATE(
    '_msg_decl.h.em',
    package_name=package_name,
    message=action.get_result_service.response_message,
    include_directives=include_directives,
    required_py_modules=required_py_modules)
}@

@{
TEMPLATE(
    '_msg_decl.h.em',
    package_name=package_name,
    message=action.get_result_service.event_message,
    include_directives=include_directives,
    required_py_modules=required_py_modules)
}@

@{
TEMPLATE(
    '_msg_decl.h.em',
    package_name=package_name,
    message=action.feedback_message, include_directives=include_directives,
    required_py_modules=required_py_modules)
}@
@[end for]@

#define MAX__IMPORT_INDEX @(len(required_py_modules))

typedef struct lazy_import_state
{
  PyObject * cached_imports[MAX__IMPORT_INDEX];
} lazy_import_state;

int @(package_name)__lazy_import_initialize(lazy_import_state * state);
int @(package_name)__lazy_import_finalize(lazy_import_state * state);
PyObject * @(package_name)__lazy_import(lazy_import_state * state, size_t index);

// Since lazy cache global state is shared between multiple typesupport implementations,
// its lifetime should be managed carefully. Extention module can call `__lazy_import`
// function only between `__lazy_import_acquire` and `__lazy_import_release` calls.
// This functions should be removed when cache state becomes module specific.
int @(package_name)__lazy_import_acquire();
int @(package_name)__lazy_import_release();
