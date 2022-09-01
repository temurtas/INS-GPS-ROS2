// generated from rosidl_typesupport_fastrtps_c/resource/idl__type_support_c.cpp.em
// with input from ht_nav_variables:msg/HtNavContactStates.idl
// generated code does not contain a copyright notice
#include "ht_nav_variables/msg/detail/ht_nav_contact_states__rosidl_typesupport_fastrtps_c.h"


#include <cassert>
#include <limits>
#include <string>
#include "rosidl_typesupport_fastrtps_c/identifier.h"
#include "rosidl_typesupport_fastrtps_c/wstring_conversion.hpp"
#include "rosidl_typesupport_fastrtps_cpp/message_type_support.h"
#include "ht_nav_variables/msg/rosidl_typesupport_fastrtps_c__visibility_control.h"
#include "ht_nav_variables/msg/detail/ht_nav_contact_states__struct.h"
#include "ht_nav_variables/msg/detail/ht_nav_contact_states__functions.h"
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

#include "ht_nav_variables/msg/detail/ht_nav_contact_state__functions.h"  // fl_wheel_contact_states, fr_wheel_contact_states, rl_wheel_contact_states, rr_wheel_contact_states

// forward declare type support functions
size_t get_serialized_size_ht_nav_variables__msg__HtNavContactState(
  const void * untyped_ros_message,
  size_t current_alignment);

size_t max_serialized_size_ht_nav_variables__msg__HtNavContactState(
  bool & full_bounded,
  size_t current_alignment);

const rosidl_message_type_support_t *
  ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_fastrtps_c, ht_nav_variables, msg, HtNavContactState)();


using _HtNavContactStates__ros_msg_type = ht_nav_variables__msg__HtNavContactStates;

static bool _HtNavContactStates__cdr_serialize(
  const void * untyped_ros_message,
  eprosima::fastcdr::Cdr & cdr)
{
  if (!untyped_ros_message) {
    fprintf(stderr, "ros message handle is null\n");
    return false;
  }
  const _HtNavContactStates__ros_msg_type * ros_message = static_cast<const _HtNavContactStates__ros_msg_type *>(untyped_ros_message);
  // Field name: time
  {
    cdr << ros_message->time;
  }

  // Field name: fl_wheel_contact_states
  {
    const message_type_support_callbacks_t * callbacks =
      static_cast<const message_type_support_callbacks_t *>(
      ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(
        rosidl_typesupport_fastrtps_c, ht_nav_variables, msg, HtNavContactState
      )()->data);
    if (!callbacks->cdr_serialize(
        &ros_message->fl_wheel_contact_states, cdr))
    {
      return false;
    }
  }

  // Field name: fr_wheel_contact_states
  {
    const message_type_support_callbacks_t * callbacks =
      static_cast<const message_type_support_callbacks_t *>(
      ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(
        rosidl_typesupport_fastrtps_c, ht_nav_variables, msg, HtNavContactState
      )()->data);
    if (!callbacks->cdr_serialize(
        &ros_message->fr_wheel_contact_states, cdr))
    {
      return false;
    }
  }

  // Field name: rl_wheel_contact_states
  {
    const message_type_support_callbacks_t * callbacks =
      static_cast<const message_type_support_callbacks_t *>(
      ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(
        rosidl_typesupport_fastrtps_c, ht_nav_variables, msg, HtNavContactState
      )()->data);
    if (!callbacks->cdr_serialize(
        &ros_message->rl_wheel_contact_states, cdr))
    {
      return false;
    }
  }

  // Field name: rr_wheel_contact_states
  {
    const message_type_support_callbacks_t * callbacks =
      static_cast<const message_type_support_callbacks_t *>(
      ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(
        rosidl_typesupport_fastrtps_c, ht_nav_variables, msg, HtNavContactState
      )()->data);
    if (!callbacks->cdr_serialize(
        &ros_message->rr_wheel_contact_states, cdr))
    {
      return false;
    }
  }

  return true;
}

static bool _HtNavContactStates__cdr_deserialize(
  eprosima::fastcdr::Cdr & cdr,
  void * untyped_ros_message)
{
  if (!untyped_ros_message) {
    fprintf(stderr, "ros message handle is null\n");
    return false;
  }
  _HtNavContactStates__ros_msg_type * ros_message = static_cast<_HtNavContactStates__ros_msg_type *>(untyped_ros_message);
  // Field name: time
  {
    cdr >> ros_message->time;
  }

  // Field name: fl_wheel_contact_states
  {
    const message_type_support_callbacks_t * callbacks =
      static_cast<const message_type_support_callbacks_t *>(
      ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(
        rosidl_typesupport_fastrtps_c, ht_nav_variables, msg, HtNavContactState
      )()->data);
    if (!callbacks->cdr_deserialize(
        cdr, &ros_message->fl_wheel_contact_states))
    {
      return false;
    }
  }

  // Field name: fr_wheel_contact_states
  {
    const message_type_support_callbacks_t * callbacks =
      static_cast<const message_type_support_callbacks_t *>(
      ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(
        rosidl_typesupport_fastrtps_c, ht_nav_variables, msg, HtNavContactState
      )()->data);
    if (!callbacks->cdr_deserialize(
        cdr, &ros_message->fr_wheel_contact_states))
    {
      return false;
    }
  }

  // Field name: rl_wheel_contact_states
  {
    const message_type_support_callbacks_t * callbacks =
      static_cast<const message_type_support_callbacks_t *>(
      ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(
        rosidl_typesupport_fastrtps_c, ht_nav_variables, msg, HtNavContactState
      )()->data);
    if (!callbacks->cdr_deserialize(
        cdr, &ros_message->rl_wheel_contact_states))
    {
      return false;
    }
  }

  // Field name: rr_wheel_contact_states
  {
    const message_type_support_callbacks_t * callbacks =
      static_cast<const message_type_support_callbacks_t *>(
      ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(
        rosidl_typesupport_fastrtps_c, ht_nav_variables, msg, HtNavContactState
      )()->data);
    if (!callbacks->cdr_deserialize(
        cdr, &ros_message->rr_wheel_contact_states))
    {
      return false;
    }
  }

  return true;
}

