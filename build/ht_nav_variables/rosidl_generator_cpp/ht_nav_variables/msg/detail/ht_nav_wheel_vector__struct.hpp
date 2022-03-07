// generated from rosidl_generator_cpp/resource/idl__struct.hpp.em
// with input from ht_nav_variables:msg/HtNavWheelVector.idl
// generated code does not contain a copyright notice

#ifndef HT_NAV_VARIABLES__MSG__DETAIL__HT_NAV_WHEEL_VECTOR__STRUCT_HPP_
#define HT_NAV_VARIABLES__MSG__DETAIL__HT_NAV_WHEEL_VECTOR__STRUCT_HPP_

#include <rosidl_runtime_cpp/bounded_vector.hpp>
#include <rosidl_runtime_cpp/message_initialization.hpp>
#include <algorithm>
#include <array>
#include <memory>
#include <string>
#include <vector>


#ifndef _WIN32
# define DEPRECATED__ht_nav_variables__msg__HtNavWheelVector __attribute__((deprecated))
#else
# define DEPRECATED__ht_nav_variables__msg__HtNavWheelVector __declspec(deprecated)
#endif

namespace ht_nav_variables
{

namespace msg
{

// message struct
template<class ContainerAllocator>
struct HtNavWheelVector_
{
  using Type = HtNavWheelVector_<ContainerAllocator>;

  explicit HtNavWheelVector_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->w1 = 0.0;
      this->w2 = 0.0;
      this->w3 = 0.0;
      this->w4 = 0.0;
    }
  }

  explicit HtNavWheelVector_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    (void)_alloc;
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->w1 = 0.0;
      this->w2 = 0.0;
      this->w3 = 0.0;
      this->w4 = 0.0;
    }
  }

  // field types and members
  using _w1_type =
    double;
  _w1_type w1;
  using _w2_type =
    double;
  _w2_type w2;
  using _w3_type =
    double;
  _w3_type w3;
  using _w4_type =
    double;
  _w4_type w4;

  // setters for named parameter idiom
  Type & set__w1(
    const double & _arg)
  {
    this->w1 = _arg;
    return *this;
  }
  Type & set__w2(
    const double & _arg)
  {
    this->w2 = _arg;
    return *this;
  }
  Type & set__w3(
    const double & _arg)
  {
    this->w3 = _arg;
    return *this;
  }
  Type & set__w4(
    const double & _arg)
  {
    this->w4 = _arg;
    return *this;
  }

  // constant declarations

  // pointer types
  using RawPtr =
    ht_nav_variables::msg::HtNavWheelVector_<ContainerAllocator> *;
  using ConstRawPtr =
    const ht_nav_variables::msg::HtNavWheelVector_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<ht_nav_variables::msg::HtNavWheelVector_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<ht_nav_variables::msg::HtNavWheelVector_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      ht_nav_variables::msg::HtNavWheelVector_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<ht_nav_variables::msg::HtNavWheelVector_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      ht_nav_variables::msg::HtNavWheelVector_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<ht_nav_variables::msg::HtNavWheelVector_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<ht_nav_variables::msg::HtNavWheelVector_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<ht_nav_variables::msg::HtNavWheelVector_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__ht_nav_variables__msg__HtNavWheelVector
    std::shared_ptr<ht_nav_variables::msg::HtNavWheelVector_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__ht_nav_variables__msg__HtNavWheelVector
    std::shared_ptr<ht_nav_variables::msg::HtNavWheelVector_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const HtNavWheelVector_ & other) const
  {
    if (this->w1 != other.w1) {
      return false;
    }
    if (this->w2 != other.w2) {
      return false;
    }
    if (this->w3 != other.w3) {
      return false;
    }
    if (this->w4 != other.w4) {
      return false;
    }
    return true;
  }
  bool operator!=(const HtNavWheelVector_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct HtNavWheelVector_

// alias to use template instance with default allocator
using HtNavWheelVector =
  ht_nav_variables::msg::HtNavWheelVector_<std::allocator<void>>;

// constant definitions

}  // namespace msg

}  // namespace ht_nav_variables

#endif  // HT_NAV_VARIABLES__MSG__DETAIL__HT_NAV_WHEEL_VECTOR__STRUCT_HPP_
