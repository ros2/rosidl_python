// generated from rosidl_generator_py/resource/_idl_pkg_bases.c.em
// generated code does not contain a copyright notice
#include <Python.h>
#include <stdbool.h>
#include <structmember.h>
#include "./_example_msgs_decl.h"


static struct PyMemberDef CustomMessageBase_members[] = {
  {"_x", T_USHORT, offsetof(CustomMessageBase, _x), 0, NULL},
  {"_ts", T_OBJECT, offsetof(CustomMessageBase, _ts), 0, NULL},
  {"_fixed_seq", T_OBJECT, offsetof(CustomMessageBase, _fixed_seq), 0, NULL},
  {"_limited_seq", T_OBJECT, offsetof(CustomMessageBase, _limited_seq), 0, NULL},
  {"_unlimited_seq", T_OBJECT, offsetof(CustomMessageBase, _unlimited_seq), 0, NULL},
  {NULL}  /* Sentinel */
};

static void CustomMessageBase_dealloc(CustomMessageBase * self)
{
  Py_XDECREF(self->_ts);
  Py_XDECREF(self->_fixed_seq);
  Py_XDECREF(self->_limited_seq);
  Py_XDECREF(self->_unlimited_seq);
  Py_TYPE(self)->tp_free((PyObject *)self);
}


static PyTypeObject CustomMessageBaseType = {
  PyVarObject_HEAD_INIT(NULL, 0)
  .tp_name = "CustomMessageBase",
  .tp_doc = "Base for CustomMessage python class",
  .tp_basicsize = sizeof(CustomMessageBase),
  .tp_itemsize = 0,
  .tp_flags = Py_TPFLAGS_DEFAULT | Py_TPFLAGS_BASETYPE,
  .tp_new = PyType_GenericNew,
  .tp_dealloc = (destructor)CustomMessageBase_dealloc,
  .tp_members = CustomMessageBase_members,
};


static int8_t _register_base_msg_type__msg__custom_message(PyObject * module)
{
  if (PyType_Ready(&CustomMessageBaseType) < 0) {
    return 1;
  }

  Py_INCREF(&CustomMessageBaseType);
  if (PyModule_AddObject(module, "CustomMessageBase", (PyObject *) &CustomMessageBaseType) < 0) {
    Py_DECREF(&CustomMessageBaseType);
    return 1;
  }
  return 0;
}
// already included above
// #include <Python.h>
// already included above
// #include <stdbool.h>
// already included above
// #include <structmember.h>
// already included above
// #include "./_example_msgs_decl.h"


static struct PyMemberDef CustomCall_RequestBase_members[] = {
  {"_my_param", T_INT, offsetof(CustomCall_RequestBase, _my_param), 0, NULL},
  {NULL}  /* Sentinel */
};

static void CustomCall_RequestBase_dealloc(CustomCall_RequestBase * self)
{
  Py_TYPE(self)->tp_free((PyObject *)self);
}


static PyTypeObject CustomCall_RequestBaseType = {
  PyVarObject_HEAD_INIT(NULL, 0)
  .tp_name = "CustomCall_RequestBase",
  .tp_doc = "Base for CustomCall_Request python class",
  .tp_basicsize = sizeof(CustomCall_RequestBase),
  .tp_itemsize = 0,
  .tp_flags = Py_TPFLAGS_DEFAULT | Py_TPFLAGS_BASETYPE,
  .tp_new = PyType_GenericNew,
  .tp_dealloc = (destructor)CustomCall_RequestBase_dealloc,
  .tp_members = CustomCall_RequestBase_members,
};


static int8_t _register_base_msg_type__srv__custom_call__request(PyObject * module)
{
  if (PyType_Ready(&CustomCall_RequestBaseType) < 0) {
    return 1;
  }

  Py_INCREF(&CustomCall_RequestBaseType);
  if (PyModule_AddObject(module, "CustomCall_RequestBase", (PyObject *) &CustomCall_RequestBaseType) < 0) {
    Py_DECREF(&CustomCall_RequestBaseType);
    return 1;
  }
  return 0;
}

// already included above
// #include <Python.h>
// already included above
// #include <stdbool.h>
// already included above
// #include <structmember.h>
// already included above
// #include "./_example_msgs_decl.h"


static struct PyMemberDef CustomCall_ResponseBase_members[] = {
  {"_my_result", T_INT, offsetof(CustomCall_ResponseBase, _my_result), 0, NULL},
  {NULL}  /* Sentinel */
};

