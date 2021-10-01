// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from ht_nav_variables:msg/HtNavDeneme.idl
// generated code does not contain a copyright notice

#ifndef HT_NAV_VARIABLES__MSG__DETAIL__HT_NAV_DENEME__BUILDER_HPP_
#define HT_NAV_VARIABLES__MSG__DETAIL__HT_NAV_DENEME__BUILDER_HPP_

#include "ht_nav_variables/msg/detail/ht_nav_deneme__struct.hpp"
#include <rosidl_runtime_cpp/message_initialization.hpp>
#include <algorithm>
#include <utility>


namespace ht_nav_variables
{

namespace msg
{

namespace builder
{

class Init_HtNavDeneme_num
{
public:
  Init_HtNavDeneme_num()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  ::ht_nav_variables::msg::HtNavDeneme num(::ht_nav_variables::msg::HtNavDeneme::_num_type arg)
  {
    msg_.num = std::move(arg);
    return std::move(msg_);
  }

private:
  ::ht_nav_variables::msg::HtNavDeneme msg_;
};

}  // namespace builder

}  // namespace msg

template<typename MessageType>
auto build();

template<>
inline
auto build<::ht_nav_variables::msg::HtNavDeneme>()
{
  return ht_nav_variables::msg::builder::Init_HtNavDeneme_num();
}

}  // namespace ht_nav_variables

#endif  // HT_NAV_VARIABLES__MSG__DETAIL__HT_NAV_DENEME__BUILDER_HPP_
