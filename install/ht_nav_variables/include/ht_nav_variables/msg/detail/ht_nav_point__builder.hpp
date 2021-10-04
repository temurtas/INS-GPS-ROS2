// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from ht_nav_variables:msg/HtNavPoint.idl
// generated code does not contain a copyright notice

#ifndef HT_NAV_VARIABLES__MSG__DETAIL__HT_NAV_POINT__BUILDER_HPP_
#define HT_NAV_VARIABLES__MSG__DETAIL__HT_NAV_POINT__BUILDER_HPP_

#include "ht_nav_variables/msg/detail/ht_nav_point__struct.hpp"
#include <rosidl_runtime_cpp/message_initialization.hpp>
#include <algorithm>
#include <utility>


namespace ht_nav_variables
{

namespace msg
{

namespace builder
{

class Init_HtNavPoint_z
{
public:
  explicit Init_HtNavPoint_z(::ht_nav_variables::msg::HtNavPoint & msg)
  : msg_(msg)
  {}
  ::ht_nav_variables::msg::HtNavPoint z(::ht_nav_variables::msg::HtNavPoint::_z_type arg)
  {
    msg_.z = std::move(arg);
    return std::move(msg_);
  }

private:
  ::ht_nav_variables::msg::HtNavPoint msg_;
};

class Init_HtNavPoint_y
{
public:
  explicit Init_HtNavPoint_y(::ht_nav_variables::msg::HtNavPoint & msg)
  : msg_(msg)
  {}
  Init_HtNavPoint_z y(::ht_nav_variables::msg::HtNavPoint::_y_type arg)
  {
    msg_.y = std::move(arg);
    return Init_HtNavPoint_z(msg_);
  }

private:
  ::ht_nav_variables::msg::HtNavPoint msg_;
};

class Init_HtNavPoint_x
{
public:
  Init_HtNavPoint_x()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_HtNavPoint_y x(::ht_nav_variables::msg::HtNavPoint::_x_type arg)
  {
    msg_.x = std::move(arg);
    return Init_HtNavPoint_y(msg_);
  }

private:
  ::ht_nav_variables::msg::HtNavPoint msg_;
};

}  // namespace builder

}  // namespace msg

template<typename MessageType>
auto build();

template<>
inline
auto build<::ht_nav_variables::msg::HtNavPoint>()
{
  return ht_nav_variables::msg::builder::Init_HtNavPoint_x();
}

}  // namespace ht_nav_variables

#endif  // HT_NAV_VARIABLES__MSG__DETAIL__HT_NAV_POINT__BUILDER_HPP_
