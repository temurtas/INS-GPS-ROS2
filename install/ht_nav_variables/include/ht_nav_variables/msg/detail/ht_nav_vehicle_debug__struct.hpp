// generated from rosidl_generator_cpp/resource/idl__struct.hpp.em
// with input from ht_nav_variables:msg/HtNavVehicleDebug.idl
// generated code does not contain a copyright notice

#ifndef HT_NAV_VARIABLES__MSG__DETAIL__HT_NAV_VEHICLE_DEBUG__STRUCT_HPP_
#define HT_NAV_VARIABLES__MSG__DETAIL__HT_NAV_VEHICLE_DEBUG__STRUCT_HPP_

#include <rosidl_runtime_cpp/bounded_vector.hpp>
#include <rosidl_runtime_cpp/message_initialization.hpp>
#include <algorithm>
#include <array>
#include <memory>
#include <string>
#include <vector>


// Include directives for member types
// Member 'wheel_variables'
#include "ht_nav_variables/msg/detail/ht_nav_tire_out__struct.hpp"
// Member 'imu_link_pva'
// Member 'fl_wheel_pva'
// Member 'fr_wheel_pva'
// Member 'rl_wheel_pva'
// Member 'rr_wheel_pva'
#include "ht_nav_variables/msg/detail/ht_nav_strap_out__struct.hpp"

#ifndef _WIN32
# define DEPRECATED__ht_nav_variables__msg__HtNavVehicleDebug __attribute__((deprecated))
#else
# define DEPRECATED__ht_nav_variables__msg__HtNavVehicleDebug __declspec(deprecated)
#endif

namespace ht_nav_variables
{

namespace msg
{

// message struct
template<class ContainerAllocator>
struct HtNavVehicleDebug_
{
  using Type = HtNavVehicleDebug_<ContainerAllocator>;

  explicit HtNavVehicleDebug_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  : wheel_variables(_init),
    imu_link_pva(_init),
    fl_wheel_pva(_init),
    fr_wheel_pva(_init),
    rl_wheel_pva(_init),
    rr_wheel_pva(_init)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->time = 0.0;
    }
  }

  explicit HtNavVehicleDebug_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  : wheel_variables(_alloc, _init),
    imu_link_pva(_alloc, _init),
    fl_wheel_pva(_alloc, _init),
    fr_wheel_pva(_alloc, _init),
    rl_wheel_pva(_alloc, _init),
    rr_wheel_pva(_alloc, _init)
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
  using _wheel_variables_type =
    ht_nav_variables::msg::HtNavTireOut_<ContainerAllocator>;
  _wheel_variables_type wheel_variables;
  using _imu_link_pva_type =
    ht_nav_variables::msg::HtNavStrapOut_<ContainerAllocator>;
  _imu_link_pva_type imu_link_pva;
  using _fl_wheel_pva_type =
    ht_nav_variables::msg::HtNavStrapOut_<ContainerAllocator>;
  _fl_wheel_pva_type fl_wheel_pva;
  using _fr_wheel_pva_type =
    ht_nav_variables::msg::HtNavStrapOut_<ContainerAllocator>;
  _fr_wheel_pva_type fr_wheel_pva;
  using _rl_wheel_pva_type =
    ht_nav_variables::msg::HtNavStrapOut_<ContainerAllocator>;
  _rl_wheel_pva_type rl_wheel_pva;
  using _rr_wheel_pva_type =
    ht_nav_variables::msg::HtNavStrapOut_<ContainerAllocator>;
  _rr_wheel_pva_type rr_wheel_pva;

  // setters for named parameter idiom
  Type & set__time(
    const double & _arg)
  {
    this->time = _arg;
    return *this;
  }
  Type & set__wheel_variables(
    const ht_nav_variables::msg::HtNavTireOut_<ContainerAllocator> & _arg)
  {
    this->wheel_variables = _arg;
    return *this;
  }
  Type & set__imu_link_pva(
    const ht_nav_variables::msg::HtNavStrapOut_<ContainerAllocator> & _arg)
  {
    this->imu_link_pva = _arg;
    return *this;
  }
  Type & set__fl_wheel_pva(
    const ht_nav_variables::msg::HtNavStrapOut_<ContainerAllocator> & _arg)
  {
    this->fl_wheel_pva = _arg;
    return *this;
  }
  Type & set__fr_wheel_pva(
    const ht_nav_variables::msg::HtNavStrapOut_<ContainerAllocator> & _arg)
  {
    this->fr_wheel_pva = _arg;
    return *this;
  }
  Type & set__rl_wheel_pva(
    const ht_nav_variables::msg::HtNavStrapOut_<ContainerAllocator> & _arg)
  {
    this->rl_wheel_pva = _arg;
    return *this;
  }
  Type & set__rr_wheel_pva(
    const ht_nav_variables::msg::HtNavStrapOut_<ContainerAllocator> & _arg)
  {
    this->rr_wheel_pva = _arg;
    return *this;
  }

  // constant declarations

  // pointer types
  using RawPtr =
    ht_nav_variables::msg::HtNavVehicleDebug_<ContainerAllocator> *;
  using ConstRawPtr =
    const ht_nav_variables::msg::HtNavVehicleDebug_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<ht_nav_variables::msg::HtNavVehicleDebug_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<ht_nav_variables::msg::HtNavVehicleDebug_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      ht_nav_variables::msg::HtNavVehicleDebug_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<ht_nav_variables::msg::HtNavVehicleDebug_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      ht_nav_variables::msg::HtNavVehicleDebug_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<ht_nav_variables::msg::HtNavVehicleDebug_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<ht_nav_variables::msg::HtNavVehicleDebug_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<ht_nav_variables::msg::HtNavVehicleDebug_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__ht_nav_variables__msg__HtNavVehicleDebug
    std::shared_ptr<ht_nav_variables::msg::HtNavVehicleDebug_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__ht_nav_variables__msg__HtNavVehicleDebug
    std::shared_ptr<ht_nav_variables::msg::HtNavVehicleDebug_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const HtNavVehicleDebug_ & other) const
  {
    if (this->time != other.time) {
      return false;
    }
    if (this->wheel_variables != other.wheel_variables) {
      return false;
    }
    if (this->imu_link_pva != other.imu_link_pva) {
      return false;
    }
    if (this->fl_wheel_pva != other.fl_wheel_pva) {
      return false;
    }
    if (this->fr_wheel_pva != other.fr_wheel_pva) {
      return false;
    }
    if (this->rl_wheel_pva != other.rl_wheel_pva) {
      return false;
    }
    if (this->rr_wheel_pva != other.rr_wheel_pva) {
      return false;
    }
    return true;
  }
  bool operator!=(const HtNavVehicleDebug_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct HtNavVehicleDebug_

// alias to use template instance with default allocator
using HtNavVehicleDebug =
  ht_nav_variables::msg::HtNavVehicleDebug_<std::allocator<void>>;

// constant definitions

}  // namespace msg

}  // namespace ht_nav_variables

#endif  // HT_NAV_VARIABLES__MSG__DETAIL__HT_NAV_VEHICLE_DEBUG__STRUCT_HPP_
