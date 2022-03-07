// generated from rosidl_generator_cpp/resource/idl__traits.hpp.em
// with input from ht_nav_variables:msg/HtNavTireOut.idl
// generated code does not contain a copyright notice

#ifndef HT_NAV_VARIABLES__MSG__DETAIL__HT_NAV_TIRE_OUT__TRAITS_HPP_
#define HT_NAV_VARIABLES__MSG__DETAIL__HT_NAV_TIRE_OUT__TRAITS_HPP_

#include "ht_nav_variables/msg/detail/ht_nav_tire_out__struct.hpp"
#include <rosidl_runtime_cpp/traits.hpp>
#include <stdint.h>
#include <type_traits>

// Include directives for member types
// Member 'wheel_side_slip_ang'
// Member 'wheel_longitudinal_slip_ratio'
// Member 'tire_lateral_forces'
// Member 'tire_longitudinal_forces'
#include "ht_nav_variables/msg/detail/ht_nav_wheel_vector__traits.hpp"

namespace rosidl_generator_traits
{

template<>
inline const char * data_type<ht_nav_variables::msg::HtNavTireOut>()
{
  return "ht_nav_variables::msg::HtNavTireOut";
}

template<>
inline const char * name<ht_nav_variables::msg::HtNavTireOut>()
{
  return "ht_nav_variables/msg/HtNavTireOut";
}

template<>
struct has_fixed_size<ht_nav_variables::msg::HtNavTireOut>
  : std::integral_constant<bool, has_fixed_size<ht_nav_variables::msg::HtNavWheelVector>::value> {};

template<>
struct has_bounded_size<ht_nav_variables::msg::HtNavTireOut>
  : std::integral_constant<bool, has_bounded_size<ht_nav_variables::msg::HtNavWheelVector>::value> {};

template<>
struct is_message<ht_nav_variables::msg::HtNavTireOut>
  : std::true_type {};

}  // namespace rosidl_generator_traits

#endif  // HT_NAV_VARIABLES__MSG__DETAIL__HT_NAV_TIRE_OUT__TRAITS_HPP_
