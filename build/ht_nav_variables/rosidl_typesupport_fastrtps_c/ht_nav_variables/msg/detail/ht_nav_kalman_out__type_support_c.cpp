// generated from rosidl_typesupport_fastrtps_c/resource/idl__type_support_c.cpp.em
// with input from ht_nav_variables:msg/HtNavKalmanOut.idl
// generated code does not contain a copyright notice
#include "ht_nav_variables/msg/detail/ht_nav_kalman_out__rosidl_typesupport_fastrtps_c.h"


#include <cassert>
#include <limits>
#include <string>
#include "rosidl_typesupport_fastrtps_c/identifier.h"
#include "rosidl_typesupport_fastrtps_c/wstring_conversion.hpp"
#include "rosidl_typesupport_fastrtps_cpp/message_type_support.h"
#include "ht_nav_variables/msg/rosidl_typesupport_fastrtps_c__visibility_control.h"
#include "ht_nav_variables/msg/detail/ht_nav_kalman_out__struct.h"
#include "ht_nav_variables/msg/detail/ht_nav_kalman_out__functions.h"
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

#include "ht_nav_variables/msg/detail/ht_nav_error_vector__functions.h"  // att_err, bias, drift, pos_err, vel_err

// forward declare type support functions
size_t get_serialized_size_ht_nav_variables__msg__HtNavErrorVector(
  const void * untyped_ros_message,
  size_t current_alignment);

size_t max_serialized_size_ht_nav_variables__msg__HtNavErrorVector(
  bool & full_bounded,
  size_t current_alignment);

const rosidl_message_type_support_t *
  ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_fastrtps_c, ht_nav_variables, msg, HtNavErrorVector)();


using _HtNavKalmanOut__ros_msg_type = ht_nav_variables__msg__HtNavKalmanOut;

static bool _HtNavKalmanOut__cdr_serialize(
  const void * untyped_ros_message,
  eprosima::fastcdr::Cdr & cdr)
{
  if (!untyped_ros_message) {
    fprintf(stderr, "ros message handle is null\n");
    return false;
  }
  const _HtNavKalmanOut__ros_msg_type * ros_message = static_cast<const _HtNavKalmanOut__ros_msg_type *>(untyped_ros_message);
  // Field name: pos_err
  {
    const message_type_support_callbacks_t * callbacks =
      static_cast<const message_type_support_callbacks_t *>(
      ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(
        rosidl_typesupport_fastrtps_c, ht_nav_variables, msg, HtNavErrorVector
      )()->data);
    if (!callbacks->cdr_serialize(
        &ros_message->pos_err, cdr))
    {
      return false;
    }
  }

  // Field name: vel_err
  {
    const message_type_support_callbacks_t * callbacks =
      static_cast<const message_type_support_callbacks_t *>(
      ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(
        rosidl_typesupport_fastrtps_c, ht_nav_variables, msg, HtNavErrorVector
      )()->data);
    if (!callbacks->cdr_serialize(
        &ros_message->vel_err, cdr))
    {
      return false;
    }
  }

  // Field name: att_err
  {
    const message_type_support_callbacks_t * callbacks =
      static_cast<const message_type_support_callbacks_t *>(
      ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(
        rosidl_typesupport_fastrtps_c, ht_nav_variables, msg, HtNavErrorVector
      )()->data);
    if (!callbacks->cdr_serialize(
        &ros_message->att_err, cdr))
    {
      return false;
    }
  }

  // Field name: bias
  {
    const message_type_support_callbacks_t * callbacks =
      static_cast<const message_type_support_callbacks_t *>(
      ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(
        rosidl_typesupport_fastrtps_c, ht_nav_variables, msg, HtNavErrorVector
      )()->data);
    if (!callbacks->cdr_serialize(
        &ros_message->bias, cdr))
    {
      return false;
    }
  }

  // Field name: drift
  {
    const message_type_support_callbacks_t * callbacks =
      static_cast<const message_type_support_callbacks_t *>(
      ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(
        rosidl_typesupport_fastrtps_c, ht_nav_variables, msg, HtNavErrorVector
      )()->data);
    if (!callbacks->cdr_serialize(
        &ros_message->drift, cdr))
    {
      return false;
    }
  }

  return true;
}

static bool _HtNavKalmanOut__cdr_deserialize(
  eprosima::fastcdr::Cdr & cdr,
  void * untyped_ros_message)
{
  if (!untyped_ros_message) {
    fprintf(stderr, "ros message handle is null\n");
    return false;
  }
  _HtNavKalmanOut__ros_msg_type * ros_message = static_cast<_HtNavKalmanOut__ros_msg_type *>(untyped_ros_message);
  // Field name: pos_err
  {
    const message_type_support_callbacks_t * callbacks =
      static_cast<const message_type_support_callbacks_t *>(
      ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(
        rosidl_typesupport_fastrtps_c, ht_nav_variables, msg, HtNavErrorVector
      )()->data);
    if (!callbacks->cdr_deserialize(
        cdr, &ros_message->pos_err))
    {
      return false;
    }
  }

  // Field name: vel_err
  {
    const message_type_support_callbacks_t * callbacks =
      static_cast<const message_type_support_callbacks_t *>(
      ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(
        rosidl_typesupport_fastrtps_c, ht_nav_variables, msg, HtNavErrorVector
      )()->data);
    if (!callbacks->cdr_deserialize(
        cdr, &ros_message->vel_err))
    {
      return false;
    }
  }

  // Field name: att_err
  {
    const message_type_support_callbacks_t * callbacks =
      static_cast<const message_type_support_callbacks_t *>(
      ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(
        rosidl_typesupport_fastrtps_c, ht_nav_variables, msg, HtNavErrorVector
      )()->data);
    if (!callbacks->cdr_deserialize(
        cdr, &ros_message->att_err))
    {
      return false;
    }
  }

  // Field name: bias
  {
    const message_type_support_callbacks_t * callbacks =
      static_cast<const message_type_support_callbacks_t *>(
      ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(
        rosidl_typesupport_fastrtps_c, ht_nav_variables, msg, HtNavErrorVector
      )()->data);
    if (!callbacks->cdr_deserialize(
        cdr, &ros_message->bias))
    {
      return false;
    }
  }

  // Field name: drift
  {
    const message_type_support_callbacks_t * callbacks =
      static_cast<const message_type_support_callbacks_t *>(
      ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(
        rosidl_typesupport_fastrtps_c, ht_nav_variables, msg, HtNavErrorVector
      )()->data);
    if (!callbacks->cdr_deserialize(
        cdr, &ros_message->drift))
    {
      return false;
    }
  }

  return true;
}

