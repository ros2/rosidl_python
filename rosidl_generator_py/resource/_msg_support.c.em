@# Included from rosidl_generator_py/resource/_idl.py.em
#define NPY_NO_DEPRECATED_API NPY_1_7_API_VERSION
@{
from rosidl_cmake import convert_camel_case_to_lower_case_underscore
from rosidl_generator_py.generate_py_impl import SPECIAL_NESTED_BASIC_TYPES
from rosidl_parser.definition import Array
from rosidl_parser.definition import BasicType
from rosidl_parser.definition import NamespacedType
from rosidl_parser.definition import NestedType
from rosidl_parser.definition import Sequence
from rosidl_parser.definition import String
from rosidl_parser.definition import WString


def primitive_msg_type_to_c(type_):
    from rosidl_generator_c import BASIC_IDL_TYPES_TO_C
    from rosidl_parser.definition import BasicType
    from rosidl_parser.definition import String
    if isinstance(type_, String):
        return 'rosidl_generator_c__String'
    assert isinstance(type_, BasicType)
    return BASIC_IDL_TYPES_TO_C[type_.type]


include_parts = [package_name] + list(interface_path.parents[0].parts) + \
    [convert_camel_case_to_lower_case_underscore(interface_path.stem)]
include_base = '/'.join(include_parts)

header_files = [
    'Python.h',
    'stdbool.h',
    'numpy/ndarrayobject.h',
    'rosidl_generator_c/visibility_control.h',
    include_base + '__struct.h',
    include_base + '__functions.h',
]
}@
@[for header_file in header_files]@
@{
repeated_header_file = header_file in include_directives
}@
@[    if repeated_header_file]@
// already included above
// @
@[    else]@
@[      if header_file == 'numpy/ndarrayobject.h']@
#ifndef _WIN32
# pragma GCC diagnostic push
# pragma GCC diagnostic ignored "-Wunused-function"
#endif
@[      end if]@
@{include_directives.add(header_file)}@
@[    end if]@
@[    if '/' not in header_file]@
#include <@(header_file)>
@[    else]@
#include "@(header_file)"
@[    end if]@
@[    if header_file == 'numpy/ndarrayobject.h' and not repeated_header_file]@
#ifndef _WIN32
# pragma GCC diagnostic pop
#endif
@[    end if]@
@[end for]@

@{
have_not_included_primitive_arrays = True
have_not_included_string = True
have_not_included_wstring = True
nested_types = set()
}@
@[for member in message.structure.members]@
@{
type_ = member.type
if isinstance(type_, NestedType):
    type_ = type_.basetype
header_files = []
if isinstance(member.type, NestedType) and have_not_included_primitive_arrays:
    have_not_included_primitive_arrays = False
    header_files += [
        'rosidl_generator_c/primitives_sequence.h',
        'rosidl_generator_c/primitives_sequence_functions.h']
if isinstance(type_, String) and have_not_included_string:
    have_not_included_string = False
    header_files += [
        'rosidl_generator_c/string.h',
        'rosidl_generator_c/string_functions.h']
if isinstance(type_, WString) and have_not_included_wstring:
    have_not_included_wstring = False
    header_files += [
        'rosidl_generator_c/u16string.h',
        'rosidl_generator_c/u16string_functions.h']
}@
@[if header_files]@
@[  for header_file in header_files]@
@[    if header_file in include_directives]@
// already included above
// @
@[    else]@
@{include_directives.add(header_file)}@
@[    end if]@
#include "@(header_file)"
@[  end for]@

@[end if]@
@{
if isinstance(member.type, NestedType) and isinstance(member.type.basetype, NamespacedType):
    nested_types.add((*member.type.basetype.namespaces, member.type.basetype.name))
}@
@[end for]@
@[if nested_types]@
// Nested array functions includes
@[  for type_ in sorted(nested_types)]@
#include "@('/'.join(type_[:-1]))/@(convert_camel_case_to_lower_case_underscore(type_[-1]))__functions.h"
@[  end for]@
// end nested array functions include
@[end if]@
@{
msg_typename = '__'.join(message.structure.type.namespaces + [message.structure.type.name])
}@
@
@[for member in message.structure.members]@
@{
type_ = member.type
if isinstance(type_, NestedType):
    type_ = type_.basetype
}@
@[  if isinstance(type_, NamespacedType)]@
@[    if type_.namespaces[0] != package_name]@
ROSIDL_GENERATOR_C_IMPORT
@[    end if]@
bool @('__'.join(type_.namespaces + [convert_camel_case_to_lower_case_underscore(type_.name)]))__convert_from_py(PyObject * _pymsg, void * _ros_message);
@[    if type_.namespaces[0] != package_name]@
ROSIDL_GENERATOR_C_IMPORT
@[    end if]@
PyObject * @('__'.join(type_.namespaces + [convert_camel_case_to_lower_case_underscore(type_.name)]))__convert_to_py(void * raw_ros_message);
@[  end if]@
@[end for]@

