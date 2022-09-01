// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from ht_nav_variables:msg/HtNavContactState.idl
// generated code does not contain a copyright notice

#ifndef HT_NAV_VARIABLES__MSG__DETAIL__HT_NAV_CONTACT_STATE__STRUCT_H_
#define HT_NAV_VARIABLES__MSG__DETAIL__HT_NAV_CONTACT_STATE__STRUCT_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>


// Constants defined in the message

// Include directives for member types
// Member 'ideal_contact_forces'
// Member 'ideal_pacejka_forces'
// Member 'ideal_slip'
#include "ht_nav_variables/msg/detail/ht_nav_vector3__struct.h"

// Struct defined in msg/HtNavContactState in the package ht_nav_variables.
typedef struct ht_nav_variables__msg__HtNavContactState
{
  double time;
  ht_nav_variables__msg__HtNavVector3 ideal_contact_forces;
  ht_nav_variables__msg__HtNavVector3 ideal_pacejka_forces;
  ht_nav_variables__msg__HtNavVector3 ideal_slip;
} ht_nav_variables__msg__HtNavContactState;

// Struct for a sequence of ht_nav_variables__msg__HtNavContactState.
typedef struct ht_nav_variables__msg__HtNavContactState__Sequence
{
  ht_nav_variables__msg__HtNavContactState * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} ht_nav_variables__msg__HtNavContactState__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // HT_NAV_VARIABLES__MSG__DETAIL__HT_NAV_CONTACT_STATE__STRUCT_H_
