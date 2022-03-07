// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from ht_nav_variables:msg/HtNavJointState.idl
// generated code does not contain a copyright notice

#ifndef HT_NAV_VARIABLES__MSG__DETAIL__HT_NAV_JOINT_STATE__BUILDER_HPP_
#define HT_NAV_VARIABLES__MSG__DETAIL__HT_NAV_JOINT_STATE__BUILDER_HPP_

#include "ht_nav_variables/msg/detail/ht_nav_joint_state__struct.hpp"
#include <rosidl_runtime_cpp/message_initialization.hpp>
#include <algorithm>
#include <utility>


namespace ht_nav_variables
{

namespace msg
{

namespace builder
{

class Init_HtNavJointState_wheel_rotation
{
public:
  explicit Init_HtNavJointState_wheel_rotation(::ht_nav_variables::msg::HtNavJointState & msg)
  : msg_(msg)
  {}
  ::ht_nav_variables::msg::HtNavJointState wheel_rotation(::ht_nav_variables::msg::HtNavJointState::_wheel_rotation_type arg)
  {
    msg_.wheel_rotation = std::move(arg);
    return std::move(msg_);
  }

private:
  ::ht_nav_variables::msg::HtNavJointState msg_;
};

class Init_HtNavJointState_steering_angle
{
public:
  Init_HtNavJointState_steering_angle()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_HtNavJointState_wheel_rotation steering_angle(::ht_nav_variables::msg::HtNavJointState::_steering_angle_type arg)
  {
    msg_.steering_angle = std::move(arg);
    return Init_HtNavJointState_wheel_rotation(msg_);
  }

private:
  ::ht_nav_variables::msg::HtNavJointState msg_;
};

}  // namespace builder

}  // namespace msg

template<typename MessageType>
auto build();

template<>
inline
auto build<::ht_nav_variables::msg::HtNavJointState>()
{
  return ht_nav_variables::msg::builder::Init_HtNavJointState_steering_angle();
}

}  // namespace ht_nav_variables

#endif  // HT_NAV_VARIABLES__MSG__DETAIL__HT_NAV_JOINT_STATE__BUILDER_HPP_
