// generated from rosidl_generator_cpp/resource/idl__struct.hpp.em
// with input from ht_nav_variables:msg/HtNavErrorVector.idl
// generated code does not contain a copyright notice

#ifndef HT_NAV_VARIABLES__MSG__DETAIL__HT_NAV_ERROR_VECTOR__STRUCT_HPP_
#define HT_NAV_VARIABLES__MSG__DETAIL__HT_NAV_ERROR_VECTOR__STRUCT_HPP_

#include <rosidl_runtime_cpp/bounded_vector.hpp>
#include <rosidl_runtime_cpp/message_initialization.hpp>
#include <algorithm>
#include <array>
#include <memory>
#include <string>
#include <vector>


#ifndef _WIN32
# define DEPRECATED__ht_nav_variables__msg__HtNavErrorVector __attribute__((deprecated))
#else
# define DEPRECATED__ht_nav_variables__msg__HtNavErrorVector __declspec(deprecated)
#endif

namespace ht_nav_variables
{

namespace msg
{

// message struct
template<class ContainerAllocator>
struct HtNavErrorVector_
{
  using Type = HtNavErrorVector_<ContainerAllocator>;

  explicit HtNavErrorVector_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->err_x = 0.0;
      this->err_y = 0.0;
      this->err_z = 0.0;
    }
  }

  explicit HtNavErrorVector_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    (void)_alloc;
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->err_x = 0.0;
      this->err_y = 0.0;
      this->err_z = 0.0;
    }
  }

  // field types and members
  using _err_x_type =
    double;
  _err_x_type err_x;
  using _err_y_type =
    double;
  _err_y_type err_y;
  using _err_z_type =
    double;
  _err_z_type err_z;

  // setters for named parameter idiom
  Type & set__err_x(
    const double & _arg)
  {
    this->err_x = _arg;
    return *this;
  }
  Type & set__err_y(
    const double & _arg)
  {
    this->err_y = _arg;
    return *this;
  }
  Type & set__err_z(
    const double & _arg)
  {
    this->err_z = _arg;
    return *this;
  }

  // constant declarations

  // pointer types
  using RawPtr =
    ht_nav_variables::msg::HtNavErrorVector_<ContainerAllocator> *;
  using ConstRawPtr =
    const ht_nav_variables::msg::HtNavErrorVector_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<ht_nav_variables::msg::HtNavErrorVector_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<ht_nav_variables::msg::HtNavErrorVector_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      ht_nav_variables::msg::HtNavErrorVector_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<ht_nav_variables::msg::HtNavErrorVector_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      ht_nav_variables::msg::HtNavErrorVector_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<ht_nav_variables::msg::HtNavErrorVector_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<ht_nav_variables::msg::HtNavErrorVector_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<ht_nav_variables::msg::HtNavErrorVector_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__ht_nav_variables__msg__HtNavErrorVector
    std::shared_ptr<ht_nav_variables::msg::HtNavErrorVector_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__ht_nav_variables__msg__HtNavErrorVector
    std::shared_ptr<ht_nav_variables::msg::HtNavErrorVector_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const HtNavErrorVector_ & other) const
  {
    if (this->err_x != other.err_x) {
      return false;
    }
    if (this->err_y != other.err_y) {
      return false;
    }
    if (this->err_z != other.err_z) {
      return false;
    }
    return true;
  }
  bool operator!=(const HtNavErrorVector_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct HtNavErrorVector_

// alias to use template instance with default allocator
using HtNavErrorVector =
  ht_nav_variables::msg::HtNavErrorVector_<std::allocator<void>>;

// constant definitions

}  // namespace msg

}  // namespace ht_nav_variables

#endif  // HT_NAV_VARIABLES__MSG__DETAIL__HT_NAV_ERROR_VECTOR__STRUCT_HPP_
