// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from ht_nav_variables:msg/HtNavErrorVector.idl
// generated code does not contain a copyright notice

#ifndef HT_NAV_VARIABLES__MSG__DETAIL__HT_NAV_ERROR_VECTOR__STRUCT_H_
#define HT_NAV_VARIABLES__MSG__DETAIL__HT_NAV_ERROR_VECTOR__STRUCT_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>


// Constants defined in the message

// Struct defined in msg/HtNavErrorVector in the package ht_nav_variables.
typedef struct ht_nav_variables__msg__HtNavErrorVector
{
  double x;
  double y;
  double z;
} ht_nav_variables__msg__HtNavErrorVector;

// Struct for a sequence of ht_nav_variables__msg__HtNavErrorVector.
typedef struct ht_nav_variables__msg__HtNavErrorVector__Sequence
{
  ht_nav_variables__msg__HtNavErrorVector * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} ht_nav_variables__msg__HtNavErrorVector__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // HT_NAV_VARIABLES__MSG__DETAIL__HT_NAV_ERROR_VECTOR__STRUCT_H_
