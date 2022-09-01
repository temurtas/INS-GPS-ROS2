// generated from rosidl_generator_c/resource/idl__functions.c.em
// with input from ht_nav_variables:msg/HtNavTireOut.idl
// generated code does not contain a copyright notice
#include "ht_nav_variables/msg/detail/ht_nav_tire_out__functions.h"

#include <assert.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>


// Include directives for member types
// Member `wheel_side_slip_ang`
// Member `wheel_longitudinal_slip_ratio`
// Member `tire_lateral_forces`
// Member `tire_longitudinal_forces`
// Member `tire_normal_forces`
#include "ht_nav_variables/msg/detail/ht_nav_wheel_vector__functions.h"

bool
ht_nav_variables__msg__HtNavTireOut__init(ht_nav_variables__msg__HtNavTireOut * msg)
{
  if (!msg) {
    return false;
  }
  // time
  // effective_radius_est
  // vehicle_mass_est
  // wheel_side_slip_ang
  if (!ht_nav_variables__msg__HtNavWheelVector__init(&msg->wheel_side_slip_ang)) {
    ht_nav_variables__msg__HtNavTireOut__fini(msg);
    return false;
  }
  // wheel_longitudinal_slip_ratio
  if (!ht_nav_variables__msg__HtNavWheelVector__init(&msg->wheel_longitudinal_slip_ratio)) {
    ht_nav_variables__msg__HtNavTireOut__fini(msg);
    return false;
  }
  // tire_lateral_forces
  if (!ht_nav_variables__msg__HtNavWheelVector__init(&msg->tire_lateral_forces)) {
    ht_nav_variables__msg__HtNavTireOut__fini(msg);
    return false;
  }
  // tire_longitudinal_forces
  if (!ht_nav_variables__msg__HtNavWheelVector__init(&msg->tire_longitudinal_forces)) {
    ht_nav_variables__msg__HtNavTireOut__fini(msg);
    return false;
  }
  // tire_normal_forces
  if (!ht_nav_variables__msg__HtNavWheelVector__init(&msg->tire_normal_forces)) {
    ht_nav_variables__msg__HtNavTireOut__fini(msg);
    return false;
  }
  return true;
}

void
ht_nav_variables__msg__HtNavTireOut__fini(ht_nav_variables__msg__HtNavTireOut * msg)
{
  if (!msg) {
    return;
  }
  // time
  // effective_radius_est
  // vehicle_mass_est
  // wheel_side_slip_ang
  ht_nav_variables__msg__HtNavWheelVector__fini(&msg->wheel_side_slip_ang);
  // wheel_longitudinal_slip_ratio
  ht_nav_variables__msg__HtNavWheelVector__fini(&msg->wheel_longitudinal_slip_ratio);
  // tire_lateral_forces
  ht_nav_variables__msg__HtNavWheelVector__fini(&msg->tire_lateral_forces);
  // tire_longitudinal_forces
  ht_nav_variables__msg__HtNavWheelVector__fini(&msg->tire_longitudinal_forces);
  // tire_normal_forces
  ht_nav_variables__msg__HtNavWheelVector__fini(&msg->tire_normal_forces);
}

ht_nav_variables__msg__HtNavTireOut *
ht_nav_variables__msg__HtNavTireOut__create()
{
  ht_nav_variables__msg__HtNavTireOut * msg = (ht_nav_variables__msg__HtNavTireOut *)malloc(sizeof(ht_nav_variables__msg__HtNavTireOut));
  if (!msg) {
    return NULL;
  }
  memset(msg, 0, sizeof(ht_nav_variables__msg__HtNavTireOut));
  bool success = ht_nav_variables__msg__HtNavTireOut__init(msg);
  if (!success) {
    free(msg);
    return NULL;
  }
  return msg;
}

void
ht_nav_variables__msg__HtNavTireOut__destroy(ht_nav_variables__msg__HtNavTireOut * msg)
{
  if (msg) {
    ht_nav_variables__msg__HtNavTireOut__fini(msg);
  }
  free(msg);
}


bool
ht_nav_variables__msg__HtNavTireOut__Sequence__init(ht_nav_variables__msg__HtNavTireOut__Sequence * array, size_t size)
{
  if (!array) {
    return false;
  }
  ht_nav_variables__msg__HtNavTireOut * data = NULL;
  if (size) {
    data = (ht_nav_variables__msg__HtNavTireOut *)calloc(size, sizeof(ht_nav_variables__msg__HtNavTireOut));
    if (!data) {
      return false;
    }
    // initialize all array elements
    size_t i;
    for (i = 0; i < size; ++i) {
      bool success = ht_nav_variables__msg__HtNavTireOut__init(&data[i]);
      if (!success) {
        break;
      }
    }
    if (i < size) {
      // if initialization failed finalize the already initialized array elements
      for (; i > 0; --i) {
        ht_nav_variables__msg__HtNavTireOut__fini(&data[i - 1]);
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
ht_nav_variables__msg__HtNavTireOut__Sequence__fini(ht_nav_variables__msg__HtNavTireOut__Sequence * array)
{
  if (!array) {
    return;
  }
  if (array->data) {
    // ensure that data and capacity values are consistent
    assert(array->capacity > 0);
    // finalize all array elements
    for (size_t i = 0; i < array->capacity; ++i) {
      ht_nav_variables__msg__HtNavTireOut__fini(&array->data[i]);
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

ht_nav_variables__msg__HtNavTireOut__Sequence *
ht_nav_variables__msg__HtNavTireOut__Sequence__create(size_t size)
{
  ht_nav_variables__msg__HtNavTireOut__Sequence * array = (ht_nav_variables__msg__HtNavTireOut__Sequence *)malloc(sizeof(ht_nav_variables__msg__HtNavTireOut__Sequence));
  if (!array) {
    return NULL;
  }
  bool success = ht_nav_variables__msg__HtNavTireOut__Sequence__init(array, size);
  if (!success) {
    free(array);
    return NULL;
  }
  return array;
}

void
ht_nav_variables__msg__HtNavTireOut__Sequence__destroy(ht_nav_variables__msg__HtNavTireOut__Sequence * array)
{
  if (array) {
    ht_nav_variables__msg__HtNavTireOut__Sequence__fini(array);
  }
  free(array);
}
