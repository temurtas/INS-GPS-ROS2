// generated from rosidl_typesupport_introspection_c/resource/idl__type_support.c.em
// with input from ht_nav_variables:msg/HtNavVehicleDebug.idl
// generated code does not contain a copyright notice

#include <stddef.h>
#include "ht_nav_variables/msg/detail/ht_nav_vehicle_debug__rosidl_typesupport_introspection_c.h"
#include "ht_nav_variables/msg/rosidl_typesupport_introspection_c__visibility_control.h"
#include "rosidl_typesupport_introspection_c/field_types.h"
#include "rosidl_typesupport_introspection_c/identifier.h"
#include "rosidl_typesupport_introspection_c/message_introspection.h"
#include "ht_nav_variables/msg/detail/ht_nav_vehicle_debug__functions.h"
#include "ht_nav_variables/msg/detail/ht_nav_vehicle_debug__struct.h"


// Include directives for member types
// Member `wheel_variables`
#include "ht_nav_variables/msg/ht_nav_tire_out.h"
// Member `wheel_variables`
#include "ht_nav_variables/msg/detail/ht_nav_tire_out__rosidl_typesupport_introspection_c.h"
// Member `imu_link_pva`
// Member `fl_wheel_pva`
// Member `fr_wheel_pva`
// Member `rl_wheel_pva`
// Member `rr_wheel_pva`
#include "ht_nav_variables/msg/ht_nav_strap_out.h"
// Member `imu_link_pva`
// Member `fl_wheel_pva`
// Member `fr_wheel_pva`
// Member `rl_wheel_pva`
// Member `rr_wheel_pva`
#include "ht_nav_variables/msg/detail/ht_nav_strap_out__rosidl_typesupport_introspection_c.h"

#ifdef __cplusplus
extern "C"
{
#endif

void HtNavVehicleDebug__rosidl_typesupport_introspection_c__HtNavVehicleDebug_init_function(
  void * message_memory, enum rosidl_runtime_c__message_initialization _init)
{
  // TODO(karsten1987): initializers are not yet implemented for typesupport c
  // see https://github.com/ros2/ros2/issues/397
  (void) _init;
  ht_nav_variables__msg__HtNavVehicleDebug__init(message_memory);
}

void HtNavVehicleDebug__rosidl_typesupport_introspection_c__HtNavVehicleDebug_fini_function(void * message_memory)
{
  ht_nav_variables__msg__HtNavVehicleDebug__fini(message_memory);
}

static rosidl_typesupport_introspection_c__MessageMember HtNavVehicleDebug__rosidl_typesupport_introspection_c__HtNavVehicleDebug_message_member_array[7] = {
  {
    "time",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_DOUBLE,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(ht_nav_variables__msg__HtNavVehicleDebug, time),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL  // resize(index) function pointer
  },
  {
    "wheel_variables",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_MESSAGE,  // type
    0,  // upper bound of string
    NULL,  // members of sub message (initialized later)
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(ht_nav_variables__msg__HtNavVehicleDebug, wheel_variables),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL  // resize(index) function pointer
  },
  {
    "imu_link_pva",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_MESSAGE,  // type
    0,  // upper bound of string
    NULL,  // members of sub message (initialized later)
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(ht_nav_variables__msg__HtNavVehicleDebug, imu_link_pva),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL  // resize(index) function pointer
  },
  {
    "fl_wheel_pva",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_MESSAGE,  // type
    0,  // upper bound of string
    NULL,  // members of sub message (initialized later)
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(ht_nav_variables__msg__HtNavVehicleDebug, fl_wheel_pva),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL  // resize(index) function pointer
  },
  {
    "fr_wheel_pva",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_MESSAGE,  // type
    0,  // upper bound of string
    NULL,  // members of sub message (initialized later)
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(ht_nav_variables__msg__HtNavVehicleDebug, fr_wheel_pva),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL  // resize(index) function pointer
  },
  {
    "rl_wheel_pva",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_MESSAGE,  // type
    0,  // upper bound of string
    NULL,  // members of sub message (initialized later)
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(ht_nav_variables__msg__HtNavVehicleDebug, rl_wheel_pva),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL  // resize(index) function pointer
  },
  {
    "rr_wheel_pva",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_MESSAGE,  // type
    0,  // upper bound of string
    NULL,  // members of sub message (initialized later)
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(ht_nav_variables__msg__HtNavVehicleDebug, rr_wheel_pva),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL  // resize(index) function pointer
  }
};

static const rosidl_typesupport_introspection_c__MessageMembers HtNavVehicleDebug__rosidl_typesupport_introspection_c__HtNavVehicleDebug_message_members = {
  "ht_nav_variables__msg",  // message namespace
  "HtNavVehicleDebug",  // message name
  7,  // number of fields
  sizeof(ht_nav_variables__msg__HtNavVehicleDebug),
  HtNavVehicleDebug__rosidl_typesupport_introspection_c__HtNavVehicleDebug_message_member_array,  // message members
  HtNavVehicleDebug__rosidl_typesupport_introspection_c__HtNavVehicleDebug_init_function,  // function to initialize message memory (memory has to be allocated)
  HtNavVehicleDebug__rosidl_typesupport_introspection_c__HtNavVehicleDebug_fini_function  // function to terminate message instance (will not free memory)
};

// this is not const since it must be initialized on first access
// since C does not allow non-integral compile-time constants
static rosidl_message_type_support_t HtNavVehicleDebug__rosidl_typesupport_introspection_c__HtNavVehicleDebug_message_type_support_handle = {
  0,
  &HtNavVehicleDebug__rosidl_typesupport_introspection_c__HtNavVehicleDebug_message_members,
  get_message_typesupport_handle_function,
};

ROSIDL_TYPESUPPORT_INTROSPECTION_C_EXPORT_ht_nav_variables
const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, ht_nav_variables, msg, HtNavVehicleDebug)() {
  HtNavVehicleDebug__rosidl_typesupport_introspection_c__HtNavVehicleDebug_message_member_array[1].members_ =
    ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, ht_nav_variables, msg, HtNavTireOut)();
  HtNavVehicleDebug__rosidl_typesupport_introspection_c__HtNavVehicleDebug_message_member_array[2].members_ =
    ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, ht_nav_variables, msg, HtNavStrapOut)();
  HtNavVehicleDebug__rosidl_typesupport_introspection_c__HtNavVehicleDebug_message_member_array[3].members_ =
    ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, ht_nav_variables, msg, HtNavStrapOut)();
  HtNavVehicleDebug__rosidl_typesupport_introspection_c__HtNavVehicleDebug_message_member_array[4].members_ =
    ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, ht_nav_variables, msg, HtNavStrapOut)();
  HtNavVehicleDebug__rosidl_typesupport_introspection_c__HtNavVehicleDebug_message_member_array[5].members_ =
    ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, ht_nav_variables, msg, HtNavStrapOut)();
  HtNavVehicleDebug__rosidl_typesupport_introspection_c__HtNavVehicleDebug_message_member_array[6].members_ =
    ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, ht_nav_variables, msg, HtNavStrapOut)();
  if (!HtNavVehicleDebug__rosidl_typesupport_introspection_c__HtNavVehicleDebug_message_type_support_handle.typesupport_identifier) {
    HtNavVehicleDebug__rosidl_typesupport_introspection_c__HtNavVehicleDebug_message_type_support_handle.typesupport_identifier =
      rosidl_typesupport_introspection_c__identifier;
  }
  return &HtNavVehicleDebug__rosidl_typesupport_introspection_c__HtNavVehicleDebug_message_type_support_handle;
}
#ifdef __cplusplus
}
#endif
