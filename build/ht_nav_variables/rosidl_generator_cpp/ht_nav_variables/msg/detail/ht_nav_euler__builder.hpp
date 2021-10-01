// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from ht_nav_variables:msg/HtNavEuler.idl
// generated code does not contain a copyright notice

#ifndef HT_NAV_VARIABLES__MSG__DETAIL__HT_NAV_EULER__BUILDER_HPP_
#define HT_NAV_VARIABLES__MSG__DETAIL__HT_NAV_EULER__BUILDER_HPP_

#include "ht_nav_variables/msg/detail/ht_nav_euler__struct.hpp"
#include <rosidl_runtime_cpp/message_initialization.hpp>
#include <algorithm>
#include <utility>


namespace ht_nav_variables
{

namespace msg
{

namespace builder
{

class Init_HtNavEuler_yaw
{
public:
  explicit Init_HtNavEuler_yaw(::ht_nav_variables::msg::HtNavEuler & msg)
  : msg_(msg)
  {}
  ::ht_nav_variables::msg::HtNavEuler yaw(::ht_nav_variables::msg::HtNavEuler::_yaw_type arg)
  {
    msg_.yaw = std::move(arg);
    return std::move(msg_);
  }

private:
  ::ht_nav_variables::msg::HtNavEuler msg_;
};

class Init_HtNavEuler_pitch
{
public:
  explicit Init_HtNavEuler_pitch(::ht_nav_variables::msg::HtNavEuler & msg)
  : msg_(msg)
  {}
  Init_HtNavEuler_yaw pitch(::ht_nav_variables::msg::HtNavEuler::_pitch_type arg)
  {
    msg_.pitch = std::move(arg);
    return Init_HtNavEuler_yaw(msg_);
  }

private:
  ::ht_nav_variables::msg::HtNavEuler msg_;
};

class Init_HtNavEuler_roll
{
public:
  Init_HtNavEuler_roll()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_HtNavEuler_pitch roll(::ht_nav_variables::msg::HtNavEuler::_roll_type arg)
  {
    msg_.roll = std::move(arg);
    return Init_HtNavEuler_pitch(msg_);
  }

private:
  ::ht_nav_variables::msg::HtNavEuler msg_;
};

}  // namespace builder

}  // namespace msg

template<typename MessageType>
auto build();

template<>
inline
auto build<::ht_nav_variables::msg::HtNavEuler>()
{
  return ht_nav_variables::msg::builder::Init_HtNavEuler_roll();
}

}  // namespace ht_nav_variables

#endif  // HT_NAV_VARIABLES__MSG__DETAIL__HT_NAV_EULER__BUILDER_HPP_
