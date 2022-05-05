// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from ht_nav_variables:msg/HtNavKalmanOut.idl
// generated code does not contain a copyright notice

#ifndef HT_NAV_VARIABLES__MSG__DETAIL__HT_NAV_KALMAN_OUT__BUILDER_HPP_
#define HT_NAV_VARIABLES__MSG__DETAIL__HT_NAV_KALMAN_OUT__BUILDER_HPP_

#include "ht_nav_variables/msg/detail/ht_nav_kalman_out__struct.hpp"
#include <rosidl_runtime_cpp/message_initialization.hpp>
#include <algorithm>
#include <utility>


namespace ht_nav_variables
{

namespace msg
{

namespace builder
{

class Init_HtNavKalmanOut_drift
{
public:
  explicit Init_HtNavKalmanOut_drift(::ht_nav_variables::msg::HtNavKalmanOut & msg)
  : msg_(msg)
  {}
  ::ht_nav_variables::msg::HtNavKalmanOut drift(::ht_nav_variables::msg::HtNavKalmanOut::_drift_type arg)
  {
    msg_.drift = std::move(arg);
    return std::move(msg_);
  }

private:
  ::ht_nav_variables::msg::HtNavKalmanOut msg_;
};

class Init_HtNavKalmanOut_bias
{
public:
  explicit Init_HtNavKalmanOut_bias(::ht_nav_variables::msg::HtNavKalmanOut & msg)
  : msg_(msg)
  {}
  Init_HtNavKalmanOut_drift bias(::ht_nav_variables::msg::HtNavKalmanOut::_bias_type arg)
  {
    msg_.bias = std::move(arg);
    return Init_HtNavKalmanOut_drift(msg_);
  }

private:
  ::ht_nav_variables::msg::HtNavKalmanOut msg_;
};

class Init_HtNavKalmanOut_att_err
{
public:
  explicit Init_HtNavKalmanOut_att_err(::ht_nav_variables::msg::HtNavKalmanOut & msg)
  : msg_(msg)
  {}
  Init_HtNavKalmanOut_bias att_err(::ht_nav_variables::msg::HtNavKalmanOut::_att_err_type arg)
  {
    msg_.att_err = std::move(arg);
    return Init_HtNavKalmanOut_bias(msg_);
  }

private:
  ::ht_nav_variables::msg::HtNavKalmanOut msg_;
};

class Init_HtNavKalmanOut_vel_err
{
public:
  explicit Init_HtNavKalmanOut_vel_err(::ht_nav_variables::msg::HtNavKalmanOut & msg)
  : msg_(msg)
  {}
  Init_HtNavKalmanOut_att_err vel_err(::ht_nav_variables::msg::HtNavKalmanOut::_vel_err_type arg)
  {
    msg_.vel_err = std::move(arg);
    return Init_HtNavKalmanOut_att_err(msg_);
  }

private:
  ::ht_nav_variables::msg::HtNavKalmanOut msg_;
};

class Init_HtNavKalmanOut_pos_err
{
public:
  explicit Init_HtNavKalmanOut_pos_err(::ht_nav_variables::msg::HtNavKalmanOut & msg)
  : msg_(msg)
  {}
  Init_HtNavKalmanOut_vel_err pos_err(::ht_nav_variables::msg::HtNavKalmanOut::_pos_err_type arg)
  {
    msg_.pos_err = std::move(arg);
    return Init_HtNavKalmanOut_vel_err(msg_);
  }

private:
  ::ht_nav_variables::msg::HtNavKalmanOut msg_;
};

class Init_HtNavKalmanOut_time
{
public:
  Init_HtNavKalmanOut_time()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_HtNavKalmanOut_pos_err time(::ht_nav_variables::msg::HtNavKalmanOut::_time_type arg)
  {
    msg_.time = std::move(arg);
    return Init_HtNavKalmanOut_pos_err(msg_);
  }

private:
  ::ht_nav_variables::msg::HtNavKalmanOut msg_;
};

}  // namespace builder

}  // namespace msg

template<typename MessageType>
auto build();

template<>
inline
auto build<::ht_nav_variables::msg::HtNavKalmanOut>()
{
  return ht_nav_variables::msg::builder::Init_HtNavKalmanOut_time();
}

}  // namespace ht_nav_variables

#endif  // HT_NAV_VARIABLES__MSG__DETAIL__HT_NAV_KALMAN_OUT__BUILDER_HPP_
