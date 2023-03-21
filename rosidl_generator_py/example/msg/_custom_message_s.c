// generated from rosidl_generator_py/resource/_idl_support.c.em
// with input from example_msgs:msg/CustomMessage.idl
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
#include "example_msgs/msg/detail/custom_message__struct.h"
#include "example_msgs/msg/detail/custom_message__functions.h"
#include "../_example_msgs_decl.h"

#include "rosidl_runtime_c/primitives_sequence.h"
#include "rosidl_runtime_c/primitives_sequence_functions.h"

ROSIDL_GENERATOR_C_IMPORT
bool builtin_interfaces__msg__time__convert_from_py(PyObject * _pymsg, void * _ros_message);
ROSIDL_GENERATOR_C_IMPORT
PyObject * builtin_interfaces__msg__time__convert_to_py(void * raw_ros_message);

ROSIDL_GENERATOR_C_EXPORT
bool example_msgs__msg__custom_message__convert_from_py(PyObject * _pymsg, void * _ros_message)
{
  // check that the passed message is of the expected Python class
  {
    PyTypeObject * py_type = (PyTypeObject *)example_msgs__lazy_import(NULL, EXAMPLE_MSGS__MSG__CUSTOM_MESSAGE__IMPORT_INDEX);
    assert(Py_TYPE(_pymsg) == py_type);
  }
  example_msgs__msg__CustomMessage * ros_message = _ros_message;

  CustomMessageBase * base_msg = (CustomMessageBase *)_pymsg;
  {  // x
    ros_message->x = base_msg->_x;
  }
  {  // ts
    PyObject * field = base_msg->_ts;
    if (!field) {
      return false;
    }
    if (!builtin_interfaces__msg__time__convert_from_py(field, &ros_message->ts)) {
      return false;
    }
  }
  {  // fixed_seq
    PyObject * field = base_msg->_fixed_seq;
    if (!field) {
      return false;
    }
    {
      // TODO(dirk-thomas) use a better way to check the type before casting
      assert(field->ob_type != NULL);
      assert(field->ob_type->tp_name != NULL);
      assert(strcmp(field->ob_type->tp_name, "numpy.ndarray") == 0);
      PyArrayObject * seq_field = (PyArrayObject *)field;
      Py_INCREF(seq_field);
      assert(PyArray_NDIM(seq_field) == 1);
      assert(PyArray_TYPE(seq_field) == NPY_INT16);
      Py_ssize_t size = 3;
      int16_t * dest = ros_message->fixed_seq;
      for (Py_ssize_t i = 0; i < size; ++i) {
        int16_t tmp = *(npy_int16 *)PyArray_GETPTR1(seq_field, i);
        memcpy(&dest[i], &tmp, sizeof(int16_t));
      }
      Py_DECREF(seq_field);
    }
  }
  {  // limited_seq
    PyObject * field = base_msg->_limited_seq;
    if (!field) {
      return false;
    }
    if (PyObject_CheckBuffer(field)) {
      // Optimization for converting arrays of primitives
      Py_buffer view;
      int rc = PyObject_GetBuffer(field, &view, PyBUF_SIMPLE);
      if (rc < 0) {
        return false;
      }
      Py_ssize_t size = view.len / sizeof(int16_t);
      if (!rosidl_runtime_c__int16__Sequence__init(&(ros_message->limited_seq), size)) {
        PyErr_SetString(PyExc_RuntimeError, "unable to create int16__Sequence ros_message");
        PyBuffer_Release(&view);
        return false;
      }
      int16_t * dest = ros_message->limited_seq.data;
      rc = PyBuffer_ToContiguous(dest, &view, view.len, 'C');
      if (rc < 0) {
        PyBuffer_Release(&view);
        return false;
      }
      PyBuffer_Release(&view);
    } else {
      PyObject * seq_field = PySequence_Fast(field, "expected a sequence in 'limited_seq'");
      if (!seq_field) {
        return false;
      }
      Py_ssize_t size = PySequence_Size(field);
      if (-1 == size) {
        Py_DECREF(seq_field);
        return false;
      }
      if (!rosidl_runtime_c__int16__Sequence__init(&(ros_message->limited_seq), size)) {
        PyErr_SetString(PyExc_RuntimeError, "unable to create int16__Sequence ros_message");
        Py_DECREF(seq_field);
        return false;
      }
      int16_t * dest = ros_message->limited_seq.data;
      for (Py_ssize_t i = 0; i < size; ++i) {
        PyObject * item = PySequence_Fast_GET_ITEM(seq_field, i);
        if (!item) {
          Py_DECREF(seq_field);
          return false;
        }
        assert(PyLong_Check(item));
        int16_t tmp = (int16_t)PyLong_AsLong(item);
        memcpy(&dest[i], &tmp, sizeof(int16_t));
      }
      Py_DECREF(seq_field);
    }
  }
  {  // unlimited_seq
    PyObject * field = base_msg->_unlimited_seq;
    if (!field) {
      return false;
    }
    if (PyObject_CheckBuffer(field)) {
      // Optimization for converting arrays of primitives
      Py_buffer view;
      int rc = PyObject_GetBuffer(field, &view, PyBUF_SIMPLE);
      if (rc < 0) {
        return false;
      }
      Py_ssize_t size = view.len / sizeof(int16_t);
      if (!rosidl_runtime_c__int16__Sequence__init(&(ros_message->unlimited_seq), size)) {
        PyErr_SetString(PyExc_RuntimeError, "unable to create int16__Sequence ros_message");
        PyBuffer_Release(&view);
        return false;
      }
      int16_t * dest = ros_message->unlimited_seq.data;
      rc = PyBuffer_ToContiguous(dest, &view, view.len, 'C');
      if (rc < 0) {
        PyBuffer_Release(&view);
        return false;
      }
      PyBuffer_Release(&view);
    } else {
      PyObject * seq_field = PySequence_Fast(field, "expected a sequence in 'unlimited_seq'");
      if (!seq_field) {
        return false;
      }
      Py_ssize_t size = PySequence_Size(field);
      if (-1 == size) {
        Py_DECREF(seq_field);
        return false;
      }
      if (!rosidl_runtime_c__int16__Sequence__init(&(ros_message->unlimited_seq), size)) {
        PyErr_SetString(PyExc_RuntimeError, "unable to create int16__Sequence ros_message");
        Py_DECREF(seq_field);
        return false;
      }
      int16_t * dest = ros_message->unlimited_seq.data;
      for (Py_ssize_t i = 0; i < size; ++i) {
        PyObject * item = PySequence_Fast_GET_ITEM(seq_field, i);
        if (!item) {
          Py_DECREF(seq_field);
          return false;
        }
        assert(PyLong_Check(item));
        int16_t tmp = (int16_t)PyLong_AsLong(item);
        memcpy(&dest[i], &tmp, sizeof(int16_t));
      }
      Py_DECREF(seq_field);
    }
  }

  return true;
}

