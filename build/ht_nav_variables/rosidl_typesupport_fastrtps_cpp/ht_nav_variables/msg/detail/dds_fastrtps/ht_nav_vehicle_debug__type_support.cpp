// generated from rosidl_typesupport_fastrtps_cpp/resource/idl__type_support.cpp.em
// with input from ht_nav_variables:msg/HtNavVehicleDebug.idl
// generated code does not contain a copyright notice
#include "ht_nav_variables/msg/detail/ht_nav_vehicle_debug__rosidl_typesupport_fastrtps_cpp.hpp"
#include "ht_nav_variables/msg/detail/ht_nav_vehicle_debug__struct.hpp"

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
  const ht_nav_variables::msg::HtNavTireOut &,
  eprosima::fastcdr::Cdr &);
bool cdr_deserialize(
  eprosima::fastcdr::Cdr &,
  ht_nav_variables::msg::HtNavTireOut &);
size_t get_serialized_size(
  const ht_nav_variables::msg::HtNavTireOut &,
  size_t current_alignment);
size_t
max_serialized_size_HtNavTireOut(
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
  const ht_nav_variables::msg::HtNavStrapOut &,
  eprosima::fastcdr::Cdr &);
bool cdr_deserialize(
  eprosima::fastcdr::Cdr &,
  ht_nav_variables::msg::HtNavStrapOut &);
size_t get_serialized_size(
  const ht_nav_variables::msg::HtNavStrapOut &,
  size_t current_alignment);
size_t
max_serialized_size_HtNavStrapOut(
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
  const ht_nav_variables::msg::HtNavStrapOut &,
  eprosima::fastcdr::Cdr &);
bool cdr_deserialize(
  eprosima::fastcdr::Cdr &,
  ht_nav_variables::msg::HtNavStrapOut &);
size_t get_serialized_size(
  const ht_nav_variables::msg::HtNavStrapOut &,
  size_t current_alignment);
size_t
max_serialized_size_HtNavStrapOut(
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
  const ht_nav_variables::msg::HtNavStrapOut &,
  eprosima::fastcdr::Cdr &);
bool cdr_deserialize(
  eprosima::fastcdr::Cdr &,
  ht_nav_variables::msg::HtNavStrapOut &);
size_t get_serialized_size(
  const ht_nav_variables::msg::HtNavStrapOut &,
  size_t current_alignment);
size_t
max_serialized_size_HtNavStrapOut(
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
  const ht_nav_variables::msg::HtNavStrapOut &,
  eprosima::fastcdr::Cdr &);
bool cdr_deserialize(
  eprosima::fastcdr::Cdr &,
  ht_nav_variables::msg::HtNavStrapOut &);
size_t get_serialized_size(
  const ht_nav_variables::msg::HtNavStrapOut &,
  size_t current_alignment);
size_t
max_serialized_size_HtNavStrapOut(
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
  const ht_nav_variables::msg::HtNavStrapOut &,
  eprosima::fastcdr::Cdr &);
bool cdr_deserialize(
  eprosima::fastcdr::Cdr &,
  ht_nav_variables::msg::HtNavStrapOut &);
size_t get_serialized_size(
  const ht_nav_variables::msg::HtNavStrapOut &,
  size_t current_alignment);
size_t
max_serialized_size_HtNavStrapOut(
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
  const ht_nav_variables::msg::HtNavVehicleDebug & ros_message,
  eprosima::fastcdr::Cdr & cdr)
{
  // Member: time
  cdr << ros_message.time;
  // Member: wheel_variables
  ht_nav_variables::msg::typesupport_fastrtps_cpp::cdr_serialize(
    ros_message.wheel_variables,
    cdr);
  // Member: imu_link_pva
  ht_nav_variables::msg::typesupport_fastrtps_cpp::cdr_serialize(
    ros_message.imu_link_pva,
    cdr);
  // Member: fl_wheel_pva
  ht_nav_variables::msg::typesupport_fastrtps_cpp::cdr_serialize(
    ros_message.fl_wheel_pva,
    cdr);
  // Member: fr_wheel_pva
  ht_nav_variables::msg::typesupport_fastrtps_cpp::cdr_serialize(
    ros_message.fr_wheel_pva,
    cdr);
  // Member: rl_wheel_pva
  ht_nav_variables::msg::typesupport_fastrtps_cpp::cdr_serialize(
    ros_message.rl_wheel_pva,
    cdr);
  // Member: rr_wheel_pva
  ht_nav_variables::msg::typesupport_fastrtps_cpp::cdr_serialize(
    ros_message.rr_wheel_pva,
    cdr);
  return true;
}

