// generated from rosidl_typesupport_introspection_c/resource/idl__type_support.c.em
// with input from ht_nav_variables:msg/HtNavStrapCarOut.idl
// generated code does not contain a copyright notice

#include <stddef.h>
#include "ht_nav_variables/msg/detail/ht_nav_strap_car_out__rosidl_typesupport_introspection_c.h"
#include "ht_nav_variables/msg/rosidl_typesupport_introspection_c__visibility_control.h"
#include "rosidl_typesupport_introspection_c/field_types.h"
#include "rosidl_typesupport_introspection_c/identifier.h"
#include "rosidl_typesupport_introspection_c/message_introspection.h"
#include "ht_nav_variables/msg/detail/ht_nav_strap_car_out__functions.h"
#include "ht_nav_variables/msg/detail/ht_nav_strap_car_out__struct.h"


// Include directives for member types
// Member `pos`
// Member `car_pos`
// Member `vel`
#include "ht_nav_variables/msg/ht_nav_vector3.h"
// Member `pos`
// Member `car_pos`
// Member `vel`
#include "ht_nav_variables/msg/detail/ht_nav_vector3__rosidl_typesupport_introspection_c.h"
// Member `euler`
#include "ht_nav_variables/msg/ht_nav_euler.h"
// Member `euler`
#include "ht_nav_variables/msg/detail/ht_nav_euler__rosidl_typesupport_introspection_c.h"
// Member `quaternion`
#include "ht_nav_variables/msg/ht_nav_quaternion.h"
// Member `quaternion`
#include "ht_nav_variables/msg/detail/ht_nav_quaternion__rosidl_typesupport_introspection_c.h"

#ifdef __cplusplus
extern "C"
{
#endif

void HtNavStrapCarOut__rosidl_typesupport_introspection_c__HtNavStrapCarOut_init_function(
  void * message_memory, enum rosidl_runtime_c__message_initialization _init)
{
  // TODO(karsten1987): initializers are not yet implemented for typesupport c
  // see https://github.com/ros2/ros2/issues/397
  (void) _init;
  ht_nav_variables__msg__HtNavStrapCarOut__init(message_memory);
}

void HtNavStrapCarOut__rosidl_typesupport_introspection_c__HtNavStrapCarOut_fini_function(void * message_memory)
{
  ht_nav_variables__msg__HtNavStrapCarOut__fini(message_memory);
}

static rosidl_typesupport_introspection_c__MessageMember HtNavStrapCarOut__rosidl_typesupport_introspection_c__HtNavStrapCarOut_message_member_array[6] = {
  {
    "time",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_DOUBLE,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(ht_nav_variables__msg__HtNavStrapCarOut, time),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL  // resize(index) function pointer
  },
  {
    "pos",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_MESSAGE,  // type
    0,  // upper bound of string
    NULL,  // members of sub message (initialized later)
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(ht_nav_variables__msg__HtNavStrapCarOut, pos),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL  // resize(index) function pointer
  },
  {
    "car_pos",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_MESSAGE,  // type
    0,  // upper bound of string
    NULL,  // members of sub message (initialized later)
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(ht_nav_variables__msg__HtNavStrapCarOut, car_pos),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL  // resize(index) function pointer
  },
  {
    "vel",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_MESSAGE,  // type
    0,  // upper bound of string
    NULL,  // members of sub message (initialized later)
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(ht_nav_variables__msg__HtNavStrapCarOut, vel),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL  // resize(index) function pointer
  },
  {
    "euler",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_MESSAGE,  // type
    0,  // upper bound of string
    NULL,  // members of sub message (initialized later)
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(ht_nav_variables__msg__HtNavStrapCarOut, euler),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL  // resize(index) function pointer
  },
  {
    "quaternion",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_MESSAGE,  // type
    0,  // upper bound of string
    NULL,  // members of sub message (initialized later)
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(ht_nav_variables__msg__HtNavStrapCarOut, quaternion),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL  // resize(index) function pointer
  }
};

static const rosidl_typesupport_introspection_c__MessageMembers HtNavStrapCarOut__rosidl_typesupport_introspection_c__HtNavStrapCarOut_message_members = {
  "ht_nav_variables__msg",  // message namespace
  "HtNavStrapCarOut",  // message name
  6,  // number of fields
  sizeof(ht_nav_variables__msg__HtNavStrapCarOut),
  HtNavStrapCarOut__rosidl_typesupport_introspection_c__HtNavStrapCarOut_message_member_array,  // message members
  HtNavStrapCarOut__rosidl_typesupport_introspection_c__HtNavStrapCarOut_init_function,  // function to initialize message memory (memory has to be allocated)
  HtNavStrapCarOut__rosidl_typesupport_introspection_c__HtNavStrapCarOut_fini_function  // function to terminate message instance (will not free memory)
};

// this is not const since it must be initialized on first access
// since C does not allow non-integral compile-time constants
static rosidl_message_type_support_t HtNavStrapCarOut__rosidl_typesupport_introspection_c__HtNavStrapCarOut_message_type_support_handle = {
  0,
  &HtNavStrapCarOut__rosidl_typesupport_introspection_c__HtNavStrapCarOut_message_members,
  get_message_typesupport_handle_function,
};

ROSIDL_TYPESUPPORT_INTROSPECTION_C_EXPORT_ht_nav_variables
const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, ht_nav_variables, msg, HtNavStrapCarOut)() {
  HtNavStrapCarOut__rosidl_typesupport_introspection_c__HtNavStrapCarOut_message_member_array[1].members_ =
    ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, ht_nav_variables, msg, HtNavVector3)();
  HtNavStrapCarOut__rosidl_typesupport_introspection_c__HtNavStrapCarOut_message_member_array[2].members_ =
    ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, ht_nav_variables, msg, HtNavVector3)();
  HtNavStrapCarOut__rosidl_typesupport_introspection_c__HtNavStrapCarOut_message_member_array[3].members_ =
    ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, ht_nav_variables, msg, HtNavVector3)();
  HtNavStrapCarOut__rosidl_typesupport_introspection_c__HtNavStrapCarOut_message_member_array[4].members_ =
    ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, ht_nav_variables, msg, HtNavEuler)();
  HtNavStrapCarOut__rosidl_typesupport_introspection_c__HtNavStrapCarOut_message_member_array[5].members_ =
    ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, ht_nav_variables, msg, HtNavQuaternion)();
  if (!HtNavStrapCarOut__rosidl_typesupport_introspection_c__HtNavStrapCarOut_message_type_support_handle.typesupport_identifier) {
    HtNavStrapCarOut__rosidl_typesupport_introspection_c__HtNavStrapCarOut_message_type_support_handle.typesupport_identifier =
      rosidl_typesupport_introspection_c__identifier;
  }
  return &HtNavStrapCarOut__rosidl_typesupport_introspection_c__HtNavStrapCarOut_message_type_support_handle;
}
#ifdef __cplusplus
}
#endif
