// generated from rosidl_generator_cpp/resource/idl__traits.hpp.em
// with input from ht_nav_variables:msg/HtNavGpsData.idl
// generated code does not contain a copyright notice

#ifndef HT_NAV_VARIABLES__MSG__DETAIL__HT_NAV_GPS_DATA__TRAITS_HPP_
#define HT_NAV_VARIABLES__MSG__DETAIL__HT_NAV_GPS_DATA__TRAITS_HPP_

#include "ht_nav_variables/msg/detail/ht_nav_gps_data__struct.hpp"
#include <rosidl_runtime_cpp/traits.hpp>
#include <stdint.h>
#include <type_traits>

// Include directives for member types
// Member 'gps_pos'
#include "ht_nav_variables/msg/detail/ht_nav_point__traits.hpp"

namespace rosidl_generator_traits
{

template<>
inline const char * data_type<ht_nav_variables::msg::HtNavGpsData>()
{
  return "ht_nav_variables::msg::HtNavGpsData";
}

template<>
inline const char * name<ht_nav_variables::msg::HtNavGpsData>()
{
  return "ht_nav_variables/msg/HtNavGpsData";
}

template<>
struct has_fixed_size<ht_nav_variables::msg::HtNavGpsData>
  : std::integral_constant<bool, has_fixed_size<ht_nav_variables::msg::HtNavPoint>::value> {};

template<>
struct has_bounded_size<ht_nav_variables::msg::HtNavGpsData>
  : std::integral_constant<bool, has_bounded_size<ht_nav_variables::msg::HtNavPoint>::value> {};

template<>
struct is_message<ht_nav_variables::msg::HtNavGpsData>
  : std::true_type {};

}  // namespace rosidl_generator_traits

#endif  // HT_NAV_VARIABLES__MSG__DETAIL__HT_NAV_GPS_DATA__TRAITS_HPP_
