// generated from rosidl_generator_py/resource/_idl_support.c.em
// with input from ht_nav_variables:msg/HtNavStrapOut.idl
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
#include "ht_nav_variables/msg/detail/ht_nav_strap_out__struct.h"
#include "ht_nav_variables/msg/detail/ht_nav_strap_out__functions.h"

bool ht_nav_variables__msg__ht_nav_point__convert_from_py(PyObject * _pymsg, void * _ros_message);
PyObject * ht_nav_variables__msg__ht_nav_point__convert_to_py(void * raw_ros_message);
bool ht_nav_variables__msg__ht_nav_vector3__convert_from_py(PyObject * _pymsg, void * _ros_message);
PyObject * ht_nav_variables__msg__ht_nav_vector3__convert_to_py(void * raw_ros_message);
bool ht_nav_variables__msg__ht_nav_euler__convert_from_py(PyObject * _pymsg, void * _ros_message);
PyObject * ht_nav_variables__msg__ht_nav_euler__convert_to_py(void * raw_ros_message);
bool ht_nav_variables__msg__ht_nav_quaternion__convert_from_py(PyObject * _pymsg, void * _ros_message);
PyObject * ht_nav_variables__msg__ht_nav_quaternion__convert_to_py(void * raw_ros_message);

ROSIDL_GENERATOR_C_EXPORT
bool ht_nav_variables__msg__ht_nav_strap_out__convert_from_py(PyObject * _pymsg, void * _ros_message)
{
  // check that the passed message is of the expected Python class
  {
    char full_classname_dest[53];
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
    assert(strncmp("ht_nav_variables.msg._ht_nav_strap_out.HtNavStrapOut", full_classname_dest, 52) == 0);
  }
  ht_nav_variables__msg__HtNavStrapOut * ros_message = _ros_message;
  {  // pos
    PyObject * field = PyObject_GetAttrString(_pymsg, "pos");
    if (!field) {
      return false;
    }
    if (!ht_nav_variables__msg__ht_nav_point__convert_from_py(field, &ros_message->pos)) {
      Py_DECREF(field);
      return false;
    }
    Py_DECREF(field);
  }
  {  // vel
    PyObject * field = PyObject_GetAttrString(_pymsg, "vel");
    if (!field) {
      return false;
    }
    if (!ht_nav_variables__msg__ht_nav_vector3__convert_from_py(field, &ros_message->vel)) {
      Py_DECREF(field);
      return false;
    }
    Py_DECREF(field);
  }
  {  // euler
    PyObject * field = PyObject_GetAttrString(_pymsg, "euler");
    if (!field) {
      return false;
    }
    if (!ht_nav_variables__msg__ht_nav_euler__convert_from_py(field, &ros_message->euler)) {
      Py_DECREF(field);
      return false;
    }
    Py_DECREF(field);
  }
  {  // quaternion
    PyObject * field = PyObject_GetAttrString(_pymsg, "quaternion");
    if (!field) {
      return false;
    }
    if (!ht_nav_variables__msg__ht_nav_quaternion__convert_from_py(field, &ros_message->quaternion)) {
      Py_DECREF(field);
      return false;
    }
    Py_DECREF(field);
  }

  return true;
}

ROSIDL_GENERATOR_C_EXPORT
PyObject * ht_nav_variables__msg__ht_nav_strap_out__convert_to_py(void * raw_ros_message)
{
  /* NOTE(esteve): Call constructor of HtNavStrapOut */
  PyObject * _pymessage = NULL;
  {
    PyObject * pymessage_module = PyImport_ImportModule("ht_nav_variables.msg._ht_nav_strap_out");
    assert(pymessage_module);
    PyObject * pymessage_class = PyObject_GetAttrString(pymessage_module, "HtNavStrapOut");
    assert(pymessage_class);
    Py_DECREF(pymessage_module);
    _pymessage = PyObject_CallObject(pymessage_class, NULL);
    Py_DECREF(pymessage_class);
    if (!_pymessage) {
      return NULL;
    }
  }
  ht_nav_variables__msg__HtNavStrapOut * ros_message = (ht_nav_variables__msg__HtNavStrapOut *)raw_ros_message;
  {  // pos
    PyObject * field = NULL;
    field = ht_nav_variables__msg__ht_nav_point__convert_to_py(&ros_message->pos);
    if (!field) {
      return NULL;
    }
    {
      int rc = PyObject_SetAttrString(_pymessage, "pos", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // vel
    PyObject * field = NULL;
    field = ht_nav_variables__msg__ht_nav_vector3__convert_to_py(&ros_message->vel);
    if (!field) {
      return NULL;
    }
    {
      int rc = PyObject_SetAttrString(_pymessage, "vel", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // euler
    PyObject * field = NULL;
    field = ht_nav_variables__msg__ht_nav_euler__convert_to_py(&ros_message->euler);
    if (!field) {
      return NULL;
    }
    {
      int rc = PyObject_SetAttrString(_pymessage, "euler", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // quaternion
    PyObject * field = NULL;
    field = ht_nav_variables__msg__ht_nav_quaternion__convert_to_py(&ros_message->quaternion);
    if (!field) {
      return NULL;
    }
    {
      int rc = PyObject_SetAttrString(_pymessage, "quaternion", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }

  // ownership of _pymessage is transferred to the caller
  return _pymessage;
}
