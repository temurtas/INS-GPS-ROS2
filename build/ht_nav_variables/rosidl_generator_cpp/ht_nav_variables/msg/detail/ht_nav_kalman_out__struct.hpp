// generated from rosidl_generator_cpp/resource/idl__struct.hpp.em
// with input from ht_nav_variables:msg/HtNavKalmanOut.idl
// generated code does not contain a copyright notice

#ifndef HT_NAV_VARIABLES__MSG__DETAIL__HT_NAV_KALMAN_OUT__STRUCT_HPP_
#define HT_NAV_VARIABLES__MSG__DETAIL__HT_NAV_KALMAN_OUT__STRUCT_HPP_

#include <rosidl_runtime_cpp/bounded_vector.hpp>
#include <rosidl_runtime_cpp/message_initialization.hpp>
#include <algorithm>
#include <array>
#include <memory>
#include <string>
#include <vector>


// Include directives for member types
// Member 'bias'
// Member 'drift'
#include "ht_nav_variables/msg/detail/ht_nav_error_vector__struct.hpp"

#ifndef _WIN32
# define DEPRECATED__ht_nav_variables__msg__HtNavKalmanOut __attribute__((deprecated))
#else
# define DEPRECATED__ht_nav_variables__msg__HtNavKalmanOut __declspec(deprecated)
#endif

namespace ht_nav_variables
{

namespace msg
{

// message struct
template<class ContainerAllocator>
struct HtNavKalmanOut_
{
  using Type = HtNavKalmanOut_<ContainerAllocator>;

  explicit HtNavKalmanOut_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  : bias(_init),
    drift(_init)
  {
    (void)_init;
  }

  explicit HtNavKalmanOut_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  : bias(_alloc, _init),
    drift(_alloc, _init)
  {
    (void)_init;
  }

  // field types and members
  using _bias_type =
    ht_nav_variables::msg::HtNavErrorVector_<ContainerAllocator>;
  _bias_type bias;
  using _drift_type =
    ht_nav_variables::msg::HtNavErrorVector_<ContainerAllocator>;
  _drift_type drift;

  // setters for named parameter idiom
  Type & set__bias(
    const ht_nav_variables::msg::HtNavErrorVector_<ContainerAllocator> & _arg)
  {
    this->bias = _arg;
    return *this;
  }
  Type & set__drift(
    const ht_nav_variables::msg::HtNavErrorVector_<ContainerAllocator> & _arg)
  {
    this->drift = _arg;
    return *this;
  }

  // constant declarations

  // pointer types
  using RawPtr =
    ht_nav_variables::msg::HtNavKalmanOut_<ContainerAllocator> *;
  using ConstRawPtr =
    const ht_nav_variables::msg::HtNavKalmanOut_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<ht_nav_variables::msg::HtNavKalmanOut_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<ht_nav_variables::msg::HtNavKalmanOut_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      ht_nav_variables::msg::HtNavKalmanOut_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<ht_nav_variables::msg::HtNavKalmanOut_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      ht_nav_variables::msg::HtNavKalmanOut_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<ht_nav_variables::msg::HtNavKalmanOut_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<ht_nav_variables::msg::HtNavKalmanOut_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<ht_nav_variables::msg::HtNavKalmanOut_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__ht_nav_variables__msg__HtNavKalmanOut
    std::shared_ptr<ht_nav_variables::msg::HtNavKalmanOut_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__ht_nav_variables__msg__HtNavKalmanOut
    std::shared_ptr<ht_nav_variables::msg::HtNavKalmanOut_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const HtNavKalmanOut_ & other) const
  {
    if (this->bias != other.bias) {
      return false;
    }
    if (this->drift != other.drift) {
      return false;
    }
    return true;
  }
  bool operator!=(const HtNavKalmanOut_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct HtNavKalmanOut_

// alias to use template instance with default allocator
using HtNavKalmanOut =
  ht_nav_variables::msg::HtNavKalmanOut_<std::allocator<void>>;

// constant definitions

}  // namespace msg

}  // namespace ht_nav_variables

#endif  // HT_NAV_VARIABLES__MSG__DETAIL__HT_NAV_KALMAN_OUT__STRUCT_HPP_
