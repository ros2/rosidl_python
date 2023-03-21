// generated from rosidl_generator_py/resource/_idl_support.c.em
// with input from example_msgs:srv/CustomCall.idl
// generated code does not contain a copyright notice
#define NPY_NO_DEPRECATED_API NPY_1_7_API_VERSION
#include <Python.h>
#include <stdbool.h>
#ifndef _WIN32
# pragma GCC diagnostic push
# pragma GCC diagnostic ignored "-Wunused-function"
#endif
#include "numpy/ndarrayobject.h"
#ifndef _WIN32
# pragma GCC diagnostic pop
#endif
#include "rosidl_runtime_c/visibility_control.h"
#include "example_msgs/srv/detail/custom_call__struct.h"
#include "example_msgs/srv/detail/custom_call__functions.h"
#include "../_example_msgs_decl.h"


ROSIDL_GENERATOR_C_EXPORT
bool example_msgs__srv__custom_call__request__convert_from_py(PyObject * _pymsg, void * _ros_message)
{
  // check that the passed message is of the expected Python class
  {
    PyTypeObject * py_type = (PyTypeObject *)example_msgs__lazy_import(NULL, EXAMPLE_MSGS__SRV__CUSTOM_CALL__REQUEST__IMPORT_INDEX);
    assert(Py_TYPE(_pymsg) == py_type);
  }
  example_msgs__srv__CustomCall_Request * ros_message = _ros_message;

  CustomCall_RequestBase * base_msg = (CustomCall_RequestBase *)_pymsg;
  {  // my_param
    ros_message->my_param = base_msg->_my_param;
  }

  return true;
}

ROSIDL_GENERATOR_C_EXPORT
PyObject * example_msgs__srv__custom_call__request__convert_to_py(void * raw_ros_message)
{
  /* NOTE(esteve): Call constructor of CustomCall_Request */
  CustomCall_RequestBase * _pymessage = NULL;
  {
    PyTypeObject * type = (PyTypeObject *)example_msgs__lazy_import(NULL, EXAMPLE_MSGS__SRV__CUSTOM_CALL__REQUEST__IMPORT_INDEX);
    if (!type) {
      return NULL;
    }
    assert(type->tp_new);

    PyObject * empty_tuple = PyTuple_New(0);
    if (!empty_tuple) {
      return NULL;
    }

    _pymessage = (CustomCall_RequestBase *)type->tp_new(type, empty_tuple, NULL);
    Py_DECREF(empty_tuple);
    if (!_pymessage) {
      return NULL;
    }
  }
  example_msgs__srv__CustomCall_Request * ros_message = (example_msgs__srv__CustomCall_Request *)raw_ros_message;
  {  // my_param
    _pymessage->_my_param = ros_message->my_param;
  }

  // ownership of _pymessage is transferred to the caller
  return (PyObject *)_pymessage;
}

#define NPY_NO_DEPRECATED_API NPY_1_7_API_VERSION
// already included above
// #include <Python.h>
// already included above
// #include <stdbool.h>
// already included above
// #include "numpy/ndarrayobject.h"
// already included above
// #include "rosidl_runtime_c/visibility_control.h"
// already included above
// #include "example_msgs/srv/detail/custom_call__struct.h"
// already included above
// #include "example_msgs/srv/detail/custom_call__functions.h"
// already included above
// #include "../_example_msgs_decl.h"


ROSIDL_GENERATOR_C_EXPORT
bool example_msgs__srv__custom_call__response__convert_from_py(PyObject * _pymsg, void * _ros_message)
{
  // check that the passed message is of the expected Python class
  {
    PyTypeObject * py_type = (PyTypeObject *)example_msgs__lazy_import(NULL, EXAMPLE_MSGS__SRV__CUSTOM_CALL__RESPONSE__IMPORT_INDEX);
    assert(Py_TYPE(_pymsg) == py_type);
  }
  example_msgs__srv__CustomCall_Response * ros_message = _ros_message;

  CustomCall_ResponseBase * base_msg = (CustomCall_ResponseBase *)_pymsg;
  {  // my_result
    ros_message->my_result = base_msg->_my_result;
  }

  return true;
}

