// generated from rosidl_typesupport_fastrtps_c/resource/idl__type_support_c.cpp.em
// with input from ht_nav_variables:msg/HtNavImuData.idl
// generated code does not contain a copyright notice
#include "ht_nav_variables/msg/detail/ht_nav_imu_data__rosidl_typesupport_fastrtps_c.h"


#include <cassert>
#include <limits>
#include <string>
#include "rosidl_typesupport_fastrtps_c/identifier.h"
#include "rosidl_typesupport_fastrtps_c/wstring_conversion.hpp"
#include "rosidl_typesupport_fastrtps_cpp/message_type_support.h"
#include "ht_nav_variables/msg/rosidl_typesupport_fastrtps_c__visibility_control.h"
#include "ht_nav_variables/msg/detail/ht_nav_imu_data__struct.h"
#include "ht_nav_variables/msg/detail/ht_nav_imu_data__functions.h"
#include "fastcdr/Cdr.h"

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

// includes and forward declarations of message dependencies and their conversion functions

#if defined(__cplusplus)
extern "C"
{
#endif

#include "ht_nav_variables/msg/detail/ht_nav_vector3__functions.h"  // ang_diff, vel_diff

// forward declare type support functions
size_t get_serialized_size_ht_nav_variables__msg__HtNavVector3(
  const void * untyped_ros_message,
  size_t current_alignment);

size_t max_serialized_size_ht_nav_variables__msg__HtNavVector3(
  bool & full_bounded,
  size_t current_alignment);

const rosidl_message_type_support_t *
  ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_fastrtps_c, ht_nav_variables, msg, HtNavVector3)();


using _HtNavImuData__ros_msg_type = ht_nav_variables__msg__HtNavImuData;

static bool _HtNavImuData__cdr_serialize(
  const void * untyped_ros_message,
  eprosima::fastcdr::Cdr & cdr)
{
  if (!untyped_ros_message) {
    fprintf(stderr, "ros message handle is null\n");
    return false;
  }
  const _HtNavImuData__ros_msg_type * ros_message = static_cast<const _HtNavImuData__ros_msg_type *>(untyped_ros_message);
  // Field name: vel_diff
  {
    const message_type_support_callbacks_t * callbacks =
      static_cast<const message_type_support_callbacks_t *>(
      ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(
        rosidl_typesupport_fastrtps_c, ht_nav_variables, msg, HtNavVector3
      )()->data);
    if (!callbacks->cdr_serialize(
        &ros_message->vel_diff, cdr))
    {
      return false;
    }
  }

  // Field name: ang_diff
  {
    const message_type_support_callbacks_t * callbacks =
      static_cast<const message_type_support_callbacks_t *>(
      ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(
        rosidl_typesupport_fastrtps_c, ht_nav_variables, msg, HtNavVector3
      )()->data);
    if (!callbacks->cdr_serialize(
        &ros_message->ang_diff, cdr))
    {
      return false;
    }
  }

  return true;
}

static bool _HtNavImuData__cdr_deserialize(
  eprosima::fastcdr::Cdr & cdr,
  void * untyped_ros_message)
{
  if (!untyped_ros_message) {
    fprintf(stderr, "ros message handle is null\n");
    return false;
  }
  _HtNavImuData__ros_msg_type * ros_message = static_cast<_HtNavImuData__ros_msg_type *>(untyped_ros_message);
  // Field name: vel_diff
  {
    const message_type_support_callbacks_t * callbacks =
      static_cast<const message_type_support_callbacks_t *>(
      ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(
        rosidl_typesupport_fastrtps_c, ht_nav_variables, msg, HtNavVector3
      )()->data);
    if (!callbacks->cdr_deserialize(
        cdr, &ros_message->vel_diff))
    {
      return false;
    }
  }

  // Field name: ang_diff
  {
    const message_type_support_callbacks_t * callbacks =
      static_cast<const message_type_support_callbacks_t *>(
      ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(
        rosidl_typesupport_fastrtps_c, ht_nav_variables, msg, HtNavVector3
      )()->data);
    if (!callbacks->cdr_deserialize(
        cdr, &ros_message->ang_diff))
    {
      return false;
    }
  }

  return true;
}

ROSIDL_TYPESUPPORT_FASTRTPS_C_PUBLIC_ht_nav_variables
size_t get_serialized_size_ht_nav_variables__msg__HtNavImuData(
  const void * untyped_ros_message,
  size_t current_alignment)
{
  const _HtNavImuData__ros_msg_type * ros_message = static_cast<const _HtNavImuData__ros_msg_type *>(untyped_ros_message);
  (void)ros_message;
  size_t initial_alignment = current_alignment;

  const size_t padding = 4;
  const size_t wchar_size = 4;
  (void)padding;
  (void)wchar_size;

  // field.name vel_diff

  current_alignment += get_serialized_size_ht_nav_variables__msg__HtNavVector3(
    &(ros_message->vel_diff), current_alignment);
  // field.name ang_diff

  current_alignment += get_serialized_size_ht_nav_variables__msg__HtNavVector3(
    &(ros_message->ang_diff), current_alignment);

  return current_alignment - initial_alignment;
}

static uint32_t _HtNavImuData__get_serialized_size(const void * untyped_ros_message)
{
  return static_cast<uint32_t>(
    get_serialized_size_ht_nav_variables__msg__HtNavImuData(
      untyped_ros_message, 0));
}

ROSIDL_TYPESUPPORT_FASTRTPS_C_PUBLIC_ht_nav_variables
size_t max_serialized_size_ht_nav_variables__msg__HtNavImuData(
  bool & full_bounded,
  size_t current_alignment)
{
  size_t initial_alignment = current_alignment;

  const size_t padding = 4;
  const size_t wchar_size = 4;
  (void)padding;
  (void)wchar_size;
  (void)full_bounded;

  // member: vel_diff
  {
    size_t array_size = 1;


    for (size_t index = 0; index < array_size; ++index) {
      current_alignment +=
        max_serialized_size_ht_nav_variables__msg__HtNavVector3(
        full_bounded, current_alignment);
    }
  }
  // member: ang_diff
  {
    size_t array_size = 1;


    for (size_t index = 0; index < array_size; ++index) {
      current_alignment +=
        max_serialized_size_ht_nav_variables__msg__HtNavVector3(
        full_bounded, current_alignment);
    }
  }

  return current_alignment - initial_alignment;
}

static size_t _HtNavImuData__max_serialized_size(bool & full_bounded)
{
  return max_serialized_size_ht_nav_variables__msg__HtNavImuData(
    full_bounded, 0);
}


static message_type_support_callbacks_t __callbacks_HtNavImuData = {
  "ht_nav_variables::msg",
  "HtNavImuData",
  _HtNavImuData__cdr_serialize,
  _HtNavImuData__cdr_deserialize,
  _HtNavImuData__get_serialized_size,
  _HtNavImuData__max_serialized_size
};

static rosidl_message_type_support_t _HtNavImuData__type_support = {
  rosidl_typesupport_fastrtps_c__identifier,
  &__callbacks_HtNavImuData,
  get_message_typesupport_handle_function,
};

const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_fastrtps_c, ht_nav_variables, msg, HtNavImuData)() {
  return &_HtNavImuData__type_support;
}

#if defined(__cplusplus)
}
#endif
