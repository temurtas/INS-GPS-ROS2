// generated from rosidl_typesupport_introspection_cpp/resource/idl__type_support.cpp.em
// with input from ht_nav_variables:msg/HtNavJointState.idl
// generated code does not contain a copyright notice

#include "array"
#include "cstddef"
#include "string"
#include "vector"
#include "rosidl_runtime_c/message_type_support_struct.h"
#include "rosidl_typesupport_cpp/message_type_support.hpp"
#include "rosidl_typesupport_interface/macros.h"
#include "ht_nav_variables/msg/detail/ht_nav_joint_state__struct.hpp"
#include "rosidl_typesupport_introspection_cpp/field_types.hpp"
#include "rosidl_typesupport_introspection_cpp/identifier.hpp"
#include "rosidl_typesupport_introspection_cpp/message_introspection.hpp"
#include "rosidl_typesupport_introspection_cpp/message_type_support_decl.hpp"
#include "rosidl_typesupport_introspection_cpp/visibility_control.h"

namespace ht_nav_variables
{

namespace msg
{

namespace rosidl_typesupport_introspection_cpp
{

void HtNavJointState_init_function(
  void * message_memory, rosidl_runtime_cpp::MessageInitialization _init)
{
  new (message_memory) ht_nav_variables::msg::HtNavJointState(_init);
}

void HtNavJointState_fini_function(void * message_memory)
{
  auto typed_message = static_cast<ht_nav_variables::msg::HtNavJointState *>(message_memory);
  typed_message->~HtNavJointState();
}

static const ::rosidl_typesupport_introspection_cpp::MessageMember HtNavJointState_message_member_array[2] = {
  {
    "steering_angle",  // name
    ::rosidl_typesupport_introspection_cpp::ROS_TYPE_MESSAGE,  // type
    0,  // upper bound of string
    ::rosidl_typesupport_introspection_cpp::get_message_type_support_handle<ht_nav_variables::msg::HtNavWheelVector>(),  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(ht_nav_variables::msg::HtNavJointState, steering_angle),  // bytes offset in struct
    nullptr,  // default value
    nullptr,  // size() function pointer
    nullptr,  // get_const(index) function pointer
    nullptr,  // get(index) function pointer
    nullptr  // resize(index) function pointer
  },
  {
    "wheel_rotation",  // name
    ::rosidl_typesupport_introspection_cpp::ROS_TYPE_MESSAGE,  // type
    0,  // upper bound of string
    ::rosidl_typesupport_introspection_cpp::get_message_type_support_handle<ht_nav_variables::msg::HtNavWheelVector>(),  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(ht_nav_variables::msg::HtNavJointState, wheel_rotation),  // bytes offset in struct
    nullptr,  // default value
    nullptr,  // size() function pointer
    nullptr,  // get_const(index) function pointer
    nullptr,  // get(index) function pointer
    nullptr  // resize(index) function pointer
  }
};

static const ::rosidl_typesupport_introspection_cpp::MessageMembers HtNavJointState_message_members = {
  "ht_nav_variables::msg",  // message namespace
  "HtNavJointState",  // message name
  2,  // number of fields
  sizeof(ht_nav_variables::msg::HtNavJointState),
  HtNavJointState_message_member_array,  // message members
  HtNavJointState_init_function,  // function to initialize message memory (memory has to be allocated)
  HtNavJointState_fini_function  // function to terminate message instance (will not free memory)
};

static const rosidl_message_type_support_t HtNavJointState_message_type_support_handle = {
  ::rosidl_typesupport_introspection_cpp::typesupport_identifier,
  &HtNavJointState_message_members,
  get_message_typesupport_handle_function,
};

}  // namespace rosidl_typesupport_introspection_cpp

}  // namespace msg

}  // namespace ht_nav_variables


namespace rosidl_typesupport_introspection_cpp
{

template<>
ROSIDL_TYPESUPPORT_INTROSPECTION_CPP_PUBLIC
const rosidl_message_type_support_t *
get_message_type_support_handle<ht_nav_variables::msg::HtNavJointState>()
{
  return &::ht_nav_variables::msg::rosidl_typesupport_introspection_cpp::HtNavJointState_message_type_support_handle;
}

}  // namespace rosidl_typesupport_introspection_cpp

#ifdef __cplusplus
extern "C"
{
#endif

ROSIDL_TYPESUPPORT_INTROSPECTION_CPP_PUBLIC
const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_cpp, ht_nav_variables, msg, HtNavJointState)() {
  return &::ht_nav_variables::msg::rosidl_typesupport_introspection_cpp::HtNavJointState_message_type_support_handle;
}

#ifdef __cplusplus
}
#endif
