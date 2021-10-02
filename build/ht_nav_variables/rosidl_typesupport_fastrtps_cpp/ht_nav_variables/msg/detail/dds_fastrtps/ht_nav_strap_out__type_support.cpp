// generated from rosidl_typesupport_fastrtps_cpp/resource/idl__type_support.cpp.em
// with input from ht_nav_variables:msg/HtNavStrapOut.idl
// generated code does not contain a copyright notice
#include "ht_nav_variables/msg/detail/ht_nav_strap_out__rosidl_typesupport_fastrtps_cpp.hpp"
#include "ht_nav_variables/msg/detail/ht_nav_strap_out__struct.hpp"

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
bool cdr_serialize(
  const ht_nav_variables::msg::HtNavVector3 &,
  eprosima::fastcdr::Cdr &);
bool cdr_deserialize(
  eprosima::fastcdr::Cdr &,
  ht_nav_variables::msg::HtNavVector3 &);
size_t get_serialized_size(
  const ht_nav_variables::msg::HtNavVector3 &,
  size_t current_alignment);
size_t
max_serialized_size_HtNavVector3(
  bool & full_bounded,
  size_t current_alignment);
}  // namespace typesupport_fastrtps_cpp
}  // namespace msg
}  // namespace ht_nav_variables

namespace ht_nav_variables
{
namespace msg
{
namespace typesupport_fastrtps_cpp
{
bool cdr_serialize(
  const ht_nav_variables::msg::HtNavVector3 &,
  eprosima::fastcdr::Cdr &);
bool cdr_deserialize(
  eprosima::fastcdr::Cdr &,
  ht_nav_variables::msg::HtNavVector3 &);
size_t get_serialized_size(
  const ht_nav_variables::msg::HtNavVector3 &,
  size_t current_alignment);
size_t
max_serialized_size_HtNavVector3(
  bool & full_bounded,
  size_t current_alignment);
}  // namespace typesupport_fastrtps_cpp
}  // namespace msg
}  // namespace ht_nav_variables

namespace ht_nav_variables
{
namespace msg
{
namespace typesupport_fastrtps_cpp
{
bool cdr_serialize(
  const ht_nav_variables::msg::HtNavEuler &,
  eprosima::fastcdr::Cdr &);
bool cdr_deserialize(
  eprosima::fastcdr::Cdr &,
  ht_nav_variables::msg::HtNavEuler &);
size_t get_serialized_size(
  const ht_nav_variables::msg::HtNavEuler &,
  size_t current_alignment);
size_t
max_serialized_size_HtNavEuler(
  bool & full_bounded,
  size_t current_alignment);
}  // namespace typesupport_fastrtps_cpp
}  // namespace msg
}  // namespace ht_nav_variables

namespace ht_nav_variables
{
namespace msg
{
namespace typesupport_fastrtps_cpp
{
bool cdr_serialize(
  const ht_nav_variables::msg::HtNavQuaternion &,
  eprosima::fastcdr::Cdr &);
bool cdr_deserialize(
  eprosima::fastcdr::Cdr &,
  ht_nav_variables::msg::HtNavQuaternion &);
size_t get_serialized_size(
  const ht_nav_variables::msg::HtNavQuaternion &,
  size_t current_alignment);
size_t
max_serialized_size_HtNavQuaternion(
  bool & full_bounded,
  size_t current_alignment);
}  // namespace typesupport_fastrtps_cpp
}  // namespace msg
}  // namespace ht_nav_variables


