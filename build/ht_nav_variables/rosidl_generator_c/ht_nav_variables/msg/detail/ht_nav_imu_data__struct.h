// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from ht_nav_variables:msg/HtNavImuData.idl
// generated code does not contain a copyright notice

#ifndef HT_NAV_VARIABLES__MSG__DETAIL__HT_NAV_IMU_DATA__STRUCT_H_
#define HT_NAV_VARIABLES__MSG__DETAIL__HT_NAV_IMU_DATA__STRUCT_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>


// Constants defined in the message

// Include directives for member types
// Member 'vel_diff'
// Member 'ang_diff'
#include "ht_nav_variables/msg/detail/ht_nav_vector3__struct.h"

// Struct defined in msg/HtNavImuData in the package ht_nav_variables.
typedef struct ht_nav_variables__msg__HtNavImuData
{
  double time;
  ht_nav_variables__msg__HtNavVector3 vel_diff;
  ht_nav_variables__msg__HtNavVector3 ang_diff;
} ht_nav_variables__msg__HtNavImuData;

// Struct for a sequence of ht_nav_variables__msg__HtNavImuData.
typedef struct ht_nav_variables__msg__HtNavImuData__Sequence
{
  ht_nav_variables__msg__HtNavImuData * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} ht_nav_variables__msg__HtNavImuData__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // HT_NAV_VARIABLES__MSG__DETAIL__HT_NAV_IMU_DATA__STRUCT_H_
