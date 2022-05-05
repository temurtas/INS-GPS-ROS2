// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from ht_nav_variables:msg/HtNavTireOut.idl
// generated code does not contain a copyright notice

#ifndef HT_NAV_VARIABLES__MSG__DETAIL__HT_NAV_TIRE_OUT__STRUCT_H_
#define HT_NAV_VARIABLES__MSG__DETAIL__HT_NAV_TIRE_OUT__STRUCT_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>


// Constants defined in the message

// Include directives for member types
// Member 'wheel_side_slip_ang'
// Member 'wheel_longitudinal_slip_ratio'
// Member 'tire_lateral_forces'
// Member 'tire_longitudinal_forces'
#include "ht_nav_variables/msg/detail/ht_nav_wheel_vector__struct.h"

// Struct defined in msg/HtNavTireOut in the package ht_nav_variables.
typedef struct ht_nav_variables__msg__HtNavTireOut
{
  double time;
  double effective_radius_est;
  double vehicle_mass_est;
  ht_nav_variables__msg__HtNavWheelVector wheel_side_slip_ang;
  ht_nav_variables__msg__HtNavWheelVector wheel_longitudinal_slip_ratio;
  ht_nav_variables__msg__HtNavWheelVector tire_lateral_forces;
  ht_nav_variables__msg__HtNavWheelVector tire_longitudinal_forces;
} ht_nav_variables__msg__HtNavTireOut;

// Struct for a sequence of ht_nav_variables__msg__HtNavTireOut.
typedef struct ht_nav_variables__msg__HtNavTireOut__Sequence
{
  ht_nav_variables__msg__HtNavTireOut * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} ht_nav_variables__msg__HtNavTireOut__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // HT_NAV_VARIABLES__MSG__DETAIL__HT_NAV_TIRE_OUT__STRUCT_H_
