// generated from rosidl_typesupport_introspection_c/resource/idl__type_support.c.em
// with input from ht_nav_variables:msg/HtNavKalmanOut.idl
// generated code does not contain a copyright notice

#include <stddef.h>
#include "ht_nav_variables/msg/detail/ht_nav_kalman_out__rosidl_typesupport_introspection_c.h"
#include "ht_nav_variables/msg/rosidl_typesupport_introspection_c__visibility_control.h"
#include "rosidl_typesupport_introspection_c/field_types.h"
#include "rosidl_typesupport_introspection_c/identifier.h"
#include "rosidl_typesupport_introspection_c/message_introspection.h"
#include "ht_nav_variables/msg/detail/ht_nav_kalman_out__functions.h"
#include "ht_nav_variables/msg/detail/ht_nav_kalman_out__struct.h"


// Include directives for member types
// Member `pos_err`
// Member `vel_err`
// Member `att_err`
// Member `bias`
// Member `drift`
#include "ht_nav_variables/msg/ht_nav_error_vector.h"
// Member `pos_err`
// Member `vel_err`
// Member `att_err`
// Member `bias`
// Member `drift`
#include "ht_nav_variables/msg/detail/ht_nav_error_vector__rosidl_typesupport_introspection_c.h"

#ifdef __cplusplus
extern "C"
{
#endif

void HtNavKalmanOut__rosidl_typesupport_introspection_c__HtNavKalmanOut_init_function(
  void * message_memory, enum rosidl_runtime_c__message_initialization _init)
{
  // TODO(karsten1987): initializers are not yet implemented for typesupport c
  // see https://github.com/ros2/ros2/issues/397
  (void) _init;
  ht_nav_variables__msg__HtNavKalmanOut__init(message_memory);
}

void HtNavKalmanOut__rosidl_typesupport_introspection_c__HtNavKalmanOut_fini_function(void * message_memory)
{
  ht_nav_variables__msg__HtNavKalmanOut__fini(message_memory);
}

static rosidl_typesupport_introspection_c__MessageMember HtNavKalmanOut__rosidl_typesupport_introspection_c__HtNavKalmanOut_message_member_array[6] = {
  {
    "time",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_DOUBLE,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(ht_nav_variables__msg__HtNavKalmanOut, time),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL  // resize(index) function pointer
  },
  {
    "pos_err",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_MESSAGE,  // type
    0,  // upper bound of string
    NULL,  // members of sub message (initialized later)
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(ht_nav_variables__msg__HtNavKalmanOut, pos_err),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL  // resize(index) function pointer
  },
  {
    "vel_err",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_MESSAGE,  // type
    0,  // upper bound of string
    NULL,  // members of sub message (initialized later)
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(ht_nav_variables__msg__HtNavKalmanOut, vel_err),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL  // resize(index) function pointer
  },
  {
    "att_err",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_MESSAGE,  // type
    0,  // upper bound of string
    NULL,  // members of sub message (initialized later)
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(ht_nav_variables__msg__HtNavKalmanOut, att_err),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL  // resize(index) function pointer
  },
  {
    "bias",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_MESSAGE,  // type
    0,  // upper bound of string
    NULL,  // members of sub message (initialized later)
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(ht_nav_variables__msg__HtNavKalmanOut, bias),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL  // resize(index) function pointer
  },
  {
    "drift",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_MESSAGE,  // type
    0,  // upper bound of string
    NULL,  // members of sub message (initialized later)
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(ht_nav_variables__msg__HtNavKalmanOut, drift),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL  // resize(index) function pointer
  }
};

static const rosidl_typesupport_introspection_c__MessageMembers HtNavKalmanOut__rosidl_typesupport_introspection_c__HtNavKalmanOut_message_members = {
  "ht_nav_variables__msg",  // message namespace
  "HtNavKalmanOut",  // message name
  6,  // number of fields
  sizeof(ht_nav_variables__msg__HtNavKalmanOut),
  HtNavKalmanOut__rosidl_typesupport_introspection_c__HtNavKalmanOut_message_member_array,  // message members
  HtNavKalmanOut__rosidl_typesupport_introspection_c__HtNavKalmanOut_init_function,  // function to initialize message memory (memory has to be allocated)
  HtNavKalmanOut__rosidl_typesupport_introspection_c__HtNavKalmanOut_fini_function  // function to terminate message instance (will not free memory)
};

// this is not const since it must be initialized on first access
// since C does not allow non-integral compile-time constants
static rosidl_message_type_support_t HtNavKalmanOut__rosidl_typesupport_introspection_c__HtNavKalmanOut_message_type_support_handle = {
  0,
  &HtNavKalmanOut__rosidl_typesupport_introspection_c__HtNavKalmanOut_message_members,
  get_message_typesupport_handle_function,
};

ROSIDL_TYPESUPPORT_INTROSPECTION_C_EXPORT_ht_nav_variables
const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, ht_nav_variables, msg, HtNavKalmanOut)() {
  HtNavKalmanOut__rosidl_typesupport_introspection_c__HtNavKalmanOut_message_member_array[1].members_ =
    ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, ht_nav_variables, msg, HtNavErrorVector)();
  HtNavKalmanOut__rosidl_typesupport_introspection_c__HtNavKalmanOut_message_member_array[2].members_ =
    ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, ht_nav_variables, msg, HtNavErrorVector)();
  HtNavKalmanOut__rosidl_typesupport_introspection_c__HtNavKalmanOut_message_member_array[3].members_ =
    ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, ht_nav_variables, msg, HtNavErrorVector)();
  HtNavKalmanOut__rosidl_typesupport_introspection_c__HtNavKalmanOut_message_member_array[4].members_ =
    ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, ht_nav_variables, msg, HtNavErrorVector)();
  HtNavKalmanOut__rosidl_typesupport_introspection_c__HtNavKalmanOut_message_member_array[5].members_ =
    ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, ht_nav_variables, msg, HtNavErrorVector)();
  if (!HtNavKalmanOut__rosidl_typesupport_introspection_c__HtNavKalmanOut_message_type_support_handle.typesupport_identifier) {
    HtNavKalmanOut__rosidl_typesupport_introspection_c__HtNavKalmanOut_message_type_support_handle.typesupport_identifier =
      rosidl_typesupport_introspection_c__identifier;
  }
  return &HtNavKalmanOut__rosidl_typesupport_introspection_c__HtNavKalmanOut_message_type_support_handle;
}
#ifdef __cplusplus
}
#endif
