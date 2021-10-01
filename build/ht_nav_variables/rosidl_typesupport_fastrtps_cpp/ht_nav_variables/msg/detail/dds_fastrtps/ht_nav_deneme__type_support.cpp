// generated from rosidl_typesupport_fastrtps_cpp/resource/idl__type_support.cpp.em
// with input from ht_nav_variables:msg/HtNavDeneme.idl
// generated code does not contain a copyright notice
#include "ht_nav_variables/msg/detail/ht_nav_deneme__rosidl_typesupport_fastrtps_cpp.hpp"
#include "ht_nav_variables/msg/detail/ht_nav_deneme__struct.hpp"

#include <limits>
#include <stdexcept>
#include <string>
#include "rosidl_typesupport_cpp/message_type_support.hpp"
#include "rosidl_typesupport_fastrtps_cpp/identifier.hpp"
#include "rosidl_typesupport_fastrtps_cpp/message_type_support.h"
#include "rosidl_typesupport_fastrtps_cpp/message_type_support_decl.hpp"
#include "rosidl_typesupport_fastrtps_cpp/wstring_conversion.hpp"
#include "fastcdr/Cdr.h"


// forward declaration of message dependencies and their conversion functions

namespace ht_nav_variables
{

namespace msg
{

namespace typesupport_fastrtps_cpp
{

bool
ROSIDL_TYPESUPPORT_FASTRTPS_CPP_PUBLIC_ht_nav_variables
cdr_serialize(
  const ht_nav_variables::msg::HtNavDeneme & ros_message,
  eprosima::fastcdr::Cdr & cdr)
{
  // Member: num
  cdr << ros_message.num;
  return true;
}

bool
ROSIDL_TYPESUPPORT_FASTRTPS_CPP_PUBLIC_ht_nav_variables
cdr_deserialize(
  eprosima::fastcdr::Cdr & cdr,
  ht_nav_variables::msg::HtNavDeneme & ros_message)
{
  // Member: num
  cdr >> ros_message.num;

  return true;
}

size_t
ROSIDL_TYPESUPPORT_FASTRTPS_CPP_PUBLIC_ht_nav_variables
get_serialized_size(
  const ht_nav_variables::msg::HtNavDeneme & ros_message,
  size_t current_alignment)
{
  size_t initial_alignment = current_alignment;

  const size_t padding = 4;
  const size_t wchar_size = 4;
  (void)padding;
  (void)wchar_size;

  // Member: num
  {
    size_t item_size = sizeof(ros_message.num);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }

  return current_alignment - initial_alignment;
}

size_t
ROSIDL_TYPESUPPORT_FASTRTPS_CPP_PUBLIC_ht_nav_variables
max_serialized_size_HtNavDeneme(
  bool & full_bounded,
  size_t current_alignment)
{
  size_t initial_alignment = current_alignment;

  const size_t padding = 4;
  const size_t wchar_size = 4;
  (void)padding;
  (void)wchar_size;
  (void)full_bounded;


  // Member: num
  {
    size_t array_size = 1;

    current_alignment += array_size * sizeof(uint64_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint64_t));
  }

  return current_alignment - initial_alignment;
}

static bool _HtNavDeneme__cdr_serialize(
  const void * untyped_ros_message,
  eprosima::fastcdr::Cdr & cdr)
{
  auto typed_message =
    static_cast<const ht_nav_variables::msg::HtNavDeneme *>(
    untyped_ros_message);
  return cdr_serialize(*typed_message, cdr);
}

static bool _HtNavDeneme__cdr_deserialize(
  eprosima::fastcdr::Cdr & cdr,
  void * untyped_ros_message)
{
  auto typed_message =
    static_cast<ht_nav_variables::msg::HtNavDeneme *>(
    untyped_ros_message);
  return cdr_deserialize(cdr, *typed_message);
}

static uint32_t _HtNavDeneme__get_serialized_size(
  const void * untyped_ros_message)
{
  auto typed_message =
    static_cast<const ht_nav_variables::msg::HtNavDeneme *>(
    untyped_ros_message);
  return static_cast<uint32_t>(get_serialized_size(*typed_message, 0));
}

static size_t _HtNavDeneme__max_serialized_size(bool & full_bounded)
{
  return max_serialized_size_HtNavDeneme(full_bounded, 0);
}

static message_type_support_callbacks_t _HtNavDeneme__callbacks = {
  "ht_nav_variables::msg",
  "HtNavDeneme",
  _HtNavDeneme__cdr_serialize,
  _HtNavDeneme__cdr_deserialize,
  _HtNavDeneme__get_serialized_size,
  _HtNavDeneme__max_serialized_size
};

static rosidl_message_type_support_t _HtNavDeneme__handle = {
  rosidl_typesupport_fastrtps_cpp::typesupport_identifier,
  &_HtNavDeneme__callbacks,
  get_message_typesupport_handle_function,
};

}  // namespace typesupport_fastrtps_cpp

}  // namespace msg

}  // namespace ht_nav_variables

namespace rosidl_typesupport_fastrtps_cpp
{

template<>
ROSIDL_TYPESUPPORT_FASTRTPS_CPP_EXPORT_ht_nav_variables
const rosidl_message_type_support_t *
get_message_type_support_handle<ht_nav_variables::msg::HtNavDeneme>()
{
  return &ht_nav_variables::msg::typesupport_fastrtps_cpp::_HtNavDeneme__handle;
}

}  // namespace rosidl_typesupport_fastrtps_cpp

#ifdef __cplusplus
extern "C"
{
#endif

const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_fastrtps_cpp, ht_nav_variables, msg, HtNavDeneme)() {
  return &ht_nav_variables::msg::typesupport_fastrtps_cpp::_HtNavDeneme__handle;
}

#ifdef __cplusplus
}
#endif
