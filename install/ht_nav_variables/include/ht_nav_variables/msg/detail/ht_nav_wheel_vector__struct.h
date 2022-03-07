// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from ht_nav_variables:msg/HtNavWheelVector.idl
// generated code does not contain a copyright notice

#ifndef HT_NAV_VARIABLES__MSG__DETAIL__HT_NAV_WHEEL_VECTOR__STRUCT_H_
#define HT_NAV_VARIABLES__MSG__DETAIL__HT_NAV_WHEEL_VECTOR__STRUCT_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>


// Constants defined in the message

// Struct defined in msg/HtNavWheelVector in the package ht_nav_variables.
typedef struct ht_nav_variables__msg__HtNavWheelVector
{
  double w1;
  double w2;
  double w3;
  double w4;
} ht_nav_variables__msg__HtNavWheelVector;

// Struct for a sequence of ht_nav_variables__msg__HtNavWheelVector.
typedef struct ht_nav_variables__msg__HtNavWheelVector__Sequence
{
  ht_nav_variables__msg__HtNavWheelVector * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} ht_nav_variables__msg__HtNavWheelVector__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // HT_NAV_VARIABLES__MSG__DETAIL__HT_NAV_WHEEL_VECTOR__STRUCT_H_