ROSIDL_TYPESUPPORT_FASTRTPS_C_PUBLIC_ht_nav_variables
size_t get_serialized_size_ht_nav_variables__msg__HtNavContactStates(
  const void * untyped_ros_message,
  size_t current_alignment)
{
  const _HtNavContactStates__ros_msg_type * ros_message = static_cast<const _HtNavContactStates__ros_msg_type *>(untyped_ros_message);
  (void)ros_message;
  size_t initial_alignment = current_alignment;

  const size_t padding = 4;
  const size_t wchar_size = 4;
  (void)padding;
  (void)wchar_size;

  // field.name time
  {
    size_t item_size = sizeof(ros_message->time);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // field.name fl_wheel_contact_states

  current_alignment += get_serialized_size_ht_nav_variables__msg__HtNavContactState(
    &(ros_message->fl_wheel_contact_states), current_alignment);
  // field.name fr_wheel_contact_states

  current_alignment += get_serialized_size_ht_nav_variables__msg__HtNavContactState(
    &(ros_message->fr_wheel_contact_states), current_alignment);
  // field.name rl_wheel_contact_states

  current_alignment += get_serialized_size_ht_nav_variables__msg__HtNavContactState(
    &(ros_message->rl_wheel_contact_states), current_alignment);
  // field.name rr_wheel_contact_states

  current_alignment += get_serialized_size_ht_nav_variables__msg__HtNavContactState(
    &(ros_message->rr_wheel_contact_states), current_alignment);

  return current_alignment - initial_alignment;
}

static uint32_t _HtNavContactStates__get_serialized_size(const void * untyped_ros_message)
{
  return static_cast<uint32_t>(
    get_serialized_size_ht_nav_variables__msg__HtNavContactStates(
      untyped_ros_message, 0));
}

ROSIDL_TYPESUPPORT_FASTRTPS_C_PUBLIC_ht_nav_variables
size_t max_serialized_size_ht_nav_variables__msg__HtNavContactStates(
  bool & full_bounded,
  size_t current_alignment)
{
  size_t initial_alignment = current_alignment;

  const size_t padding = 4;
  const size_t wchar_size = 4;
  (void)padding;
  (void)wchar_size;
  (void)full_bounded;

  // member: time
  {
    size_t array_size = 1;

    current_alignment += array_size * sizeof(uint64_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint64_t));
  }
  // member: fl_wheel_contact_states
  {
    size_t array_size = 1;


    for (size_t index = 0; index < array_size; ++index) {
      current_alignment +=
        max_serialized_size_ht_nav_variables__msg__HtNavContactState(
        full_bounded, current_alignment);
    }
  }
  // member: fr_wheel_contact_states
  {
    size_t array_size = 1;


    for (size_t index = 0; index < array_size; ++index) {
      current_alignment +=
        max_serialized_size_ht_nav_variables__msg__HtNavContactState(
        full_bounded, current_alignment);
    }
  }
  // member: rl_wheel_contact_states
  {
    size_t array_size = 1;


    for (size_t index = 0; index < array_size; ++index) {
      current_alignment +=
        max_serialized_size_ht_nav_variables__msg__HtNavContactState(
        full_bounded, current_alignment);
    }
  }
  // member: rr_wheel_contact_states
  {
    size_t array_size = 1;


    for (size_t index = 0; index < array_size; ++index) {
      current_alignment +=
        max_serialized_size_ht_nav_variables__msg__HtNavContactState(
        full_bounded, current_alignment);
    }
  }

  return current_alignment - initial_alignment;
}

static size_t _HtNavContactStates__max_serialized_size(bool & full_bounded)
{
  return max_serialized_size_ht_nav_variables__msg__HtNavContactStates(
    full_bounded, 0);
}


static message_type_support_callbacks_t __callbacks_HtNavContactStates = {
  "ht_nav_variables::msg",
  "HtNavContactStates",
  _HtNavContactStates__cdr_serialize,
  _HtNavContactStates__cdr_deserialize,
  _HtNavContactStates__get_serialized_size,
  _HtNavContactStates__max_serialized_size
};

static rosidl_message_type_support_t _HtNavContactStates__type_support = {
  rosidl_typesupport_fastrtps_c__identifier,
  &__callbacks_HtNavContactStates,
  get_message_typesupport_handle_function,
};

const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_fastrtps_c, ht_nav_variables, msg, HtNavContactStates)() {
  return &_HtNavContactStates__type_support;
}

#if defined(__cplusplus)
}
#endif
