@{
module_name, type_name = full_type_name.rsplit(".", maxsplit=1)
ensure_is_type = locals().get('ensure_is_type', False)
}@
@
static PyObject * @(func_name)()
{
  // TODO(almaslov) proper deinitialization
  static PyObject * py_type = NULL;
  if (py_type != NULL) {
    return py_type;
  }

  PyObject * module = PyImport_ImportModule("@(module_name)");
  if (!module) {
    return NULL;
  }
  py_type = PyObject_GetAttrString(module, "@(type_name)");
  Py_DECREF(module);
  if (!py_type) {
    return NULL;
  }
@[if ensure_is_type]@
  if (!PyType_Check(py_type)) {
    PyErr_SetString(PyExc_RuntimeError, "@(type_name) is not a python type");
    return NULL;
  }
@[end if]@

  return py_type;
}

