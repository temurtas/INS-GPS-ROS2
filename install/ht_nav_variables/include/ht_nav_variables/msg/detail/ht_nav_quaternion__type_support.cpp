// generated from rosidl_typesupport_introspection_cpp/resource/idl__type_support.cpp.em
// with input from ht_nav_variables:msg/HtNavQuaternion.idl
// generated code does not contain a copyright notice

#include "array"
#include "cstddef"
#include "string"
#include "vector"
#include "rosidl_runtime_c/message_type_support_struct.h"
#include "rosidl_typesupport_cpp/message_type_support.hpp"
#include "rosidl_typesupport_interface/macros.h"
#include "ht_nav_variables/msg/detail/ht_nav_quaternion__struct.hpp"
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

void HtNavQuaternion_init_function(
  void * message_memory, rosidl_runtime_cpp::MessageInitialization _init)
{
  new (message_memory) ht_nav_variables::msg::HtNavQuaternion(_init);
}

void HtNavQuaternion_fini_function(void * message_memory)
{
  auto typed_message = static_cast<ht_nav_variables::msg::HtNavQuaternion *>(message_memory);
  typed_message->~HtNavQuaternion();
}

static const ::rosidl_typesupport_introspection_cpp::MessageMember HtNavQuaternion_message_member_array[4] = {
  {
    "x",  // name
    ::rosidl_typesupport_introspection_cpp::ROS_TYPE_DOUBLE,  // type
    0,  // upper bound of string
    nullptr,  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(ht_nav_variables::msg::HtNavQuaternion, x),  // bytes offset in struct
    nullptr,  // default value
    nullptr,  // size() function pointer
    nullptr,  // get_const(index) function pointer
    nullptr,  // get(index) function pointer
    nullptr  // resize(index) function pointer
  },
  {
    "y",  // name
    ::rosidl_typesupport_introspection_cpp::ROS_TYPE_DOUBLE,  // type
    0,  // upper bound of string
    nullptr,  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(ht_nav_variables::msg::HtNavQuaternion, y),  // bytes offset in struct
    nullptr,  // default value
    nullptr,  // size() function pointer
    nullptr,  // get_const(index) function pointer
    nullptr,  // get(index) function pointer
    nullptr  // resize(index) function pointer
  },
  {
    "z",  // name
    ::rosidl_typesupport_introspection_cpp::ROS_TYPE_DOUBLE,  // type
    0,  // upper bound of string
    nullptr,  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(ht_nav_variables::msg::HtNavQuaternion, z),  // bytes offset in struct
    nullptr,  // default value
    nullptr,  // size() function pointer
    nullptr,  // get_const(index) function pointer
    nullptr,  // get(index) function pointer
    nullptr  // resize(index) function pointer
  },
  {
    "w",  // name
    ::rosidl_typesupport_introspection_cpp::ROS_TYPE_DOUBLE,  // type
    0,  // upper bound of string
    nullptr,  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(ht_nav_variables::msg::HtNavQuaternion, w),  // bytes offset in struct
    nullptr,  // default value
    nullptr,  // size() function pointer
    nullptr,  // get_const(index) function pointer
    nullptr,  // get(index) function pointer
    nullptr  // resize(index) function pointer
  }
};

static const ::rosidl_typesupport_introspection_cpp::MessageMembers HtNavQuaternion_message_members = {
  "ht_nav_variables::msg",  // message namespace
  "HtNavQuaternion",  // message name
  4,  // number of fields
  sizeof(ht_nav_variables::msg::HtNavQuaternion),
  HtNavQuaternion_message_member_array,  // message members
  HtNavQuaternion_init_function,  // function to initialize message memory (memory has to be allocated)
  HtNavQuaternion_fini_function  // function to terminate message instance (will not free memory)
};

static const rosidl_message_type_support_t HtNavQuaternion_message_type_support_handle = {
  ::rosidl_typesupport_introspection_cpp::typesupport_identifier,
  &HtNavQuaternion_message_members,
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
get_message_type_support_handle<ht_nav_variables::msg::HtNavQuaternion>()
{
  return &::ht_nav_variables::msg::rosidl_typesupport_introspection_cpp::HtNavQuaternion_message_type_support_handle;
}

}  // namespace rosidl_typesupport_introspection_cpp

#ifdef __cplusplus
extern "C"
{
#endif

ROSIDL_TYPESUPPORT_INTROSPECTION_CPP_PUBLIC
const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_cpp, ht_nav_variables, msg, HtNavQuaternion)() {
  return &::ht_nav_variables::msg::rosidl_typesupport_introspection_cpp::HtNavQuaternion_message_type_support_handle;
}

#ifdef __cplusplus
}
#endif
