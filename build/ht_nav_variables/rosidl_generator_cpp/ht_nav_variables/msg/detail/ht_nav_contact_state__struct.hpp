// generated from rosidl_generator_cpp/resource/idl__struct.hpp.em
// with input from ht_nav_variables:msg/HtNavContactState.idl
// generated code does not contain a copyright notice

#ifndef HT_NAV_VARIABLES__MSG__DETAIL__HT_NAV_CONTACT_STATE__STRUCT_HPP_
#define HT_NAV_VARIABLES__MSG__DETAIL__HT_NAV_CONTACT_STATE__STRUCT_HPP_

#include <rosidl_runtime_cpp/bounded_vector.hpp>
#include <rosidl_runtime_cpp/message_initialization.hpp>
#include <algorithm>
#include <array>
#include <memory>
#include <string>
#include <vector>


// Include directives for member types
// Member 'ideal_contact_forces'
// Member 'ideal_pacejka_forces'
// Member 'ideal_slip'
#include "ht_nav_variables/msg/detail/ht_nav_vector3__struct.hpp"

#ifndef _WIN32
# define DEPRECATED__ht_nav_variables__msg__HtNavContactState __attribute__((deprecated))
#else
# define DEPRECATED__ht_nav_variables__msg__HtNavContactState __declspec(deprecated)
#endif

namespace ht_nav_variables
{

namespace msg
{

// message struct
template<class ContainerAllocator>
struct HtNavContactState_
{
  using Type = HtNavContactState_<ContainerAllocator>;

  explicit HtNavContactState_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  : ideal_contact_forces(_init),
    ideal_pacejka_forces(_init),
    ideal_slip(_init)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->time = 0.0;
    }
  }

  explicit HtNavContactState_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  : ideal_contact_forces(_alloc, _init),
    ideal_pacejka_forces(_alloc, _init),
    ideal_slip(_alloc, _init)
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
  using _ideal_contact_forces_type =
    ht_nav_variables::msg::HtNavVector3_<ContainerAllocator>;
  _ideal_contact_forces_type ideal_contact_forces;
  using _ideal_pacejka_forces_type =
    ht_nav_variables::msg::HtNavVector3_<ContainerAllocator>;
  _ideal_pacejka_forces_type ideal_pacejka_forces;
  using _ideal_slip_type =
    ht_nav_variables::msg::HtNavVector3_<ContainerAllocator>;
  _ideal_slip_type ideal_slip;

  // setters for named parameter idiom
  Type & set__time(
    const double & _arg)
  {
    this->time = _arg;
    return *this;
  }
  Type & set__ideal_contact_forces(
    const ht_nav_variables::msg::HtNavVector3_<ContainerAllocator> & _arg)
  {
    this->ideal_contact_forces = _arg;
    return *this;
  }
  Type & set__ideal_pacejka_forces(
    const ht_nav_variables::msg::HtNavVector3_<ContainerAllocator> & _arg)
  {
    this->ideal_pacejka_forces = _arg;
    return *this;
  }
  Type & set__ideal_slip(
    const ht_nav_variables::msg::HtNavVector3_<ContainerAllocator> & _arg)
  {
    this->ideal_slip = _arg;
    return *this;
  }

  // constant declarations

  // pointer types
  using RawPtr =
    ht_nav_variables::msg::HtNavContactState_<ContainerAllocator> *;
  using ConstRawPtr =
    const ht_nav_variables::msg::HtNavContactState_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<ht_nav_variables::msg::HtNavContactState_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<ht_nav_variables::msg::HtNavContactState_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      ht_nav_variables::msg::HtNavContactState_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<ht_nav_variables::msg::HtNavContactState_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      ht_nav_variables::msg::HtNavContactState_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<ht_nav_variables::msg::HtNavContactState_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<ht_nav_variables::msg::HtNavContactState_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<ht_nav_variables::msg::HtNavContactState_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__ht_nav_variables__msg__HtNavContactState
    std::shared_ptr<ht_nav_variables::msg::HtNavContactState_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__ht_nav_variables__msg__HtNavContactState
    std::shared_ptr<ht_nav_variables::msg::HtNavContactState_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const HtNavContactState_ & other) const
  {
    if (this->time != other.time) {
      return false;
    }
    if (this->ideal_contact_forces != other.ideal_contact_forces) {
      return false;
    }
    if (this->ideal_pacejka_forces != other.ideal_pacejka_forces) {
      return false;
    }
    if (this->ideal_slip != other.ideal_slip) {
      return false;
    }
    return true;
  }
  bool operator!=(const HtNavContactState_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct HtNavContactState_

// alias to use template instance with default allocator
using HtNavContactState =
  ht_nav_variables::msg::HtNavContactState_<std::allocator<void>>;

// constant definitions

}  // namespace msg

}  // namespace ht_nav_variables

#endif  // HT_NAV_VARIABLES__MSG__DETAIL__HT_NAV_CONTACT_STATE__STRUCT_HPP_