ROSIDL_GENERATOR_C_EXPORT
PyObject * example_msgs__srv__custom_call__response__convert_to_py(void * raw_ros_message)
{
  /* NOTE(esteve): Call constructor of CustomCall_Response */
  CustomCall_ResponseBase * _pymessage = NULL;
  {
    PyTypeObject * type = (PyTypeObject *)example_msgs__lazy_import(NULL, EXAMPLE_MSGS__SRV__CUSTOM_CALL__RESPONSE__IMPORT_INDEX);
    if (!type) {
      return NULL;
    }
    assert(type->tp_new);

    PyObject * empty_tuple = PyTuple_New(0);
    if (!empty_tuple) {
      return NULL;
    }

    _pymessage = (CustomCall_ResponseBase *)type->tp_new(type, empty_tuple, NULL);
    Py_DECREF(empty_tuple);
    if (!_pymessage) {
      return NULL;
    }
  }
  example_msgs__srv__CustomCall_Response * ros_message = (example_msgs__srv__CustomCall_Response *)raw_ros_message;
  {  // my_result
    _pymessage->_my_result = ros_message->my_result;
  }

  // ownership of _pymessage is transferred to the caller
  return (PyObject *)_pymessage;
}

#define NPY_NO_DEPRECATED_API NPY_1_7_API_VERSION
// already included above
// #include <Python.h>
// already included above
// #include <stdbool.h>
// already included above
// #include "numpy/ndarrayobject.h"
// already included above
// #include "rosidl_runtime_c/visibility_control.h"
// already included above
// #include "example_msgs/srv/detail/custom_call__struct.h"
// already included above
// #include "example_msgs/srv/detail/custom_call__functions.h"
// already included above
// #include "../_example_msgs_decl.h"

#include "rosidl_runtime_c/primitives_sequence.h"
#include "rosidl_runtime_c/primitives_sequence_functions.h"

// Nested array functions includes


// end nested array functions include
ROSIDL_GENERATOR_C_IMPORT
bool service_msgs__msg__service_event_info__convert_from_py(PyObject * _pymsg, void * _ros_message);
ROSIDL_GENERATOR_C_IMPORT
PyObject * service_msgs__msg__service_event_info__convert_to_py(void * raw_ros_message);
bool example_msgs__srv__custom_call__request__convert_from_py(PyObject * _pymsg, void * _ros_message);
PyObject * example_msgs__srv__custom_call__request__convert_to_py(void * raw_ros_message);
bool example_msgs__srv__custom_call__response__convert_from_py(PyObject * _pymsg, void * _ros_message);
PyObject * example_msgs__srv__custom_call__response__convert_to_py(void * raw_ros_message);

ROSIDL_GENERATOR_C_EXPORT
bool example_msgs__srv__custom_call__event__convert_from_py(PyObject * _pymsg, void * _ros_message)
{
  // check that the passed message is of the expected Python class
  {
    PyTypeObject * py_type = (PyTypeObject *)example_msgs__lazy_import(NULL, EXAMPLE_MSGS__SRV__CUSTOM_CALL__EVENT__IMPORT_INDEX);
    assert(Py_TYPE(_pymsg) == py_type);
  }
  example_msgs__srv__CustomCall_Event * ros_message = _ros_message;

  CustomCall_EventBase * base_msg = (CustomCall_EventBase *)_pymsg;
  {  // info
    PyObject * field = base_msg->_info;
    if (!field) {
      return false;
    }
    if (!service_msgs__msg__service_event_info__convert_from_py(field, &ros_message->info)) {
      return false;
    }
  }
  {  // request
    PyObject * field = base_msg->_request;
    if (!field) {
      return false;
    }
    PyObject * seq_field = PySequence_Fast(field, "expected a sequence in 'request'");
    if (!seq_field) {
      return false;
    }
    Py_ssize_t size = PySequence_Size(field);
    if (-1 == size) {
      Py_DECREF(seq_field);
      return false;
    }
    if (!example_msgs__srv__CustomCall_Request__Sequence__init(&(ros_message->request), size)) {
      PyErr_SetString(PyExc_RuntimeError, "unable to create example_msgs__srv__CustomCall_Request__Sequence ros_message");
      Py_DECREF(seq_field);
      return false;
    }
    example_msgs__srv__CustomCall_Request * dest = ros_message->request.data;
    for (Py_ssize_t i = 0; i < size; ++i) {
      if (!example_msgs__srv__custom_call__request__convert_from_py(PySequence_Fast_GET_ITEM(seq_field, i), &dest[i])) {
        Py_DECREF(seq_field);
        return false;
      }
    }
    Py_DECREF(seq_field);
  }
  {  // response
    PyObject * field = base_msg->_response;
    if (!field) {
      return false;
    }
    PyObject * seq_field = PySequence_Fast(field, "expected a sequence in 'response'");
    if (!seq_field) {
      return false;
    }
    Py_ssize_t size = PySequence_Size(field);
    if (-1 == size) {
      Py_DECREF(seq_field);
      return false;
    }
    if (!example_msgs__srv__CustomCall_Response__Sequence__init(&(ros_message->response), size)) {
      PyErr_SetString(PyExc_RuntimeError, "unable to create example_msgs__srv__CustomCall_Response__Sequence ros_message");
      Py_DECREF(seq_field);
      return false;
    }
    example_msgs__srv__CustomCall_Response * dest = ros_message->response.data;
    for (Py_ssize_t i = 0; i < size; ++i) {
      if (!example_msgs__srv__custom_call__response__convert_from_py(PySequence_Fast_GET_ITEM(seq_field, i), &dest[i])) {
        Py_DECREF(seq_field);
        return false;
      }
    }
    Py_DECREF(seq_field);
  }

  return true;
}

