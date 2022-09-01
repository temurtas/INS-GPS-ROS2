// generated from rosidl_typesupport_introspection_c/resource/idl__type_support.c.em
// with input from ht_nav_variables:msg/HtNavContactStates.idl
// generated code does not contain a copyright notice

#include <stddef.h>
#include "ht_nav_variables/msg/detail/ht_nav_contact_states__rosidl_typesupport_introspection_c.h"
#include "ht_nav_variables/msg/rosidl_typesupport_introspection_c__visibility_control.h"
#include "rosidl_typesupport_introspection_c/field_types.h"
#include "rosidl_typesupport_introspection_c/identifier.h"
#include "rosidl_typesupport_introspection_c/message_introspection.h"
#include "ht_nav_variables/msg/detail/ht_nav_contact_states__functions.h"
#include "ht_nav_variables/msg/detail/ht_nav_contact_states__struct.h"


// Include directives for member types
// Member `fl_wheel_contact_states`
// Member `fr_wheel_contact_states`
// Member `rl_wheel_contact_states`
// Member `rr_wheel_contact_states`
#include "ht_nav_variables/msg/ht_nav_contact_state.h"
// Member `fl_wheel_contact_states`
// Member `fr_wheel_contact_states`
// Member `rl_wheel_contact_states`
// Member `rr_wheel_contact_states`
#include "ht_nav_variables/msg/detail/ht_nav_contact_state__rosidl_typesupport_introspection_c.h"

#ifdef __cplusplus
extern "C"
{
#endif

void HtNavContactStates__rosidl_typesupport_introspection_c__HtNavContactStates_init_function(
  void * message_memory, enum rosidl_runtime_c__message_initialization _init)
{
  // TODO(karsten1987): initializers are not yet implemented for typesupport c
  // see https://github.com/ros2/ros2/issues/397
  (void) _init;
  ht_nav_variables__msg__HtNavContactStates__init(message_memory);
}

void HtNavContactStates__rosidl_typesupport_introspection_c__HtNavContactStates_fini_function(void * message_memory)
{
  ht_nav_variables__msg__HtNavContactStates__fini(message_memory);
}

static rosidl_typesupport_introspection_c__MessageMember HtNavContactStates__rosidl_typesupport_introspection_c__HtNavContactStates_message_member_array[5] = {
  {
    "time",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_DOUBLE,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(ht_nav_variables__msg__HtNavContactStates, time),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL  // resize(index) function pointer
  },
  {
    "fl_wheel_contact_states",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_MESSAGE,  // type
    0,  // upper bound of string
    NULL,  // members of sub message (initialized later)
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(ht_nav_variables__msg__HtNavContactStates, fl_wheel_contact_states),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL  // resize(index) function pointer
  },
  {
    "fr_wheel_contact_states",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_MESSAGE,  // type
    0,  // upper bound of string
    NULL,  // members of sub message (initialized later)
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(ht_nav_variables__msg__HtNavContactStates, fr_wheel_contact_states),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL  // resize(index) function pointer
  },
  {
    "rl_wheel_contact_states",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_MESSAGE,  // type
    0,  // upper bound of string
    NULL,  // members of sub message (initialized later)
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(ht_nav_variables__msg__HtNavContactStates, rl_wheel_contact_states),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL  // resize(index) function pointer
  },
  {
    "rr_wheel_contact_states",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_MESSAGE,  // type
    0,  // upper bound of string
    NULL,  // members of sub message (initialized later)
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(ht_nav_variables__msg__HtNavContactStates, rr_wheel_contact_states),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL  // resize(index) function pointer
  }
};

static const rosidl_typesupport_introspection_c__MessageMembers HtNavContactStates__rosidl_typesupport_introspection_c__HtNavContactStates_message_members = {
  "ht_nav_variables__msg",  // message namespace
  "HtNavContactStates",  // message name
  5,  // number of fields
  sizeof(ht_nav_variables__msg__HtNavContactStates),
  HtNavContactStates__rosidl_typesupport_introspection_c__HtNavContactStates_message_member_array,  // message members
  HtNavContactStates__rosidl_typesupport_introspection_c__HtNavContactStates_init_function,  // function to initialize message memory (memory has to be allocated)
  HtNavContactStates__rosidl_typesupport_introspection_c__HtNavContactStates_fini_function  // function to terminate message instance (will not free memory)
};

// this is not const since it must be initialized on first access
// since C does not allow non-integral compile-time constants
static rosidl_message_type_support_t HtNavContactStates__rosidl_typesupport_introspection_c__HtNavContactStates_message_type_support_handle = {
  0,
  &HtNavContactStates__rosidl_typesupport_introspection_c__HtNavContactStates_message_members,
  get_message_typesupport_handle_function,
};

ROSIDL_TYPESUPPORT_INTROSPECTION_C_EXPORT_ht_nav_variables
const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, ht_nav_variables, msg, HtNavContactStates)() {
  HtNavContactStates__rosidl_typesupport_introspection_c__HtNavContactStates_message_member_array[1].members_ =
    ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, ht_nav_variables, msg, HtNavContactState)();
  HtNavContactStates__rosidl_typesupport_introspection_c__HtNavContactStates_message_member_array[2].members_ =
    ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, ht_nav_variables, msg, HtNavContactState)();
  HtNavContactStates__rosidl_typesupport_introspection_c__HtNavContactStates_message_member_array[3].members_ =
    ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, ht_nav_variables, msg, HtNavContactState)();
  HtNavContactStates__rosidl_typesupport_introspection_c__HtNavContactStates_message_member_array[4].members_ =
    ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, ht_nav_variables, msg, HtNavContactState)();
  if (!HtNavContactStates__rosidl_typesupport_introspection_c__HtNavContactStates_message_type_support_handle.typesupport_identifier) {
    HtNavContactStates__rosidl_typesupport_introspection_c__HtNavContactStates_message_type_support_handle.typesupport_identifier =
      rosidl_typesupport_introspection_c__identifier;
  }
  return &HtNavContactStates__rosidl_typesupport_introspection_c__HtNavContactStates_message_type_support_handle;
}
#ifdef __cplusplus
}
#endif
