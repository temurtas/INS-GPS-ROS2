// generated from rosidl_generator_c/resource/idl__functions.c.em
// with input from ht_nav_variables:msg/HtNavVehicleDebug.idl
// generated code does not contain a copyright notice
#include "ht_nav_variables/msg/detail/ht_nav_vehicle_debug__functions.h"

#include <assert.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>


// Include directives for member types
// Member `wheel_variables`
#include "ht_nav_variables/msg/detail/ht_nav_tire_out__functions.h"
// Member `imu_link_pva`
// Member `fl_wheel_pva`
// Member `fr_wheel_pva`
// Member `rl_wheel_pva`
// Member `rr_wheel_pva`
#include "ht_nav_variables/msg/detail/ht_nav_strap_out__functions.h"

bool
ht_nav_variables__msg__HtNavVehicleDebug__init(ht_nav_variables__msg__HtNavVehicleDebug * msg)
{
  if (!msg) {
    return false;
  }
  // time
  // wheel_variables
  if (!ht_nav_variables__msg__HtNavTireOut__init(&msg->wheel_variables)) {
    ht_nav_variables__msg__HtNavVehicleDebug__fini(msg);
    return false;
  }
  // imu_link_pva
  if (!ht_nav_variables__msg__HtNavStrapOut__init(&msg->imu_link_pva)) {
    ht_nav_variables__msg__HtNavVehicleDebug__fini(msg);
    return false;
  }
  // fl_wheel_pva
  if (!ht_nav_variables__msg__HtNavStrapOut__init(&msg->fl_wheel_pva)) {
    ht_nav_variables__msg__HtNavVehicleDebug__fini(msg);
    return false;
  }
  // fr_wheel_pva
  if (!ht_nav_variables__msg__HtNavStrapOut__init(&msg->fr_wheel_pva)) {
    ht_nav_variables__msg__HtNavVehicleDebug__fini(msg);
    return false;
  }
  // rl_wheel_pva
  if (!ht_nav_variables__msg__HtNavStrapOut__init(&msg->rl_wheel_pva)) {
    ht_nav_variables__msg__HtNavVehicleDebug__fini(msg);
    return false;
  }
  // rr_wheel_pva
  if (!ht_nav_variables__msg__HtNavStrapOut__init(&msg->rr_wheel_pva)) {
    ht_nav_variables__msg__HtNavVehicleDebug__fini(msg);
    return false;
  }
  return true;
}

void
ht_nav_variables__msg__HtNavVehicleDebug__fini(ht_nav_variables__msg__HtNavVehicleDebug * msg)
{
  if (!msg) {
    return;
  }
  // time
  // wheel_variables
  ht_nav_variables__msg__HtNavTireOut__fini(&msg->wheel_variables);
  // imu_link_pva
  ht_nav_variables__msg__HtNavStrapOut__fini(&msg->imu_link_pva);
  // fl_wheel_pva
  ht_nav_variables__msg__HtNavStrapOut__fini(&msg->fl_wheel_pva);
  // fr_wheel_pva
  ht_nav_variables__msg__HtNavStrapOut__fini(&msg->fr_wheel_pva);
  // rl_wheel_pva
  ht_nav_variables__msg__HtNavStrapOut__fini(&msg->rl_wheel_pva);
  // rr_wheel_pva
  ht_nav_variables__msg__HtNavStrapOut__fini(&msg->rr_wheel_pva);
}

ht_nav_variables__msg__HtNavVehicleDebug *
ht_nav_variables__msg__HtNavVehicleDebug__create()
{
  ht_nav_variables__msg__HtNavVehicleDebug * msg = (ht_nav_variables__msg__HtNavVehicleDebug *)malloc(sizeof(ht_nav_variables__msg__HtNavVehicleDebug));
  if (!msg) {
    return NULL;
  }
  memset(msg, 0, sizeof(ht_nav_variables__msg__HtNavVehicleDebug));
  bool success = ht_nav_variables__msg__HtNavVehicleDebug__init(msg);
  if (!success) {
    free(msg);
    return NULL;
  }
  return msg;
}

void
ht_nav_variables__msg__HtNavVehicleDebug__destroy(ht_nav_variables__msg__HtNavVehicleDebug * msg)
{
  if (msg) {
    ht_nav_variables__msg__HtNavVehicleDebug__fini(msg);
  }
  free(msg);
}


bool
ht_nav_variables__msg__HtNavVehicleDebug__Sequence__init(ht_nav_variables__msg__HtNavVehicleDebug__Sequence * array, size_t size)
{
  if (!array) {
    return false;
  }
  ht_nav_variables__msg__HtNavVehicleDebug * data = NULL;
  if (size) {
    data = (ht_nav_variables__msg__HtNavVehicleDebug *)calloc(size, sizeof(ht_nav_variables__msg__HtNavVehicleDebug));
    if (!data) {
      return false;
    }
    // initialize all array elements
    size_t i;
    for (i = 0; i < size; ++i) {
      bool success = ht_nav_variables__msg__HtNavVehicleDebug__init(&data[i]);
      if (!success) {
        break;
      }
    }
    if (i < size) {
      // if initialization failed finalize the already initialized array elements
      for (; i > 0; --i) {
        ht_nav_variables__msg__HtNavVehicleDebug__fini(&data[i - 1]);
      }
      free(data);
      return false;
    }
  }
  array->data = data;
  array->size = size;
  array->capacity = size;
  return true;
}

void
ht_nav_variables__msg__HtNavVehicleDebug__Sequence__fini(ht_nav_variables__msg__HtNavVehicleDebug__Sequence * array)
{
  if (!array) {
    return;
  }
  if (array->data) {
    // ensure that data and capacity values are consistent
    assert(array->capacity > 0);
    // finalize all array elements
    for (size_t i = 0; i < array->capacity; ++i) {
      ht_nav_variables__msg__HtNavVehicleDebug__fini(&array->data[i]);
    }
    free(array->data);
    array->data = NULL;
    array->size = 0;
    array->capacity = 0;
  } else {
    // ensure that data, size, and capacity values are consistent
    assert(0 == array->size);
    assert(0 == array->capacity);
  }
}

ht_nav_variables__msg__HtNavVehicleDebug__Sequence *
ht_nav_variables__msg__HtNavVehicleDebug__Sequence__create(size_t size)
{
  ht_nav_variables__msg__HtNavVehicleDebug__Sequence * array = (ht_nav_variables__msg__HtNavVehicleDebug__Sequence *)malloc(sizeof(ht_nav_variables__msg__HtNavVehicleDebug__Sequence));
  if (!array) {
    return NULL;
  }
  bool success = ht_nav_variables__msg__HtNavVehicleDebug__Sequence__init(array, size);
  if (!success) {
    free(array);
    return NULL;
  }
  return array;
}

void
ht_nav_variables__msg__HtNavVehicleDebug__Sequence__destroy(ht_nav_variables__msg__HtNavVehicleDebug__Sequence * array)
{
  if (array) {
    ht_nav_variables__msg__HtNavVehicleDebug__Sequence__fini(array);
  }
  free(array);
}