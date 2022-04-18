// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from ht_nav_variables:msg/HtNavVehicleDebug.idl
// generated code does not contain a copyright notice

#ifndef HT_NAV_VARIABLES__MSG__DETAIL__HT_NAV_VEHICLE_DEBUG__STRUCT_H_
#define HT_NAV_VARIABLES__MSG__DETAIL__HT_NAV_VEHICLE_DEBUG__STRUCT_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>


// Constants defined in the message

// Include directives for member types
// Member 'wheel_variables'
#include "ht_nav_variables/msg/detail/ht_nav_tire_out__struct.h"
// Member 'imu_link_pva'
// Member 'fl_wheel_pva'
// Member 'fr_wheel_pva'
// Member 'rl_wheel_pva'
// Member 'rr_wheel_pva'
#include "ht_nav_variables/msg/detail/ht_nav_strap_out__struct.h"

// Struct defined in msg/HtNavVehicleDebug in the package ht_nav_variables.
typedef struct ht_nav_variables__msg__HtNavVehicleDebug
{
  double time;
  ht_nav_variables__msg__HtNavTireOut wheel_variables;
  ht_nav_variables__msg__HtNavStrapOut imu_link_pva;
  ht_nav_variables__msg__HtNavStrapOut fl_wheel_pva;
  ht_nav_variables__msg__HtNavStrapOut fr_wheel_pva;
  ht_nav_variables__msg__HtNavStrapOut rl_wheel_pva;
  ht_nav_variables__msg__HtNavStrapOut rr_wheel_pva;
} ht_nav_variables__msg__HtNavVehicleDebug;

// Struct for a sequence of ht_nav_variables__msg__HtNavVehicleDebug.
typedef struct ht_nav_variables__msg__HtNavVehicleDebug__Sequence
{
  ht_nav_variables__msg__HtNavVehicleDebug * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} ht_nav_variables__msg__HtNavVehicleDebug__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // HT_NAV_VARIABLES__MSG__DETAIL__HT_NAV_VEHICLE_DEBUG__STRUCT_H_
