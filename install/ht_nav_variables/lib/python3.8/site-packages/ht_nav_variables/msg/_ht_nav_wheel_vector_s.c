// generated from rosidl_generator_py/resource/_idl_support.c.em
// with input from ht_nav_variables:msg/HtNavWheelVector.idl
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
#include "ht_nav_variables/msg/detail/ht_nav_wheel_vector__struct.h"
#include "ht_nav_variables/msg/detail/ht_nav_wheel_vector__functions.h"


ROSIDL_GENERATOR_C_EXPORT
bool ht_nav_variables__msg__ht_nav_wheel_vector__convert_from_py(PyObject * _pymsg, void * _ros_message)
{
  // check that the passed message is of the expected Python class
  {
    char full_classname_dest[59];
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
    assert(strncmp("ht_nav_variables.msg._ht_nav_wheel_vector.HtNavWheelVector", full_classname_dest, 58) == 0);
  }
  ht_nav_variables__msg__HtNavWheelVector * ros_message = _ros_message;
  {  // w1
    PyObject * field = PyObject_GetAttrString(_pymsg, "w1");
    if (!field) {
      return false;
    }
    assert(PyFloat_Check(field));
    ros_message->w1 = PyFloat_AS_DOUBLE(field);
    Py_DECREF(field);
  }
  {  // w2
    PyObject * field = PyObject_GetAttrString(_pymsg, "w2");
    if (!field) {
      return false;
    }
    assert(PyFloat_Check(field));
    ros_message->w2 = PyFloat_AS_DOUBLE(field);
    Py_DECREF(field);
  }
  {  // w3
    PyObject * field = PyObject_GetAttrString(_pymsg, "w3");
    if (!field) {
      return false;
    }
    assert(PyFloat_Check(field));
    ros_message->w3 = PyFloat_AS_DOUBLE(field);
    Py_DECREF(field);
  }
  {  // w4
    PyObject * field = PyObject_GetAttrString(_pymsg, "w4");
    if (!field) {
      return false;
    }
    assert(PyFloat_Check(field));
    ros_message->w4 = PyFloat_AS_DOUBLE(field);
    Py_DECREF(field);
  }

  return true;
}

ROSIDL_GENERATOR_C_EXPORT
PyObject * ht_nav_variables__msg__ht_nav_wheel_vector__convert_to_py(void * raw_ros_message)
{
  /* NOTE(esteve): Call constructor of HtNavWheelVector */
  PyObject * _pymessage = NULL;
  {
    PyObject * pymessage_module = PyImport_ImportModule("ht_nav_variables.msg._ht_nav_wheel_vector");
    assert(pymessage_module);
    PyObject * pymessage_class = PyObject_GetAttrString(pymessage_module, "HtNavWheelVector");
    assert(pymessage_class);
    Py_DECREF(pymessage_module);
    _pymessage = PyObject_CallObject(pymessage_class, NULL);
    Py_DECREF(pymessage_class);
    if (!_pymessage) {
      return NULL;
    }
  }
  ht_nav_variables__msg__HtNavWheelVector * ros_message = (ht_nav_variables__msg__HtNavWheelVector *)raw_ros_message;
  {  // w1
    PyObject * field = NULL;
    field = PyFloat_FromDouble(ros_message->w1);
    {
      int rc = PyObject_SetAttrString(_pymessage, "w1", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // w2
    PyObject * field = NULL;
    field = PyFloat_FromDouble(ros_message->w2);
    {
      int rc = PyObject_SetAttrString(_pymessage, "w2", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // w3
    PyObject * field = NULL;
    field = PyFloat_FromDouble(ros_message->w3);
    {
      int rc = PyObject_SetAttrString(_pymessage, "w3", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // w4
    PyObject * field = NULL;
    field = PyFloat_FromDouble(ros_message->w4);
    {
      int rc = PyObject_SetAttrString(_pymessage, "w4", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }

  // ownership of _pymessage is transferred to the caller
  return _pymessage;
}
