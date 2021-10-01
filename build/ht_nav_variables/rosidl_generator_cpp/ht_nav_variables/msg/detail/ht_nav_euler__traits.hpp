// generated from rosidl_generator_cpp/resource/idl__traits.hpp.em
// with input from ht_nav_variables:msg/HtNavEuler.idl
// generated code does not contain a copyright notice

#ifndef HT_NAV_VARIABLES__MSG__DETAIL__HT_NAV_EULER__TRAITS_HPP_
#define HT_NAV_VARIABLES__MSG__DETAIL__HT_NAV_EULER__TRAITS_HPP_

#include "ht_nav_variables/msg/detail/ht_nav_euler__struct.hpp"
#include <rosidl_runtime_cpp/traits.hpp>
#include <stdint.h>
#include <type_traits>

namespace rosidl_generator_traits
{

template<>
inline const char * data_type<ht_nav_variables::msg::HtNavEuler>()
{
  return "ht_nav_variables::msg::HtNavEuler";
}

template<>
inline const char * name<ht_nav_variables::msg::HtNavEuler>()
{
  return "ht_nav_variables/msg/HtNavEuler";
}

template<>
struct has_fixed_size<ht_nav_variables::msg::HtNavEuler>
  : std::integral_constant<bool, true> {};

template<>
struct has_bounded_size<ht_nav_variables::msg::HtNavEuler>
  : std::integral_constant<bool, true> {};

template<>
struct is_message<ht_nav_variables::msg::HtNavEuler>
  : std::true_type {};

}  // namespace rosidl_generator_traits

#endif  // HT_NAV_VARIABLES__MSG__DETAIL__HT_NAV_EULER__TRAITS_HPP_
