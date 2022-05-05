// generated from rosidl_generator_cpp/resource/idl__traits.hpp.em
// with input from ht_nav_variables:msg/HtNavStrapCarOut.idl
// generated code does not contain a copyright notice

#ifndef HT_NAV_VARIABLES__MSG__DETAIL__HT_NAV_STRAP_CAR_OUT__TRAITS_HPP_
#define HT_NAV_VARIABLES__MSG__DETAIL__HT_NAV_STRAP_CAR_OUT__TRAITS_HPP_

#include "ht_nav_variables/msg/detail/ht_nav_strap_car_out__struct.hpp"
#include <rosidl_runtime_cpp/traits.hpp>
#include <stdint.h>
#include <type_traits>

// Include directives for member types
// Member 'pos'
// Member 'car_pos'
// Member 'vel'
#include "ht_nav_variables/msg/detail/ht_nav_vector3__traits.hpp"
// Member 'euler'
#include "ht_nav_variables/msg/detail/ht_nav_euler__traits.hpp"
// Member 'quaternion'
#include "ht_nav_variables/msg/detail/ht_nav_quaternion__traits.hpp"

namespace rosidl_generator_traits
{

template<>
inline const char * data_type<ht_nav_variables::msg::HtNavStrapCarOut>()
{
  return "ht_nav_variables::msg::HtNavStrapCarOut";
}

template<>
inline const char * name<ht_nav_variables::msg::HtNavStrapCarOut>()
{
  return "ht_nav_variables/msg/HtNavStrapCarOut";
}

template<>
struct has_fixed_size<ht_nav_variables::msg::HtNavStrapCarOut>
  : std::integral_constant<bool, has_fixed_size<ht_nav_variables::msg::HtNavEuler>::value && has_fixed_size<ht_nav_variables::msg::HtNavQuaternion>::value && has_fixed_size<ht_nav_variables::msg::HtNavVector3>::value> {};

template<>
struct has_bounded_size<ht_nav_variables::msg::HtNavStrapCarOut>
  : std::integral_constant<bool, has_bounded_size<ht_nav_variables::msg::HtNavEuler>::value && has_bounded_size<ht_nav_variables::msg::HtNavQuaternion>::value && has_bounded_size<ht_nav_variables::msg::HtNavVector3>::value> {};

template<>
struct is_message<ht_nav_variables::msg::HtNavStrapCarOut>
  : std::true_type {};

}  // namespace rosidl_generator_traits

#endif  // HT_NAV_VARIABLES__MSG__DETAIL__HT_NAV_STRAP_CAR_OUT__TRAITS_HPP_
