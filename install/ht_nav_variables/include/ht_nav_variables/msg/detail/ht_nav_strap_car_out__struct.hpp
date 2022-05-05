// generated from rosidl_generator_cpp/resource/idl__struct.hpp.em
// with input from ht_nav_variables:msg/HtNavStrapCarOut.idl
// generated code does not contain a copyright notice

#ifndef HT_NAV_VARIABLES__MSG__DETAIL__HT_NAV_STRAP_CAR_OUT__STRUCT_HPP_
#define HT_NAV_VARIABLES__MSG__DETAIL__HT_NAV_STRAP_CAR_OUT__STRUCT_HPP_

#include <rosidl_runtime_cpp/bounded_vector.hpp>
#include <rosidl_runtime_cpp/message_initialization.hpp>
#include <algorithm>
#include <array>
#include <memory>
#include <string>
#include <vector>


// Include directives for member types
// Member 'pos'
// Member 'car_pos'
// Member 'vel'
#include "ht_nav_variables/msg/detail/ht_nav_vector3__struct.hpp"
// Member 'euler'
#include "ht_nav_variables/msg/detail/ht_nav_euler__struct.hpp"
// Member 'quaternion'
#include "ht_nav_variables/msg/detail/ht_nav_quaternion__struct.hpp"

#ifndef _WIN32
# define DEPRECATED__ht_nav_variables__msg__HtNavStrapCarOut __attribute__((deprecated))
#else
# define DEPRECATED__ht_nav_variables__msg__HtNavStrapCarOut __declspec(deprecated)
#endif

namespace ht_nav_variables
{

namespace msg
{

// message struct
template<class ContainerAllocator>
struct HtNavStrapCarOut_
{
  using Type = HtNavStrapCarOut_<ContainerAllocator>;

  explicit HtNavStrapCarOut_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  : pos(_init),
    car_pos(_init),
    vel(_init),
    euler(_init),
    quaternion(_init)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->time = 0.0;
    }
  }

  explicit HtNavStrapCarOut_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  : pos(_alloc, _init),
    car_pos(_alloc, _init),
    vel(_alloc, _init),
    euler(_alloc, _init),
    quaternion(_alloc, _init)
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
  using _pos_type =
    ht_nav_variables::msg::HtNavVector3_<ContainerAllocator>;
  _pos_type pos;
  using _car_pos_type =
    ht_nav_variables::msg::HtNavVector3_<ContainerAllocator>;
  _car_pos_type car_pos;
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
  Type & set__time(
    const double & _arg)
  {
    this->time = _arg;
    return *this;
  }
  Type & set__pos(
    const ht_nav_variables::msg::HtNavVector3_<ContainerAllocator> & _arg)
  {
    this->pos = _arg;
    return *this;
  }
  Type & set__car_pos(
    const ht_nav_variables::msg::HtNavVector3_<ContainerAllocator> & _arg)
  {
    this->car_pos = _arg;
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
    ht_nav_variables::msg::HtNavStrapCarOut_<ContainerAllocator> *;
  using ConstRawPtr =
    const ht_nav_variables::msg::HtNavStrapCarOut_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<ht_nav_variables::msg::HtNavStrapCarOut_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<ht_nav_variables::msg::HtNavStrapCarOut_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      ht_nav_variables::msg::HtNavStrapCarOut_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<ht_nav_variables::msg::HtNavStrapCarOut_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      ht_nav_variables::msg::HtNavStrapCarOut_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<ht_nav_variables::msg::HtNavStrapCarOut_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<ht_nav_variables::msg::HtNavStrapCarOut_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<ht_nav_variables::msg::HtNavStrapCarOut_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__ht_nav_variables__msg__HtNavStrapCarOut
    std::shared_ptr<ht_nav_variables::msg::HtNavStrapCarOut_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__ht_nav_variables__msg__HtNavStrapCarOut
    std::shared_ptr<ht_nav_variables::msg::HtNavStrapCarOut_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const HtNavStrapCarOut_ & other) const
  {
    if (this->time != other.time) {
      return false;
    }
    if (this->pos != other.pos) {
      return false;
    }
    if (this->car_pos != other.car_pos) {
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
  bool operator!=(const HtNavStrapCarOut_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct HtNavStrapCarOut_

// alias to use template instance with default allocator
using HtNavStrapCarOut =
  ht_nav_variables::msg::HtNavStrapCarOut_<std::allocator<void>>;

// constant definitions

}  // namespace msg

}  // namespace ht_nav_variables

#endif  // HT_NAV_VARIABLES__MSG__DETAIL__HT_NAV_STRAP_CAR_OUT__STRUCT_HPP_
