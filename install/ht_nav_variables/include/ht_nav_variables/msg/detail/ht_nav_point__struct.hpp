// generated from rosidl_generator_cpp/resource/idl__struct.hpp.em
// with input from ht_nav_variables:msg/HtNavPoint.idl
// generated code does not contain a copyright notice

#ifndef HT_NAV_VARIABLES__MSG__DETAIL__HT_NAV_POINT__STRUCT_HPP_
#define HT_NAV_VARIABLES__MSG__DETAIL__HT_NAV_POINT__STRUCT_HPP_

#include <rosidl_runtime_cpp/bounded_vector.hpp>
#include <rosidl_runtime_cpp/message_initialization.hpp>
#include <algorithm>
#include <array>
#include <memory>
#include <string>
#include <vector>


#ifndef _WIN32
# define DEPRECATED__ht_nav_variables__msg__HtNavPoint __attribute__((deprecated))
#else
# define DEPRECATED__ht_nav_variables__msg__HtNavPoint __declspec(deprecated)
#endif

namespace ht_nav_variables
{

namespace msg
{

// message struct
template<class ContainerAllocator>
struct HtNavPoint_
{
  using Type = HtNavPoint_<ContainerAllocator>;

  explicit HtNavPoint_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->structure_needs_at_least_one_member = 0;
    }
  }

  explicit HtNavPoint_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    (void)_alloc;
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->structure_needs_at_least_one_member = 0;
    }
  }

  // field types and members
  using _structure_needs_at_least_one_member_type =
    uint8_t;
  _structure_needs_at_least_one_member_type structure_needs_at_least_one_member;


  // constant declarations

  // pointer types
  using RawPtr =
    ht_nav_variables::msg::HtNavPoint_<ContainerAllocator> *;
  using ConstRawPtr =
    const ht_nav_variables::msg::HtNavPoint_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<ht_nav_variables::msg::HtNavPoint_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<ht_nav_variables::msg::HtNavPoint_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      ht_nav_variables::msg::HtNavPoint_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<ht_nav_variables::msg::HtNavPoint_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      ht_nav_variables::msg::HtNavPoint_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<ht_nav_variables::msg::HtNavPoint_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<ht_nav_variables::msg::HtNavPoint_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<ht_nav_variables::msg::HtNavPoint_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__ht_nav_variables__msg__HtNavPoint
    std::shared_ptr<ht_nav_variables::msg::HtNavPoint_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__ht_nav_variables__msg__HtNavPoint
    std::shared_ptr<ht_nav_variables::msg::HtNavPoint_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const HtNavPoint_ & other) const
  {
    if (this->structure_needs_at_least_one_member != other.structure_needs_at_least_one_member) {
      return false;
    }
    return true;
  }
  bool operator!=(const HtNavPoint_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct HtNavPoint_

// alias to use template instance with default allocator
using HtNavPoint =
  ht_nav_variables::msg::HtNavPoint_<std::allocator<void>>;

// constant definitions

}  // namespace msg

}  // namespace ht_nav_variables

#endif  // HT_NAV_VARIABLES__MSG__DETAIL__HT_NAV_POINT__STRUCT_HPP_
