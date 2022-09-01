// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from ht_nav_variables:msg/HtNavContactState.idl
// generated code does not contain a copyright notice

#ifndef HT_NAV_VARIABLES__MSG__DETAIL__HT_NAV_CONTACT_STATE__BUILDER_HPP_
#define HT_NAV_VARIABLES__MSG__DETAIL__HT_NAV_CONTACT_STATE__BUILDER_HPP_

#include "ht_nav_variables/msg/detail/ht_nav_contact_state__struct.hpp"
#include <rosidl_runtime_cpp/message_initialization.hpp>
#include <algorithm>
#include <utility>


namespace ht_nav_variables
{

namespace msg
{

namespace builder
{

class Init_HtNavContactState_ideal_slip
{
public:
  explicit Init_HtNavContactState_ideal_slip(::ht_nav_variables::msg::HtNavContactState & msg)
  : msg_(msg)
  {}
  ::ht_nav_variables::msg::HtNavContactState ideal_slip(::ht_nav_variables::msg::HtNavContactState::_ideal_slip_type arg)
  {
    msg_.ideal_slip = std::move(arg);
    return std::move(msg_);
  }

private:
  ::ht_nav_variables::msg::HtNavContactState msg_;
};

class Init_HtNavContactState_ideal_pacejka_forces
{
public:
  explicit Init_HtNavContactState_ideal_pacejka_forces(::ht_nav_variables::msg::HtNavContactState & msg)
  : msg_(msg)
  {}
  Init_HtNavContactState_ideal_slip ideal_pacejka_forces(::ht_nav_variables::msg::HtNavContactState::_ideal_pacejka_forces_type arg)
  {
    msg_.ideal_pacejka_forces = std::move(arg);
    return Init_HtNavContactState_ideal_slip(msg_);
  }

private:
  ::ht_nav_variables::msg::HtNavContactState msg_;
};

class Init_HtNavContactState_ideal_contact_forces
{
public:
  explicit Init_HtNavContactState_ideal_contact_forces(::ht_nav_variables::msg::HtNavContactState & msg)
  : msg_(msg)
  {}
  Init_HtNavContactState_ideal_pacejka_forces ideal_contact_forces(::ht_nav_variables::msg::HtNavContactState::_ideal_contact_forces_type arg)
  {
    msg_.ideal_contact_forces = std::move(arg);
    return Init_HtNavContactState_ideal_pacejka_forces(msg_);
  }

private:
  ::ht_nav_variables::msg::HtNavContactState msg_;
};

class Init_HtNavContactState_time
{
public:
  Init_HtNavContactState_time()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_HtNavContactState_ideal_contact_forces time(::ht_nav_variables::msg::HtNavContactState::_time_type arg)
  {
    msg_.time = std::move(arg);
    return Init_HtNavContactState_ideal_contact_forces(msg_);
  }

private:
  ::ht_nav_variables::msg::HtNavContactState msg_;
};

}  // namespace builder

}  // namespace msg

template<typename MessageType>
auto build();

template<>
inline
auto build<::ht_nav_variables::msg::HtNavContactState>()
{
  return ht_nav_variables::msg::builder::Init_HtNavContactState_time();
}

}  // namespace ht_nav_variables

#endif  // HT_NAV_VARIABLES__MSG__DETAIL__HT_NAV_CONTACT_STATE__BUILDER_HPP_
