// generated from rosidl_typesupport_introspection_c/resource/idl__type_support.c.em
// with input from ht_nav_variables:msg/HtNavWheelVector.idl
// generated code does not contain a copyright notice

#include <stddef.h>
#include "ht_nav_variables/msg/detail/ht_nav_wheel_vector__rosidl_typesupport_introspection_c.h"
#include "ht_nav_variables/msg/rosidl_typesupport_introspection_c__visibility_control.h"
#include "rosidl_typesupport_introspection_c/field_types.h"
#include "rosidl_typesupport_introspection_c/identifier.h"
#include "rosidl_typesupport_introspection_c/message_introspection.h"
#include "ht_nav_variables/msg/detail/ht_nav_wheel_vector__functions.h"
#include "ht_nav_variables/msg/detail/ht_nav_wheel_vector__struct.h"


#ifdef __cplusplus
extern "C"
{
#endif

void HtNavWheelVector__rosidl_typesupport_introspection_c__HtNavWheelVector_init_function(
  void * message_memory, enum rosidl_runtime_c__message_initialization _init)
{
  // TODO(karsten1987): initializers are not yet implemented for typesupport c
  // see https://github.com/ros2/ros2/issues/397
  (void) _init;
  ht_nav_variables__msg__HtNavWheelVector__init(message_memory);
}

void HtNavWheelVector__rosidl_typesupport_introspection_c__HtNavWheelVector_fini_function(void * message_memory)
{
  ht_nav_variables__msg__HtNavWheelVector__fini(message_memory);
}

static rosidl_typesupport_introspection_c__MessageMember HtNavWheelVector__rosidl_typesupport_introspection_c__HtNavWheelVector_message_member_array[4] = {
  {
    "w1",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_DOUBLE,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(ht_nav_variables__msg__HtNavWheelVector, w1),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL  // resize(index) function pointer
  },
  {
    "w2",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_DOUBLE,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(ht_nav_variables__msg__HtNavWheelVector, w2),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL  // resize(index) function pointer
  },
  {
    "w3",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_DOUBLE,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(ht_nav_variables__msg__HtNavWheelVector, w3),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL  // resize(index) function pointer
  },
  {
    "w4",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_DOUBLE,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(ht_nav_variables__msg__HtNavWheelVector, w4),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL  // resize(index) function pointer
  }
};

static const rosidl_typesupport_introspection_c__MessageMembers HtNavWheelVector__rosidl_typesupport_introspection_c__HtNavWheelVector_message_members = {
  "ht_nav_variables__msg",  // message namespace
  "HtNavWheelVector",  // message name
  4,  // number of fields
  sizeof(ht_nav_variables__msg__HtNavWheelVector),
  HtNavWheelVector__rosidl_typesupport_introspection_c__HtNavWheelVector_message_member_array,  // message members
  HtNavWheelVector__rosidl_typesupport_introspection_c__HtNavWheelVector_init_function,  // function to initialize message memory (memory has to be allocated)
  HtNavWheelVector__rosidl_typesupport_introspection_c__HtNavWheelVector_fini_function  // function to terminate message instance (will not free memory)
};

// this is not const since it must be initialized on first access
// since C does not allow non-integral compile-time constants
static rosidl_message_type_support_t HtNavWheelVector__rosidl_typesupport_introspection_c__HtNavWheelVector_message_type_support_handle = {
  0,
  &HtNavWheelVector__rosidl_typesupport_introspection_c__HtNavWheelVector_message_members,
  get_message_typesupport_handle_function,
};

ROSIDL_TYPESUPPORT_INTROSPECTION_C_EXPORT_ht_nav_variables
const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, ht_nav_variables, msg, HtNavWheelVector)() {
  if (!HtNavWheelVector__rosidl_typesupport_introspection_c__HtNavWheelVector_message_type_support_handle.typesupport_identifier) {
    HtNavWheelVector__rosidl_typesupport_introspection_c__HtNavWheelVector_message_type_support_handle.typesupport_identifier =
      rosidl_typesupport_introspection_c__identifier;
  }
  return &HtNavWheelVector__rosidl_typesupport_introspection_c__HtNavWheelVector_message_type_support_handle;
}
#ifdef __cplusplus
}
#endif
