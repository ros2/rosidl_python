// generated from rosidl_generator_py/resource/_idl_pkg_import.c.em
// generated code does not contain a copyright notice
@
@#######################################################################
@# EmPy template for generating _<idl>_import.c files
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
from collections import OrderedDict
from rosidl_parser.definition import Action
from rosidl_parser.definition import Message
from rosidl_parser.definition import Service
from rosidl_pycommon import convert_camel_case_to_lower_case_underscore


def collect_py_deps(dst, message: Message):
    from rosidl_generator_py.generate_py_impl import SPECIAL_NESTED_BASIC_TYPES
    from rosidl_parser.definition import ACTION_FEEDBACK_SUFFIX
    from rosidl_parser.definition import ACTION_GOAL_SUFFIX
    from rosidl_parser.definition import ACTION_RESULT_SUFFIX
    from rosidl_parser.definition import ACTION_GOAL_SERVICE_SUFFIX
    from rosidl_parser.definition import ACTION_RESULT_SERVICE_SUFFIX
    from rosidl_parser.definition import ACTION_FEEDBACK_MESSAGE_SUFFIX
    from rosidl_parser.definition import SERVICE_EVENT_MESSAGE_SUFFIX
    from rosidl_parser.definition import SERVICE_REQUEST_MESSAGE_SUFFIX
    from rosidl_parser.definition import SERVICE_RESPONSE_MESSAGE_SUFFIX
    from rosidl_parser.definition import AbstractNestedType
    from rosidl_parser.definition import AbstractSequence
    from rosidl_parser.definition import Array
    from rosidl_parser.definition import BasicType
    from rosidl_parser.definition import NamespacedType
    from rosidl_pycommon import convert_camel_case_to_lower_case_underscore

    def cut_service_or_action_suffix(name):
        for suffix in (
            SERVICE_EVENT_MESSAGE_SUFFIX, SERVICE_REQUEST_MESSAGE_SUFFIX, SERVICE_RESPONSE_MESSAGE_SUFFIX,
            ACTION_GOAL_SERVICE_SUFFIX, ACTION_RESULT_SERVICE_SUFFIX, ACTION_FEEDBACK_MESSAGE_SUFFIX,
            ACTION_FEEDBACK_SUFFIX, ACTION_GOAL_SUFFIX, ACTION_RESULT_SUFFIX,
        ):
            if name.endswith(suffix):
                name = name[:-len(suffix)]
        return name

    for member in message.structure.members:
        if isinstance(member.type, AbstractNestedType) and isinstance(member.type.value_type, BasicType) and member.type.value_type.typename in SPECIAL_NESTED_BASIC_TYPES:
            if isinstance(member.type, Array):
                if 'numpy.ndarray' not in dst:
                    dst['numpy.ndarray'] = ('numpy', 'ndarray', False)
                dtype = SPECIAL_NESTED_BASIC_TYPES[member.type.value_type.typename]['dtype']
                if dtype not in dst:
                    module, name = dtype.rsplit('.', maxsplit=1)
                    dst[dtype] = (module, name, False)
            elif isinstance(member.type, AbstractSequence) and 'array.array' not in dst:
                dst['array.array'] = ('array', 'array', False)

    interface_name = cut_service_or_action_suffix(message.structure.namespaced_type.name)
    module_name = '_' + convert_camel_case_to_lower_case_underscore(interface_name)
    full_module_name = ".".join((*message.structure.namespaced_type.namespaces, module_name))
    object_name = message.structure.namespaced_type.name
    type_name = ".".join(message.structure.namespaced_type.namespaced_name())

    assert type_name not in dst
    # For example_msgs.srv.MyService_Request from example_msgs/srv/MyService.srv added
    #   ["example_msgs.srv.MyService_Request"] = ("example_msgs.msg._my_service", "MyService_Request", True)
    dst[type_name] = (full_module_name, object_name, True)


required_py_objects = OrderedDict()

for message in content.get_elements_of_type(Message):
    collect_py_deps(required_py_objects, message)

for service in content.get_elements_of_type(Service):
    collect_py_deps(required_py_objects, service.request_message)
    collect_py_deps(required_py_objects, service.response_message)
    collect_py_deps(required_py_objects, service.event_message)

for action in content.get_elements_of_type(Action):
    collect_py_deps(required_py_objects, action.goal)
    collect_py_deps(required_py_objects, action.result)
    collect_py_deps(required_py_objects, action.feedback)
    collect_py_deps(required_py_objects, action.send_goal_service.request_message)
    collect_py_deps(required_py_objects, action.send_goal_service.response_message)
    collect_py_deps(required_py_objects, action.send_goal_service.event_message)
    collect_py_deps(required_py_objects, action.get_result_service.request_message)
    collect_py_deps(required_py_objects, action.get_result_service.response_message)
    collect_py_deps(required_py_objects, action.get_result_service.event_message)
    collect_py_deps(required_py_objects, action.feedback_message)

}@
#include <Python.h>
#include <stdbool.h>
#include "./_@(package_name)_decl.h"


typedef struct
{
  const char * module_name;
  const char * object_name;
  bool ensure_is_type;
} lazy_import_info;


static lazy_import_info import_infos[MAX__IMPORT_INDEX] = {
@[for type_name, (module_name, object_name, ensure) in required_py_objects.items()]@
@{  parts = type_name.split('.')}@
@{  const_name = '__'.join(parts[:-1] + [convert_camel_case_to_lower_case_underscore(parts[-1])]).upper()}@
@{  ensure_is_type = "true" if ensure else "false"}@
  // @(type_name)
  [@(const_name)__IMPORT_INDEX] = {"@(module_name)", "@(object_name)", @(ensure_is_type)},
@[end for]@
};

int @(package_name)__lazy_import_initialize(lazy_import_state * state)
{
  assert(state != NULL);
  for (size_t i = 0; i < MAX__IMPORT_INDEX; ++i) {
    state->cached_imports[i] = NULL;
  }
  return 0;
}

int @(package_name)__lazy_import_finalize(lazy_import_state * state)
{
  assert(state != NULL);
  for (size_t i = 0; i < MAX__IMPORT_INDEX; ++i) {
    Py_CLEAR(state->cached_imports[i]);
  }
  return 0;
}


static PyObject * state_storage = NULL;

PyObject * @(package_name)__lazy_import(lazy_import_state * state, size_t index)
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

int @(package_name)__lazy_import_acquire()
{
  if (state_storage == NULL) {
    lazy_import_state * state = PyMem_Malloc(sizeof(lazy_import_state));
    if (@(package_name)__lazy_import_initialize(state) != 0) {
      return 1;
    }
    state_storage = PyCapsule_New(state, NULL, clear_storage);
  } else {
    Py_INCREF(state_storage);
  }
  return 0;
}

int @(package_name)__lazy_import_release()
{
  Py_DECREF(state_storage);
  return 0;
}
