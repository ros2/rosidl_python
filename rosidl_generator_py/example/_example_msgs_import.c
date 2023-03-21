// generated from rosidl_generator_py/resource/_idl_pkg_import.c.em
// generated code does not contain a copyright notice
#include <Python.h>
#include <stdbool.h>
#include "./_example_msgs_decl.h"


typedef struct
{
  const char * module_name;
  const char * object_name;
  bool ensure_is_type;
} lazy_import_info;


static lazy_import_info import_infos[MAX__IMPORT_INDEX] = {
  // numpy.ndarray
  [NUMPY__NDARRAY__IMPORT_INDEX] = {"numpy", "ndarray", false},
  // numpy.int16
  [NUMPY__INT16__IMPORT_INDEX] = {"numpy", "int16", false},
  // array.array
  [ARRAY__ARRAY__IMPORT_INDEX] = {"array", "array", false},
  // example_msgs.msg.CustomMessage
  [EXAMPLE_MSGS__MSG__CUSTOM_MESSAGE__IMPORT_INDEX] = {"example_msgs.msg._custom_message", "CustomMessage", true},
  // example_msgs.srv.CustomCall_Request
  [EXAMPLE_MSGS__SRV__CUSTOM_CALL__REQUEST__IMPORT_INDEX] = {"example_msgs.srv._custom_call", "CustomCall_Request", true},
  // example_msgs.srv.CustomCall_Response
  [EXAMPLE_MSGS__SRV__CUSTOM_CALL__RESPONSE__IMPORT_INDEX] = {"example_msgs.srv._custom_call", "CustomCall_Response", true},
  // example_msgs.srv.CustomCall_Event
  [EXAMPLE_MSGS__SRV__CUSTOM_CALL__EVENT__IMPORT_INDEX] = {"example_msgs.srv._custom_call", "CustomCall_Event", true},
};

int example_msgs__lazy_import_initialize(lazy_import_state * state)
{
  assert(state != NULL);
  for (size_t i = 0; i < MAX__IMPORT_INDEX; ++i) {
    state->cached_imports[i] = NULL;
  }
  return 0;
}

int example_msgs__lazy_import_finalize(lazy_import_state * state)
{
  assert(state != NULL);
  for (size_t i = 0; i < MAX__IMPORT_INDEX; ++i) {
    Py_CLEAR(state->cached_imports[i]);
  }
  return 0;
}


static PyObject * state_storage = NULL;

PyObject * example_msgs__lazy_import(lazy_import_state * state, size_t index)
{
  if (state == NULL) {
    if (state_storage == NULL) {
      PyErr_SetString(PyExc_RuntimeError, "Internal error. Module not initilized properly");
      return NULL;
    }
    state = (lazy_import_state *)PyCapsule_GetPointer(state_storage, NULL);
    if (state == NULL) {
      return NULL;
    }
  }

  assert(index < MAX__IMPORT_INDEX);
  PyObject * py_type = state->cached_imports[index];
  if (py_type != NULL) {
    return py_type;
  }

  const lazy_import_info * info = &import_infos[index];
  PyObject * module = PyImport_ImportModule(info->module_name);
  if (!module) {
    return NULL;
  }
  py_type = PyObject_GetAttrString(module, info->object_name);
  Py_DECREF(module);
  if (!py_type) {
    return NULL;
  }
  if (info->ensure_is_type && !PyType_Check(py_type)) {
    PyErr_SetString(PyExc_RuntimeError, "Imported object is not a python type");
    return NULL;
  }

  state->cached_imports[index] = py_type;
  return py_type;
}

static void clear_storage(PyObject * capsule)
{
  (void)capsule;
  state_storage = NULL;
}

int example_msgs__lazy_import_acquire()
{
  if (state_storage == NULL) {
    lazy_import_state * state = PyMem_Malloc(sizeof(lazy_import_state));
    if (example_msgs__lazy_import_initialize(state) != 0) {
      return 1;
    }
    state_storage = PyCapsule_New(state, NULL, clear_storage);
  } else {
    Py_INCREF(state_storage);
  }
  return 0;
}

int example_msgs__lazy_import_release()
{
  Py_DECREF(state_storage);
  return 0;
}
