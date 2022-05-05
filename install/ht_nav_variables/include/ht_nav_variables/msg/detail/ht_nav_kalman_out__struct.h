// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from ht_nav_variables:msg/HtNavKalmanOut.idl
// generated code does not contain a copyright notice

#ifndef HT_NAV_VARIABLES__MSG__DETAIL__HT_NAV_KALMAN_OUT__STRUCT_H_
#define HT_NAV_VARIABLES__MSG__DETAIL__HT_NAV_KALMAN_OUT__STRUCT_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>


// Constants defined in the message

// Include directives for member types
// Member 'pos_err'
// Member 'vel_err'
// Member 'att_err'
// Member 'bias'
// Member 'drift'
#include "ht_nav_variables/msg/detail/ht_nav_error_vector__struct.h"

// Struct defined in msg/HtNavKalmanOut in the package ht_nav_variables.
typedef struct ht_nav_variables__msg__HtNavKalmanOut
{
  double time;
  ht_nav_variables__msg__HtNavErrorVector pos_err;
  ht_nav_variables__msg__HtNavErrorVector vel_err;
  ht_nav_variables__msg__HtNavErrorVector att_err;
  ht_nav_variables__msg__HtNavErrorVector bias;
  ht_nav_variables__msg__HtNavErrorVector drift;
} ht_nav_variables__msg__HtNavKalmanOut;

// Struct for a sequence of ht_nav_variables__msg__HtNavKalmanOut.
typedef struct ht_nav_variables__msg__HtNavKalmanOut__Sequence
{
  ht_nav_variables__msg__HtNavKalmanOut * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} ht_nav_variables__msg__HtNavKalmanOut__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // HT_NAV_VARIABLES__MSG__DETAIL__HT_NAV_KALMAN_OUT__STRUCT_H_
