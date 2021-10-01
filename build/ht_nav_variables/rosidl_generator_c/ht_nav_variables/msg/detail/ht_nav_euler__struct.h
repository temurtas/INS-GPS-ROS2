// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from ht_nav_variables:msg/HtNavEuler.idl
// generated code does not contain a copyright notice

#ifndef HT_NAV_VARIABLES__MSG__DETAIL__HT_NAV_EULER__STRUCT_H_
#define HT_NAV_VARIABLES__MSG__DETAIL__HT_NAV_EULER__STRUCT_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>


// Constants defined in the message

// Struct defined in msg/HtNavEuler in the package ht_nav_variables.
typedef struct ht_nav_variables__msg__HtNavEuler
{
  double roll;
  double pitch;
  double yaw;
} ht_nav_variables__msg__HtNavEuler;

// Struct for a sequence of ht_nav_variables__msg__HtNavEuler.
typedef struct ht_nav_variables__msg__HtNavEuler__Sequence
{
  ht_nav_variables__msg__HtNavEuler * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} ht_nav_variables__msg__HtNavEuler__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // HT_NAV_VARIABLES__MSG__DETAIL__HT_NAV_EULER__STRUCT_H_
