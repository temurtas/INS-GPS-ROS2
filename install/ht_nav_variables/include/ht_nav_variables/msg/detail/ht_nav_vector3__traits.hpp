// generated from rosidl_generator_cpp/resource/idl__traits.hpp.em
// with input from ht_nav_variables:msg/HtNavVector3.idl
// generated code does not contain a copyright notice

#ifndef HT_NAV_VARIABLES__MSG__DETAIL__HT_NAV_VECTOR3__TRAITS_HPP_
#define HT_NAV_VARIABLES__MSG__DETAIL__HT_NAV_VECTOR3__TRAITS_HPP_

#include "ht_nav_variables/msg/detail/ht_nav_vector3__struct.hpp"
#include <rosidl_runtime_cpp/traits.hpp>
#include <stdint.h>
#include <type_traits>

namespace rosidl_generator_traits
{

template<>
inline const char * data_type<ht_nav_variables::msg::HtNavVector3>()
{
  return "ht_nav_variables::msg::HtNavVector3";
}

template<>
inline const char * name<ht_nav_variables::msg::HtNavVector3>()
{
  return "ht_nav_variables/msg/HtNavVector3";
}

template<>
struct has_fixed_size<ht_nav_variables::msg::HtNavVector3>
  : std::integral_constant<bool, true> {};

template<>
struct has_bounded_size<ht_nav_variables::msg::HtNavVector3>
  : std::integral_constant<bool, true> {};

template<>
struct is_message<ht_nav_variables::msg::HtNavVector3>
  : std::true_type {};

}  // namespace rosidl_generator_traits

#endif  // HT_NAV_VARIABLES__MSG__DETAIL__HT_NAV_VECTOR3__TRAITS_HPP_