static void CustomCall_ResponseBase_dealloc(CustomCall_ResponseBase * self)
{
  Py_TYPE(self)->tp_free((PyObject *)self);
}


static PyTypeObject CustomCall_ResponseBaseType = {
  PyVarObject_HEAD_INIT(NULL, 0)
  .tp_name = "CustomCall_ResponseBase",
  .tp_doc = "Base for CustomCall_Response python class",
  .tp_basicsize = sizeof(CustomCall_ResponseBase),
  .tp_itemsize = 0,
  .tp_flags = Py_TPFLAGS_DEFAULT | Py_TPFLAGS_BASETYPE,
  .tp_new = PyType_GenericNew,
  .tp_dealloc = (destructor)CustomCall_ResponseBase_dealloc,
  .tp_members = CustomCall_ResponseBase_members,
};


static int8_t _register_base_msg_type__srv__custom_call__response(PyObject * module)
{
  if (PyType_Ready(&CustomCall_ResponseBaseType) < 0) {
    return 1;
  }

  Py_INCREF(&CustomCall_ResponseBaseType);
  if (PyModule_AddObject(module, "CustomCall_ResponseBase", (PyObject *) &CustomCall_ResponseBaseType) < 0) {
    Py_DECREF(&CustomCall_ResponseBaseType);
    return 1;
  }
  return 0;
}

// already included above
// #include <Python.h>
// already included above
// #include <stdbool.h>
// already included above
// #include <structmember.h>
// already included above
// #include "./_example_msgs_decl.h"


static struct PyMemberDef CustomCall_EventBase_members[] = {
  {"_info", T_OBJECT, offsetof(CustomCall_EventBase, _info), 0, NULL},
  {"_request", T_OBJECT, offsetof(CustomCall_EventBase, _request), 0, NULL},
  {"_response", T_OBJECT, offsetof(CustomCall_EventBase, _response), 0, NULL},
  {NULL}  /* Sentinel */
};

static void CustomCall_EventBase_dealloc(CustomCall_EventBase * self)
{
  Py_XDECREF(self->_info);
  Py_XDECREF(self->_request);
  Py_XDECREF(self->_response);
  Py_TYPE(self)->tp_free((PyObject *)self);
}


static PyTypeObject CustomCall_EventBaseType = {
  PyVarObject_HEAD_INIT(NULL, 0)
  .tp_name = "CustomCall_EventBase",
  .tp_doc = "Base for CustomCall_Event python class",
  .tp_basicsize = sizeof(CustomCall_EventBase),
  .tp_itemsize = 0,
  .tp_flags = Py_TPFLAGS_DEFAULT | Py_TPFLAGS_BASETYPE,
  .tp_new = PyType_GenericNew,
  .tp_dealloc = (destructor)CustomCall_EventBase_dealloc,
  .tp_members = CustomCall_EventBase_members,
};


static int8_t _register_base_msg_type__srv__custom_call__event(PyObject * module)
{
  if (PyType_Ready(&CustomCall_EventBaseType) < 0) {
    return 1;
  }

  Py_INCREF(&CustomCall_EventBaseType);
  if (PyModule_AddObject(module, "CustomCall_EventBase", (PyObject *) &CustomCall_EventBaseType) < 0) {
    Py_DECREF(&CustomCall_EventBaseType);
    return 1;
  }
  return 0;
}


static PyModuleDef _module = {
  PyModuleDef_HEAD_INIT,
  .m_name = "_example_msgs_bases",
  .m_doc = "Extention module for example_msgs messages",
  .m_size = -1,
};


PyMODINIT_FUNC
PyInit__example_msgs_bases(void)
{
  PyObject * pymodule = NULL;
  pymodule = PyModule_Create(&_module);
  if (!pymodule) {
    return NULL;
  }
  int8_t err;

  err = _register_base_msg_type__msg__custom_message(pymodule);
  if (err) {
    Py_XDECREF(pymodule);
    return NULL;
  }

  err = _register_base_msg_type__srv__custom_call__request(pymodule);
  if (err) {
    Py_XDECREF(pymodule);
    return NULL;
  }

  err = _register_base_msg_type__srv__custom_call__response(pymodule);
  if (err) {
    Py_XDECREF(pymodule);
    return NULL;
  }

  err = _register_base_msg_type__srv__custom_call__event(pymodule);
  if (err) {
    Py_XDECREF(pymodule);
    return NULL;
  }

  return pymodule;
}