@{
module_name = '_' + convert_camel_case_to_lower_case_underscore(interface_path.stem)
}@
ROSIDL_GENERATOR_C_EXPORT
bool @('__'.join(message.structure.type.namespaces + [convert_camel_case_to_lower_case_underscore(message.structure.type.name)]))__convert_from_py(PyObject * _pymsg, void * _ros_message)
{
@{
full_classname = '%s.%s.%s' % ('.'.join(message.structure.type.namespaces), module_name, message.structure.type.name)
}@
  // check that the passed message is of the expected Python class
  {
    char full_classname_dest[@(len(full_classname) + 1)];
    {
      char * class_name = NULL;
      char * module_name = NULL;
      {
        PyObject * class_attr = PyObject_GetAttrString(_pymsg, "__class__");
        if (class_attr) {
          PyObject * name_attr = PyObject_GetAttrString(class_attr, "__name__");
          if (name_attr) {
            class_name = (char *)PyUnicode_1BYTE_DATA(name_attr);
            Py_DECREF(name_attr);
          }
          PyObject * module_attr = PyObject_GetAttrString(class_attr, "__module__");
          if (module_attr) {
            module_name = (char *)PyUnicode_1BYTE_DATA(module_attr);
            Py_DECREF(module_attr);
          }
          Py_DECREF(class_attr);
        }
      }
      if (!class_name || !module_name) {
        return false;
      }
      snprintf(full_classname_dest, sizeof(full_classname_dest), "%s.%s", module_name, class_name);
    }
    assert(strncmp(
        "@(full_classname)",
        full_classname_dest, @(len(full_classname))) == 0);
  }
  @(msg_typename) * ros_message = _ros_message;
@[for member in message.structure.members]@
@{
type_ = member.type
if isinstance(type_, NestedType):
    type_ = type_.basetype
}@
  {  // @(member.name)
    PyObject * field = PyObject_GetAttrString(_pymsg, "@(member.name)");
    if (!field) {
      return false;
    }
@[  if isinstance(type_, NamespacedType)]@
@{
nested_type = '__'.join(type_.namespaces + [type_.name])
}@
@[    if isinstance(member.type, NestedType)]@
    PyObject * seq_field = PySequence_Fast(field, "expected a sequence in '@(member.name)'");
    if (!seq_field) {
      Py_DECREF(field);
      return false;
    }
@[      if isinstance(member.type, Sequence)]@
    Py_ssize_t size = PySequence_Size(field);
    if (-1 == size) {
      Py_DECREF(seq_field);
      Py_DECREF(field);
      return false;
    }
    if (!@(nested_type)__Sequence__init(&(ros_message->@(member.name)), size)) {
      PyErr_SetString(PyExc_RuntimeError, "unable to create @(nested_type)__Sequence ros_message");
      Py_DECREF(seq_field);
      Py_DECREF(field);
      return false;
    }
    @(nested_type) * dest = ros_message->@(member.name).data;
@[      else]@
    Py_ssize_t size = @(member.type.size);
    @(nested_type) * dest = ros_message->@(member.name);
@[      end if]@
    for (Py_ssize_t i = 0; i < size; ++i) {
      if (!@('__'.join(type_.namespaces + [convert_camel_case_to_lower_case_underscore(type_.name)]))__convert_from_py(PySequence_Fast_GET_ITEM(seq_field, i), &dest[i])) {
        Py_DECREF(seq_field);
        Py_DECREF(field);
        return false;
      }
    }
    Py_DECREF(seq_field);
@[    else]@
    if (!@('__'.join(type_.namespaces + [convert_camel_case_to_lower_case_underscore(type_.name)]))__convert_from_py(field, &ros_message->@(member.name))) {
      Py_DECREF(field);
      return false;
    }
@[    end if]@
@[  elif isinstance(member.type, NestedType)]@
@[    if isinstance(member.type, Array) and isinstance(member.type.basetype, BasicType) and member.type.basetype.type in SPECIAL_NESTED_BASIC_TYPES]@
    // TODO(dirk-thomas) use a better way to check the type before casting
    assert(field->ob_type != NULL);
    assert(field->ob_type->tp_name != NULL);
    assert(strcmp(field->ob_type->tp_name, "numpy.ndarray") == 0);
    PyArrayObject * seq_field = (PyArrayObject *)field;
    Py_INCREF(seq_field);
    assert(PyArray_NDIM(seq_field) == 1);
    assert(PyArray_TYPE(seq_field) == @(SPECIAL_NESTED_BASIC_TYPES[member.type.basetype.type]['dtype'].replace('numpy.', 'NPY_').upper()));
@[    else]@
    PyObject * seq_field = PySequence_Fast(field, "expected a sequence in '@(member.name)'");
    if (!seq_field) {
      Py_DECREF(field);
      return false;
    }
@[    end if]@
@[    if isinstance(member.type, Sequence)]@
    Py_ssize_t size = PySequence_Size(field);
    if (-1 == size) {
      Py_DECREF(seq_field);
      Py_DECREF(field);
      return false;
    }
@[      if isinstance(member.type.basetype, String)]@
    if (!rosidl_generator_c__String__Sequence__init(&(ros_message->@(member.name)), size)) {
      PyErr_SetString(PyExc_RuntimeError, "unable to create String__Sequence ros_message");
      Py_DECREF(seq_field);
      Py_DECREF(field);
      return false;
    }
@[      else]@
    if (!rosidl_generator_c__@(member.type.basetype.type)__Sequence__init(&(ros_message->@(member.name)), size)) {
      PyErr_SetString(PyExc_RuntimeError, "unable to create @(member.type.basetype.type)__Sequence ros_message");
      Py_DECREF(seq_field);
      Py_DECREF(field);
      return false;
    }
@[      end if]@
    @primitive_msg_type_to_c(member.type.basetype) * dest = ros_message->@(member.name).data;
@[    else]@
    Py_ssize_t size = @(member.type.size);
    @primitive_msg_type_to_c(member.type.basetype) * dest = ros_message->@(member.name);
@[    end if]@
    for (Py_ssize_t i = 0; i < size; ++i) {
@[    if not isinstance(member.type, Array) or not isinstance(member.type.basetype, BasicType) or member.type.basetype.type not in SPECIAL_NESTED_BASIC_TYPES]@
      PyObject * item = PySequence_Fast_GET_ITEM(seq_field, i);
      if (!item) {
        Py_DECREF(seq_field);
        Py_DECREF(field);
        return false;
      }
@[    end if]@
@[    if isinstance(member.type, Array) and isinstance(member.type.basetype, BasicType) and member.type.basetype.type in SPECIAL_NESTED_BASIC_TYPES]@
      @primitive_msg_type_to_c(member.type.basetype) tmp = *(@(SPECIAL_NESTED_BASIC_TYPES[member.type.basetype.type]['dtype'].replace('numpy.', 'npy_')) *)PyArray_GETPTR1(seq_field, i);
@[    elif isinstance(member.type.basetype, BasicType) and member.type.basetype.type == 'char']@
      assert(PyUnicode_Check(item));
      PyObject * encoded_item = PyUnicode_AsASCIIString(item);
      if (!encoded_item) {
        Py_DECREF(seq_field);
        Py_DECREF(field);
        return false;
      }
      @primitive_msg_type_to_c(member.type.basetype) tmp = PyBytes_AS_STRING(encoded_item)[0];
      Py_DECREF(encoded_item);
@[    elif isinstance(member.type.basetype, BasicType) and member.type.basetype.type == 'octet']@
      assert(PyBytes_Check(item));
      @primitive_msg_type_to_c(member.type.basetype) tmp = PyBytes_AS_STRING(item)[0];
@[    elif isinstance(member.type.basetype, String)]@
      assert(PyUnicode_Check(item));
      PyObject * encoded_item = PyUnicode_AsASCIIString(item);
      if (!encoded_item) {
        Py_DECREF(seq_field);
        Py_DECREF(field);
        return false;
      }
      rosidl_generator_c__String__assign(&dest[i], PyBytes_AS_STRING(encoded_item));
      Py_DECREF(encoded_item);
@[    elif isinstance(member.type.basetype, BasicType) and member.type.basetype.type == 'boolean']@
      assert(PyBool_Check(item));
      @primitive_msg_type_to_c(member.type.basetype) tmp = (item == Py_True);
@[    elif isinstance(member.type.basetype, BasicType) and member.type.basetype.type in ('float', 'double')]@
      assert(PyFloat_Check(item));
@[      if member.type.basetype.type == 'float']@
      @primitive_msg_type_to_c(member.type.basetype) tmp = (float)PyFloat_AS_DOUBLE(item);
@[      else]@
      @primitive_msg_type_to_c(member.type.basetype) tmp = PyFloat_AS_DOUBLE(item);
@[      end if]@
@[    elif isinstance(member.type.basetype, BasicType) and member.type.basetype.type in (
        'int8',
        'int16',
        'int32',
    )]@
      assert(PyLong_Check(item));
      @primitive_msg_type_to_c(member.type.basetype) tmp = (@(primitive_msg_type_to_c(member.type.basetype)))PyLong_AsLong(item);
@[    elif isinstance(member.type.basetype, BasicType) and member.type.basetype.type in (
        'uint8',
        'uint16',
        'uint32',
    )]@
      assert(PyLong_Check(item));
@[      if isinstance(member.type.basetype, BasicType) and member.type.basetype.type == 'uint32']@
      @primitive_msg_type_to_c(member.type.basetype) tmp = PyLong_AsUnsignedLong(item);
@[      else]@
      @primitive_msg_type_to_c(member.type.basetype) tmp = (@(primitive_msg_type_to_c(member.type.basetype)))PyLong_AsUnsignedLong(item);
@[      end if]
@[    elif isinstance(member.type.basetype, BasicType) and member.type.basetype.type == 'int64']@
      assert(PyLong_Check(item));
      @primitive_msg_type_to_c(member.type.basetype) tmp = PyLong_AsLongLong(item);
@[    elif isinstance(member.type.basetype, BasicType) and member.type.basetype.type == 'uint64']@
      assert(PyLong_Check(item));
      @primitive_msg_type_to_c(member.type.basetype) tmp = PyLong_AsUnsignedLongLong(item);
@[    end if]@
@[    if isinstance(member.type.basetype, BasicType)]@
      memcpy(&dest[i], &tmp, sizeof(@primitive_msg_type_to_c(member.type.basetype)));
@[    end if]@
    }
    Py_DECREF(seq_field);
@[  elif isinstance(member.type, BasicType) and member.type.type == 'char']@
    assert(PyUnicode_Check(field));
    PyObject * encoded_field = PyUnicode_AsASCIIString(field);
    if (!encoded_field) {
      Py_DECREF(field);
      return false;
    }
    ros_message->@(member.name) = PyBytes_AS_STRING(encoded_field)[0];
    Py_DECREF(encoded_field);
@[  elif isinstance(member.type, BasicType) and member.type.type == 'octet']@
    assert(PyBytes_Check(field));
    ros_message->@(member.name) = PyBytes_AS_STRING(field)[0];
@[  elif isinstance(member.type, String)]@
    assert(PyUnicode_Check(field));
    PyObject * encoded_field = PyUnicode_AsASCIIString(field);
    if (!encoded_field) {
      Py_DECREF(field);
      return false;
    }
    rosidl_generator_c__String__assign(&ros_message->@(member.name), PyBytes_AS_STRING(encoded_field));
    Py_DECREF(encoded_field);
@[  elif isinstance(member.type, BasicType) and member.type.type == 'boolean']@
    assert(PyBool_Check(field));
    ros_message->@(member.name) = (Py_True == field);
@[  elif isinstance(member.type, BasicType) and member.type.type in ('float', 'double')]@
    assert(PyFloat_Check(field));
@[    if member.type.type == 'float']@
    ros_message->@(member.name) = (float)PyFloat_AS_DOUBLE(field);
@[    else]@
    ros_message->@(member.name) = PyFloat_AS_DOUBLE(field);
@[    end if]@
@[  elif isinstance(member.type, BasicType) and member.type.type in (
        'int8',
        'int16',
        'int32',
    )]@
    assert(PyLong_Check(field));
    ros_message->@(member.name) = (@(primitive_msg_type_to_c(member.type)))PyLong_AsLong(field);
@[  elif isinstance(member.type, BasicType) and member.type.type in (
        'uint8',
        'uint16',
        'uint32',
    )]@
    assert(PyLong_Check(field));
@[    if member.type.type == 'uint32']@
    ros_message->@(member.name) = PyLong_AsUnsignedLong(field);
@[    else]@
    ros_message->@(member.name) = (@(primitive_msg_type_to_c(member.type)))PyLong_AsUnsignedLong(field);
@[    end if]@
@[  elif isinstance(member.type, BasicType) and member.type.type == 'int64']@
    assert(PyLong_Check(field));
    ros_message->@(member.name) = PyLong_AsLongLong(field);
@[  elif isinstance(member.type, BasicType) and member.type.type == 'uint64']@
    assert(PyLong_Check(field));
    ros_message->@(member.name) = PyLong_AsUnsignedLongLong(field);
@[  else]@
    assert(false);
@[  end if]@
    Py_DECREF(field);
  }
@[end for]@

  return true;
}