namespace ht_nav_variables
{

namespace msg
{

namespace typesupport_fastrtps_cpp
{

bool
ROSIDL_TYPESUPPORT_FASTRTPS_CPP_PUBLIC_ht_nav_variables
cdr_serialize(
  const ht_nav_variables::msg::HtNavStrapOut & ros_message,
  eprosima::fastcdr::Cdr & cdr)
{
  // Member: pos
  ht_nav_variables::msg::typesupport_fastrtps_cpp::cdr_serialize(
    ros_message.pos,
    cdr);
  // Member: vel
  ht_nav_variables::msg::typesupport_fastrtps_cpp::cdr_serialize(
    ros_message.vel,
    cdr);
  // Member: euler
  ht_nav_variables::msg::typesupport_fastrtps_cpp::cdr_serialize(
    ros_message.euler,
    cdr);
  // Member: quaternion
  ht_nav_variables::msg::typesupport_fastrtps_cpp::cdr_serialize(
    ros_message.quaternion,
    cdr);
  return true;
}

bool
ROSIDL_TYPESUPPORT_FASTRTPS_CPP_PUBLIC_ht_nav_variables
cdr_deserialize(
  eprosima::fastcdr::Cdr & cdr,
  ht_nav_variables::msg::HtNavStrapOut & ros_message)
{
  // Member: pos
  ht_nav_variables::msg::typesupport_fastrtps_cpp::cdr_deserialize(
    cdr, ros_message.pos);

  // Member: vel
  ht_nav_variables::msg::typesupport_fastrtps_cpp::cdr_deserialize(
    cdr, ros_message.vel);

  // Member: euler
  ht_nav_variables::msg::typesupport_fastrtps_cpp::cdr_deserialize(
    cdr, ros_message.euler);

  // Member: quaternion
  ht_nav_variables::msg::typesupport_fastrtps_cpp::cdr_deserialize(
    cdr, ros_message.quaternion);

  return true;
}

size_t
ROSIDL_TYPESUPPORT_FASTRTPS_CPP_PUBLIC_ht_nav_variables
get_serialized_size(
  const ht_nav_variables::msg::HtNavStrapOut & ros_message,
  size_t current_alignment)
{
  size_t initial_alignment = current_alignment;

  const size_t padding = 4;
  const size_t wchar_size = 4;
  (void)padding;
  (void)wchar_size;

  // Member: pos

  current_alignment +=
    ht_nav_variables::msg::typesupport_fastrtps_cpp::get_serialized_size(
    ros_message.pos, current_alignment);
  // Member: vel

  current_alignment +=
    ht_nav_variables::msg::typesupport_fastrtps_cpp::get_serialized_size(
    ros_message.vel, current_alignment);
  // Member: euler

  current_alignment +=
    ht_nav_variables::msg::typesupport_fastrtps_cpp::get_serialized_size(
    ros_message.euler, current_alignment);
  // Member: quaternion

  current_alignment +=
    ht_nav_variables::msg::typesupport_fastrtps_cpp::get_serialized_size(
    ros_message.quaternion, current_alignment);

  return current_alignment - initial_alignment;
}

size_t
ROSIDL_TYPESUPPORT_FASTRTPS_CPP_PUBLIC_ht_nav_variables
max_serialized_size_HtNavStrapOut(
  bool & full_bounded,
  size_t current_alignment)
{
  size_t initial_alignment = current_alignment;

  const size_t padding = 4;
  const size_t wchar_size = 4;
  (void)padding;
  (void)wchar_size;
  (void)full_bounded;


  // Member: pos
  {
    size_t array_size = 1;


    for (size_t index = 0; index < array_size; ++index) {
      current_alignment +=
        ht_nav_variables::msg::typesupport_fastrtps_cpp::max_serialized_size_HtNavVector3(
        full_bounded, current_alignment);
    }
  }

  // Member: vel
  {
    size_t array_size = 1;


    for (size_t index = 0; index < array_size; ++index) {
      current_alignment +=
        ht_nav_variables::msg::typesupport_fastrtps_cpp::max_serialized_size_HtNavVector3(
        full_bounded, current_alignment);
    }
  }

  // Member: euler
  {
    size_t array_size = 1;


    for (size_t index = 0; index < array_size; ++index) {
      current_alignment +=
        ht_nav_variables::msg::typesupport_fastrtps_cpp::max_serialized_size_HtNavEuler(
        full_bounded, current_alignment);
    }
  }

  // Member: quaternion
  {
    size_t array_size = 1;


    for (size_t index = 0; index < array_size; ++index) {
      current_alignment +=
        ht_nav_variables::msg::typesupport_fastrtps_cpp::max_serialized_size_HtNavQuaternion(
        full_bounded, current_alignment);
    }
  }

  return current_alignment - initial_alignment;
}

static bool _HtNavStrapOut__cdr_serialize(
  const void * untyped_ros_message,
  eprosima::fastcdr::Cdr & cdr)
{
  auto typed_message =
    static_cast<const ht_nav_variables::msg::HtNavStrapOut *>(
    untyped_ros_message);
  return cdr_serialize(*typed_message, cdr);
}

static bool _HtNavStrapOut__cdr_deserialize(
  eprosima::fastcdr::Cdr & cdr,
  void * untyped_ros_message)
{
  auto typed_message =
    static_cast<ht_nav_variables::msg::HtNavStrapOut *>(
    untyped_ros_message);
  return cdr_deserialize(cdr, *typed_message);
}

static uint32_t _HtNavStrapOut__get_serialized_size(
  const void * untyped_ros_message)
{
  auto typed_message =
    static_cast<const ht_nav_variables::msg::HtNavStrapOut *>(
    untyped_ros_message);
  return static_cast<uint32_t>(get_serialized_size(*typed_message, 0));
}

static size_t _HtNavStrapOut__max_serialized_size(bool & full_bounded)
{
  return max_serialized_size_HtNavStrapOut(full_bounded, 0);
}

static message_type_support_callbacks_t _HtNavStrapOut__callbacks = {
  "ht_nav_variables::msg",
  "HtNavStrapOut",
  _HtNavStrapOut__cdr_serialize,
  _HtNavStrapOut__cdr_deserialize,
  _HtNavStrapOut__get_serialized_size,
  _HtNavStrapOut__max_serialized_size
};

static rosidl_message_type_support_t _HtNavStrapOut__handle = {
  rosidl_typesupport_fastrtps_cpp::typesupport_identifier,
  &_HtNavStrapOut__callbacks,
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
get_message_type_support_handle<ht_nav_variables::msg::HtNavStrapOut>()
{
  return &ht_nav_variables::msg::typesupport_fastrtps_cpp::_HtNavStrapOut__handle;
}

}  // namespace rosidl_typesupport_fastrtps_cpp

#ifdef __cplusplus
extern "C"
{
#endif

const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_fastrtps_cpp, ht_nav_variables, msg, HtNavStrapOut)() {
  return &ht_nav_variables::msg::typesupport_fastrtps_cpp::_HtNavStrapOut__handle;
}

#ifdef __cplusplus
}
#endif
