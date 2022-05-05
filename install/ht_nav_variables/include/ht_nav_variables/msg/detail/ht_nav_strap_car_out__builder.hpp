// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from ht_nav_variables:msg/HtNavStrapCarOut.idl
// generated code does not contain a copyright notice

#ifndef HT_NAV_VARIABLES__MSG__DETAIL__HT_NAV_STRAP_CAR_OUT__BUILDER_HPP_
#define HT_NAV_VARIABLES__MSG__DETAIL__HT_NAV_STRAP_CAR_OUT__BUILDER_HPP_

#include "ht_nav_variables/msg/detail/ht_nav_strap_car_out__struct.hpp"
#include <rosidl_runtime_cpp/message_initialization.hpp>
#include <algorithm>
#include <utility>


namespace ht_nav_variables
{

namespace msg
{

namespace builder
{

class Init_HtNavStrapCarOut_quaternion
{
public:
  explicit Init_HtNavStrapCarOut_quaternion(::ht_nav_variables::msg::HtNavStrapCarOut & msg)
  : msg_(msg)
  {}
  ::ht_nav_variables::msg::HtNavStrapCarOut quaternion(::ht_nav_variables::msg::HtNavStrapCarOut::_quaternion_type arg)
  {
    msg_.quaternion = std::move(arg);
    return std::move(msg_);
  }

private:
  ::ht_nav_variables::msg::HtNavStrapCarOut msg_;
};

class Init_HtNavStrapCarOut_euler
{
public:
  explicit Init_HtNavStrapCarOut_euler(::ht_nav_variables::msg::HtNavStrapCarOut & msg)
  : msg_(msg)
  {}
  Init_HtNavStrapCarOut_quaternion euler(::ht_nav_variables::msg::HtNavStrapCarOut::_euler_type arg)
  {
    msg_.euler = std::move(arg);
    return Init_HtNavStrapCarOut_quaternion(msg_);
  }

private:
  ::ht_nav_variables::msg::HtNavStrapCarOut msg_;
};

class Init_HtNavStrapCarOut_vel
{
public:
  explicit Init_HtNavStrapCarOut_vel(::ht_nav_variables::msg::HtNavStrapCarOut & msg)
  : msg_(msg)
  {}
  Init_HtNavStrapCarOut_euler vel(::ht_nav_variables::msg::HtNavStrapCarOut::_vel_type arg)
  {
    msg_.vel = std::move(arg);
    return Init_HtNavStrapCarOut_euler(msg_);
  }

private:
  ::ht_nav_variables::msg::HtNavStrapCarOut msg_;
};

class Init_HtNavStrapCarOut_car_pos
{
public:
  explicit Init_HtNavStrapCarOut_car_pos(::ht_nav_variables::msg::HtNavStrapCarOut & msg)
  : msg_(msg)
  {}
  Init_HtNavStrapCarOut_vel car_pos(::ht_nav_variables::msg::HtNavStrapCarOut::_car_pos_type arg)
  {
    msg_.car_pos = std::move(arg);
    return Init_HtNavStrapCarOut_vel(msg_);
  }

private:
  ::ht_nav_variables::msg::HtNavStrapCarOut msg_;
};

class Init_HtNavStrapCarOut_pos
{
public:
  explicit Init_HtNavStrapCarOut_pos(::ht_nav_variables::msg::HtNavStrapCarOut & msg)
  : msg_(msg)
  {}
  Init_HtNavStrapCarOut_car_pos pos(::ht_nav_variables::msg::HtNavStrapCarOut::_pos_type arg)
  {
    msg_.pos = std::move(arg);
    return Init_HtNavStrapCarOut_car_pos(msg_);
  }

private:
  ::ht_nav_variables::msg::HtNavStrapCarOut msg_;
};

class Init_HtNavStrapCarOut_time
{
public:
  Init_HtNavStrapCarOut_time()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_HtNavStrapCarOut_pos time(::ht_nav_variables::msg::HtNavStrapCarOut::_time_type arg)
  {
    msg_.time = std::move(arg);
    return Init_HtNavStrapCarOut_pos(msg_);
  }

private:
  ::ht_nav_variables::msg::HtNavStrapCarOut msg_;
};

}  // namespace builder

}  // namespace msg

template<typename MessageType>
auto build();

template<>
inline
auto build<::ht_nav_variables::msg::HtNavStrapCarOut>()
{
  return ht_nav_variables::msg::builder::Init_HtNavStrapCarOut_time();
}

}  // namespace ht_nav_variables

#endif  // HT_NAV_VARIABLES__MSG__DETAIL__HT_NAV_STRAP_CAR_OUT__BUILDER_HPP_
