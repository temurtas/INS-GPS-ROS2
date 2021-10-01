// generated from rosidl_typesupport_fastrtps_cpp/resource/idl__rosidl_typesupport_fastrtps_cpp.hpp.em
// with input from ht_nav_variables:msg/HtNavEuler.idl
// generated code does not contain a copyright notice

#ifndef HT_NAV_VARIABLES__MSG__DETAIL__HT_NAV_EULER__ROSIDL_TYPESUPPORT_FASTRTPS_CPP_HPP_
#define HT_NAV_VARIABLES__MSG__DETAIL__HT_NAV_EULER__ROSIDL_TYPESUPPORT_FASTRTPS_CPP_HPP_

#include "rosidl_runtime_c/message_type_support_struct.h"
#include "rosidl_typesupport_interface/macros.h"
#include "ht_nav_variables/msg/rosidl_typesupport_fastrtps_cpp__visibility_control.h"
#include "ht_nav_variables/msg/detail/ht_nav_euler__struct.hpp"

#ifndef _WIN32
# pragma GCC diagnostic push
# pragma GCC diagnostic ignored "-Wunused-parameter"
# ifdef __clang__
#  pragma clang diagnostic ignored "-Wdeprecated-register"
#  pragma clang diagnostic ignored "-Wreturn-type-c-linkage"
# endif
#endif
#ifndef _WIN32
# pragma GCC diagnostic pop
#endif

#include "fastcdr/Cdr.h"

namespace ht_nav_variables
{

namespace msg
{

namespace typesupport_fastrtps_cpp
{

bool
ROSIDL_TYPESUPPORT_FASTRTPS_CPP_PUBLIC_ht_nav_variables
cdr_serialize(
  const ht_nav_variables::msg::HtNavEuler & ros_message,
  eprosima::fastcdr::Cdr & cdr);

bool
ROSIDL_TYPESUPPORT_FASTRTPS_CPP_PUBLIC_ht_nav_variables
cdr_deserialize(
  eprosima::fastcdr::Cdr & cdr,
  ht_nav_variables::msg::HtNavEuler & ros_message);

size_t
ROSIDL_TYPESUPPORT_FASTRTPS_CPP_PUBLIC_ht_nav_variables
get_serialized_size(
  const ht_nav_variables::msg::HtNavEuler & ros_message,
  size_t current_alignment);

size_t
ROSIDL_TYPESUPPORT_FASTRTPS_CPP_PUBLIC_ht_nav_variables
max_serialized_size_HtNavEuler(
  bool & full_bounded,
  size_t current_alignment);

}  // namespace typesupport_fastrtps_cpp

}  // namespace msg

}  // namespace ht_nav_variables

#ifdef __cplusplus
extern "C"
{
#endif

ROSIDL_TYPESUPPORT_FASTRTPS_CPP_PUBLIC_ht_nav_variables
const rosidl_message_type_support_t *
  ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_fastrtps_cpp, ht_nav_variables, msg, HtNavEuler)();

#ifdef __cplusplus
}
#endif

#endif  // HT_NAV_VARIABLES__MSG__DETAIL__HT_NAV_EULER__ROSIDL_TYPESUPPORT_FASTRTPS_CPP_HPP_