bool
ROSIDL_TYPESUPPORT_FASTRTPS_CPP_PUBLIC_ht_nav_variables
cdr_deserialize(
  eprosima::fastcdr::Cdr & cdr,
  ht_nav_variables::msg::HtNavVehicleDebug & ros_message)
{
  // Member: time
  cdr >> ros_message.time;

  // Member: wheel_variables
  ht_nav_variables::msg::typesupport_fastrtps_cpp::cdr_deserialize(
    cdr, ros_message.wheel_variables);

  // Member: imu_link_pva
  ht_nav_variables::msg::typesupport_fastrtps_cpp::cdr_deserialize(
    cdr, ros_message.imu_link_pva);

  // Member: fl_wheel_pva
  ht_nav_variables::msg::typesupport_fastrtps_cpp::cdr_deserialize(
    cdr, ros_message.fl_wheel_pva);

  // Member: fr_wheel_pva
  ht_nav_variables::msg::typesupport_fastrtps_cpp::cdr_deserialize(
    cdr, ros_message.fr_wheel_pva);

  // Member: rl_wheel_pva
  ht_nav_variables::msg::typesupport_fastrtps_cpp::cdr_deserialize(
    cdr, ros_message.rl_wheel_pva);

  // Member: rr_wheel_pva
  ht_nav_variables::msg::typesupport_fastrtps_cpp::cdr_deserialize(
    cdr, ros_message.rr_wheel_pva);

  return true;
}

size_t
ROSIDL_TYPESUPPORT_FASTRTPS_CPP_PUBLIC_ht_nav_variables
get_serialized_size(
  const ht_nav_variables::msg::HtNavVehicleDebug & ros_message,
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
  // Member: wheel_variables

  current_alignment +=
    ht_nav_variables::msg::typesupport_fastrtps_cpp::get_serialized_size(
    ros_message.wheel_variables, current_alignment);
  // Member: imu_link_pva

  current_alignment +=
    ht_nav_variables::msg::typesupport_fastrtps_cpp::get_serialized_size(
    ros_message.imu_link_pva, current_alignment);
  // Member: fl_wheel_pva

  current_alignment +=
    ht_nav_variables::msg::typesupport_fastrtps_cpp::get_serialized_size(
    ros_message.fl_wheel_pva, current_alignment);
  // Member: fr_wheel_pva

  current_alignment +=
    ht_nav_variables::msg::typesupport_fastrtps_cpp::get_serialized_size(
    ros_message.fr_wheel_pva, current_alignment);
  // Member: rl_wheel_pva

  current_alignment +=
    ht_nav_variables::msg::typesupport_fastrtps_cpp::get_serialized_size(
    ros_message.rl_wheel_pva, current_alignment);
  // Member: rr_wheel_pva

  current_alignment +=
    ht_nav_variables::msg::typesupport_fastrtps_cpp::get_serialized_size(
    ros_message.rr_wheel_pva, current_alignment);

  return current_alignment - initial_alignment;
}

