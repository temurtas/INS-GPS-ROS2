// generated from rosidl_typesupport_introspection_c/resource/idl__type_support.c.em
// with input from ht_nav_variables:msg/HtNavTireOut.idl
// generated code does not contain a copyright notice

#include <stddef.h>
#include "ht_nav_variables/msg/detail/ht_nav_tire_out__rosidl_typesupport_introspection_c.h"
#include "ht_nav_variables/msg/rosidl_typesupport_introspection_c__visibility_control.h"
#include "rosidl_typesupport_introspection_c/field_types.h"
#include "rosidl_typesupport_introspection_c/identifier.h"
#include "rosidl_typesupport_introspection_c/message_introspection.h"
#include "ht_nav_variables/msg/detail/ht_nav_tire_out__functions.h"
#include "ht_nav_variables/msg/detail/ht_nav_tire_out__struct.h"


// Include directives for member types
// Member `wheel_side_slip_ang`
// Member `wheel_longitudinal_slip_ratio`
// Member `tire_lateral_forces`
// Member `tire_longitudinal_forces`
#include "ht_nav_variables/msg/ht_nav_wheel_vector.h"
// Member `wheel_side_slip_ang`
// Member `wheel_longitudinal_slip_ratio`
// Member `tire_lateral_forces`
// Member `tire_longitudinal_forces`
#include "ht_nav_variables/msg/detail/ht_nav_wheel_vector__rosidl_typesupport_introspection_c.h"

#ifdef __cplusplus
extern "C"
{
#endif

void HtNavTireOut__rosidl_typesupport_introspection_c__HtNavTireOut_init_function(
  void * message_memory, enum rosidl_runtime_c__message_initialization _init)
{
  // TODO(karsten1987): initializers are not yet implemented for typesupport c
  // see https://github.com/ros2/ros2/issues/397
  (void) _init;
  ht_nav_variables__msg__HtNavTireOut__init(message_memory);
}

void HtNavTireOut__rosidl_typesupport_introspection_c__HtNavTireOut_fini_function(void * message_memory)
{
  ht_nav_variables__msg__HtNavTireOut__fini(message_memory);
}

static rosidl_typesupport_introspection_c__MessageMember HtNavTireOut__rosidl_typesupport_introspection_c__HtNavTireOut_message_member_array[6] = {
  {
    "effective_radius_est",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_DOUBLE,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(ht_nav_variables__msg__HtNavTireOut, effective_radius_est),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL  // resize(index) function pointer
  },
  {
    "vehicle_mass_est",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_DOUBLE,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(ht_nav_variables__msg__HtNavTireOut, vehicle_mass_est),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL  // resize(index) function pointer
  },
  {
    "wheel_side_slip_ang",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_MESSAGE,  // type
    0,  // upper bound of string
    NULL,  // members of sub message (initialized later)
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(ht_nav_variables__msg__HtNavTireOut, wheel_side_slip_ang),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL  // resize(index) function pointer
  },
  {
    "wheel_longitudinal_slip_ratio",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_MESSAGE,  // type
    0,  // upper bound of string
    NULL,  // members of sub message (initialized later)
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(ht_nav_variables__msg__HtNavTireOut, wheel_longitudinal_slip_ratio),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL  // resize(index) function pointer
  },
  {
    "tire_lateral_forces",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_MESSAGE,  // type
    0,  // upper bound of string
    NULL,  // members of sub message (initialized later)
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(ht_nav_variables__msg__HtNavTireOut, tire_lateral_forces),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL  // resize(index) function pointer
  },
  {
    "tire_longitudinal_forces",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_MESSAGE,  // type
    0,  // upper bound of string
    NULL,  // members of sub message (initialized later)
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(ht_nav_variables__msg__HtNavTireOut, tire_longitudinal_forces),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL  // resize(index) function pointer
  }
};

static const rosidl_typesupport_introspection_c__MessageMembers HtNavTireOut__rosidl_typesupport_introspection_c__HtNavTireOut_message_members = {
  "ht_nav_variables__msg",  // message namespace
  "HtNavTireOut",  // message name
  6,  // number of fields
  sizeof(ht_nav_variables__msg__HtNavTireOut),
  HtNavTireOut__rosidl_typesupport_introspection_c__HtNavTireOut_message_member_array,  // message members
  HtNavTireOut__rosidl_typesupport_introspection_c__HtNavTireOut_init_function,  // function to initialize message memory (memory has to be allocated)
  HtNavTireOut__rosidl_typesupport_introspection_c__HtNavTireOut_fini_function  // function to terminate message instance (will not free memory)
};

// this is not const since it must be initialized on first access
// since C does not allow non-integral compile-time constants
static rosidl_message_type_support_t HtNavTireOut__rosidl_typesupport_introspection_c__HtNavTireOut_message_type_support_handle = {
  0,
  &HtNavTireOut__rosidl_typesupport_introspection_c__HtNavTireOut_message_members,
  get_message_typesupport_handle_function,
};

ROSIDL_TYPESUPPORT_INTROSPECTION_C_EXPORT_ht_nav_variables
const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, ht_nav_variables, msg, HtNavTireOut)() {
  HtNavTireOut__rosidl_typesupport_introspection_c__HtNavTireOut_message_member_array[2].members_ =
    ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, ht_nav_variables, msg, HtNavWheelVector)();
  HtNavTireOut__rosidl_typesupport_introspection_c__HtNavTireOut_message_member_array[3].members_ =
    ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, ht_nav_variables, msg, HtNavWheelVector)();
  HtNavTireOut__rosidl_typesupport_introspection_c__HtNavTireOut_message_member_array[4].members_ =
    ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, ht_nav_variables, msg, HtNavWheelVector)();
  HtNavTireOut__rosidl_typesupport_introspection_c__HtNavTireOut_message_member_array[5].members_ =
    ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, ht_nav_variables, msg, HtNavWheelVector)();
  if (!HtNavTireOut__rosidl_typesupport_introspection_c__HtNavTireOut_message_type_support_handle.typesupport_identifier) {
    HtNavTireOut__rosidl_typesupport_introspection_c__HtNavTireOut_message_type_support_handle.typesupport_identifier =
      rosidl_typesupport_introspection_c__identifier;
  }
  return &HtNavTireOut__rosidl_typesupport_introspection_c__HtNavTireOut_message_type_support_handle;
}
#ifdef __cplusplus
}
#endif
