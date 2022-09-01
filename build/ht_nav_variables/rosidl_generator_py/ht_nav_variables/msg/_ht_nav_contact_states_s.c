// generated from rosidl_generator_py/resource/_idl_support.c.em
// with input from ht_nav_variables:msg/HtNavContactStates.idl
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
#include "ht_nav_variables/msg/detail/ht_nav_contact_states__struct.h"
#include "ht_nav_variables/msg/detail/ht_nav_contact_states__functions.h"

bool ht_nav_variables__msg__ht_nav_contact_state__convert_from_py(PyObject * _pymsg, void * _ros_message);
PyObject * ht_nav_variables__msg__ht_nav_contact_state__convert_to_py(void * raw_ros_message);
bool ht_nav_variables__msg__ht_nav_contact_state__convert_from_py(PyObject * _pymsg, void * _ros_message);
PyObject * ht_nav_variables__msg__ht_nav_contact_state__convert_to_py(void * raw_ros_message);
bool ht_nav_variables__msg__ht_nav_contact_state__convert_from_py(PyObject * _pymsg, void * _ros_message);
PyObject * ht_nav_variables__msg__ht_nav_contact_state__convert_to_py(void * raw_ros_message);
bool ht_nav_variables__msg__ht_nav_contact_state__convert_from_py(PyObject * _pymsg, void * _ros_message);
PyObject * ht_nav_variables__msg__ht_nav_contact_state__convert_to_py(void * raw_ros_message);

ROSIDL_GENERATOR_C_EXPORT
bool ht_nav_variables__msg__ht_nav_contact_states__convert_from_py(PyObject * _pymsg, void * _ros_message)
{
  // check that the passed message is of the expected Python class
  {
    char full_classname_dest[63];
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
    assert(strncmp("ht_nav_variables.msg._ht_nav_contact_states.HtNavContactStates", full_classname_dest, 62) == 0);
  }
  ht_nav_variables__msg__HtNavContactStates * ros_message = _ros_message;
  {  // time
    PyObject * field = PyObject_GetAttrString(_pymsg, "time");
    if (!field) {
      return false;
    }
    assert(PyFloat_Check(field));
    ros_message->time = PyFloat_AS_DOUBLE(field);
    Py_DECREF(field);
  }
  {  // fl_wheel_contact_states
    PyObject * field = PyObject_GetAttrString(_pymsg, "fl_wheel_contact_states");
    if (!field) {
      return false;
    }
    if (!ht_nav_variables__msg__ht_nav_contact_state__convert_from_py(field, &ros_message->fl_wheel_contact_states)) {
      Py_DECREF(field);
      return false;
    }
    Py_DECREF(field);
  }
  {  // fr_wheel_contact_states
    PyObject * field = PyObject_GetAttrString(_pymsg, "fr_wheel_contact_states");
    if (!field) {
      return false;
    }
    if (!ht_nav_variables__msg__ht_nav_contact_state__convert_from_py(field, &ros_message->fr_wheel_contact_states)) {
      Py_DECREF(field);
      return false;
    }
    Py_DECREF(field);
  }
  {  // rl_wheel_contact_states
    PyObject * field = PyObject_GetAttrString(_pymsg, "rl_wheel_contact_states");
    if (!field) {
      return false;
    }
    if (!ht_nav_variables__msg__ht_nav_contact_state__convert_from_py(field, &ros_message->rl_wheel_contact_states)) {
      Py_DECREF(field);
      return false;
    }
    Py_DECREF(field);
  }
  {  // rr_wheel_contact_states
    PyObject * field = PyObject_GetAttrString(_pymsg, "rr_wheel_contact_states");
    if (!field) {
      return false;
    }
    if (!ht_nav_variables__msg__ht_nav_contact_state__convert_from_py(field, &ros_message->rr_wheel_contact_states)) {
      Py_DECREF(field);
      return false;
    }
    Py_DECREF(field);
  }

  return true;
}

ROSIDL_GENERATOR_C_EXPORT
PyObject * ht_nav_variables__msg__ht_nav_contact_states__convert_to_py(void * raw_ros_message)
{
  /* NOTE(esteve): Call constructor of HtNavContactStates */
  PyObject * _pymessage = NULL;
  {
    PyObject * pymessage_module = PyImport_ImportModule("ht_nav_variables.msg._ht_nav_contact_states");
    assert(pymessage_module);
    PyObject * pymessage_class = PyObject_GetAttrString(pymessage_module, "HtNavContactStates");
    assert(pymessage_class);
    Py_DECREF(pymessage_module);
    _pymessage = PyObject_CallObject(pymessage_class, NULL);
    Py_DECREF(pymessage_class);
    if (!_pymessage) {
      return NULL;
    }
  }
  ht_nav_variables__msg__HtNavContactStates * ros_message = (ht_nav_variables__msg__HtNavContactStates *)raw_ros_message;
  {  // time
    PyObject * field = NULL;
    field = PyFloat_FromDouble(ros_message->time);
    {
      int rc = PyObject_SetAttrString(_pymessage, "time", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // fl_wheel_contact_states
    PyObject * field = NULL;
    field = ht_nav_variables__msg__ht_nav_contact_state__convert_to_py(&ros_message->fl_wheel_contact_states);
    if (!field) {
      return NULL;
    }
    {
      int rc = PyObject_SetAttrString(_pymessage, "fl_wheel_contact_states", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // fr_wheel_contact_states
    PyObject * field = NULL;
    field = ht_nav_variables__msg__ht_nav_contact_state__convert_to_py(&ros_message->fr_wheel_contact_states);
    if (!field) {
      return NULL;
    }
    {
      int rc = PyObject_SetAttrString(_pymessage, "fr_wheel_contact_states", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // rl_wheel_contact_states
    PyObject * field = NULL;
    field = ht_nav_variables__msg__ht_nav_contact_state__convert_to_py(&ros_message->rl_wheel_contact_states);
    if (!field) {
      return NULL;
    }
    {
      int rc = PyObject_SetAttrString(_pymessage, "rl_wheel_contact_states", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // rr_wheel_contact_states
    PyObject * field = NULL;
    field = ht_nav_variables__msg__ht_nav_contact_state__convert_to_py(&ros_message->rr_wheel_contact_states);
    if (!field) {
      return NULL;
    }
    {
      int rc = PyObject_SetAttrString(_pymessage, "rr_wheel_contact_states", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }

  // ownership of _pymessage is transferred to the caller
  return _pymessage;
}
