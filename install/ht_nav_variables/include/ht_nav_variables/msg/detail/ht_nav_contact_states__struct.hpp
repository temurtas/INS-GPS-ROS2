// generated from rosidl_generator_cpp/resource/idl__struct.hpp.em
// with input from ht_nav_variables:msg/HtNavContactStates.idl
// generated code does not contain a copyright notice

#ifndef HT_NAV_VARIABLES__MSG__DETAIL__HT_NAV_CONTACT_STATES__STRUCT_HPP_
#define HT_NAV_VARIABLES__MSG__DETAIL__HT_NAV_CONTACT_STATES__STRUCT_HPP_

#include <rosidl_runtime_cpp/bounded_vector.hpp>
#include <rosidl_runtime_cpp/message_initialization.hpp>
#include <algorithm>
#include <array>
#include <memory>
#include <string>
#include <vector>


// Include directives for member types
// Member 'fl_wheel_contact_states'
// Member 'fr_wheel_contact_states'
// Member 'rl_wheel_contact_states'
// Member 'rr_wheel_contact_states'
#include "ht_nav_variables/msg/detail/ht_nav_contact_state__struct.hpp"

#ifndef _WIN32
# define DEPRECATED__ht_nav_variables__msg__HtNavContactStates __attribute__((deprecated))
#else
# define DEPRECATED__ht_nav_variables__msg__HtNavContactStates __declspec(deprecated)
#endif

namespace ht_nav_variables
{

namespace msg
{

// message struct
template<class ContainerAllocator>
struct HtNavContactStates_
{
  using Type = HtNavContactStates_<ContainerAllocator>;

  explicit HtNavContactStates_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  : fl_wheel_contact_states(_init),
    fr_wheel_contact_states(_init),
    rl_wheel_contact_states(_init),
    rr_wheel_contact_states(_init)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->time = 0.0;
    }
  }

  explicit HtNavContactStates_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  : fl_wheel_contact_states(_alloc, _init),
    fr_wheel_contact_states(_alloc, _init),
    rl_wheel_contact_states(_alloc, _init),
    rr_wheel_contact_states(_alloc, _init)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->time = 0.0;
    }
  }

  // field types and members
  using _time_type =
    double;
  _time_type time;
  using _fl_wheel_contact_states_type =
    ht_nav_variables::msg::HtNavContactState_<ContainerAllocator>;
  _fl_wheel_contact_states_type fl_wheel_contact_states;
  using _fr_wheel_contact_states_type =
    ht_nav_variables::msg::HtNavContactState_<ContainerAllocator>;
  _fr_wheel_contact_states_type fr_wheel_contact_states;
  using _rl_wheel_contact_states_type =
    ht_nav_variables::msg::HtNavContactState_<ContainerAllocator>;
  _rl_wheel_contact_states_type rl_wheel_contact_states;
  using _rr_wheel_contact_states_type =
    ht_nav_variables::msg::HtNavContactState_<ContainerAllocator>;
  _rr_wheel_contact_states_type rr_wheel_contact_states;

  // setters for named parameter idiom
  Type & set__time(
    const double & _arg)
  {
    this->time = _arg;
    return *this;
  }
  Type & set__fl_wheel_contact_states(
    const ht_nav_variables::msg::HtNavContactState_<ContainerAllocator> & _arg)
  {
    this->fl_wheel_contact_states = _arg;
    return *this;
  }
  Type & set__fr_wheel_contact_states(
    const ht_nav_variables::msg::HtNavContactState_<ContainerAllocator> & _arg)
  {
    this->fr_wheel_contact_states = _arg;
    return *this;
  }
  Type & set__rl_wheel_contact_states(
    const ht_nav_variables::msg::HtNavContactState_<ContainerAllocator> & _arg)
  {
    this->rl_wheel_contact_states = _arg;
    return *this;
  }
  Type & set__rr_wheel_contact_states(
    const ht_nav_variables::msg::HtNavContactState_<ContainerAllocator> & _arg)
  {
    this->rr_wheel_contact_states = _arg;
    return *this;
  }

  // constant declarations

  // pointer types
  using RawPtr =
    ht_nav_variables::msg::HtNavContactStates_<ContainerAllocator> *;
  using ConstRawPtr =
    const ht_nav_variables::msg::HtNavContactStates_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<ht_nav_variables::msg::HtNavContactStates_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<ht_nav_variables::msg::HtNavContactStates_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      ht_nav_variables::msg::HtNavContactStates_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<ht_nav_variables::msg::HtNavContactStates_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      ht_nav_variables::msg::HtNavContactStates_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<ht_nav_variables::msg::HtNavContactStates_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<ht_nav_variables::msg::HtNavContactStates_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<ht_nav_variables::msg::HtNavContactStates_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__ht_nav_variables__msg__HtNavContactStates
    std::shared_ptr<ht_nav_variables::msg::HtNavContactStates_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__ht_nav_variables__msg__HtNavContactStates
    std::shared_ptr<ht_nav_variables::msg::HtNavContactStates_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const HtNavContactStates_ & other) const
  {
    if (this->time != other.time) {
      return false;
    }
    if (this->fl_wheel_contact_states != other.fl_wheel_contact_states) {
      return false;
    }
    if (this->fr_wheel_contact_states != other.fr_wheel_contact_states) {
      return false;
    }
    if (this->rl_wheel_contact_states != other.rl_wheel_contact_states) {
      return false;
    }
    if (this->rr_wheel_contact_states != other.rr_wheel_contact_states) {
      return false;
    }
    return true;
  }
  bool operator!=(const HtNavContactStates_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct HtNavContactStates_

// alias to use template instance with default allocator
using HtNavContactStates =
  ht_nav_variables::msg::HtNavContactStates_<std::allocator<void>>;

// constant definitions

}  // namespace msg

}  // namespace ht_nav_variables

#endif  // HT_NAV_VARIABLES__MSG__DETAIL__HT_NAV_CONTACT_STATES__STRUCT_HPP_
