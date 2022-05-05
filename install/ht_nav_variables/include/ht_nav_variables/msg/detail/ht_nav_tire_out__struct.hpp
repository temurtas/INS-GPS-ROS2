// generated from rosidl_generator_cpp/resource/idl__struct.hpp.em
// with input from ht_nav_variables:msg/HtNavTireOut.idl
// generated code does not contain a copyright notice

#ifndef HT_NAV_VARIABLES__MSG__DETAIL__HT_NAV_TIRE_OUT__STRUCT_HPP_
#define HT_NAV_VARIABLES__MSG__DETAIL__HT_NAV_TIRE_OUT__STRUCT_HPP_

#include <rosidl_runtime_cpp/bounded_vector.hpp>
#include <rosidl_runtime_cpp/message_initialization.hpp>
#include <algorithm>
#include <array>
#include <memory>
#include <string>
#include <vector>


// Include directives for member types
// Member 'wheel_side_slip_ang'
// Member 'wheel_longitudinal_slip_ratio'
// Member 'tire_lateral_forces'
// Member 'tire_longitudinal_forces'
#include "ht_nav_variables/msg/detail/ht_nav_wheel_vector__struct.hpp"

#ifndef _WIN32
# define DEPRECATED__ht_nav_variables__msg__HtNavTireOut __attribute__((deprecated))
#else
# define DEPRECATED__ht_nav_variables__msg__HtNavTireOut __declspec(deprecated)
#endif

namespace ht_nav_variables
{

namespace msg
{

// message struct
template<class ContainerAllocator>
struct HtNavTireOut_
{
  using Type = HtNavTireOut_<ContainerAllocator>;

  explicit HtNavTireOut_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  : wheel_side_slip_ang(_init),
    wheel_longitudinal_slip_ratio(_init),
    tire_lateral_forces(_init),
    tire_longitudinal_forces(_init)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->time = 0.0;
      this->effective_radius_est = 0.0;
      this->vehicle_mass_est = 0.0;
    }
  }

  explicit HtNavTireOut_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  : wheel_side_slip_ang(_alloc, _init),
    wheel_longitudinal_slip_ratio(_alloc, _init),
    tire_lateral_forces(_alloc, _init),
    tire_longitudinal_forces(_alloc, _init)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->time = 0.0;
      this->effective_radius_est = 0.0;
      this->vehicle_mass_est = 0.0;
    }
  }

  // field types and members
  using _time_type =
    double;
  _time_type time;
  using _effective_radius_est_type =
    double;
  _effective_radius_est_type effective_radius_est;
  using _vehicle_mass_est_type =
    double;
  _vehicle_mass_est_type vehicle_mass_est;
  using _wheel_side_slip_ang_type =
    ht_nav_variables::msg::HtNavWheelVector_<ContainerAllocator>;
  _wheel_side_slip_ang_type wheel_side_slip_ang;
  using _wheel_longitudinal_slip_ratio_type =
    ht_nav_variables::msg::HtNavWheelVector_<ContainerAllocator>;
  _wheel_longitudinal_slip_ratio_type wheel_longitudinal_slip_ratio;
  using _tire_lateral_forces_type =
    ht_nav_variables::msg::HtNavWheelVector_<ContainerAllocator>;
  _tire_lateral_forces_type tire_lateral_forces;
  using _tire_longitudinal_forces_type =
    ht_nav_variables::msg::HtNavWheelVector_<ContainerAllocator>;
  _tire_longitudinal_forces_type tire_longitudinal_forces;

  // setters for named parameter idiom
  Type & set__time(
    const double & _arg)
  {
    this->time = _arg;
    return *this;
  }
  Type & set__effective_radius_est(
    const double & _arg)
  {
    this->effective_radius_est = _arg;
    return *this;
  }
  Type & set__vehicle_mass_est(
    const double & _arg)
  {
    this->vehicle_mass_est = _arg;
    return *this;
  }
  Type & set__wheel_side_slip_ang(
    const ht_nav_variables::msg::HtNavWheelVector_<ContainerAllocator> & _arg)
  {
    this->wheel_side_slip_ang = _arg;
    return *this;
  }
  Type & set__wheel_longitudinal_slip_ratio(
    const ht_nav_variables::msg::HtNavWheelVector_<ContainerAllocator> & _arg)
  {
    this->wheel_longitudinal_slip_ratio = _arg;
    return *this;
  }
  Type & set__tire_lateral_forces(
    const ht_nav_variables::msg::HtNavWheelVector_<ContainerAllocator> & _arg)
  {
    this->tire_lateral_forces = _arg;
    return *this;
  }
  Type & set__tire_longitudinal_forces(
    const ht_nav_variables::msg::HtNavWheelVector_<ContainerAllocator> & _arg)
  {
    this->tire_longitudinal_forces = _arg;
    return *this;
  }

  // constant declarations

  // pointer types
  using RawPtr =
    ht_nav_variables::msg::HtNavTireOut_<ContainerAllocator> *;
  using ConstRawPtr =
    const ht_nav_variables::msg::HtNavTireOut_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<ht_nav_variables::msg::HtNavTireOut_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<ht_nav_variables::msg::HtNavTireOut_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      ht_nav_variables::msg::HtNavTireOut_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<ht_nav_variables::msg::HtNavTireOut_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      ht_nav_variables::msg::HtNavTireOut_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<ht_nav_variables::msg::HtNavTireOut_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<ht_nav_variables::msg::HtNavTireOut_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<ht_nav_variables::msg::HtNavTireOut_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__ht_nav_variables__msg__HtNavTireOut
    std::shared_ptr<ht_nav_variables::msg::HtNavTireOut_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__ht_nav_variables__msg__HtNavTireOut
    std::shared_ptr<ht_nav_variables::msg::HtNavTireOut_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const HtNavTireOut_ & other) const
  {
    if (this->time != other.time) {
      return false;
    }
    if (this->effective_radius_est != other.effective_radius_est) {
      return false;
    }
    if (this->vehicle_mass_est != other.vehicle_mass_est) {
      return false;
    }
    if (this->wheel_side_slip_ang != other.wheel_side_slip_ang) {
      return false;
    }
    if (this->wheel_longitudinal_slip_ratio != other.wheel_longitudinal_slip_ratio) {
      return false;
    }
    if (this->tire_lateral_forces != other.tire_lateral_forces) {
      return false;
    }
    if (this->tire_longitudinal_forces != other.tire_longitudinal_forces) {
      return false;
    }
    return true;
  }
  bool operator!=(const HtNavTireOut_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct HtNavTireOut_

// alias to use template instance with default allocator
using HtNavTireOut =
  ht_nav_variables::msg::HtNavTireOut_<std::allocator<void>>;

// constant definitions

}  // namespace msg

}  // namespace ht_nav_variables

#endif  // HT_NAV_VARIABLES__MSG__DETAIL__HT_NAV_TIRE_OUT__STRUCT_HPP_
