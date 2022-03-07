// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from ht_nav_variables:msg/HtNavTireOut.idl
// generated code does not contain a copyright notice

#ifndef HT_NAV_VARIABLES__MSG__DETAIL__HT_NAV_TIRE_OUT__BUILDER_HPP_
#define HT_NAV_VARIABLES__MSG__DETAIL__HT_NAV_TIRE_OUT__BUILDER_HPP_

#include "ht_nav_variables/msg/detail/ht_nav_tire_out__struct.hpp"
#include <rosidl_runtime_cpp/message_initialization.hpp>
#include <algorithm>
#include <utility>


namespace ht_nav_variables
{

namespace msg
{

namespace builder
{

class Init_HtNavTireOut_tire_longitudinal_forces
{
public:
  explicit Init_HtNavTireOut_tire_longitudinal_forces(::ht_nav_variables::msg::HtNavTireOut & msg)
  : msg_(msg)
  {}
  ::ht_nav_variables::msg::HtNavTireOut tire_longitudinal_forces(::ht_nav_variables::msg::HtNavTireOut::_tire_longitudinal_forces_type arg)
  {
    msg_.tire_longitudinal_forces = std::move(arg);
    return std::move(msg_);
  }

private:
  ::ht_nav_variables::msg::HtNavTireOut msg_;
};

class Init_HtNavTireOut_tire_lateral_forces
{
public:
  explicit Init_HtNavTireOut_tire_lateral_forces(::ht_nav_variables::msg::HtNavTireOut & msg)
  : msg_(msg)
  {}
  Init_HtNavTireOut_tire_longitudinal_forces tire_lateral_forces(::ht_nav_variables::msg::HtNavTireOut::_tire_lateral_forces_type arg)
  {
    msg_.tire_lateral_forces = std::move(arg);
    return Init_HtNavTireOut_tire_longitudinal_forces(msg_);
  }

private:
  ::ht_nav_variables::msg::HtNavTireOut msg_;
};

class Init_HtNavTireOut_wheel_longitudinal_slip_ratio
{
public:
  explicit Init_HtNavTireOut_wheel_longitudinal_slip_ratio(::ht_nav_variables::msg::HtNavTireOut & msg)
  : msg_(msg)
  {}
  Init_HtNavTireOut_tire_lateral_forces wheel_longitudinal_slip_ratio(::ht_nav_variables::msg::HtNavTireOut::_wheel_longitudinal_slip_ratio_type arg)
  {
    msg_.wheel_longitudinal_slip_ratio = std::move(arg);
    return Init_HtNavTireOut_tire_lateral_forces(msg_);
  }

private:
  ::ht_nav_variables::msg::HtNavTireOut msg_;
};

class Init_HtNavTireOut_wheel_side_slip_ang
{
public:
  explicit Init_HtNavTireOut_wheel_side_slip_ang(::ht_nav_variables::msg::HtNavTireOut & msg)
  : msg_(msg)
  {}
  Init_HtNavTireOut_wheel_longitudinal_slip_ratio wheel_side_slip_ang(::ht_nav_variables::msg::HtNavTireOut::_wheel_side_slip_ang_type arg)
  {
    msg_.wheel_side_slip_ang = std::move(arg);
    return Init_HtNavTireOut_wheel_longitudinal_slip_ratio(msg_);
  }

private:
  ::ht_nav_variables::msg::HtNavTireOut msg_;
};

class Init_HtNavTireOut_vehicle_mass_est
{
public:
  explicit Init_HtNavTireOut_vehicle_mass_est(::ht_nav_variables::msg::HtNavTireOut & msg)
  : msg_(msg)
  {}
  Init_HtNavTireOut_wheel_side_slip_ang vehicle_mass_est(::ht_nav_variables::msg::HtNavTireOut::_vehicle_mass_est_type arg)
  {
    msg_.vehicle_mass_est = std::move(arg);
    return Init_HtNavTireOut_wheel_side_slip_ang(msg_);
  }

private:
  ::ht_nav_variables::msg::HtNavTireOut msg_;
};

class Init_HtNavTireOut_effective_radius_est
{
public:
  Init_HtNavTireOut_effective_radius_est()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_HtNavTireOut_vehicle_mass_est effective_radius_est(::ht_nav_variables::msg::HtNavTireOut::_effective_radius_est_type arg)
  {
    msg_.effective_radius_est = std::move(arg);
    return Init_HtNavTireOut_vehicle_mass_est(msg_);
  }

private:
  ::ht_nav_variables::msg::HtNavTireOut msg_;
};

}  // namespace builder

}  // namespace msg

template<typename MessageType>
auto build();

template<>
inline
auto build<::ht_nav_variables::msg::HtNavTireOut>()
{
  return ht_nav_variables::msg::builder::Init_HtNavTireOut_effective_radius_est();
}

}  // namespace ht_nav_variables

#endif  // HT_NAV_VARIABLES__MSG__DETAIL__HT_NAV_TIRE_OUT__BUILDER_HPP_
