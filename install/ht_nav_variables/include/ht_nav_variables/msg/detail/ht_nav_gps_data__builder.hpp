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

class Init_HtNavGpsData_gps_pos
{
public:
  Init_HtNavGpsData_gps_pos()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  ::ht_nav_variables::msg::HtNavGpsData gps_pos(::ht_nav_variables::msg::HtNavGpsData::_gps_pos_type arg)
  {
    msg_.gps_pos = std::move(arg);
    return std::move(msg_);
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
  return ht_nav_variables::msg::builder::Init_HtNavGpsData_gps_pos();
}

}  // namespace ht_nav_variables

#endif  // HT_NAV_VARIABLES__MSG__DETAIL__HT_NAV_GPS_DATA__BUILDER_HPP_
