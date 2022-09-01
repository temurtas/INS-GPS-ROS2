// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from ht_nav_variables:msg/HtNavContactStates.idl
// generated code does not contain a copyright notice

#ifndef HT_NAV_VARIABLES__MSG__DETAIL__HT_NAV_CONTACT_STATES__BUILDER_HPP_
#define HT_NAV_VARIABLES__MSG__DETAIL__HT_NAV_CONTACT_STATES__BUILDER_HPP_

#include "ht_nav_variables/msg/detail/ht_nav_contact_states__struct.hpp"
#include <rosidl_runtime_cpp/message_initialization.hpp>
#include <algorithm>
#include <utility>


namespace ht_nav_variables
{

namespace msg
{

namespace builder
{

class Init_HtNavContactStates_rr_wheel_contact_states
{
public:
  explicit Init_HtNavContactStates_rr_wheel_contact_states(::ht_nav_variables::msg::HtNavContactStates & msg)
  : msg_(msg)
  {}
  ::ht_nav_variables::msg::HtNavContactStates rr_wheel_contact_states(::ht_nav_variables::msg::HtNavContactStates::_rr_wheel_contact_states_type arg)
  {
    msg_.rr_wheel_contact_states = std::move(arg);
    return std::move(msg_);
  }

private:
  ::ht_nav_variables::msg::HtNavContactStates msg_;
};

class Init_HtNavContactStates_rl_wheel_contact_states
{
public:
  explicit Init_HtNavContactStates_rl_wheel_contact_states(::ht_nav_variables::msg::HtNavContactStates & msg)
  : msg_(msg)
  {}
  Init_HtNavContactStates_rr_wheel_contact_states rl_wheel_contact_states(::ht_nav_variables::msg::HtNavContactStates::_rl_wheel_contact_states_type arg)
  {
    msg_.rl_wheel_contact_states = std::move(arg);
    return Init_HtNavContactStates_rr_wheel_contact_states(msg_);
  }

private:
  ::ht_nav_variables::msg::HtNavContactStates msg_;
};

class Init_HtNavContactStates_fr_wheel_contact_states
{
public:
  explicit Init_HtNavContactStates_fr_wheel_contact_states(::ht_nav_variables::msg::HtNavContactStates & msg)
  : msg_(msg)
  {}
  Init_HtNavContactStates_rl_wheel_contact_states fr_wheel_contact_states(::ht_nav_variables::msg::HtNavContactStates::_fr_wheel_contact_states_type arg)
  {
    msg_.fr_wheel_contact_states = std::move(arg);
    return Init_HtNavContactStates_rl_wheel_contact_states(msg_);
  }

private:
  ::ht_nav_variables::msg::HtNavContactStates msg_;
};

class Init_HtNavContactStates_fl_wheel_contact_states
{
public:
  explicit Init_HtNavContactStates_fl_wheel_contact_states(::ht_nav_variables::msg::HtNavContactStates & msg)
  : msg_(msg)
  {}
  Init_HtNavContactStates_fr_wheel_contact_states fl_wheel_contact_states(::ht_nav_variables::msg::HtNavContactStates::_fl_wheel_contact_states_type arg)
  {
    msg_.fl_wheel_contact_states = std::move(arg);
    return Init_HtNavContactStates_fr_wheel_contact_states(msg_);
  }

private:
  ::ht_nav_variables::msg::HtNavContactStates msg_;
};

class Init_HtNavContactStates_time
{
public:
  Init_HtNavContactStates_time()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_HtNavContactStates_fl_wheel_contact_states time(::ht_nav_variables::msg::HtNavContactStates::_time_type arg)
  {
    msg_.time = std::move(arg);
    return Init_HtNavContactStates_fl_wheel_contact_states(msg_);
  }

private:
  ::ht_nav_variables::msg::HtNavContactStates msg_;
};

}  // namespace builder

}  // namespace msg

template<typename MessageType>
auto build();

template<>
inline
auto build<::ht_nav_variables::msg::HtNavContactStates>()
{
  return ht_nav_variables::msg::builder::Init_HtNavContactStates_time();
}

}  // namespace ht_nav_variables

#endif  // HT_NAV_VARIABLES__MSG__DETAIL__HT_NAV_CONTACT_STATES__BUILDER_HPP_
