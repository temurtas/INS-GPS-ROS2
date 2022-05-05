// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from ht_nav_variables:msg/HtNavGpsData.idl
// generated code does not contain a copyright notice

#ifndef HT_NAV_VARIABLES__MSG__DETAIL__HT_NAV_GPS_DATA__BUILDER_HPP_
#define HT_NAV_VARIABLES__MSG__DETAIL__HT_NAV_GPS_DATA__BUILDER_HPP_

#include "ht_nav_variables/msg/detail/ht_nav_gps_data__struct.hpp"
#include <rosidl_runtime_cpp/message_initialization.hpp>
#include <algorithm>
#include <utility>


namespace ht_nav_variables
{

namespace msg
{

namespace builder
{

class Init_HtNavGpsData_gps_vel
{
public:
  explicit Init_HtNavGpsData_gps_vel(::ht_nav_variables::msg::HtNavGpsData & msg)
  : msg_(msg)
  {}
  ::ht_nav_variables::msg::HtNavGpsData gps_vel(::ht_nav_variables::msg::HtNavGpsData::_gps_vel_type arg)
  {
    msg_.gps_vel = std::move(arg);
    return std::move(msg_);
  }

private:
  ::ht_nav_variables::msg::HtNavGpsData msg_;
};

class Init_HtNavGpsData_gps_pos
{
public:
  explicit Init_HtNavGpsData_gps_pos(::ht_nav_variables::msg::HtNavGpsData & msg)
  : msg_(msg)
  {}
  Init_HtNavGpsData_gps_vel gps_pos(::ht_nav_variables::msg::HtNavGpsData::_gps_pos_type arg)
  {
    msg_.gps_pos = std::move(arg);
    return Init_HtNavGpsData_gps_vel(msg_);
  }

private:
  ::ht_nav_variables::msg::HtNavGpsData msg_;
};

class Init_HtNavGpsData_time
{
public:
  Init_HtNavGpsData_time()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_HtNavGpsData_gps_pos time(::ht_nav_variables::msg::HtNavGpsData::_time_type arg)
  {
    msg_.time = std::move(arg);
    return Init_HtNavGpsData_gps_pos(msg_);
  }

private:
  ::ht_nav_variables::msg::HtNavGpsData msg_;
};

}  // namespace builder

}  // namespace msg

template<typename MessageType>
auto build();

template<>
inline
auto build<::ht_nav_variables::msg::HtNavGpsData>()
{
  return ht_nav_variables::msg::builder::Init_HtNavGpsData_time();
}

}  // namespace ht_nav_variables

#endif  // HT_NAV_VARIABLES__MSG__DETAIL__HT_NAV_GPS_DATA__BUILDER_HPP_
