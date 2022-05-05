// generated from rosidl_generator_c/resource/idl__functions.c.em
// with input from ht_nav_variables:msg/HtNavImuData.idl
// generated code does not contain a copyright notice
#include "ht_nav_variables/msg/detail/ht_nav_imu_data__functions.h"

#include <assert.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>


// Include directives for member types
// Member `vel_diff`
// Member `ang_diff`
#include "ht_nav_variables/msg/detail/ht_nav_vector3__functions.h"

bool
ht_nav_variables__msg__HtNavImuData__init(ht_nav_variables__msg__HtNavImuData * msg)
{
  if (!msg) {
    return false;
  }
  // time
  // vel_diff
  if (!ht_nav_variables__msg__HtNavVector3__init(&msg->vel_diff)) {
    ht_nav_variables__msg__HtNavImuData__fini(msg);
    return false;
  }
  // ang_diff
  if (!ht_nav_variables__msg__HtNavVector3__init(&msg->ang_diff)) {
    ht_nav_variables__msg__HtNavImuData__fini(msg);
    return false;
  }
  return true;
}

void
ht_nav_variables__msg__HtNavImuData__fini(ht_nav_variables__msg__HtNavImuData * msg)
{
  if (!msg) {
    return;
  }
  // time
  // vel_diff
  ht_nav_variables__msg__HtNavVector3__fini(&msg->vel_diff);
  // ang_diff
  ht_nav_variables__msg__HtNavVector3__fini(&msg->ang_diff);
}

ht_nav_variables__msg__HtNavImuData *
ht_nav_variables__msg__HtNavImuData__create()
{
  ht_nav_variables__msg__HtNavImuData * msg = (ht_nav_variables__msg__HtNavImuData *)malloc(sizeof(ht_nav_variables__msg__HtNavImuData));
  if (!msg) {
    return NULL;
  }
  memset(msg, 0, sizeof(ht_nav_variables__msg__HtNavImuData));
  bool success = ht_nav_variables__msg__HtNavImuData__init(msg);
  if (!success) {
    free(msg);
    return NULL;
  }
  return msg;
}

void
ht_nav_variables__msg__HtNavImuData__destroy(ht_nav_variables__msg__HtNavImuData * msg)
{
  if (msg) {
    ht_nav_variables__msg__HtNavImuData__fini(msg);
  }
  free(msg);
}


bool
ht_nav_variables__msg__HtNavImuData__Sequence__init(ht_nav_variables__msg__HtNavImuData__Sequence * array, size_t size)
{
  if (!array) {
    return false;
  }
  ht_nav_variables__msg__HtNavImuData * data = NULL;
  if (size) {
    data = (ht_nav_variables__msg__HtNavImuData *)calloc(size, sizeof(ht_nav_variables__msg__HtNavImuData));
    if (!data) {
      return false;
    }
    // initialize all array elements
    size_t i;
    for (i = 0; i < size; ++i) {
      bool success = ht_nav_variables__msg__HtNavImuData__init(&data[i]);
      if (!success) {
        break;
      }
    }
    if (i < size) {
      // if initialization failed finalize the already initialized array elements
      for (; i > 0; --i) {
        ht_nav_variables__msg__HtNavImuData__fini(&data[i - 1]);
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
ht_nav_variables__msg__HtNavImuData__Sequence__fini(ht_nav_variables__msg__HtNavImuData__Sequence * array)
{
  if (!array) {
    return;
  }
  if (array->data) {
    // ensure that data and capacity values are consistent
    assert(array->capacity > 0);
    // finalize all array elements
    for (size_t i = 0; i < array->capacity; ++i) {
      ht_nav_variables__msg__HtNavImuData__fini(&array->data[i]);
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

ht_nav_variables__msg__HtNavImuData__Sequence *
ht_nav_variables__msg__HtNavImuData__Sequence__create(size_t size)
{
  ht_nav_variables__msg__HtNavImuData__Sequence * array = (ht_nav_variables__msg__HtNavImuData__Sequence *)malloc(sizeof(ht_nav_variables__msg__HtNavImuData__Sequence));
  if (!array) {
    return NULL;
  }
  bool success = ht_nav_variables__msg__HtNavImuData__Sequence__init(array, size);
  if (!success) {
    free(array);
    return NULL;
  }
  return array;
}

void
ht_nav_variables__msg__HtNavImuData__Sequence__destroy(ht_nav_variables__msg__HtNavImuData__Sequence * array)
{
  if (array) {
    ht_nav_variables__msg__HtNavImuData__Sequence__fini(array);
  }
  free(array);
}
