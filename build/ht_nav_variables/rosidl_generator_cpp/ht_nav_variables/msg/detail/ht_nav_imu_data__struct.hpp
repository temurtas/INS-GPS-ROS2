// generated from rosidl_generator_cpp/resource/idl__struct.hpp.em
// with input from ht_nav_variables:msg/HtNavImuData.idl
// generated code does not contain a copyright notice

#ifndef HT_NAV_VARIABLES__MSG__DETAIL__HT_NAV_IMU_DATA__STRUCT_HPP_
#define HT_NAV_VARIABLES__MSG__DETAIL__HT_NAV_IMU_DATA__STRUCT_HPP_

#include <rosidl_runtime_cpp/bounded_vector.hpp>
#include <rosidl_runtime_cpp/message_initialization.hpp>
#include <algorithm>
#include <array>
#include <memory>
#include <string>
#include <vector>


// Include directives for member types
// Member 'vel_diff'
// Member 'ang_diff'
#include "ht_nav_variables/msg/detail/ht_nav_vector3__struct.hpp"

#ifndef _WIN32
# define DEPRECATED__ht_nav_variables__msg__HtNavImuData __attribute__((deprecated))
#else
# define DEPRECATED__ht_nav_variables__msg__HtNavImuData __declspec(deprecated)
#endif

namespace ht_nav_variables
{

namespace msg
{

// message struct
template<class ContainerAllocator>
struct HtNavImuData_
{
  using Type = HtNavImuData_<ContainerAllocator>;

  explicit HtNavImuData_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  : vel_diff(_init),
    ang_diff(_init)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->time = 0.0;
    }
  }

  explicit HtNavImuData_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  : vel_diff(_alloc, _init),
    ang_diff(_alloc, _init)
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
  using _vel_diff_type =
    ht_nav_variables::msg::HtNavVector3_<ContainerAllocator>;
  _vel_diff_type vel_diff;
  using _ang_diff_type =
    ht_nav_variables::msg::HtNavVector3_<ContainerAllocator>;
  _ang_diff_type ang_diff;

  // setters for named parameter idiom
  Type & set__time(
    const double & _arg)
  {
    this->time = _arg;
    return *this;
  }
  Type & set__vel_diff(
    const ht_nav_variables::msg::HtNavVector3_<ContainerAllocator> & _arg)
  {
    this->vel_diff = _arg;
    return *this;
  }
  Type & set__ang_diff(
    const ht_nav_variables::msg::HtNavVector3_<ContainerAllocator> & _arg)
  {
    this->ang_diff = _arg;
    return *this;
  }

  // constant declarations

  // pointer types
  using RawPtr =
    ht_nav_variables::msg::HtNavImuData_<ContainerAllocator> *;
  using ConstRawPtr =
    const ht_nav_variables::msg::HtNavImuData_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<ht_nav_variables::msg::HtNavImuData_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<ht_nav_variables::msg::HtNavImuData_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      ht_nav_variables::msg::HtNavImuData_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<ht_nav_variables::msg::HtNavImuData_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      ht_nav_variables::msg::HtNavImuData_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<ht_nav_variables::msg::HtNavImuData_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<ht_nav_variables::msg::HtNavImuData_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<ht_nav_variables::msg::HtNavImuData_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__ht_nav_variables__msg__HtNavImuData
    std::shared_ptr<ht_nav_variables::msg::HtNavImuData_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__ht_nav_variables__msg__HtNavImuData
    std::shared_ptr<ht_nav_variables::msg::HtNavImuData_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const HtNavImuData_ & other) const
  {
    if (this->time != other.time) {
      return false;
    }
    if (this->vel_diff != other.vel_diff) {
      return false;
    }
    if (this->ang_diff != other.ang_diff) {
      return false;
    }
    return true;
  }
  bool operator!=(const HtNavImuData_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct HtNavImuData_

// alias to use template instance with default allocator
using HtNavImuData =
  ht_nav_variables::msg::HtNavImuData_<std::allocator<void>>;

// constant definitions

}  // namespace msg

}  // namespace ht_nav_variables

#endif  // HT_NAV_VARIABLES__MSG__DETAIL__HT_NAV_IMU_DATA__STRUCT_HPP_