size_t
ROSIDL_TYPESUPPORT_FASTRTPS_CPP_PUBLIC_ht_nav_variables
max_serialized_size_HtNavVehicleDebug(
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

  // Member: wheel_variables
  {
    size_t array_size = 1;


    for (size_t index = 0; index < array_size; ++index) {
      current_alignment +=
        ht_nav_variables::msg::typesupport_fastrtps_cpp::max_serialized_size_HtNavTireOut(
        full_bounded, current_alignment);
    }
  }

  // Member: imu_link_pva
  {
    size_t array_size = 1;


    for (size_t index = 0; index < array_size; ++index) {
      current_alignment +=
        ht_nav_variables::msg::typesupport_fastrtps_cpp::max_serialized_size_HtNavStrapOut(
        full_bounded, current_alignment);
    }
  }

  // Member: fl_wheel_pva
  {
    size_t array_size = 1;


    for (size_t index = 0; index < array_size; ++index) {
      current_alignment +=
        ht_nav_variables::msg::typesupport_fastrtps_cpp::max_serialized_size_HtNavStrapOut(
        full_bounded, current_alignment);
    }
  }

  // Member: fr_wheel_pva
  {
    size_t array_size = 1;


    for (size_t index = 0; index < array_size; ++index) {
      current_alignment +=
        ht_nav_variables::msg::typesupport_fastrtps_cpp::max_serialized_size_HtNavStrapOut(
        full_bounded, current_alignment);
    }
  }

  // Member: rl_wheel_pva
  {
    size_t array_size = 1;


    for (size_t index = 0; index < array_size; ++index) {
      current_alignment +=
        ht_nav_variables::msg::typesupport_fastrtps_cpp::max_serialized_size_HtNavStrapOut(
        full_bounded, current_alignment);
    }
  }

  // Member: rr_wheel_pva
  {
    size_t array_size = 1;


    for (size_t index = 0; index < array_size; ++index) {
      current_alignment +=
        ht_nav_variables::msg::typesupport_fastrtps_cpp::max_serialized_size_HtNavStrapOut(
        full_bounded, current_alignment);
    }
  }

  return current_alignment - initial_alignment;
}

static bool _HtNavVehicleDebug__cdr_serialize(
  const void * untyped_ros_message,
  eprosima::fastcdr::Cdr & cdr)
{
  auto typed_message =
    static_cast<const ht_nav_variables::msg::HtNavVehicleDebug *>(
    untyped_ros_message);
  return cdr_serialize(*typed_message, cdr);
}

static bool _HtNavVehicleDebug__cdr_deserialize(
  eprosima::fastcdr::Cdr & cdr,
  void * untyped_ros_message)
{
  auto typed_message =
    static_cast<ht_nav_variables::msg::HtNavVehicleDebug *>(
    untyped_ros_message);
  return cdr_deserialize(cdr, *typed_message);
}

static uint32_t _HtNavVehicleDebug__get_serialized_size(
  const void * untyped_ros_message)
{
  auto typed_message =
    static_cast<const ht_nav_variables::msg::HtNavVehicleDebug *>(
    untyped_ros_message);
  return static_cast<uint32_t>(get_serialized_size(*typed_message, 0));
}

static size_t _HtNavVehicleDebug__max_serialized_size(bool & full_bounded)
{
  return max_serialized_size_HtNavVehicleDebug(full_bounded, 0);
}

static message_type_support_callbacks_t _HtNavVehicleDebug__callbacks = {
  "ht_nav_variables::msg",
  "HtNavVehicleDebug",
  _HtNavVehicleDebug__cdr_serialize,
  _HtNavVehicleDebug__cdr_deserialize,
  _HtNavVehicleDebug__get_serialized_size,
  _HtNavVehicleDebug__max_serialized_size
};

static rosidl_message_type_support_t _HtNavVehicleDebug__handle = {
  rosidl_typesupport_fastrtps_cpp::typesupport_identifier,
  &_HtNavVehicleDebug__callbacks,
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
get_message_type_support_handle<ht_nav_variables::msg::HtNavVehicleDebug>()
{
  return &ht_nav_variables::msg::typesupport_fastrtps_cpp::_HtNavVehicleDebug__handle;
}

}  // namespace rosidl_typesupport_fastrtps_cpp

#ifdef __cplusplus
extern "C"
{
#endif

const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_fastrtps_cpp, ht_nav_variables, msg, HtNavVehicleDebug)() {
  return &ht_nav_variables::msg::typesupport_fastrtps_cpp::_HtNavVehicleDebug__handle;
}

#ifdef __cplusplus
}
#endif
