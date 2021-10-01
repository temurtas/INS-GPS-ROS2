// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from ht_nav_variables:msg/HtNavStrapOut.idl
// generated code does not contain a copyright notice

#ifndef HT_NAV_VARIABLES__MSG__DETAIL__HT_NAV_STRAP_OUT__BUILDER_HPP_
#define HT_NAV_VARIABLES__MSG__DETAIL__HT_NAV_STRAP_OUT__BUILDER_HPP_

#include "ht_nav_variables/msg/detail/ht_nav_strap_out__struct.hpp"
#include <rosidl_runtime_cpp/message_initialization.hpp>
#include <algorithm>
#include <utility>


namespace ht_nav_variables
{

namespace msg
{

namespace builder
{

class Init_HtNavStrapOut_quaternion
{
public:
  explicit Init_HtNavStrapOut_quaternion(::ht_nav_variables::msg::HtNavStrapOut & msg)
  : msg_(msg)
  {}
  ::ht_nav_variables::msg::HtNavStrapOut quaternion(::ht_nav_variables::msg::HtNavStrapOut::_quaternion_type arg)
  {
    msg_.quaternion = std::move(arg);
    return std::move(msg_);
  }

private:
  ::ht_nav_variables::msg::HtNavStrapOut msg_;
};

class Init_HtNavStrapOut_euler
{
public:
  explicit Init_HtNavStrapOut_euler(::ht_nav_variables::msg::HtNavStrapOut & msg)
  : msg_(msg)
  {}
  Init_HtNavStrapOut_quaternion euler(::ht_nav_variables::msg::HtNavStrapOut::_euler_type arg)
  {
    msg_.euler = std::move(arg);
    return Init_HtNavStrapOut_quaternion(msg_);
  }

private:
  ::ht_nav_variables::msg::HtNavStrapOut msg_;
};

class Init_HtNavStrapOut_vel
{
public:
  explicit Init_HtNavStrapOut_vel(::ht_nav_variables::msg::HtNavStrapOut & msg)
  : msg_(msg)
  {}
  Init_HtNavStrapOut_euler vel(::ht_nav_variables::msg::HtNavStrapOut::_vel_type arg)
  {
    msg_.vel = std::move(arg);
    return Init_HtNavStrapOut_euler(msg_);
  }

private:
  ::ht_nav_variables::msg::HtNavStrapOut msg_;
};

class Init_HtNavStrapOut_pos
{
public:
  Init_HtNavStrapOut_pos()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_HtNavStrapOut_vel pos(::ht_nav_variables::msg::HtNavStrapOut::_pos_type arg)
  {
    msg_.pos = std::move(arg);
    return Init_HtNavStrapOut_vel(msg_);
  }

private:
  ::ht_nav_variables::msg::HtNavStrapOut msg_;
};

}  // namespace builder

}  // namespace msg

template<typename MessageType>
auto build();

template<>
inline
auto build<::ht_nav_variables::msg::HtNavStrapOut>()
{
  return ht_nav_variables::msg::builder::Init_HtNavStrapOut_pos();
}

}  // namespace ht_nav_variables

#endif  // HT_NAV_VARIABLES__MSG__DETAIL__HT_NAV_STRAP_OUT__BUILDER_HPP_
