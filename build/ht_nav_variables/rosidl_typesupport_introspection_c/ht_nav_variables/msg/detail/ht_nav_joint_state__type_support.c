// generated from rosidl_typesupport_introspection_c/resource/idl__type_support.c.em
// with input from ht_nav_variables:msg/HtNavJointState.idl
// generated code does not contain a copyright notice

#include <stddef.h>
#include "ht_nav_variables/msg/detail/ht_nav_joint_state__rosidl_typesupport_introspection_c.h"
#include "ht_nav_variables/msg/rosidl_typesupport_introspection_c__visibility_control.h"
#include "rosidl_typesupport_introspection_c/field_types.h"
#include "rosidl_typesupport_introspection_c/identifier.h"
#include "rosidl_typesupport_introspection_c/message_introspection.h"
#include "ht_nav_variables/msg/detail/ht_nav_joint_state__functions.h"
#include "ht_nav_variables/msg/detail/ht_nav_joint_state__struct.h"


// Include directives for member types
// Member `steering_angle`
// Member `wheel_rotation`
// Member `normal_force`
#include "ht_nav_variables/msg/ht_nav_wheel_vector.h"
// Member `steering_angle`
// Member `wheel_rotation`
// Member `normal_force`
#include "ht_nav_variables/msg/detail/ht_nav_wheel_vector__rosidl_typesupport_introspection_c.h"

#ifdef __cplusplus
extern "C"
{
#endif

void HtNavJointState__rosidl_typesupport_introspection_c__HtNavJointState_init_function(
  void * message_memory, enum rosidl_runtime_c__message_initialization _init)
{
  // TODO(karsten1987): initializers are not yet implemented for typesupport c
  // see https://github.com/ros2/ros2/issues/397
  (void) _init;
  ht_nav_variables__msg__HtNavJointState__init(message_memory);
}

void HtNavJointState__rosidl_typesupport_introspection_c__HtNavJointState_fini_function(void * message_memory)
{
  ht_nav_variables__msg__HtNavJointState__fini(message_memory);
}

static rosidl_typesupport_introspection_c__MessageMember HtNavJointState__rosidl_typesupport_introspection_c__HtNavJointState_message_member_array[4] = {
  {
    "time",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_DOUBLE,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(ht_nav_variables__msg__HtNavJointState, time),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL  // resize(index) function pointer
  },
  {
    "steering_angle",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_MESSAGE,  // type
    0,  // upper bound of string
    NULL,  // members of sub message (initialized later)
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(ht_nav_variables__msg__HtNavJointState, steering_angle),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL  // resize(index) function pointer
  },
  {
    "wheel_rotation",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_MESSAGE,  // type
    0,  // upper bound of string
    NULL,  // members of sub message (initialized later)
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(ht_nav_variables__msg__HtNavJointState, wheel_rotation),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL  // resize(index) function pointer
  },
  {
    "normal_force",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_MESSAGE,  // type
    0,  // upper bound of string
    NULL,  // members of sub message (initialized later)
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(ht_nav_variables__msg__HtNavJointState, normal_force),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL  // resize(index) function pointer
  }
};

static const rosidl_typesupport_introspection_c__MessageMembers HtNavJointState__rosidl_typesupport_introspection_c__HtNavJointState_message_members = {
  "ht_nav_variables__msg",  // message namespace
  "HtNavJointState",  // message name
  4,  // number of fields
  sizeof(ht_nav_variables__msg__HtNavJointState),
  HtNavJointState__rosidl_typesupport_introspection_c__HtNavJointState_message_member_array,  // message members
  HtNavJointState__rosidl_typesupport_introspection_c__HtNavJointState_init_function,  // function to initialize message memory (memory has to be allocated)
  HtNavJointState__rosidl_typesupport_introspection_c__HtNavJointState_fini_function  // function to terminate message instance (will not free memory)
};

// this is not const since it must be initialized on first access
// since C does not allow non-integral compile-time constants
static rosidl_message_type_support_t HtNavJointState__rosidl_typesupport_introspection_c__HtNavJointState_message_type_support_handle = {
  0,
  &HtNavJointState__rosidl_typesupport_introspection_c__HtNavJointState_message_members,
  get_message_typesupport_handle_function,
};

ROSIDL_TYPESUPPORT_INTROSPECTION_C_EXPORT_ht_nav_variables
const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, ht_nav_variables, msg, HtNavJointState)() {
  HtNavJointState__rosidl_typesupport_introspection_c__HtNavJointState_message_member_array[1].members_ =
    ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, ht_nav_variables, msg, HtNavWheelVector)();
  HtNavJointState__rosidl_typesupport_introspection_c__HtNavJointState_message_member_array[2].members_ =
    ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, ht_nav_variables, msg, HtNavWheelVector)();
  HtNavJointState__rosidl_typesupport_introspection_c__HtNavJointState_message_member_array[3].members_ =
    ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, ht_nav_variables, msg, HtNavWheelVector)();
  if (!HtNavJointState__rosidl_typesupport_introspection_c__HtNavJointState_message_type_support_handle.typesupport_identifier) {
    HtNavJointState__rosidl_typesupport_introspection_c__HtNavJointState_message_type_support_handle.typesupport_identifier =
      rosidl_typesupport_introspection_c__identifier;
  }
  return &HtNavJointState__rosidl_typesupport_introspection_c__HtNavJointState_message_type_support_handle;
}
#ifdef __cplusplus
}
#endif
