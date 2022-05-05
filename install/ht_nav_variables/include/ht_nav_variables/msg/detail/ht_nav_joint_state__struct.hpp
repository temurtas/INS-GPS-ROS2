// generated from rosidl_generator_cpp/resource/idl__struct.hpp.em
// with input from ht_nav_variables:msg/HtNavJointState.idl
// generated code does not contain a copyright notice

#ifndef HT_NAV_VARIABLES__MSG__DETAIL__HT_NAV_JOINT_STATE__STRUCT_HPP_
#define HT_NAV_VARIABLES__MSG__DETAIL__HT_NAV_JOINT_STATE__STRUCT_HPP_

#include <rosidl_runtime_cpp/bounded_vector.hpp>
#include <rosidl_runtime_cpp/message_initialization.hpp>
#include <algorithm>
#include <array>
#include <memory>
#include <string>
#include <vector>


// Include directives for member types
// Member 'steering_angle'
// Member 'wheel_rotation'
#include "ht_nav_variables/msg/detail/ht_nav_wheel_vector__struct.hpp"

#ifndef _WIN32
# define DEPRECATED__ht_nav_variables__msg__HtNavJointState __attribute__((deprecated))
#else
# define DEPRECATED__ht_nav_variables__msg__HtNavJointState __declspec(deprecated)
#endif

namespace ht_nav_variables
{

namespace msg
{

// message struct
template<class ContainerAllocator>
struct HtNavJointState_
{
  using Type = HtNavJointState_<ContainerAllocator>;

  explicit HtNavJointState_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  : steering_angle(_init),
    wheel_rotation(_init)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->time = 0.0;
    }
  }

  explicit HtNavJointState_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  : steering_angle(_alloc, _init),
    wheel_rotation(_alloc, _init)
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
  using _steering_angle_type =
    ht_nav_variables::msg::HtNavWheelVector_<ContainerAllocator>;
  _steering_angle_type steering_angle;
  using _wheel_rotation_type =
    ht_nav_variables::msg::HtNavWheelVector_<ContainerAllocator>;
  _wheel_rotation_type wheel_rotation;

  // setters for named parameter idiom
  Type & set__time(
    const double & _arg)
  {
    this->time = _arg;
    return *this;
  }
  Type & set__steering_angle(
    const ht_nav_variables::msg::HtNavWheelVector_<ContainerAllocator> & _arg)
  {
    this->steering_angle = _arg;
    return *this;
  }
  Type & set__wheel_rotation(
    const ht_nav_variables::msg::HtNavWheelVector_<ContainerAllocator> & _arg)
  {
    this->wheel_rotation = _arg;
    return *this;
  }

  // constant declarations

  // pointer types
  using RawPtr =
    ht_nav_variables::msg::HtNavJointState_<ContainerAllocator> *;
  using ConstRawPtr =
    const ht_nav_variables::msg::HtNavJointState_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<ht_nav_variables::msg::HtNavJointState_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<ht_nav_variables::msg::HtNavJointState_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      ht_nav_variables::msg::HtNavJointState_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<ht_nav_variables::msg::HtNavJointState_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      ht_nav_variables::msg::HtNavJointState_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<ht_nav_variables::msg::HtNavJointState_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<ht_nav_variables::msg::HtNavJointState_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<ht_nav_variables::msg::HtNavJointState_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__ht_nav_variables__msg__HtNavJointState
    std::shared_ptr<ht_nav_variables::msg::HtNavJointState_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__ht_nav_variables__msg__HtNavJointState
    std::shared_ptr<ht_nav_variables::msg::HtNavJointState_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const HtNavJointState_ & other) const
  {
    if (this->time != other.time) {
      return false;
    }
    if (this->steering_angle != other.steering_angle) {
      return false;
    }
    if (this->wheel_rotation != other.wheel_rotation) {
      return false;
    }
    return true;
  }
  bool operator!=(const HtNavJointState_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct HtNavJointState_

// alias to use template instance with default allocator
using HtNavJointState =
  ht_nav_variables::msg::HtNavJointState_<std::allocator<void>>;

// constant definitions

}  // namespace msg

}  // namespace ht_nav_variables

#endif  // HT_NAV_VARIABLES__MSG__DETAIL__HT_NAV_JOINT_STATE__STRUCT_HPP_
