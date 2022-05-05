// generated from rosidl_typesupport_fastrtps_c/resource/idl__type_support_c.cpp.em
// with input from ht_nav_variables:msg/HtNavTireOut.idl
// generated code does not contain a copyright notice
#include "ht_nav_variables/msg/detail/ht_nav_tire_out__rosidl_typesupport_fastrtps_c.h"


#include <cassert>
#include <limits>
#include <string>
#include "rosidl_typesupport_fastrtps_c/identifier.h"
#include "rosidl_typesupport_fastrtps_c/wstring_conversion.hpp"
#include "rosidl_typesupport_fastrtps_cpp/message_type_support.h"
#include "ht_nav_variables/msg/rosidl_typesupport_fastrtps_c__visibility_control.h"
#include "ht_nav_variables/msg/detail/ht_nav_tire_out__struct.h"
#include "ht_nav_variables/msg/detail/ht_nav_tire_out__functions.h"
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

#include "ht_nav_variables/msg/detail/ht_nav_wheel_vector__functions.h"  // tire_lateral_forces, tire_longitudinal_forces, wheel_longitudinal_slip_ratio, wheel_side_slip_ang

// forward declare type support functions
size_t get_serialized_size_ht_nav_variables__msg__HtNavWheelVector(
  const void * untyped_ros_message,
  size_t current_alignment);

size_t max_serialized_size_ht_nav_variables__msg__HtNavWheelVector(
  bool & full_bounded,
  size_t current_alignment);

const rosidl_message_type_support_t *
  ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_fastrtps_c, ht_nav_variables, msg, HtNavWheelVector)();


using _HtNavTireOut__ros_msg_type = ht_nav_variables__msg__HtNavTireOut;

static bool _HtNavTireOut__cdr_serialize(
  const void * untyped_ros_message,
  eprosima::fastcdr::Cdr & cdr)
{
  if (!untyped_ros_message) {
    fprintf(stderr, "ros message handle is null\n");
    return false;
  }
  const _HtNavTireOut__ros_msg_type * ros_message = static_cast<const _HtNavTireOut__ros_msg_type *>(untyped_ros_message);
  // Field name: time
  {
    cdr << ros_message->time;
  }

  // Field name: effective_radius_est
  {
    cdr << ros_message->effective_radius_est;
  }

  // Field name: vehicle_mass_est
  {
    cdr << ros_message->vehicle_mass_est;
  }

  // Field name: wheel_side_slip_ang
  {
    const message_type_support_callbacks_t * callbacks =
      static_cast<const message_type_support_callbacks_t *>(
      ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(
        rosidl_typesupport_fastrtps_c, ht_nav_variables, msg, HtNavWheelVector
      )()->data);
    if (!callbacks->cdr_serialize(
        &ros_message->wheel_side_slip_ang, cdr))
    {
      return false;
    }
  }

  // Field name: wheel_longitudinal_slip_ratio
  {
    const message_type_support_callbacks_t * callbacks =
      static_cast<const message_type_support_callbacks_t *>(
      ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(
        rosidl_typesupport_fastrtps_c, ht_nav_variables, msg, HtNavWheelVector
      )()->data);
    if (!callbacks->cdr_serialize(
        &ros_message->wheel_longitudinal_slip_ratio, cdr))
    {
      return false;
    }
  }

  // Field name: tire_lateral_forces
  {
    const message_type_support_callbacks_t * callbacks =
      static_cast<const message_type_support_callbacks_t *>(
      ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(
        rosidl_typesupport_fastrtps_c, ht_nav_variables, msg, HtNavWheelVector
      )()->data);
    if (!callbacks->cdr_serialize(
        &ros_message->tire_lateral_forces, cdr))
    {
      return false;
    }
  }

  // Field name: tire_longitudinal_forces
  {
    const message_type_support_callbacks_t * callbacks =
      static_cast<const message_type_support_callbacks_t *>(
      ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(
        rosidl_typesupport_fastrtps_c, ht_nav_variables, msg, HtNavWheelVector
      )()->data);
    if (!callbacks->cdr_serialize(
        &ros_message->tire_longitudinal_forces, cdr))
    {
      return false;
    }
  }

  return true;
}

static bool _HtNavTireOut__cdr_deserialize(
  eprosima::fastcdr::Cdr & cdr,
  void * untyped_ros_message)
{
  if (!untyped_ros_message) {
    fprintf(stderr, "ros message handle is null\n");
    return false;
  }
  _HtNavTireOut__ros_msg_type * ros_message = static_cast<_HtNavTireOut__ros_msg_type *>(untyped_ros_message);
  // Field name: time
  {
    cdr >> ros_message->time;
  }

  // Field name: effective_radius_est
  {
    cdr >> ros_message->effective_radius_est;
  }

  // Field name: vehicle_mass_est
  {
    cdr >> ros_message->vehicle_mass_est;
  }

  // Field name: wheel_side_slip_ang
  {
    const message_type_support_callbacks_t * callbacks =
      static_cast<const message_type_support_callbacks_t *>(
      ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(
        rosidl_typesupport_fastrtps_c, ht_nav_variables, msg, HtNavWheelVector
      )()->data);
    if (!callbacks->cdr_deserialize(
        cdr, &ros_message->wheel_side_slip_ang))
    {
      return false;
    }
  }

  // Field name: wheel_longitudinal_slip_ratio
  {
    const message_type_support_callbacks_t * callbacks =
      static_cast<const message_type_support_callbacks_t *>(
      ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(
        rosidl_typesupport_fastrtps_c, ht_nav_variables, msg, HtNavWheelVector
      )()->data);
    if (!callbacks->cdr_deserialize(
        cdr, &ros_message->wheel_longitudinal_slip_ratio))
    {
      return false;
    }
  }

  // Field name: tire_lateral_forces
  {
    const message_type_support_callbacks_t * callbacks =
      static_cast<const message_type_support_callbacks_t *>(
      ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(
        rosidl_typesupport_fastrtps_c, ht_nav_variables, msg, HtNavWheelVector
      )()->data);
    if (!callbacks->cdr_deserialize(
        cdr, &ros_message->tire_lateral_forces))
    {
      return false;
    }
  }

  // Field name: tire_longitudinal_forces
  {
    const message_type_support_callbacks_t * callbacks =
      static_cast<const message_type_support_callbacks_t *>(
      ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(
        rosidl_typesupport_fastrtps_c, ht_nav_variables, msg, HtNavWheelVector
      )()->data);
    if (!callbacks->cdr_deserialize(
        cdr, &ros_message->tire_longitudinal_forces))
    {
      return false;
    }
  }

  return true;
}

