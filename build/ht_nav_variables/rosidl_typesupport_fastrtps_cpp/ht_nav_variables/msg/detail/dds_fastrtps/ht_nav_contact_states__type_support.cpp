// generated from rosidl_typesupport_fastrtps_cpp/resource/idl__type_support.cpp.em
// with input from ht_nav_variables:msg/HtNavContactStates.idl
// generated code does not contain a copyright notice
#include "ht_nav_variables/msg/detail/ht_nav_contact_states__rosidl_typesupport_fastrtps_cpp.hpp"
#include "ht_nav_variables/msg/detail/ht_nav_contact_states__struct.hpp"

#include <limits>
#include <stdexcept>
#include <string>
#include "rosidl_typesupport_cpp/message_type_support.hpp"
#include "rosidl_typesupport_fastrtps_cpp/identifier.hpp"
#include "rosidl_typesupport_fastrtps_cpp/message_type_support.h"
#include "rosidl_typesupport_fastrtps_cpp/message_type_support_decl.hpp"
#include "rosidl_typesupport_fastrtps_cpp/wstring_conversion.hpp"
#include "fastcdr/Cdr.h"


// forward declaration of message dependencies and their conversion functions
namespace ht_nav_variables
{
namespace msg
{
namespace typesupport_fastrtps_cpp
{
bool cdr_serialize(
  const ht_nav_variables::msg::HtNavContactState &,
  eprosima::fastcdr::Cdr &);
bool cdr_deserialize(
  eprosima::fastcdr::Cdr &,
  ht_nav_variables::msg::HtNavContactState &);
size_t get_serialized_size(
  const ht_nav_variables::msg::HtNavContactState &,
  size_t current_alignment);
size_t
max_serialized_size_HtNavContactState(
  bool & full_bounded,
  size_t current_alignment);
}  // namespace typesupport_fastrtps_cpp
}  // namespace msg
}  // namespace ht_nav_variables

namespace ht_nav_variables
{
namespace msg
{
namespace typesupport_fastrtps_cpp
{
bool cdr_serialize(
  const ht_nav_variables::msg::HtNavContactState &,
  eprosima::fastcdr::Cdr &);
bool cdr_deserialize(
  eprosima::fastcdr::Cdr &,
  ht_nav_variables::msg::HtNavContactState &);
size_t get_serialized_size(
  const ht_nav_variables::msg::HtNavContactState &,
  size_t current_alignment);
size_t
max_serialized_size_HtNavContactState(
  bool & full_bounded,
  size_t current_alignment);
}  // namespace typesupport_fastrtps_cpp
}  // namespace msg
}  // namespace ht_nav_variables

namespace ht_nav_variables
{
namespace msg
{
namespace typesupport_fastrtps_cpp
{
bool cdr_serialize(
  const ht_nav_variables::msg::HtNavContactState &,
  eprosima::fastcdr::Cdr &);
bool cdr_deserialize(
  eprosima::fastcdr::Cdr &,
  ht_nav_variables::msg::HtNavContactState &);
size_t get_serialized_size(
  const ht_nav_variables::msg::HtNavContactState &,
  size_t current_alignment);
size_t
max_serialized_size_HtNavContactState(
  bool & full_bounded,
  size_t current_alignment);
}  // namespace typesupport_fastrtps_cpp
}  // namespace msg
}  // namespace ht_nav_variables

namespace ht_nav_variables
{
namespace msg
{
namespace typesupport_fastrtps_cpp
{
bool cdr_serialize(
  const ht_nav_variables::msg::HtNavContactState &,
  eprosima::fastcdr::Cdr &);
bool cdr_deserialize(
  eprosima::fastcdr::Cdr &,
  ht_nav_variables::msg::HtNavContactState &);
size_t get_serialized_size(
  const ht_nav_variables::msg::HtNavContactState &,
  size_t current_alignment);
size_t
max_serialized_size_HtNavContactState(
  bool & full_bounded,
  size_t current_alignment);
}  // namespace typesupport_fastrtps_cpp
}  // namespace msg
}  // namespace ht_nav_variables


