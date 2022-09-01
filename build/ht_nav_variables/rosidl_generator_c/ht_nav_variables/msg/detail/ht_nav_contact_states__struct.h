// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from ht_nav_variables:msg/HtNavContactStates.idl
// generated code does not contain a copyright notice

#ifndef HT_NAV_VARIABLES__MSG__DETAIL__HT_NAV_CONTACT_STATES__STRUCT_H_
#define HT_NAV_VARIABLES__MSG__DETAIL__HT_NAV_CONTACT_STATES__STRUCT_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>


// Constants defined in the message

// Include directives for member types
// Member 'fl_wheel_contact_states'
// Member 'fr_wheel_contact_states'
// Member 'rl_wheel_contact_states'
// Member 'rr_wheel_contact_states'
#include "ht_nav_variables/msg/detail/ht_nav_contact_state__struct.h"

// Struct defined in msg/HtNavContactStates in the package ht_nav_variables.
typedef struct ht_nav_variables__msg__HtNavContactStates
{
  double time;
  ht_nav_variables__msg__HtNavContactState fl_wheel_contact_states;
  ht_nav_variables__msg__HtNavContactState fr_wheel_contact_states;
  ht_nav_variables__msg__HtNavContactState rl_wheel_contact_states;
  ht_nav_variables__msg__HtNavContactState rr_wheel_contact_states;
} ht_nav_variables__msg__HtNavContactStates;

// Struct for a sequence of ht_nav_variables__msg__HtNavContactStates.
typedef struct ht_nav_variables__msg__HtNavContactStates__Sequence
{
  ht_nav_variables__msg__HtNavContactStates * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} ht_nav_variables__msg__HtNavContactStates__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // HT_NAV_VARIABLES__MSG__DETAIL__HT_NAV_CONTACT_STATES__STRUCT_H_
