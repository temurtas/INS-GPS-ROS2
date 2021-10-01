// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from ht_nav_variables:msg/HtNavErrorVector.idl
// generated code does not contain a copyright notice

#ifndef HT_NAV_VARIABLES__MSG__DETAIL__HT_NAV_ERROR_VECTOR__BUILDER_HPP_
#define HT_NAV_VARIABLES__MSG__DETAIL__HT_NAV_ERROR_VECTOR__BUILDER_HPP_

#include "ht_nav_variables/msg/detail/ht_nav_error_vector__struct.hpp"
#include <rosidl_runtime_cpp/message_initialization.hpp>
#include <algorithm>
#include <utility>


namespace ht_nav_variables
{

namespace msg
{

namespace builder
{

class Init_HtNavErrorVector_err_z
{
public:
  explicit Init_HtNavErrorVector_err_z(::ht_nav_variables::msg::HtNavErrorVector & msg)
  : msg_(msg)
  {}
  ::ht_nav_variables::msg::HtNavErrorVector err_z(::ht_nav_variables::msg::HtNavErrorVector::_err_z_type arg)
  {
    msg_.err_z = std::move(arg);
    return std::move(msg_);
  }

private:
  ::ht_nav_variables::msg::HtNavErrorVector msg_;
};

class Init_HtNavErrorVector_err_y
{
public:
  explicit Init_HtNavErrorVector_err_y(::ht_nav_variables::msg::HtNavErrorVector & msg)
  : msg_(msg)
  {}
  Init_HtNavErrorVector_err_z err_y(::ht_nav_variables::msg::HtNavErrorVector::_err_y_type arg)
  {
    msg_.err_y = std::move(arg);
    return Init_HtNavErrorVector_err_z(msg_);
  }

private:
  ::ht_nav_variables::msg::HtNavErrorVector msg_;
};

class Init_HtNavErrorVector_err_x
{
public:
  Init_HtNavErrorVector_err_x()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_HtNavErrorVector_err_y err_x(::ht_nav_variables::msg::HtNavErrorVector::_err_x_type arg)
  {
    msg_.err_x = std::move(arg);
    return Init_HtNavErrorVector_err_y(msg_);
  }

private:
  ::ht_nav_variables::msg::HtNavErrorVector msg_;
};

}  // namespace builder

}  // namespace msg

template<typename MessageType>
auto build();

template<>
inline
auto build<::ht_nav_variables::msg::HtNavErrorVector>()
{
  return ht_nav_variables::msg::builder::Init_HtNavErrorVector_err_x();
}

}  // namespace ht_nav_variables

#endif  // HT_NAV_VARIABLES__MSG__DETAIL__HT_NAV_ERROR_VECTOR__BUILDER_HPP_
