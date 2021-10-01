// generated from rosidl_typesupport_introspection_c/resource/idl__type_support.c.em
// with input from ht_nav_variables:msg/HtNavQuaternion.idl
// generated code does not contain a copyright notice

#include <stddef.h>
#include "ht_nav_variables/msg/detail/ht_nav_quaternion__rosidl_typesupport_introspection_c.h"
#include "ht_nav_variables/msg/rosidl_typesupport_introspection_c__visibility_control.h"
#include "rosidl_typesupport_introspection_c/field_types.h"
#include "rosidl_typesupport_introspection_c/identifier.h"
#include "rosidl_typesupport_introspection_c/message_introspection.h"
#include "ht_nav_variables/msg/detail/ht_nav_quaternion__functions.h"
#include "ht_nav_variables/msg/detail/ht_nav_quaternion__struct.h"


#ifdef __cplusplus
extern "C"
{
#endif

void HtNavQuaternion__rosidl_typesupport_introspection_c__HtNavQuaternion_init_function(
  void * message_memory, enum rosidl_runtime_c__message_initialization _init)
{
  // TODO(karsten1987): initializers are not yet implemented for typesupport c
  // see https://github.com/ros2/ros2/issues/397
  (void) _init;
  ht_nav_variables__msg__HtNavQuaternion__init(message_memory);
}

void HtNavQuaternion__rosidl_typesupport_introspection_c__HtNavQuaternion_fini_function(void * message_memory)
{
  ht_nav_variables__msg__HtNavQuaternion__fini(message_memory);
}

static rosidl_typesupport_introspection_c__MessageMember HtNavQuaternion__rosidl_typesupport_introspection_c__HtNavQuaternion_message_member_array[4] = {
  {
    "x",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_DOUBLE,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(ht_nav_variables__msg__HtNavQuaternion, x),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL  // resize(index) function pointer
  },
  {
    "y",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_DOUBLE,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(ht_nav_variables__msg__HtNavQuaternion, y),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL  // resize(index) function pointer
  },
  {
    "z",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_DOUBLE,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(ht_nav_variables__msg__HtNavQuaternion, z),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL  // resize(index) function pointer
  },
  {
    "w",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_DOUBLE,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(ht_nav_variables__msg__HtNavQuaternion, w),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL  // resize(index) function pointer
  }
};

static const rosidl_typesupport_introspection_c__MessageMembers HtNavQuaternion__rosidl_typesupport_introspection_c__HtNavQuaternion_message_members = {
  "ht_nav_variables__msg",  // message namespace
  "HtNavQuaternion",  // message name
  4,  // number of fields
  sizeof(ht_nav_variables__msg__HtNavQuaternion),
  HtNavQuaternion__rosidl_typesupport_introspection_c__HtNavQuaternion_message_member_array,  // message members
  HtNavQuaternion__rosidl_typesupport_introspection_c__HtNavQuaternion_init_function,  // function to initialize message memory (memory has to be allocated)
  HtNavQuaternion__rosidl_typesupport_introspection_c__HtNavQuaternion_fini_function  // function to terminate message instance (will not free memory)
};

// this is not const since it must be initialized on first access
// since C does not allow non-integral compile-time constants
static rosidl_message_type_support_t HtNavQuaternion__rosidl_typesupport_introspection_c__HtNavQuaternion_message_type_support_handle = {
  0,
  &HtNavQuaternion__rosidl_typesupport_introspection_c__HtNavQuaternion_message_members,
  get_message_typesupport_handle_function,
};

ROSIDL_TYPESUPPORT_INTROSPECTION_C_EXPORT_ht_nav_variables
const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, ht_nav_variables, msg, HtNavQuaternion)() {
  if (!HtNavQuaternion__rosidl_typesupport_introspection_c__HtNavQuaternion_message_type_support_handle.typesupport_identifier) {
    HtNavQuaternion__rosidl_typesupport_introspection_c__HtNavQuaternion_message_type_support_handle.typesupport_identifier =
      rosidl_typesupport_introspection_c__identifier;
  }
  return &HtNavQuaternion__rosidl_typesupport_introspection_c__HtNavQuaternion_message_type_support_handle;
}
#ifdef __cplusplus
}
#endif