ROSIDL_TYPESUPPORT_FASTRTPS_C_PUBLIC_ht_nav_variables
size_t get_serialized_size_ht_nav_variables__msg__HtNavTireOut(
  const void * untyped_ros_message,
  size_t current_alignment)
{
  const _HtNavTireOut__ros_msg_type * ros_message = static_cast<const _HtNavTireOut__ros_msg_type *>(untyped_ros_message);
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
  // field.name effective_radius_est
  {
    size_t item_size = sizeof(ros_message->effective_radius_est);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // field.name vehicle_mass_est
  {
    size_t item_size = sizeof(ros_message->vehicle_mass_est);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // field.name wheel_side_slip_ang

  current_alignment += get_serialized_size_ht_nav_variables__msg__HtNavWheelVector(
    &(ros_message->wheel_side_slip_ang), current_alignment);
  // field.name wheel_longitudinal_slip_ratio

  current_alignment += get_serialized_size_ht_nav_variables__msg__HtNavWheelVector(
    &(ros_message->wheel_longitudinal_slip_ratio), current_alignment);
  // field.name tire_lateral_forces

  current_alignment += get_serialized_size_ht_nav_variables__msg__HtNavWheelVector(
    &(ros_message->tire_lateral_forces), current_alignment);
  // field.name tire_longitudinal_forces

  current_alignment += get_serialized_size_ht_nav_variables__msg__HtNavWheelVector(
    &(ros_message->tire_longitudinal_forces), current_alignment);

  return current_alignment - initial_alignment;
}

static uint32_t _HtNavTireOut__get_serialized_size(const void * untyped_ros_message)
{
  return static_cast<uint32_t>(
    get_serialized_size_ht_nav_variables__msg__HtNavTireOut(
      untyped_ros_message, 0));
}

ROSIDL_TYPESUPPORT_FASTRTPS_C_PUBLIC_ht_nav_variables
size_t max_serialized_size_ht_nav_variables__msg__HtNavTireOut(
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
  // member: effective_radius_est
  {
    size_t array_size = 1;

    current_alignment += array_size * sizeof(uint64_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint64_t));
  }
  // member: vehicle_mass_est
  {
    size_t array_size = 1;

    current_alignment += array_size * sizeof(uint64_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint64_t));
  }
  // member: wheel_side_slip_ang
  {
    size_t array_size = 1;


    for (size_t index = 0; index < array_size; ++index) {
      current_alignment +=
        max_serialized_size_ht_nav_variables__msg__HtNavWheelVector(
        full_bounded, current_alignment);
    }
  }
  // member: wheel_longitudinal_slip_ratio
  {
    size_t array_size = 1;


    for (size_t index = 0; index < array_size; ++index) {
      current_alignment +=
        max_serialized_size_ht_nav_variables__msg__HtNavWheelVector(
        full_bounded, current_alignment);
    }
  }
  // member: tire_lateral_forces
  {
    size_t array_size = 1;


    for (size_t index = 0; index < array_size; ++index) {
      current_alignment +=
        max_serialized_size_ht_nav_variables__msg__HtNavWheelVector(
        full_bounded, current_alignment);
    }
  }
  // member: tire_longitudinal_forces
  {
    size_t array_size = 1;


    for (size_t index = 0; index < array_size; ++index) {
      current_alignment +=
        max_serialized_size_ht_nav_variables__msg__HtNavWheelVector(
        full_bounded, current_alignment);
    }
  }

  return current_alignment - initial_alignment;
}

static size_t _HtNavTireOut__max_serialized_size(bool & full_bounded)
{
  return max_serialized_size_ht_nav_variables__msg__HtNavTireOut(
    full_bounded, 0);
}


static message_type_support_callbacks_t __callbacks_HtNavTireOut = {
  "ht_nav_variables::msg",
  "HtNavTireOut",
  _HtNavTireOut__cdr_serialize,
  _HtNavTireOut__cdr_deserialize,
  _HtNavTireOut__get_serialized_size,
  _HtNavTireOut__max_serialized_size
};

static rosidl_message_type_support_t _HtNavTireOut__type_support = {
  rosidl_typesupport_fastrtps_c__identifier,
  &__callbacks_HtNavTireOut,
  get_message_typesupport_handle_function,
};

const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_fastrtps_c, ht_nav_variables, msg, HtNavTireOut)() {
  return &_HtNavTireOut__type_support;
}

#if defined(__cplusplus)
}
#endif