ROSIDL_GENERATOR_C_EXPORT
PyObject * example_msgs__srv__custom_call__event__convert_to_py(void * raw_ros_message)
{
  /* NOTE(esteve): Call constructor of CustomCall_Event */
  CustomCall_EventBase * _pymessage = NULL;
  {
    PyTypeObject * type = (PyTypeObject *)example_msgs__lazy_import(NULL, EXAMPLE_MSGS__SRV__CUSTOM_CALL__EVENT__IMPORT_INDEX);
    if (!type) {
      return NULL;
    }
    assert(type->tp_new);

    PyObject * empty_tuple = PyTuple_New(0);
    if (!empty_tuple) {
      return NULL;
    }

    _pymessage = (CustomCall_EventBase *)type->tp_new(type, empty_tuple, NULL);
    Py_DECREF(empty_tuple);
    if (!_pymessage) {
      return NULL;
    }
  }
  example_msgs__srv__CustomCall_Event * ros_message = (example_msgs__srv__CustomCall_Event *)raw_ros_message;
  {  // info
    PyObject * field = NULL;
    field = service_msgs__msg__service_event_info__convert_to_py(&ros_message->info);
    if (!field) {
      return NULL;
    }
    // reference is transfered to object
    _pymessage->_info = field;
  }
  {  // request
    PyObject * field = NULL;
    size_t size = ros_message->request.size;
    field = PyList_New(size);
    if (!field) {
      return NULL;
    }
    example_msgs__srv__CustomCall_Request * item;
    for (size_t i = 0; i < size; ++i) {
      item = &(ros_message->request.data[i]);
      PyObject * pyitem = example_msgs__srv__custom_call__request__convert_to_py(item);
      if (!pyitem) {
        Py_DECREF(field);
        return NULL;
      }
      int rc = PyList_SetItem(field, i, pyitem);
      (void)rc;
      assert(rc == 0);
    }
    assert(PySequence_Check(field));
    // reference is transfered to object
    _pymessage->_request = field;
  }
  {  // response
    PyObject * field = NULL;
    size_t size = ros_message->response.size;
    field = PyList_New(size);
    if (!field) {
      return NULL;
    }
    example_msgs__srv__CustomCall_Response * item;
    for (size_t i = 0; i < size; ++i) {
      item = &(ros_message->response.data[i]);
      PyObject * pyitem = example_msgs__srv__custom_call__response__convert_to_py(item);
      if (!pyitem) {
        Py_DECREF(field);
        return NULL;
      }
      int rc = PyList_SetItem(field, i, pyitem);
      (void)rc;
      assert(rc == 0);
    }
    assert(PySequence_Check(field));
    // reference is transfered to object
    _pymessage->_response = field;
  }

  // ownership of _pymessage is transferred to the caller
  return (PyObject *)_pymessage;
}
