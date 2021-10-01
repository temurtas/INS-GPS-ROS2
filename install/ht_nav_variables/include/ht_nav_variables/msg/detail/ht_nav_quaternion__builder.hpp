// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from ht_nav_variables:msg/HtNavQuaternion.idl
// generated code does not contain a copyright notice

#ifndef HT_NAV_VARIABLES__MSG__DETAIL__HT_NAV_QUATERNION__BUILDER_HPP_
#define HT_NAV_VARIABLES__MSG__DETAIL__HT_NAV_QUATERNION__BUILDER_HPP_

#include "ht_nav_variables/msg/detail/ht_nav_quaternion__struct.hpp"
#include <rosidl_runtime_cpp/message_initialization.hpp>
#include <algorithm>
#include <utility>


namespace ht_nav_variables
{

namespace msg
{

namespace builder
{

class Init_HtNavQuaternion_w
{
public:
  explicit Init_HtNavQuaternion_w(::ht_nav_variables::msg::HtNavQuaternion & msg)
  : msg_(msg)
  {}
  ::ht_nav_variables::msg::HtNavQuaternion w(::ht_nav_variables::msg::HtNavQuaternion::_w_type arg)
  {
    msg_.w = std::move(arg);
    return std::move(msg_);
  }

private:
  ::ht_nav_variables::msg::HtNavQuaternion msg_;
};

class Init_HtNavQuaternion_z
{
public:
  explicit Init_HtNavQuaternion_z(::ht_nav_variables::msg::HtNavQuaternion & msg)
  : msg_(msg)
  {}
  Init_HtNavQuaternion_w z(::ht_nav_variables::msg::HtNavQuaternion::_z_type arg)
  {
    msg_.z = std::move(arg);
    return Init_HtNavQuaternion_w(msg_);
  }

private:
  ::ht_nav_variables::msg::HtNavQuaternion msg_;
};

class Init_HtNavQuaternion_y
{
public:
  explicit Init_HtNavQuaternion_y(::ht_nav_variables::msg::HtNavQuaternion & msg)
  : msg_(msg)
  {}
  Init_HtNavQuaternion_z y(::ht_nav_variables::msg::HtNavQuaternion::_y_type arg)
  {
    msg_.y = std::move(arg);
    return Init_HtNavQuaternion_z(msg_);
  }

private:
  ::ht_nav_variables::msg::HtNavQuaternion msg_;
};

class Init_HtNavQuaternion_x
{
public:
  Init_HtNavQuaternion_x()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_HtNavQuaternion_y x(::ht_nav_variables::msg::HtNavQuaternion::_x_type arg)
  {
    msg_.x = std::move(arg);
    return Init_HtNavQuaternion_y(msg_);
  }

private:
  ::ht_nav_variables::msg::HtNavQuaternion msg_;
};

}  // namespace builder

}  // namespace msg

template<typename MessageType>
auto build();

template<>
inline
auto build<::ht_nav_variables::msg::HtNavQuaternion>()
{
  return ht_nav_variables::msg::builder::Init_HtNavQuaternion_x();
}

}  // namespace ht_nav_variables

#endif  // HT_NAV_VARIABLES__MSG__DETAIL__HT_NAV_QUATERNION__BUILDER_HPP_