ROSIDL_GENERATOR_C_EXPORT
PyObject * @('__'.join(message.structure.type.namespaces + [convert_camel_case_to_lower_case_underscore(message.structure.type.name)]))__convert_to_py(void * raw_ros_message)
{
  /* NOTE(esteve): Call constructor of @(message.structure.type.name) */
  PyObject * _pymessage = NULL;
  {
    PyObject * pymessage_module = PyImport_ImportModule("@('.'.join(message.structure.type.namespaces)).@(module_name)");
    assert(pymessage_module);
    PyObject * pymessage_class = PyObject_GetAttrString(pymessage_module, "@(message.structure.type.name)");
    assert(pymessage_class);
    Py_DECREF(pymessage_module);
    _pymessage = PyObject_CallObject(pymessage_class, NULL);
    Py_DECREF(pymessage_class);
    if (!_pymessage) {
      return NULL;
    }
  }
  @(msg_typename) * ros_message = (@(msg_typename) *)raw_ros_message;
@[for member in message.structure.members]@
@{
type_ = member.type
if isinstance(type_, NestedType):
    type_ = type_.basetype
}@
  {  // @(member.name)
    PyObject * field = NULL;
@[ if isinstance(member.type, NestedType) and isinstance(member.type.basetype, BasicType) and member.type.basetype.type in SPECIAL_NESTED_BASIC_TYPES]@
@[    if isinstance(member.type, Array)]@
    field = PyObject_GetAttrString(_pymessage, "@(member.name)");
    if (!field) {
      return NULL;
    }
    assert(field->ob_type != NULL);
    assert(field->ob_type->tp_name != NULL);
    assert(strcmp(field->ob_type->tp_name, "numpy.ndarray") == 0);
    PyArrayObject * seq_field = (PyArrayObject *)field;
    assert(PyArray_NDIM(seq_field) == 1);
    assert(PyArray_TYPE(seq_field) == @(SPECIAL_NESTED_BASIC_TYPES[member.type.basetype.type]['dtype'].replace('numpy.', 'NPY_').upper()));
    assert(sizeof(@(SPECIAL_NESTED_BASIC_TYPES[member.type.basetype.type]['dtype'].replace('numpy.', 'npy_'))) == sizeof(@primitive_msg_type_to_c(member.type.basetype)));
    @(SPECIAL_NESTED_BASIC_TYPES[member.type.basetype.type]['dtype'].replace('numpy.', 'npy_')) * dst = (@(SPECIAL_NESTED_BASIC_TYPES[member.type.basetype.type]['dtype'].replace('numpy.', 'npy_')) *)PyArray_GETPTR1(seq_field, 0);
    @primitive_msg_type_to_c(member.type.basetype) * src = &(ros_message->@(member.name)[0]);
    memcpy(dst, src, @(member.type.size) * sizeof(@primitive_msg_type_to_c(member.type.basetype)));
    Py_DECREF(field);
@[    elif isinstance(member.type, Sequence)]@
    if (ros_message->@(member.name).size > 0) {
      field = PyObject_GetAttrString(_pymessage, "@(member.name)");
      if (!field) {
        return NULL;
      }
      assert(field->ob_type != NULL);
      assert(field->ob_type->tp_name != NULL);
      assert(strcmp(field->ob_type->tp_name, "array.array") == 0);
      // ensure that itemsize matches the sizeof of the ROS message field
      PyObject * itemsize_attr = PyObject_GetAttrString(field, "itemsize");
      assert(itemsize_attr != NULL);
      size_t itemsize = PyLong_AsSize_t(itemsize_attr);
      Py_DECREF(itemsize_attr);
      if (itemsize != sizeof(@primitive_msg_type_to_c(member.type.basetype))) {
        PyErr_SetString(PyExc_RuntimeError, "itemsize doesn't match expectation");
        Py_DECREF(field);
        return NULL;
      }
      // populating the array.array using the frombytes method
      PyObject * frombytes = PyObject_GetAttrString(field, "frombytes");
      assert(frombytes != NULL);
      @primitive_msg_type_to_c(member.type.basetype) * src = &(ros_message->@(member.name).data[0]);
      PyObject * data = PyBytes_FromStringAndSize((const char *)src, ros_message->@(member.name).size * sizeof(@primitive_msg_type_to_c(member.type.basetype)));
      assert(data != NULL);
      PyObject * ret = PyObject_CallFunctionObjArgs(frombytes, data, NULL);
      Py_DECREF(data);
      Py_DECREF(frombytes);
      if (!ret) {
        Py_DECREF(field);
        return NULL;
      }
      Py_DECREF(ret);
      Py_DECREF(field);
    }
@[    end if]@
@[ else]@
@[  if isinstance(type_, NamespacedType)]@
@{
nested_type = '__'.join(type_.namespaces + [type_.name])
}@
@[    if isinstance(member.type, NestedType)]@
@[      if isinstance(member.type, Sequence)]@
    size_t size = ros_message->@(member.name).size;
@[      else]@
    size_t size = @(member.type.size);
@[      end if]@
    field = PyList_New(size);
    if (!field) {
      return NULL;
    }
    @(nested_type) * item;
    for (size_t i = 0; i < size; ++i) {
@[      if isinstance(member.type, Sequence)]@
      item = &(ros_message->@(member.name).data[i]);
@[      else]@
      item = &(ros_message->@(member.name)[i]);
@[      end if]@
      PyObject * pyitem = @('__'.join(type_.namespaces + [convert_camel_case_to_lower_case_underscore(type_.name)]))__convert_to_py(item);
      if (!pyitem) {
        Py_DECREF(field);
        return NULL;
      }
      int rc = PyList_SetItem(field, i, pyitem);
      (void)rc;
      assert(rc == 0);
    }
    assert(PySequence_Check(field));
@[    else]@
    field = @('__'.join(type_.namespaces + [convert_camel_case_to_lower_case_underscore(type_.name)]))__convert_to_py(&ros_message->@(member.name));
    if (!field) {
      return NULL;
    }
@[    end if]@
@[  elif isinstance(member.type, NestedType)]@
@[    if isinstance(member.type, Sequence)]@
    size_t size = ros_message->@(member.name).size;
    @primitive_msg_type_to_c(member.type.basetype) * src = ros_message->@(member.name).data;
@[    else]@
    size_t size = @(member.type.size);
    @primitive_msg_type_to_c(member.type.basetype) * src = ros_message->@(member.name);
@[    end if]@
    field = PyList_New(size);
    if (!field) {
      return NULL;
    }
    for (size_t i = 0; i < size; ++i) {
@[    if isinstance(member.type.basetype, BasicType) and member.type.basetype.type == 'char']@
      int rc = PyList_SetItem(field, i, Py_BuildValue("C", src[i]));
      (void)rc;
      assert(rc == 0);
@[    elif isinstance(member.type.basetype, BasicType) and member.type.basetype.type == 'octet']@
      int rc = PyList_SetItem(field, i, PyBytes_FromStringAndSize((const char *)&src[i], 1));
      (void)rc;
      assert(rc == 0);
@[    elif isinstance(member.type.basetype, String)]@
      PyObject * decoded_item = PyUnicode_DecodeASCII(src[i].data, strlen(src[i].data), "strict");
      if (!decoded_item) {
        return NULL;
      }
      int rc = PyList_SetItem(field, i, decoded_item);
      (void)rc;
      assert(rc == 0);
@[    elif isinstance(member.type.basetype, BasicType) and member.type.basetype.type == 'boolean']@
@# using PyBool_FromLong because PyList_SetItem will steal ownership of the passed item
      int rc = PyList_SetItem(field, i, PyBool_FromLong(src[i] ? 1 : 0));
      (void)rc;
      assert(rc == 0);
@[    elif isinstance(member.type.basetype, BasicType) and member.type.basetype.type in ('float', 'double')]@
      int rc = PyList_SetItem(field, i, PyFloat_FromDouble(src[i]));
      (void)rc;
      assert(rc == 0);
@[    elif isinstance(member.type.basetype, BasicType) and member.type.basetype.type in (
        'int8',
        'int16',
        'int32',
    )]@
      int rc = PyList_SetItem(field, i, PyLong_FromLong(src[i]));
      (void)rc;
      assert(rc == 0);
@[    elif isinstance(member.type.basetype, BasicType) and member.type.basetype.type in (
        'uint8',
        'uint16',
        'uint32',
    )]@
      int rc = PyList_SetItem(field, i, PyLong_FromUnsignedLong(src[i]));
      (void)rc;
      assert(rc == 0);
@[    elif isinstance(member.type.basetype, BasicType) and member.type.basetype.type == 'int64']@
      int rc = PyList_SetItem(field, i, PyLong_FromLongLong(src[i]));
      (void)rc;
      assert(rc == 0);
@[    elif isinstance(member.type.basetype, BasicType) and member.type.basetype.type == 'uint64']@
      int rc = PyList_SetItem(field, i, PyLong_FromUnsignedLongLong(src[i]));
      (void)rc;
      assert(rc == 0);
@[    end if]@
    }
    assert(PySequence_Check(field));
@[  elif isinstance(member.type, BasicType) and member.type.type == 'char']@
    field = Py_BuildValue("C", ros_message->@(member.name));
    if (!field) {
      return NULL;
    }
@[  elif isinstance(member.type, BasicType) and member.type.type == 'octet']@
    field = PyBytes_FromStringAndSize((const char *)&ros_message->@(member.name), 1);
    if (!field) {
      return NULL;
    }
@[  elif isinstance(member.type, String)]@
    field = PyUnicode_DecodeASCII(
      ros_message->@(member.name).data,
      strlen(ros_message->@(member.name).data),
      "strict");
    if (!field) {
      return NULL;
    }
@[  elif isinstance(member.type, BasicType) and member.type.type == 'boolean']@
@# using PyBool_FromLong allows treating the variable uniformly by calling Py_DECREF on it later
    field = PyBool_FromLong(ros_message->@(member.name) ? 1 : 0);
@[  elif isinstance(member.type, BasicType) and member.type.type in ('float', 'double')]@
    field = PyFloat_FromDouble(ros_message->@(member.name));
@[  elif isinstance(member.type, BasicType) and member.type.type in (
        'int8',
        'int16',
        'int32',
    )]@
    field = PyLong_FromLong(ros_message->@(member.name));
@[  elif isinstance(member.type, BasicType) and member.type.type in (
        'uint8',
        'uint16',
        'uint32',
    )]@
    field = PyLong_FromUnsignedLong(ros_message->@(member.name));
@[  elif isinstance(member.type, BasicType) and member.type.type == 'int64']@
    field = PyLong_FromLongLong(ros_message->@(member.name));
@[  elif isinstance(member.type, BasicType) and member.type.type == 'uint64']@
    field = PyLong_FromUnsignedLongLong(ros_message->@(member.name));
@[  else]@
    assert(false);
@[  end if]@
    {
      int rc = PyObject_SetAttrString(_pymessage, "@(member.name)", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
@[ end if]@
  }
@[end for]@

  // ownership of _pymessage is transferred to the caller
  return _pymessage;
}
