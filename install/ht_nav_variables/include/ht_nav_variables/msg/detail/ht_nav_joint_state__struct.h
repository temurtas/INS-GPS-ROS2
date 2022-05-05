// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from ht_nav_variables:msg/HtNavJointState.idl
// generated code does not contain a copyright notice

#ifndef HT_NAV_VARIABLES__MSG__DETAIL__HT_NAV_JOINT_STATE__STRUCT_H_
#define HT_NAV_VARIABLES__MSG__DETAIL__HT_NAV_JOINT_STATE__STRUCT_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>


// Constants defined in the message

// Include directives for member types
// Member 'steering_angle'
// Member 'wheel_rotation'
#include "ht_nav_variables/msg/detail/ht_nav_wheel_vector__struct.h"

// Struct defined in msg/HtNavJointState in the package ht_nav_variables.
typedef struct ht_nav_variables__msg__HtNavJointState
{
  double time;
  ht_nav_variables__msg__HtNavWheelVector steering_angle;
  ht_nav_variables__msg__HtNavWheelVector wheel_rotation;
} ht_nav_variables__msg__HtNavJointState;

// Struct for a sequence of ht_nav_variables__msg__HtNavJointState.
typedef struct ht_nav_variables__msg__HtNavJointState__Sequence
{
  ht_nav_variables__msg__HtNavJointState * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} ht_nav_variables__msg__HtNavJointState__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // HT_NAV_VARIABLES__MSG__DETAIL__HT_NAV_JOINT_STATE__STRUCT_H_
