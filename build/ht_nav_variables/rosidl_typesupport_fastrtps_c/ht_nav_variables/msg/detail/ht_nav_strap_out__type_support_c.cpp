// generated from rosidl_typesupport_fastrtps_c/resource/idl__type_support_c.cpp.em
// with input from ht_nav_variables:msg/HtNavStrapOut.idl
// generated code does not contain a copyright notice
#include "ht_nav_variables/msg/detail/ht_nav_strap_out__rosidl_typesupport_fastrtps_c.h"


#include <cassert>
#include <limits>
#include <string>
#include "rosidl_typesupport_fastrtps_c/identifier.h"
#include "rosidl_typesupport_fastrtps_c/wstring_conversion.hpp"
#include "rosidl_typesupport_fastrtps_cpp/message_type_support.h"
#include "ht_nav_variables/msg/rosidl_typesupport_fastrtps_c__visibility_control.h"
#include "ht_nav_variables/msg/detail/ht_nav_strap_out__struct.h"
#include "ht_nav_variables/msg/detail/ht_nav_strap_out__functions.h"
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

#include "ht_nav_variables/msg/detail/ht_nav_euler__functions.h"  // euler
#include "ht_nav_variables/msg/detail/ht_nav_quaternion__functions.h"  // quaternion
#include "ht_nav_variables/msg/detail/ht_nav_vector3__functions.h"  // pos, vel

// forward declare type support functions
size_t get_serialized_size_ht_nav_variables__msg__HtNavEuler(
  const void * untyped_ros_message,
  size_t current_alignment);

size_t max_serialized_size_ht_nav_variables__msg__HtNavEuler(
  bool & full_bounded,
  size_t current_alignment);

const rosidl_message_type_support_t *
  ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_fastrtps_c, ht_nav_variables, msg, HtNavEuler)();
size_t get_serialized_size_ht_nav_variables__msg__HtNavQuaternion(
  const void * untyped_ros_message,
  size_t current_alignment);

size_t max_serialized_size_ht_nav_variables__msg__HtNavQuaternion(
  bool & full_bounded,
  size_t current_alignment);

const rosidl_message_type_support_t *
  ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_fastrtps_c, ht_nav_variables, msg, HtNavQuaternion)();
size_t get_serialized_size_ht_nav_variables__msg__HtNavVector3(
  const void * untyped_ros_message,
  size_t current_alignment);

size_t max_serialized_size_ht_nav_variables__msg__HtNavVector3(
  bool & full_bounded,
  size_t current_alignment);

const rosidl_message_type_support_t *
  ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_fastrtps_c, ht_nav_variables, msg, HtNavVector3)();


using _HtNavStrapOut__ros_msg_type = ht_nav_variables__msg__HtNavStrapOut;

static bool _HtNavStrapOut__cdr_serialize(
  const void * untyped_ros_message,
  eprosima::fastcdr::Cdr & cdr)
{
  if (!untyped_ros_message) {
    fprintf(stderr, "ros message handle is null\n");
    return false;
  }
  const _HtNavStrapOut__ros_msg_type * ros_message = static_cast<const _HtNavStrapOut__ros_msg_type *>(untyped_ros_message);
  // Field name: pos
  {
    const message_type_support_callbacks_t * callbacks =
      static_cast<const message_type_support_callbacks_t *>(
      ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(
        rosidl_typesupport_fastrtps_c, ht_nav_variables, msg, HtNavVector3
      )()->data);
    if (!callbacks->cdr_serialize(
        &ros_message->pos, cdr))
    {
      return false;
    }
  }

  // Field name: vel
  {
    const message_type_support_callbacks_t * callbacks =
      static_cast<const message_type_support_callbacks_t *>(
      ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(
        rosidl_typesupport_fastrtps_c, ht_nav_variables, msg, HtNavVector3
      )()->data);
    if (!callbacks->cdr_serialize(
        &ros_message->vel, cdr))
    {
      return false;
    }
  }

  // Field name: euler
  {
    const message_type_support_callbacks_t * callbacks =
      static_cast<const message_type_support_callbacks_t *>(
      ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(
        rosidl_typesupport_fastrtps_c, ht_nav_variables, msg, HtNavEuler
      )()->data);
    if (!callbacks->cdr_serialize(
        &ros_message->euler, cdr))
    {
      return false;
    }
  }

  // Field name: quaternion
  {
    const message_type_support_callbacks_t * callbacks =
      static_cast<const message_type_support_callbacks_t *>(
      ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(
        rosidl_typesupport_fastrtps_c, ht_nav_variables, msg, HtNavQuaternion
      )()->data);
    if (!callbacks->cdr_serialize(
        &ros_message->quaternion, cdr))
    {
      return false;
    }
  }

  return true;
}

