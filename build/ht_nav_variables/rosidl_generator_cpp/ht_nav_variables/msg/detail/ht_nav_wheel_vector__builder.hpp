// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from ht_nav_variables:msg/HtNavWheelVector.idl
// generated code does not contain a copyright notice

#ifndef HT_NAV_VARIABLES__MSG__DETAIL__HT_NAV_WHEEL_VECTOR__BUILDER_HPP_
#define HT_NAV_VARIABLES__MSG__DETAIL__HT_NAV_WHEEL_VECTOR__BUILDER_HPP_

#include "ht_nav_variables/msg/detail/ht_nav_wheel_vector__struct.hpp"
#include <rosidl_runtime_cpp/message_initialization.hpp>
#include <algorithm>
#include <utility>


namespace ht_nav_variables
{

namespace msg
{

namespace builder
{

class Init_HtNavWheelVector_w4
{
public:
  explicit Init_HtNavWheelVector_w4(::ht_nav_variables::msg::HtNavWheelVector & msg)
  : msg_(msg)
  {}
  ::ht_nav_variables::msg::HtNavWheelVector w4(::ht_nav_variables::msg::HtNavWheelVector::_w4_type arg)
  {
    msg_.w4 = std::move(arg);
    return std::move(msg_);
  }

private:
  ::ht_nav_variables::msg::HtNavWheelVector msg_;
};

class Init_HtNavWheelVector_w3
{
public:
  explicit Init_HtNavWheelVector_w3(::ht_nav_variables::msg::HtNavWheelVector & msg)
  : msg_(msg)
  {}
  Init_HtNavWheelVector_w4 w3(::ht_nav_variables::msg::HtNavWheelVector::_w3_type arg)
  {
    msg_.w3 = std::move(arg);
    return Init_HtNavWheelVector_w4(msg_);
  }

private:
  ::ht_nav_variables::msg::HtNavWheelVector msg_;
};

class Init_HtNavWheelVector_w2
{
public:
  explicit Init_HtNavWheelVector_w2(::ht_nav_variables::msg::HtNavWheelVector & msg)
  : msg_(msg)
  {}
  Init_HtNavWheelVector_w3 w2(::ht_nav_variables::msg::HtNavWheelVector::_w2_type arg)
  {
    msg_.w2 = std::move(arg);
    return Init_HtNavWheelVector_w3(msg_);
  }

private:
  ::ht_nav_variables::msg::HtNavWheelVector msg_;
};

class Init_HtNavWheelVector_w1
{
public:
  Init_HtNavWheelVector_w1()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_HtNavWheelVector_w2 w1(::ht_nav_variables::msg::HtNavWheelVector::_w1_type arg)
  {
    msg_.w1 = std::move(arg);
    return Init_HtNavWheelVector_w2(msg_);
  }

private:
  ::ht_nav_variables::msg::HtNavWheelVector msg_;
};

}  // namespace builder

}  // namespace msg

template<typename MessageType>
auto build();

template<>
inline
auto build<::ht_nav_variables::msg::HtNavWheelVector>()
{
  return ht_nav_variables::msg::builder::Init_HtNavWheelVector_w1();
}

}  // namespace ht_nav_variables

#endif  // HT_NAV_VARIABLES__MSG__DETAIL__HT_NAV_WHEEL_VECTOR__BUILDER_HPP_
