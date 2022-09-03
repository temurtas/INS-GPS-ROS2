// generated from rosidl_generator_py/resource/_idl_support.c.em
// with input from ht_nav_variables:msg/HtNavContactState.idl
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
#include "ht_nav_variables/msg/detail/ht_nav_contact_state__struct.h"
#include "ht_nav_variables/msg/detail/ht_nav_contact_state__functions.h"

bool ht_nav_variables__msg__ht_nav_vector3__convert_from_py(PyObject * _pymsg, void * _ros_message);
PyObject * ht_nav_variables__msg__ht_nav_vector3__convert_to_py(void * raw_ros_message);
bool ht_nav_variables__msg__ht_nav_vector3__convert_from_py(PyObject * _pymsg, void * _ros_message);
PyObject * ht_nav_variables__msg__ht_nav_vector3__convert_to_py(void * raw_ros_message);
bool ht_nav_variables__msg__ht_nav_vector3__convert_from_py(PyObject * _pymsg, void * _ros_message);
PyObject * ht_nav_variables__msg__ht_nav_vector3__convert_to_py(void * raw_ros_message);

ROSIDL_GENERATOR_C_EXPORT
bool ht_nav_variables__msg__ht_nav_contact_state__convert_from_py(PyObject * _pymsg, void * _ros_message)
{
  // check that the passed message is of the expected Python class
  {
    char full_classname_dest[61];
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
    assert(strncmp("ht_nav_variables.msg._ht_nav_contact_state.HtNavContactState", full_classname_dest, 60) == 0);
  }
  ht_nav_variables__msg__HtNavContactState * ros_message = _ros_message;
  {  // time
    PyObject * field = PyObject_GetAttrString(_pymsg, "time");
    if (!field) {
      return false;
    }
    assert(PyFloat_Check(field));
    ros_message->time = PyFloat_AS_DOUBLE(field);
    Py_DECREF(field);
  }
  {  // ideal_contact_forces
    PyObject * field = PyObject_GetAttrString(_pymsg, "ideal_contact_forces");
    if (!field) {
      return false;
    }
    if (!ht_nav_variables__msg__ht_nav_vector3__convert_from_py(field, &ros_message->ideal_contact_forces)) {
      Py_DECREF(field);
      return false;
    }
    Py_DECREF(field);
  }
  {  // ideal_pacejka_forces
    PyObject * field = PyObject_GetAttrString(_pymsg, "ideal_pacejka_forces");
    if (!field) {
      return false;
    }
    if (!ht_nav_variables__msg__ht_nav_vector3__convert_from_py(field, &ros_message->ideal_pacejka_forces)) {
      Py_DECREF(field);
      return false;
    }
    Py_DECREF(field);
  }
  {  // ideal_slip
    PyObject * field = PyObject_GetAttrString(_pymsg, "ideal_slip");
    if (!field) {
      return false;
    }
    if (!ht_nav_variables__msg__ht_nav_vector3__convert_from_py(field, &ros_message->ideal_slip)) {
      Py_DECREF(field);
      return false;
    }
    Py_DECREF(field);
  }

  return true;
}

ROSIDL_GENERATOR_C_EXPORT
PyObject * ht_nav_variables__msg__ht_nav_contact_state__convert_to_py(void * raw_ros_message)
{
  /* NOTE(esteve): Call constructor of HtNavContactState */
  PyObject * _pymessage = NULL;
  {
    PyObject * pymessage_module = PyImport_ImportModule("ht_nav_variables.msg._ht_nav_contact_state");
    assert(pymessage_module);
    PyObject * pymessage_class = PyObject_GetAttrString(pymessage_module, "HtNavContactState");
    assert(pymessage_class);
    Py_DECREF(pymessage_module);
    _pymessage = PyObject_CallObject(pymessage_class, NULL);
    Py_DECREF(pymessage_class);
    if (!_pymessage) {
      return NULL;
    }
  }
  ht_nav_variables__msg__HtNavContactState * ros_message = (ht_nav_variables__msg__HtNavContactState *)raw_ros_message;
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
  {  // ideal_contact_forces
    PyObject * field = NULL;
    field = ht_nav_variables__msg__ht_nav_vector3__convert_to_py(&ros_message->ideal_contact_forces);
    if (!field) {
      return NULL;
    }
    {
      int rc = PyObject_SetAttrString(_pymessage, "ideal_contact_forces", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // ideal_pacejka_forces
    PyObject * field = NULL;
    field = ht_nav_variables__msg__ht_nav_vector3__convert_to_py(&ros_message->ideal_pacejka_forces);
    if (!field) {
      return NULL;
    }
    {
      int rc = PyObject_SetAttrString(_pymessage, "ideal_pacejka_forces", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // ideal_slip
    PyObject * field = NULL;
    field = ht_nav_variables__msg__ht_nav_vector3__convert_to_py(&ros_message->ideal_slip);
    if (!field) {
      return NULL;
    }
    {
      int rc = PyObject_SetAttrString(_pymessage, "ideal_slip", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }

  // ownership of _pymessage is transferred to the caller
  return _pymessage;
}