static bool _HtNavStrapOut__cdr_deserialize(
  eprosima::fastcdr::Cdr & cdr,
  void * untyped_ros_message)
{
  if (!untyped_ros_message) {
    fprintf(stderr, "ros message handle is null\n");
    return false;
  }
  _HtNavStrapOut__ros_msg_type * ros_message = static_cast<_HtNavStrapOut__ros_msg_type *>(untyped_ros_message);
  // Field name: pos
  {
    const message_type_support_callbacks_t * callbacks =
      static_cast<const message_type_support_callbacks_t *>(
      ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(
        rosidl_typesupport_fastrtps_c, ht_nav_variables, msg, HtNavVector3
      )()->data);
    if (!callbacks->cdr_deserialize(
        cdr, &ros_message->pos))
    {
      return false;
    }
  }

  // Field name: vel
  {
    const message_type_support_callbacks_t * callbacks =
      static_cast<const message_type_support_callbacks_t *>(
      ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(
        rosidl_typesupport_fastrtps_c, ht_nav_variables, msg, HtNavVector3
      )()->data);
    if (!callbacks->cdr_deserialize(
        cdr, &ros_message->vel))
    {
      return false;
    }
  }

  // Field name: euler
  {
    const message_type_support_callbacks_t * callbacks =
      static_cast<const message_type_support_callbacks_t *>(
      ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(
        rosidl_typesupport_fastrtps_c, ht_nav_variables, msg, HtNavEuler
      )()->data);
    if (!callbacks->cdr_deserialize(
        cdr, &ros_message->euler))
    {
      return false;
    }
  }

  // Field name: quaternion
  {
    const message_type_support_callbacks_t * callbacks =
      static_cast<const message_type_support_callbacks_t *>(
      ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(
        rosidl_typesupport_fastrtps_c, ht_nav_variables, msg, HtNavQuaternion
      )()->data);
    if (!callbacks->cdr_deserialize(
        cdr, &ros_message->quaternion))
    {
      return false;
    }
  }

  return true;
}

ROSIDL_TYPESUPPORT_FASTRTPS_C_PUBLIC_ht_nav_variables
size_t get_serialized_size_ht_nav_variables__msg__HtNavStrapOut(
  const void * untyped_ros_message,
  size_t current_alignment)
{
  const _HtNavStrapOut__ros_msg_type * ros_message = static_cast<const _HtNavStrapOut__ros_msg_type *>(untyped_ros_message);
  (void)ros_message;
  size_t initial_alignment = current_alignment;

  const size_t padding = 4;
  const size_t wchar_size = 4;
  (void)padding;
  (void)wchar_size;

  // field.name pos

  current_alignment += get_serialized_size_ht_nav_variables__msg__HtNavVector3(
    &(ros_message->pos), current_alignment);
  // field.name vel

  current_alignment += get_serialized_size_ht_nav_variables__msg__HtNavVector3(
    &(ros_message->vel), current_alignment);
  // field.name euler

  current_alignment += get_serialized_size_ht_nav_variables__msg__HtNavEuler(
    &(ros_message->euler), current_alignment);
  // field.name quaternion

  current_alignment += get_serialized_size_ht_nav_variables__msg__HtNavQuaternion(
    &(ros_message->quaternion), current_alignment);

  return current_alignment - initial_alignment;
}

static uint32_t _HtNavStrapOut__get_serialized_size(const void * untyped_ros_message)
{
  return static_cast<uint32_t>(
    get_serialized_size_ht_nav_variables__msg__HtNavStrapOut(
      untyped_ros_message, 0));
}

ROSIDL_TYPESUPPORT_FASTRTPS_C_PUBLIC_ht_nav_variables
size_t max_serialized_size_ht_nav_variables__msg__HtNavStrapOut(
  bool & full_bounded,
  size_t current_alignment)
{
  size_t initial_alignment = current_alignment;

  const size_t padding = 4;
  const size_t wchar_size = 4;
  (void)padding;
  (void)wchar_size;
  (void)full_bounded;

  // member: pos
  {
    size_t array_size = 1;


    for (size_t index = 0; index < array_size; ++index) {
      current_alignment +=
        max_serialized_size_ht_nav_variables__msg__HtNavVector3(
        full_bounded, current_alignment);
    }
  }
  // member: vel
  {
    size_t array_size = 1;


    for (size_t index = 0; index < array_size; ++index) {
      current_alignment +=
        max_serialized_size_ht_nav_variables__msg__HtNavVector3(
        full_bounded, current_alignment);
    }
  }
  // member: euler
  {
    size_t array_size = 1;


    for (size_t index = 0; index < array_size; ++index) {
      current_alignment +=
        max_serialized_size_ht_nav_variables__msg__HtNavEuler(
        full_bounded, current_alignment);
    }
  }
  // member: quaternion
  {
    size_t array_size = 1;


    for (size_t index = 0; index < array_size; ++index) {
      current_alignment +=
        max_serialized_size_ht_nav_variables__msg__HtNavQuaternion(
        full_bounded, current_alignment);
    }
  }

  return current_alignment - initial_alignment;
}

static size_t _HtNavStrapOut__max_serialized_size(bool & full_bounded)
{
  return max_serialized_size_ht_nav_variables__msg__HtNavStrapOut(
    full_bounded, 0);
}


static message_type_support_callbacks_t __callbacks_HtNavStrapOut = {
  "ht_nav_variables::msg",
  "HtNavStrapOut",
  _HtNavStrapOut__cdr_serialize,
  _HtNavStrapOut__cdr_deserialize,
  _HtNavStrapOut__get_serialized_size,
  _HtNavStrapOut__max_serialized_size
};

static rosidl_message_type_support_t _HtNavStrapOut__type_support = {
  rosidl_typesupport_fastrtps_c__identifier,
  &__callbacks_HtNavStrapOut,
  get_message_typesupport_handle_function,
};

const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_fastrtps_c, ht_nav_variables, msg, HtNavStrapOut)() {
  return &_HtNavStrapOut__type_support;
}

#if defined(__cplusplus)
}
#endif
