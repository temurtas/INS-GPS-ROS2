// generated from rosidl_generator_cpp/resource/idl__struct.hpp.em
// with input from ht_nav_variables:msg/HtNavGpsData.idl
// generated code does not contain a copyright notice

#ifndef HT_NAV_VARIABLES__MSG__DETAIL__HT_NAV_GPS_DATA__STRUCT_HPP_
#define HT_NAV_VARIABLES__MSG__DETAIL__HT_NAV_GPS_DATA__STRUCT_HPP_

#include <rosidl_runtime_cpp/bounded_vector.hpp>
#include <rosidl_runtime_cpp/message_initialization.hpp>
#include <algorithm>
#include <array>
#include <memory>
#include <string>
#include <vector>


// Include directives for member types
// Member 'gps_pos'
#include "ht_nav_variables/msg/detail/ht_nav_point__struct.hpp"

#ifndef _WIN32
# define DEPRECATED__ht_nav_variables__msg__HtNavGpsData __attribute__((deprecated))
#else
# define DEPRECATED__ht_nav_variables__msg__HtNavGpsData __declspec(deprecated)
#endif

namespace ht_nav_variables
{

namespace msg
{

// message struct
template<class ContainerAllocator>
struct HtNavGpsData_
{
  using Type = HtNavGpsData_<ContainerAllocator>;

  explicit HtNavGpsData_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  : gps_pos(_init)
  {
    (void)_init;
  }

  explicit HtNavGpsData_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  : gps_pos(_alloc, _init)
  {
    (void)_init;
  }

  // field types and members
  using _gps_pos_type =
    ht_nav_variables::msg::HtNavPoint_<ContainerAllocator>;
  _gps_pos_type gps_pos;

  // setters for named parameter idiom
  Type & set__gps_pos(
    const ht_nav_variables::msg::HtNavPoint_<ContainerAllocator> & _arg)
  {
    this->gps_pos = _arg;
    return *this;
  }

  // constant declarations

  // pointer types
  using RawPtr =
    ht_nav_variables::msg::HtNavGpsData_<ContainerAllocator> *;
  using ConstRawPtr =
    const ht_nav_variables::msg::HtNavGpsData_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<ht_nav_variables::msg::HtNavGpsData_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<ht_nav_variables::msg::HtNavGpsData_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      ht_nav_variables::msg::HtNavGpsData_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<ht_nav_variables::msg::HtNavGpsData_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      ht_nav_variables::msg::HtNavGpsData_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<ht_nav_variables::msg::HtNavGpsData_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<ht_nav_variables::msg::HtNavGpsData_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<ht_nav_variables::msg::HtNavGpsData_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__ht_nav_variables__msg__HtNavGpsData
    std::shared_ptr<ht_nav_variables::msg::HtNavGpsData_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__ht_nav_variables__msg__HtNavGpsData
    std::shared_ptr<ht_nav_variables::msg::HtNavGpsData_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const HtNavGpsData_ & other) const
  {
    if (this->gps_pos != other.gps_pos) {
      return false;
    }
    return true;
  }
  bool operator!=(const HtNavGpsData_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct HtNavGpsData_

// alias to use template instance with default allocator
using HtNavGpsData =
  ht_nav_variables::msg::HtNavGpsData_<std::allocator<void>>;

// constant definitions

}  // namespace msg

}  // namespace ht_nav_variables

#endif  // HT_NAV_VARIABLES__MSG__DETAIL__HT_NAV_GPS_DATA__STRUCT_HPP_
