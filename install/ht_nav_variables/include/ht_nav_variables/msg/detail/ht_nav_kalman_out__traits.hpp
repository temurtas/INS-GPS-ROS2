// generated from rosidl_generator_cpp/resource/idl__traits.hpp.em
// with input from ht_nav_variables:msg/HtNavKalmanOut.idl
// generated code does not contain a copyright notice

#ifndef HT_NAV_VARIABLES__MSG__DETAIL__HT_NAV_KALMAN_OUT__TRAITS_HPP_
#define HT_NAV_VARIABLES__MSG__DETAIL__HT_NAV_KALMAN_OUT__TRAITS_HPP_

#include "ht_nav_variables/msg/detail/ht_nav_kalman_out__struct.hpp"
#include <rosidl_runtime_cpp/traits.hpp>
#include <stdint.h>
#include <type_traits>

// Include directives for member types
// Member 'pos_err'
// Member 'vel_err'
// Member 'att_err'
// Member 'bias'
// Member 'drift'
#include "ht_nav_variables/msg/detail/ht_nav_error_vector__traits.hpp"

namespace rosidl_generator_traits
{

template<>
inline const char * data_type<ht_nav_variables::msg::HtNavKalmanOut>()
{
  return "ht_nav_variables::msg::HtNavKalmanOut";
}

template<>
inline const char * name<ht_nav_variables::msg::HtNavKalmanOut>()
{
  return "ht_nav_variables/msg/HtNavKalmanOut";
}

template<>
struct has_fixed_size<ht_nav_variables::msg::HtNavKalmanOut>
  : std::integral_constant<bool, has_fixed_size<ht_nav_variables::msg::HtNavErrorVector>::value> {};

template<>
struct has_bounded_size<ht_nav_variables::msg::HtNavKalmanOut>
  : std::integral_constant<bool, has_bounded_size<ht_nav_variables::msg::HtNavErrorVector>::value> {};

template<>
struct is_message<ht_nav_variables::msg::HtNavKalmanOut>
  : std::true_type {};

}  // namespace rosidl_generator_traits

#endif  // HT_NAV_VARIABLES__MSG__DETAIL__HT_NAV_KALMAN_OUT__TRAITS_HPP_