namespace ht_nav_variables
{

namespace msg
{

namespace typesupport_fastrtps_cpp
{

bool
ROSIDL_TYPESUPPORT_FASTRTPS_CPP_PUBLIC_ht_nav_variables
cdr_serialize(
  const ht_nav_variables::msg::HtNavContactStates & ros_message,
  eprosima::fastcdr::Cdr & cdr)
{
  // Member: time
  cdr << ros_message.time;
  // Member: fl_wheel_contact_states
  ht_nav_variables::msg::typesupport_fastrtps_cpp::cdr_serialize(
    ros_message.fl_wheel_contact_states,
    cdr);
  // Member: fr_wheel_contact_states
  ht_nav_variables::msg::typesupport_fastrtps_cpp::cdr_serialize(
    ros_message.fr_wheel_contact_states,
    cdr);
  // Member: rl_wheel_contact_states
  ht_nav_variables::msg::typesupport_fastrtps_cpp::cdr_serialize(
    ros_message.rl_wheel_contact_states,
    cdr);
  // Member: rr_wheel_contact_states
  ht_nav_variables::msg::typesupport_fastrtps_cpp::cdr_serialize(
    ros_message.rr_wheel_contact_states,
    cdr);
  return true;
}

bool
ROSIDL_TYPESUPPORT_FASTRTPS_CPP_PUBLIC_ht_nav_variables
cdr_deserialize(
  eprosima::fastcdr::Cdr & cdr,
  ht_nav_variables::msg::HtNavContactStates & ros_message)
{
  // Member: time
  cdr >> ros_message.time;

  // Member: fl_wheel_contact_states
  ht_nav_variables::msg::typesupport_fastrtps_cpp::cdr_deserialize(
    cdr, ros_message.fl_wheel_contact_states);

  // Member: fr_wheel_contact_states
  ht_nav_variables::msg::typesupport_fastrtps_cpp::cdr_deserialize(
    cdr, ros_message.fr_wheel_contact_states);

  // Member: rl_wheel_contact_states
  ht_nav_variables::msg::typesupport_fastrtps_cpp::cdr_deserialize(
    cdr, ros_message.rl_wheel_contact_states);

  // Member: rr_wheel_contact_states
  ht_nav_variables::msg::typesupport_fastrtps_cpp::cdr_deserialize(
    cdr, ros_message.rr_wheel_contact_states);

  return true;
}

size_t
ROSIDL_TYPESUPPORT_FASTRTPS_CPP_PUBLIC_ht_nav_variables
get_serialized_size(
  const ht_nav_variables::msg::HtNavContactStates & ros_message,
  size_t current_alignment)
{
  size_t initial_alignment = current_alignment;

  const size_t padding = 4;
  const size_t wchar_size = 4;
  (void)padding;
  (void)wchar_size;

  // Member: time
  {
    size_t item_size = sizeof(ros_message.time);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // Member: fl_wheel_contact_states

  current_alignment +=
    ht_nav_variables::msg::typesupport_fastrtps_cpp::get_serialized_size(
    ros_message.fl_wheel_contact_states, current_alignment);
  // Member: fr_wheel_contact_states

  current_alignment +=
    ht_nav_variables::msg::typesupport_fastrtps_cpp::get_serialized_size(
    ros_message.fr_wheel_contact_states, current_alignment);
  // Member: rl_wheel_contact_states

  current_alignment +=
    ht_nav_variables::msg::typesupport_fastrtps_cpp::get_serialized_size(
    ros_message.rl_wheel_contact_states, current_alignment);
  // Member: rr_wheel_contact_states

  current_alignment +=
    ht_nav_variables::msg::typesupport_fastrtps_cpp::get_serialized_size(
    ros_message.rr_wheel_contact_states, current_alignment);

  return current_alignment - initial_alignment;
}

size_t
ROSIDL_TYPESUPPORT_FASTRTPS_CPP_PUBLIC_ht_nav_variables
max_serialized_size_HtNavContactStates(
  bool & full_bounded,
  size_t current_alignment)
{
  size_t initial_alignment = current_alignment;

  const size_t padding = 4;
  const size_t wchar_size = 4;
  (void)padding;
  (void)wchar_size;
  (void)full_bounded;


  // Member: time
  {
    size_t array_size = 1;

    current_alignment += array_size * sizeof(uint64_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint64_t));
  }

  // Member: fl_wheel_contact_states
  {
    size_t array_size = 1;


    for (size_t index = 0; index < array_size; ++index) {
      current_alignment +=
        ht_nav_variables::msg::typesupport_fastrtps_cpp::max_serialized_size_HtNavContactState(
        full_bounded, current_alignment);
    }
  }

  // Member: fr_wheel_contact_states
  {
    size_t array_size = 1;


    for (size_t index = 0; index < array_size; ++index) {
      current_alignment +=
        ht_nav_variables::msg::typesupport_fastrtps_cpp::max_serialized_size_HtNavContactState(
        full_bounded, current_alignment);
    }
  }

  // Member: rl_wheel_contact_states
  {
    size_t array_size = 1;


    for (size_t index = 0; index < array_size; ++index) {
      current_alignment +=
        ht_nav_variables::msg::typesupport_fastrtps_cpp::max_serialized_size_HtNavContactState(
        full_bounded, current_alignment);
    }
  }

  // Member: rr_wheel_contact_states
  {
    size_t array_size = 1;


    for (size_t index = 0; index < array_size; ++index) {
      current_alignment +=
        ht_nav_variables::msg::typesupport_fastrtps_cpp::max_serialized_size_HtNavContactState(
        full_bounded, current_alignment);
    }
  }

  return current_alignment - initial_alignment;
}

static bool _HtNavContactStates__cdr_serialize(
  const void * untyped_ros_message,
  eprosima::fastcdr::Cdr & cdr)
{
  auto typed_message =
    static_cast<const ht_nav_variables::msg::HtNavContactStates *>(
    untyped_ros_message);
  return cdr_serialize(*typed_message, cdr);
}

static bool _HtNavContactStates__cdr_deserialize(
  eprosima::fastcdr::Cdr & cdr,
  void * untyped_ros_message)
{
  auto typed_message =
    static_cast<ht_nav_variables::msg::HtNavContactStates *>(
    untyped_ros_message);
  return cdr_deserialize(cdr, *typed_message);
}

static uint32_t _HtNavContactStates__get_serialized_size(
  const void * untyped_ros_message)
{
  auto typed_message =
    static_cast<const ht_nav_variables::msg::HtNavContactStates *>(
    untyped_ros_message);
  return static_cast<uint32_t>(get_serialized_size(*typed_message, 0));
}

static size_t _HtNavContactStates__max_serialized_size(bool & full_bounded)
{
  return max_serialized_size_HtNavContactStates(full_bounded, 0);
}

static message_type_support_callbacks_t _HtNavContactStates__callbacks = {
  "ht_nav_variables::msg",
  "HtNavContactStates",
  _HtNavContactStates__cdr_serialize,
  _HtNavContactStates__cdr_deserialize,
  _HtNavContactStates__get_serialized_size,
  _HtNavContactStates__max_serialized_size
};

static rosidl_message_type_support_t _HtNavContactStates__handle = {
  rosidl_typesupport_fastrtps_cpp::typesupport_identifier,
  &_HtNavContactStates__callbacks,
  get_message_typesupport_handle_function,
};

}  // namespace typesupport_fastrtps_cpp

}  // namespace msg

}  // namespace ht_nav_variables

namespace rosidl_typesupport_fastrtps_cpp
{

template<>
ROSIDL_TYPESUPPORT_FASTRTPS_CPP_EXPORT_ht_nav_variables
const rosidl_message_type_support_t *
get_message_type_support_handle<ht_nav_variables::msg::HtNavContactStates>()
{
  return &ht_nav_variables::msg::typesupport_fastrtps_cpp::_HtNavContactStates__handle;
}

}  // namespace rosidl_typesupport_fastrtps_cpp

#ifdef __cplusplus
extern "C"
{
#endif

const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_fastrtps_cpp, ht_nav_variables, msg, HtNavContactStates)() {
  return &ht_nav_variables::msg::typesupport_fastrtps_cpp::_HtNavContactStates__handle;
}

#ifdef __cplusplus
}
#endif
