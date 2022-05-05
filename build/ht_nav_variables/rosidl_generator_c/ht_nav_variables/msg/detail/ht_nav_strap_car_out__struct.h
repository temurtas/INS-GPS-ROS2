// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from ht_nav_variables:msg/HtNavStrapCarOut.idl
// generated code does not contain a copyright notice

#ifndef HT_NAV_VARIABLES__MSG__DETAIL__HT_NAV_STRAP_CAR_OUT__STRUCT_H_
#define HT_NAV_VARIABLES__MSG__DETAIL__HT_NAV_STRAP_CAR_OUT__STRUCT_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>


// Constants defined in the message

// Include directives for member types
// Member 'pos'
// Member 'car_pos'
// Member 'vel'
#include "ht_nav_variables/msg/detail/ht_nav_vector3__struct.h"
// Member 'euler'
#include "ht_nav_variables/msg/detail/ht_nav_euler__struct.h"
// Member 'quaternion'
#include "ht_nav_variables/msg/detail/ht_nav_quaternion__struct.h"

// Struct defined in msg/HtNavStrapCarOut in the package ht_nav_variables.
typedef struct ht_nav_variables__msg__HtNavStrapCarOut
{
  double time;
  ht_nav_variables__msg__HtNavVector3 pos;
  ht_nav_variables__msg__HtNavVector3 car_pos;
  ht_nav_variables__msg__HtNavVector3 vel;
  ht_nav_variables__msg__HtNavEuler euler;
  ht_nav_variables__msg__HtNavQuaternion quaternion;
} ht_nav_variables__msg__HtNavStrapCarOut;

// Struct for a sequence of ht_nav_variables__msg__HtNavStrapCarOut.
typedef struct ht_nav_variables__msg__HtNavStrapCarOut__Sequence
{
  ht_nav_variables__msg__HtNavStrapCarOut * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} ht_nav_variables__msg__HtNavStrapCarOut__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // HT_NAV_VARIABLES__MSG__DETAIL__HT_NAV_STRAP_CAR_OUT__STRUCT_H_
