// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from ht_nav_variables:msg/HtNavImuData.idl
// generated code does not contain a copyright notice

#ifndef HT_NAV_VARIABLES__MSG__DETAIL__HT_NAV_IMU_DATA__BUILDER_HPP_
#define HT_NAV_VARIABLES__MSG__DETAIL__HT_NAV_IMU_DATA__BUILDER_HPP_

#include "ht_nav_variables/msg/detail/ht_nav_imu_data__struct.hpp"
#include <rosidl_runtime_cpp/message_initialization.hpp>
#include <algorithm>
#include <utility>


namespace ht_nav_variables
{

namespace msg
{

namespace builder
{

class Init_HtNavImuData_ang_diff
{
public:
  explicit Init_HtNavImuData_ang_diff(::ht_nav_variables::msg::HtNavImuData & msg)
  : msg_(msg)
  {}
  ::ht_nav_variables::msg::HtNavImuData ang_diff(::ht_nav_variables::msg::HtNavImuData::_ang_diff_type arg)
  {
    msg_.ang_diff = std::move(arg);
    return std::move(msg_);
  }

private:
  ::ht_nav_variables::msg::HtNavImuData msg_;
};

class Init_HtNavImuData_vel_diff
{
public:
  Init_HtNavImuData_vel_diff()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_HtNavImuData_ang_diff vel_diff(::ht_nav_variables::msg::HtNavImuData::_vel_diff_type arg)
  {
    msg_.vel_diff = std::move(arg);
    return Init_HtNavImuData_ang_diff(msg_);
  }

private:
  ::ht_nav_variables::msg::HtNavImuData msg_;
};

}  // namespace builder

}  // namespace msg

template<typename MessageType>
auto build();

template<>
inline
auto build<::ht_nav_variables::msg::HtNavImuData>()
{
  return ht_nav_variables::msg::builder::Init_HtNavImuData_vel_diff();
}

}  // namespace ht_nav_variables

#endif  // HT_NAV_VARIABLES__MSG__DETAIL__HT_NAV_IMU_DATA__BUILDER_HPP_
