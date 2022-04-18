// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from ht_nav_variables:msg/HtNavVehicleDebug.idl
// generated code does not contain a copyright notice

#ifndef HT_NAV_VARIABLES__MSG__DETAIL__HT_NAV_VEHICLE_DEBUG__BUILDER_HPP_
#define HT_NAV_VARIABLES__MSG__DETAIL__HT_NAV_VEHICLE_DEBUG__BUILDER_HPP_

#include "ht_nav_variables/msg/detail/ht_nav_vehicle_debug__struct.hpp"
#include <rosidl_runtime_cpp/message_initialization.hpp>
#include <algorithm>
#include <utility>


namespace ht_nav_variables
{

namespace msg
{

namespace builder
{

class Init_HtNavVehicleDebug_rr_wheel_pva
{
public:
  explicit Init_HtNavVehicleDebug_rr_wheel_pva(::ht_nav_variables::msg::HtNavVehicleDebug & msg)
  : msg_(msg)
  {}
  ::ht_nav_variables::msg::HtNavVehicleDebug rr_wheel_pva(::ht_nav_variables::msg::HtNavVehicleDebug::_rr_wheel_pva_type arg)
  {
    msg_.rr_wheel_pva = std::move(arg);
    return std::move(msg_);
  }

private:
  ::ht_nav_variables::msg::HtNavVehicleDebug msg_;
};

class Init_HtNavVehicleDebug_rl_wheel_pva
{
public:
  explicit Init_HtNavVehicleDebug_rl_wheel_pva(::ht_nav_variables::msg::HtNavVehicleDebug & msg)
  : msg_(msg)
  {}
  Init_HtNavVehicleDebug_rr_wheel_pva rl_wheel_pva(::ht_nav_variables::msg::HtNavVehicleDebug::_rl_wheel_pva_type arg)
  {
    msg_.rl_wheel_pva = std::move(arg);
    return Init_HtNavVehicleDebug_rr_wheel_pva(msg_);
  }

private:
  ::ht_nav_variables::msg::HtNavVehicleDebug msg_;
};

class Init_HtNavVehicleDebug_fr_wheel_pva
{
public:
  explicit Init_HtNavVehicleDebug_fr_wheel_pva(::ht_nav_variables::msg::HtNavVehicleDebug & msg)
  : msg_(msg)
  {}
  Init_HtNavVehicleDebug_rl_wheel_pva fr_wheel_pva(::ht_nav_variables::msg::HtNavVehicleDebug::_fr_wheel_pva_type arg)
  {
    msg_.fr_wheel_pva = std::move(arg);
    return Init_HtNavVehicleDebug_rl_wheel_pva(msg_);
  }

private:
  ::ht_nav_variables::msg::HtNavVehicleDebug msg_;
};

class Init_HtNavVehicleDebug_fl_wheel_pva
{
public:
  explicit Init_HtNavVehicleDebug_fl_wheel_pva(::ht_nav_variables::msg::HtNavVehicleDebug & msg)
  : msg_(msg)
  {}
  Init_HtNavVehicleDebug_fr_wheel_pva fl_wheel_pva(::ht_nav_variables::msg::HtNavVehicleDebug::_fl_wheel_pva_type arg)
  {
    msg_.fl_wheel_pva = std::move(arg);
    return Init_HtNavVehicleDebug_fr_wheel_pva(msg_);
  }

private:
  ::ht_nav_variables::msg::HtNavVehicleDebug msg_;
};

class Init_HtNavVehicleDebug_imu_link_pva
{
public:
  explicit Init_HtNavVehicleDebug_imu_link_pva(::ht_nav_variables::msg::HtNavVehicleDebug & msg)
  : msg_(msg)
  {}
  Init_HtNavVehicleDebug_fl_wheel_pva imu_link_pva(::ht_nav_variables::msg::HtNavVehicleDebug::_imu_link_pva_type arg)
  {
    msg_.imu_link_pva = std::move(arg);
    return Init_HtNavVehicleDebug_fl_wheel_pva(msg_);
  }

private:
  ::ht_nav_variables::msg::HtNavVehicleDebug msg_;
};

class Init_HtNavVehicleDebug_wheel_variables
{
public:
  explicit Init_HtNavVehicleDebug_wheel_variables(::ht_nav_variables::msg::HtNavVehicleDebug & msg)
  : msg_(msg)
  {}
  Init_HtNavVehicleDebug_imu_link_pva wheel_variables(::ht_nav_variables::msg::HtNavVehicleDebug::_wheel_variables_type arg)
  {
    msg_.wheel_variables = std::move(arg);
    return Init_HtNavVehicleDebug_imu_link_pva(msg_);
  }

private:
  ::ht_nav_variables::msg::HtNavVehicleDebug msg_;
};

class Init_HtNavVehicleDebug_time
{
public:
  Init_HtNavVehicleDebug_time()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_HtNavVehicleDebug_wheel_variables time(::ht_nav_variables::msg::HtNavVehicleDebug::_time_type arg)
  {
    msg_.time = std::move(arg);
    return Init_HtNavVehicleDebug_wheel_variables(msg_);
  }

private:
  ::ht_nav_variables::msg::HtNavVehicleDebug msg_;
};

}  // namespace builder

}  // namespace msg

template<typename MessageType>
auto build();

template<>
inline
auto build<::ht_nav_variables::msg::HtNavVehicleDebug>()
{
  return ht_nav_variables::msg::builder::Init_HtNavVehicleDebug_time();
}

}  // namespace ht_nav_variables

#endif  // HT_NAV_VARIABLES__MSG__DETAIL__HT_NAV_VEHICLE_DEBUG__BUILDER_HPP_