ROSIDL_TYPESUPPORT_FASTRTPS_C_PUBLIC_ht_nav_variables
size_t get_serialized_size_ht_nav_variables__msg__HtNavKalmanOut(
  const void * untyped_ros_message,
  size_t current_alignment)
{
  const _HtNavKalmanOut__ros_msg_type * ros_message = static_cast<const _HtNavKalmanOut__ros_msg_type *>(untyped_ros_message);
  (void)ros_message;
  size_t initial_alignment = current_alignment;

  const size_t padding = 4;
  const size_t wchar_size = 4;
  (void)padding;
  (void)wchar_size;

  // field.name pos_err

  current_alignment += get_serialized_size_ht_nav_variables__msg__HtNavErrorVector(
    &(ros_message->pos_err), current_alignment);
  // field.name vel_err

  current_alignment += get_serialized_size_ht_nav_variables__msg__HtNavErrorVector(
    &(ros_message->vel_err), current_alignment);
  // field.name att_err

  current_alignment += get_serialized_size_ht_nav_variables__msg__HtNavErrorVector(
    &(ros_message->att_err), current_alignment);
  // field.name bias

  current_alignment += get_serialized_size_ht_nav_variables__msg__HtNavErrorVector(
    &(ros_message->bias), current_alignment);
  // field.name drift

  current_alignment += get_serialized_size_ht_nav_variables__msg__HtNavErrorVector(
    &(ros_message->drift), current_alignment);

  return current_alignment - initial_alignment;
}

static uint32_t _HtNavKalmanOut__get_serialized_size(const void * untyped_ros_message)
{
  return static_cast<uint32_t>(
    get_serialized_size_ht_nav_variables__msg__HtNavKalmanOut(
      untyped_ros_message, 0));
}

ROSIDL_TYPESUPPORT_FASTRTPS_C_PUBLIC_ht_nav_variables
size_t max_serialized_size_ht_nav_variables__msg__HtNavKalmanOut(
  bool & full_bounded,
  size_t current_alignment)
{
  size_t initial_alignment = current_alignment;

  const size_t padding = 4;
  const size_t wchar_size = 4;
  (void)padding;
  (void)wchar_size;
  (void)full_bounded;

  // member: pos_err
  {
    size_t array_size = 1;


    for (size_t index = 0; index < array_size; ++index) {
      current_alignment +=
        max_serialized_size_ht_nav_variables__msg__HtNavErrorVector(
        full_bounded, current_alignment);
    }
  }
  // member: vel_err
  {
    size_t array_size = 1;


    for (size_t index = 0; index < array_size; ++index) {
      current_alignment +=
        max_serialized_size_ht_nav_variables__msg__HtNavErrorVector(
        full_bounded, current_alignment);
    }
  }
  // member: att_err
  {
    size_t array_size = 1;


    for (size_t index = 0; index < array_size; ++index) {
      current_alignment +=
        max_serialized_size_ht_nav_variables__msg__HtNavErrorVector(
        full_bounded, current_alignment);
    }
  }
  // member: bias
  {
    size_t array_size = 1;


    for (size_t index = 0; index < array_size; ++index) {
      current_alignment +=
        max_serialized_size_ht_nav_variables__msg__HtNavErrorVector(
        full_bounded, current_alignment);
    }
  }
  // member: drift
  {
    size_t array_size = 1;


    for (size_t index = 0; index < array_size; ++index) {
      current_alignment +=
        max_serialized_size_ht_nav_variables__msg__HtNavErrorVector(
        full_bounded, current_alignment);
    }
  }

  return current_alignment - initial_alignment;
}

static size_t _HtNavKalmanOut__max_serialized_size(bool & full_bounded)
{
  return max_serialized_size_ht_nav_variables__msg__HtNavKalmanOut(
    full_bounded, 0);
}


static message_type_support_callbacks_t __callbacks_HtNavKalmanOut = {
  "ht_nav_variables::msg",
  "HtNavKalmanOut",
  _HtNavKalmanOut__cdr_serialize,
  _HtNavKalmanOut__cdr_deserialize,
  _HtNavKalmanOut__get_serialized_size,
  _HtNavKalmanOut__max_serialized_size
};

static rosidl_message_type_support_t _HtNavKalmanOut__type_support = {
  rosidl_typesupport_fastrtps_c__identifier,
  &__callbacks_HtNavKalmanOut,
  get_message_typesupport_handle_function,
};

const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_fastrtps_c, ht_nav_variables, msg, HtNavKalmanOut)() {
  return &_HtNavKalmanOut__type_support;
}

#if defined(__cplusplus)
}
#endif
