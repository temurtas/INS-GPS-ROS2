// generated from rosidl_generator_cpp/resource/idl__traits.hpp.em
// with input from ht_nav_variables:msg/HtNavVehicleDebug.idl
// generated code does not contain a copyright notice

#ifndef HT_NAV_VARIABLES__MSG__DETAIL__HT_NAV_VEHICLE_DEBUG__TRAITS_HPP_
#define HT_NAV_VARIABLES__MSG__DETAIL__HT_NAV_VEHICLE_DEBUG__TRAITS_HPP_

#include "ht_nav_variables/msg/detail/ht_nav_vehicle_debug__struct.hpp"
#include <rosidl_runtime_cpp/traits.hpp>
#include <stdint.h>
#include <type_traits>

// Include directives for member types
// Member 'wheel_variables'
#include "ht_nav_variables/msg/detail/ht_nav_tire_out__traits.hpp"
// Member 'imu_link_pva'
// Member 'fl_wheel_pva'
// Member 'fr_wheel_pva'
// Member 'rl_wheel_pva'
// Member 'rr_wheel_pva'
#include "ht_nav_variables/msg/detail/ht_nav_strap_out__traits.hpp"

namespace rosidl_generator_traits
{

template<>
inline const char * data_type<ht_nav_variables::msg::HtNavVehicleDebug>()
{
  return "ht_nav_variables::msg::HtNavVehicleDebug";
}

template<>
inline const char * name<ht_nav_variables::msg::HtNavVehicleDebug>()
{
  return "ht_nav_variables/msg/HtNavVehicleDebug";
}

template<>
struct has_fixed_size<ht_nav_variables::msg::HtNavVehicleDebug>
  : std::integral_constant<bool, has_fixed_size<ht_nav_variables::msg::HtNavStrapOut>::value && has_fixed_size<ht_nav_variables::msg::HtNavTireOut>::value> {};

template<>
struct has_bounded_size<ht_nav_variables::msg::HtNavVehicleDebug>
  : std::integral_constant<bool, has_bounded_size<ht_nav_variables::msg::HtNavStrapOut>::value && has_bounded_size<ht_nav_variables::msg::HtNavTireOut>::value> {};

template<>
struct is_message<ht_nav_variables::msg::HtNavVehicleDebug>
  : std::true_type {};

}  // namespace rosidl_generator_traits

#endif  // HT_NAV_VARIABLES__MSG__DETAIL__HT_NAV_VEHICLE_DEBUG__TRAITS_HPP_
