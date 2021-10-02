// generated from rosidl_generator_cpp/resource/idl__struct.hpp.em
// with input from ht_nav_variables:msg/HtNavStrapOut.idl
// generated code does not contain a copyright notice

#ifndef HT_NAV_VARIABLES__MSG__DETAIL__HT_NAV_STRAP_OUT__STRUCT_HPP_
#define HT_NAV_VARIABLES__MSG__DETAIL__HT_NAV_STRAP_OUT__STRUCT_HPP_

#include <rosidl_runtime_cpp/bounded_vector.hpp>
#include <rosidl_runtime_cpp/message_initialization.hpp>
#include <algorithm>
#include <array>
#include <memory>
#include <string>
#include <vector>


// Include directives for member types
// Member 'pos'
// Member 'vel'
#include "ht_nav_variables/msg/detail/ht_nav_vector3__struct.hpp"
// Member 'euler'
#include "ht_nav_variables/msg/detail/ht_nav_euler__struct.hpp"
// Member 'quaternion'
#include "ht_nav_variables/msg/detail/ht_nav_quaternion__struct.hpp"

#ifndef _WIN32
# define DEPRECATED__ht_nav_variables__msg__HtNavStrapOut __attribute__((deprecated))
#else
# define DEPRECATED__ht_nav_variables__msg__HtNavStrapOut __declspec(deprecated)
#endif

namespace ht_nav_variables
{

namespace msg
{

// message struct
template<class ContainerAllocator>
struct HtNavStrapOut_
{
  using Type = HtNavStrapOut_<ContainerAllocator>;

  explicit HtNavStrapOut_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  : pos(_init),
    vel(_init),
    euler(_init),
    quaternion(_init)
  {
    (void)_init;
  }

  explicit HtNavStrapOut_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  : pos(_alloc, _init),
    vel(_alloc, _init),
    euler(_alloc, _init),
    quaternion(_alloc, _init)
  {
    (void)_init;
  }

  // field types and members
  using _pos_type =
    ht_nav_variables::msg::HtNavVector3_<ContainerAllocator>;
  _pos_type pos;
  using _vel_type =
    ht_nav_variables::msg::HtNavVector3_<ContainerAllocator>;
  _vel_type vel;
  using _euler_type =
    ht_nav_variables::msg::HtNavEuler_<ContainerAllocator>;
  _euler_type euler;
  using _quaternion_type =
    ht_nav_variables::msg::HtNavQuaternion_<ContainerAllocator>;
  _quaternion_type quaternion;

  // setters for named parameter idiom
  Type & set__pos(
    const ht_nav_variables::msg::HtNavVector3_<ContainerAllocator> & _arg)
  {
    this->pos = _arg;
    return *this;
  }
  Type & set__vel(
    const ht_nav_variables::msg::HtNavVector3_<ContainerAllocator> & _arg)
  {
    this->vel = _arg;
    return *this;
  }
  Type & set__euler(
    const ht_nav_variables::msg::HtNavEuler_<ContainerAllocator> & _arg)
  {
    this->euler = _arg;
    return *this;
  }
  Type & set__quaternion(
    const ht_nav_variables::msg::HtNavQuaternion_<ContainerAllocator> & _arg)
  {
    this->quaternion = _arg;
    return *this;
  }

  // constant declarations

  // pointer types
  using RawPtr =
    ht_nav_variables::msg::HtNavStrapOut_<ContainerAllocator> *;
  using ConstRawPtr =
    const ht_nav_variables::msg::HtNavStrapOut_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<ht_nav_variables::msg::HtNavStrapOut_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<ht_nav_variables::msg::HtNavStrapOut_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      ht_nav_variables::msg::HtNavStrapOut_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<ht_nav_variables::msg::HtNavStrapOut_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      ht_nav_variables::msg::HtNavStrapOut_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<ht_nav_variables::msg::HtNavStrapOut_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<ht_nav_variables::msg::HtNavStrapOut_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<ht_nav_variables::msg::HtNavStrapOut_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__ht_nav_variables__msg__HtNavStrapOut
    std::shared_ptr<ht_nav_variables::msg::HtNavStrapOut_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__ht_nav_variables__msg__HtNavStrapOut
    std::shared_ptr<ht_nav_variables::msg::HtNavStrapOut_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const HtNavStrapOut_ & other) const
  {
    if (this->pos != other.pos) {
      return false;
    }
    if (this->vel != other.vel) {
      return false;
    }
    if (this->euler != other.euler) {
      return false;
    }
    if (this->quaternion != other.quaternion) {
      return false;
    }
    return true;
  }
  bool operator!=(const HtNavStrapOut_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct HtNavStrapOut_

// alias to use template instance with default allocator
using HtNavStrapOut =
  ht_nav_variables::msg::HtNavStrapOut_<std::allocator<void>>;

// constant definitions

}  // namespace msg

}  // namespace ht_nav_variables

#endif  // HT_NAV_VARIABLES__MSG__DETAIL__HT_NAV_STRAP_OUT__STRUCT_HPP_
