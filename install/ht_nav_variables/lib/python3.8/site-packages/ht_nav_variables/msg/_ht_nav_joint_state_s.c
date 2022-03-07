// generated from rosidl_generator_py/resource/_idl_support.c.em
// with input from ht_nav_variables:msg/HtNavJointState.idl
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
#include "ht_nav_variables/msg/detail/ht_nav_joint_state__struct.h"
#include "ht_nav_variables/msg/detail/ht_nav_joint_state__functions.h"

bool ht_nav_variables__msg__ht_nav_wheel_vector__convert_from_py(PyObject * _pymsg, void * _ros_message);
PyObject * ht_nav_variables__msg__ht_nav_wheel_vector__convert_to_py(void * raw_ros_message);
bool ht_nav_variables__msg__ht_nav_wheel_vector__convert_from_py(PyObject * _pymsg, void * _ros_message);
PyObject * ht_nav_variables__msg__ht_nav_wheel_vector__convert_to_py(void * raw_ros_message);

ROSIDL_GENERATOR_C_EXPORT
bool ht_nav_variables__msg__ht_nav_joint_state__convert_from_py(PyObject * _pymsg, void * _ros_message)
{
  // check that the passed message is of the expected Python class
  {
    char full_classname_dest[57];
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
    assert(strncmp("ht_nav_variables.msg._ht_nav_joint_state.HtNavJointState", full_classname_dest, 56) == 0);
  }
  ht_nav_variables__msg__HtNavJointState * ros_message = _ros_message;
  {  // steering_angle
    PyObject * field = PyObject_GetAttrString(_pymsg, "steering_angle");
    if (!field) {
      return false;
    }
    if (!ht_nav_variables__msg__ht_nav_wheel_vector__convert_from_py(field, &ros_message->steering_angle)) {
      Py_DECREF(field);
      return false;
    }
    Py_DECREF(field);
  }
  {  // wheel_rotation
    PyObject * field = PyObject_GetAttrString(_pymsg, "wheel_rotation");
    if (!field) {
      return false;
    }
    if (!ht_nav_variables__msg__ht_nav_wheel_vector__convert_from_py(field, &ros_message->wheel_rotation)) {
      Py_DECREF(field);
      return false;
    }
    Py_DECREF(field);
  }

  return true;
}

ROSIDL_GENERATOR_C_EXPORT
PyObject * ht_nav_variables__msg__ht_nav_joint_state__convert_to_py(void * raw_ros_message)
{
  /* NOTE(esteve): Call constructor of HtNavJointState */
  PyObject * _pymessage = NULL;
  {
    PyObject * pymessage_module = PyImport_ImportModule("ht_nav_variables.msg._ht_nav_joint_state");
    assert(pymessage_module);
    PyObject * pymessage_class = PyObject_GetAttrString(pymessage_module, "HtNavJointState");
    assert(pymessage_class);
    Py_DECREF(pymessage_module);
    _pymessage = PyObject_CallObject(pymessage_class, NULL);
    Py_DECREF(pymessage_class);
    if (!_pymessage) {
      return NULL;
    }
  }
  ht_nav_variables__msg__HtNavJointState * ros_message = (ht_nav_variables__msg__HtNavJointState *)raw_ros_message;
  {  // steering_angle
    PyObject * field = NULL;
    field = ht_nav_variables__msg__ht_nav_wheel_vector__convert_to_py(&ros_message->steering_angle);
    if (!field) {
      return NULL;
    }
    {
      int rc = PyObject_SetAttrString(_pymessage, "steering_angle", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // wheel_rotation
    PyObject * field = NULL;
    field = ht_nav_variables__msg__ht_nav_wheel_vector__convert_to_py(&ros_message->wheel_rotation);
    if (!field) {
      return NULL;
    }
    {
      int rc = PyObject_SetAttrString(_pymessage, "wheel_rotation", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }

  // ownership of _pymessage is transferred to the caller
  return _pymessage;
}