ROSIDL_GENERATOR_C_EXPORT
PyObject * example_msgs__msg__custom_message__convert_to_py(void * raw_ros_message)
{
  /* NOTE(esteve): Call constructor of CustomMessage */
  CustomMessageBase * _pymessage = NULL;
  {
    PyTypeObject * type = (PyTypeObject *)example_msgs__lazy_import(NULL, EXAMPLE_MSGS__MSG__CUSTOM_MESSAGE__IMPORT_INDEX);
    if (!type) {
      return NULL;
    }
    assert(type->tp_new);

    PyObject * empty_tuple = PyTuple_New(0);
    if (!empty_tuple) {
      return NULL;
    }

    _pymessage = (CustomMessageBase *)type->tp_new(type, empty_tuple, NULL);
    Py_DECREF(empty_tuple);
    if (!_pymessage) {
      return NULL;
    }
  }
  example_msgs__msg__CustomMessage * ros_message = (example_msgs__msg__CustomMessage *)raw_ros_message;
  {  // x
    _pymessage->_x = ros_message->x;
  }
  {  // ts
    PyObject * field = NULL;
    field = builtin_interfaces__msg__time__convert_to_py(&ros_message->ts);
    if (!field) {
      return NULL;
    }
    // reference is transfered to object
    _pymessage->_ts = field;
  }
  {  // fixed_seq
    PyObject * field = NULL;

    PyObject * array_type = example_msgs__lazy_import(NULL, NUMPY__NDARRAY__IMPORT_INDEX);
    if (!array_type) {
      return NULL;
    }
    PyObject * element_type = example_msgs__lazy_import(NULL, NUMPY__INT16__IMPORT_INDEX);
    if (!element_type) {
      return NULL;
    }
    PyObject * dims = Py_BuildValue("(i)", 3);
    field = PyObject_CallFunctionObjArgs(array_type, dims, element_type, NULL);
    Py_DECREF(dims);
    assert(strcmp(field->ob_type->tp_name, "numpy.ndarray") == 0);
    PyArrayObject * seq_field = (PyArrayObject *)field;
    assert(PyArray_NDIM(seq_field) == 1);
    assert(PyArray_TYPE(seq_field) == NPY_INT16);
    assert(sizeof(npy_int16) == sizeof(int16_t));
    npy_int16 * dst = (npy_int16 *)PyArray_GETPTR1(seq_field, 0);
    int16_t * src = &(ros_message->fixed_seq[0]);
    memcpy(dst, src, 3 * sizeof(int16_t));
    // reference is transfered to object
    _pymessage->_fixed_seq = field;
  }
  {  // limited_seq
    PyObject * field = NULL;
    {
      PyObject * array_type = example_msgs__lazy_import(NULL, ARRAY__ARRAY__IMPORT_INDEX);
      if (!array_type) {
        return NULL;
      }
      PyObject * type_code = PyUnicode_FromOrdinal('h');
      assert(type_code);

      field = PyObject_CallFunctionObjArgs(array_type, type_code, NULL);
      Py_DECREF(type_code);
      if (!field) {
        return NULL;
      }
    }
    assert(field->ob_type != NULL);
    assert(field->ob_type->tp_name != NULL);
    assert(strcmp(field->ob_type->tp_name, "array.array") == 0);
    // ensure that itemsize matches the sizeof of the ROS message field
    PyObject * itemsize_attr = PyObject_GetAttrString(field, "itemsize");
    assert(itemsize_attr != NULL);
    size_t itemsize = PyLong_AsSize_t(itemsize_attr);
    Py_DECREF(itemsize_attr);
    if (itemsize != sizeof(int16_t)) {
      PyErr_SetString(PyExc_RuntimeError, "itemsize doesn't match expectation");
      Py_DECREF(field);
      return NULL;
    }
    // clear the array, poor approach to remove potential default values
    Py_ssize_t length = PyObject_Length(field);
    if (-1 == length) {
      Py_DECREF(field);
      return NULL;
    }
    if (length > 0) {
      PyObject * pop = PyObject_GetAttrString(field, "pop");
      assert(pop != NULL);
      for (Py_ssize_t i = 0; i < length; ++i) {
        PyObject * ret = PyObject_CallFunctionObjArgs(pop, NULL);
        if (!ret) {
          Py_DECREF(pop);
          Py_DECREF(field);
          return NULL;
        }
        Py_DECREF(ret);
      }
      Py_DECREF(pop);
    }
    if (ros_message->limited_seq.size > 0) {
      // populating the array.array using the frombytes method
      PyObject * frombytes = PyObject_GetAttrString(field, "frombytes");
      assert(frombytes != NULL);
      int16_t * src = &(ros_message->limited_seq.data[0]);
      PyObject * data = PyBytes_FromStringAndSize((const char *)src, ros_message->limited_seq.size * sizeof(int16_t));
      assert(data != NULL);
      PyObject * ret = PyObject_CallFunctionObjArgs(frombytes, data, NULL);
      Py_DECREF(data);
      Py_DECREF(frombytes);
      if (!ret) {
        Py_DECREF(field);
        return NULL;
      }
      Py_DECREF(ret);
    }
    // reference is transfered to object
    _pymessage->_limited_seq = field;
  }
  {  // unlimited_seq
    PyObject * field = NULL;
    {
      PyObject * array_type = example_msgs__lazy_import(NULL, ARRAY__ARRAY__IMPORT_INDEX);
      if (!array_type) {
        return NULL;
      }
      PyObject * type_code = PyUnicode_FromOrdinal('h');
      assert(type_code);

      field = PyObject_CallFunctionObjArgs(array_type, type_code, NULL);
      Py_DECREF(type_code);
      if (!field) {
        return NULL;
      }
    }
    assert(field->ob_type != NULL);
    assert(field->ob_type->tp_name != NULL);
    assert(strcmp(field->ob_type->tp_name, "array.array") == 0);
    // ensure that itemsize matches the sizeof of the ROS message field
    PyObject * itemsize_attr = PyObject_GetAttrString(field, "itemsize");
    assert(itemsize_attr != NULL);
    size_t itemsize = PyLong_AsSize_t(itemsize_attr);
    Py_DECREF(itemsize_attr);
    if (itemsize != sizeof(int16_t)) {
      PyErr_SetString(PyExc_RuntimeError, "itemsize doesn't match expectation");
      Py_DECREF(field);
      return NULL;
    }
    // clear the array, poor approach to remove potential default values
    Py_ssize_t length = PyObject_Length(field);
    if (-1 == length) {
      Py_DECREF(field);
      return NULL;
    }
    if (length > 0) {
      PyObject * pop = PyObject_GetAttrString(field, "pop");
      assert(pop != NULL);
      for (Py_ssize_t i = 0; i < length; ++i) {
        PyObject * ret = PyObject_CallFunctionObjArgs(pop, NULL);
        if (!ret) {
          Py_DECREF(pop);
          Py_DECREF(field);
          return NULL;
        }
        Py_DECREF(ret);
      }
      Py_DECREF(pop);
    }
    if (ros_message->unlimited_seq.size > 0) {
      // populating the array.array using the frombytes method
      PyObject * frombytes = PyObject_GetAttrString(field, "frombytes");
      assert(frombytes != NULL);
      int16_t * src = &(ros_message->unlimited_seq.data[0]);
      PyObject * data = PyBytes_FromStringAndSize((const char *)src, ros_message->unlimited_seq.size * sizeof(int16_t));
      assert(data != NULL);
      PyObject * ret = PyObject_CallFunctionObjArgs(frombytes, data, NULL);
      Py_DECREF(data);
      Py_DECREF(frombytes);
      if (!ret) {
        Py_DECREF(field);
        return NULL;
      }
      Py_DECREF(ret);
    }
    // reference is transfered to object
    _pymessage->_unlimited_seq = field;
  }

  // ownership of _pymessage is transferred to the caller
  return (PyObject *)_pymessage;
}
