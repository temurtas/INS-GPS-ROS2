// generated from rosidl_generator_cpp/resource/idl__traits.hpp.em
// with input from ht_nav_variables:msg/HtNavContactStates.idl
// generated code does not contain a copyright notice

#ifndef HT_NAV_VARIABLES__MSG__DETAIL__HT_NAV_CONTACT_STATES__TRAITS_HPP_
#define HT_NAV_VARIABLES__MSG__DETAIL__HT_NAV_CONTACT_STATES__TRAITS_HPP_

#include "ht_nav_variables/msg/detail/ht_nav_contact_states__struct.hpp"
#include <rosidl_runtime_cpp/traits.hpp>
#include <stdint.h>
#include <type_traits>

// Include directives for member types
// Member 'fl_wheel_contact_states'
// Member 'fr_wheel_contact_states'
// Member 'rl_wheel_contact_states'
// Member 'rr_wheel_contact_states'
#include "ht_nav_variables/msg/detail/ht_nav_contact_state__traits.hpp"

namespace rosidl_generator_traits
{

template<>
inline const char * data_type<ht_nav_variables::msg::HtNavContactStates>()
{
  return "ht_nav_variables::msg::HtNavContactStates";
}

template<>
inline const char * name<ht_nav_variables::msg::HtNavContactStates>()
{
  return "ht_nav_variables/msg/HtNavContactStates";
}

template<>
struct has_fixed_size<ht_nav_variables::msg::HtNavContactStates>
  : std::integral_constant<bool, has_fixed_size<ht_nav_variables::msg::HtNavContactState>::value> {};

template<>
struct has_bounded_size<ht_nav_variables::msg::HtNavContactStates>
  : std::integral_constant<bool, has_bounded_size<ht_nav_variables::msg::HtNavContactState>::value> {};

template<>
struct is_message<ht_nav_variables::msg::HtNavContactStates>
  : std::true_type {};

}  // namespace rosidl_generator_traits

#endif  // HT_NAV_VARIABLES__MSG__DETAIL__HT_NAV_CONTACT_STATES__TRAITS_HPP_
