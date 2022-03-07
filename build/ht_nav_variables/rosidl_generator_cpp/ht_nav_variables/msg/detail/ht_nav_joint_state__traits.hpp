// generated from rosidl_generator_cpp/resource/idl__traits.hpp.em
// with input from ht_nav_variables:msg/HtNavJointState.idl
// generated code does not contain a copyright notice

#ifndef HT_NAV_VARIABLES__MSG__DETAIL__HT_NAV_JOINT_STATE__TRAITS_HPP_
#define HT_NAV_VARIABLES__MSG__DETAIL__HT_NAV_JOINT_STATE__TRAITS_HPP_

#include "ht_nav_variables/msg/detail/ht_nav_joint_state__struct.hpp"
#include <rosidl_runtime_cpp/traits.hpp>
#include <stdint.h>
#include <type_traits>

// Include directives for member types
// Member 'steering_angle'
// Member 'wheel_rotation'
#include "ht_nav_variables/msg/detail/ht_nav_wheel_vector__traits.hpp"

namespace rosidl_generator_traits
{

template<>
inline const char * data_type<ht_nav_variables::msg::HtNavJointState>()
{
  return "ht_nav_variables::msg::HtNavJointState";
}

template<>
inline const char * name<ht_nav_variables::msg::HtNavJointState>()
{
  return "ht_nav_variables/msg/HtNavJointState";
}

template<>
struct has_fixed_size<ht_nav_variables::msg::HtNavJointState>
  : std::integral_constant<bool, has_fixed_size<ht_nav_variables::msg::HtNavWheelVector>::value> {};

template<>
struct has_bounded_size<ht_nav_variables::msg::HtNavJointState>
  : std::integral_constant<bool, has_bounded_size<ht_nav_variables::msg::HtNavWheelVector>::value> {};

template<>
struct is_message<ht_nav_variables::msg::HtNavJointState>
  : std::true_type {};

}  // namespace rosidl_generator_traits

#endif  // HT_NAV_VARIABLES__MSG__DETAIL__HT_NAV_JOINT_STATE__TRAITS_HPP_
