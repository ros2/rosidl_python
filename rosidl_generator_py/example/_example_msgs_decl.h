// generated from rosidl_generator_py/resource/_idl_pkg_decl.c.em
// generated code does not contain a copyright notice
#pragma once
#include <Python.h>
#include <stdbool.h>
#include <structmember.h>


typedef struct
{
  PyObject_HEAD
  /* Type-specific fields go here. */
  uint16_t _x;
  PyObject * _ts;
  PyObject * _fixed_seq;
  PyObject * _limited_seq;
  PyObject * _unlimited_seq;
} CustomMessageBase;

// Import support constants for CustomMessageBase type
#define NUMPY__NDARRAY__IMPORT_INDEX 0
#define NUMPY__INT16__IMPORT_INDEX 1
#define ARRAY__ARRAY__IMPORT_INDEX 2
#define EXAMPLE_MSGS__MSG__CUSTOM_MESSAGE__IMPORT_INDEX 3

// already included above
// #include <Python.h>
// already included above
// #include <stdbool.h>
// already included above
// #include <structmember.h>


typedef struct
{
  PyObject_HEAD
  /* Type-specific fields go here. */
  int32_t _my_param;
} CustomCall_RequestBase;

// Import support constants for CustomCall_RequestBase type
#define EXAMPLE_MSGS__SRV__CUSTOM_CALL__REQUEST__IMPORT_INDEX 4


// already included above
// #include <Python.h>
// already included above
// #include <stdbool.h>
// already included above
// #include <structmember.h>


typedef struct
{
  PyObject_HEAD
  /* Type-specific fields go here. */
  int32_t _my_result;
} CustomCall_ResponseBase;

// Import support constants for CustomCall_ResponseBase type
#define EXAMPLE_MSGS__SRV__CUSTOM_CALL__RESPONSE__IMPORT_INDEX 5


// already included above
// #include <Python.h>
// already included above
// #include <stdbool.h>
// already included above
// #include <structmember.h>


typedef struct
{
  PyObject_HEAD
  /* Type-specific fields go here. */
  PyObject * _info;
  PyObject * _request;
  PyObject * _response;
} CustomCall_EventBase;

// Import support constants for CustomCall_EventBase type
#define EXAMPLE_MSGS__SRV__CUSTOM_CALL__EVENT__IMPORT_INDEX 6


#define MAX__IMPORT_INDEX 7

typedef struct lazy_import_state
{
  PyObject * cached_imports[MAX__IMPORT_INDEX];
} lazy_import_state;

int example_msgs__lazy_import_initialize(lazy_import_state * state);
int example_msgs__lazy_import_finalize(lazy_import_state * state);
PyObject * example_msgs__lazy_import(lazy_import_state * state, size_t index);

// Since lazy cache global state is shared between multiple typesupport implementations,
// its lifetime should be managed carefully. Extention module can call `__lazy_import`
// function only between `__lazy_import_acquire` and `__lazy_import_release` calls.
// This functions should be removed when cache state becomes module specific.
int example_msgs__lazy_import_acquire();
int example_msgs__lazy_import_release();
