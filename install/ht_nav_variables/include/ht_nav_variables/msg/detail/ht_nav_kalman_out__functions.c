// generated from rosidl_generator_c/resource/idl__functions.c.em
// with input from ht_nav_variables:msg/HtNavKalmanOut.idl
// generated code does not contain a copyright notice
#include "ht_nav_variables/msg/detail/ht_nav_kalman_out__functions.h"

#include <assert.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>


// Include directives for member types
// Member `pos_err`
// Member `vel_err`
// Member `att_err`
// Member `bias`
// Member `drift`
#include "ht_nav_variables/msg/detail/ht_nav_error_vector__functions.h"

bool
ht_nav_variables__msg__HtNavKalmanOut__init(ht_nav_variables__msg__HtNavKalmanOut * msg)
{
  if (!msg) {
    return false;
  }
  // time
  // pos_err
  if (!ht_nav_variables__msg__HtNavErrorVector__init(&msg->pos_err)) {
    ht_nav_variables__msg__HtNavKalmanOut__fini(msg);
    return false;
  }
  // vel_err
  if (!ht_nav_variables__msg__HtNavErrorVector__init(&msg->vel_err)) {
    ht_nav_variables__msg__HtNavKalmanOut__fini(msg);
    return false;
  }
  // att_err
  if (!ht_nav_variables__msg__HtNavErrorVector__init(&msg->att_err)) {
    ht_nav_variables__msg__HtNavKalmanOut__fini(msg);
    return false;
  }
  // bias
  if (!ht_nav_variables__msg__HtNavErrorVector__init(&msg->bias)) {
    ht_nav_variables__msg__HtNavKalmanOut__fini(msg);
    return false;
  }
  // drift
  if (!ht_nav_variables__msg__HtNavErrorVector__init(&msg->drift)) {
    ht_nav_variables__msg__HtNavKalmanOut__fini(msg);
    return false;
  }
  return true;
}

void
ht_nav_variables__msg__HtNavKalmanOut__fini(ht_nav_variables__msg__HtNavKalmanOut * msg)
{
  if (!msg) {
    return;
  }
  // time
  // pos_err
  ht_nav_variables__msg__HtNavErrorVector__fini(&msg->pos_err);
  // vel_err
  ht_nav_variables__msg__HtNavErrorVector__fini(&msg->vel_err);
  // att_err
  ht_nav_variables__msg__HtNavErrorVector__fini(&msg->att_err);
  // bias
  ht_nav_variables__msg__HtNavErrorVector__fini(&msg->bias);
  // drift
  ht_nav_variables__msg__HtNavErrorVector__fini(&msg->drift);
}

ht_nav_variables__msg__HtNavKalmanOut *
ht_nav_variables__msg__HtNavKalmanOut__create()
{
  ht_nav_variables__msg__HtNavKalmanOut * msg = (ht_nav_variables__msg__HtNavKalmanOut *)malloc(sizeof(ht_nav_variables__msg__HtNavKalmanOut));
  if (!msg) {
    return NULL;
  }
  memset(msg, 0, sizeof(ht_nav_variables__msg__HtNavKalmanOut));
  bool success = ht_nav_variables__msg__HtNavKalmanOut__init(msg);
  if (!success) {
    free(msg);
    return NULL;
  }
  return msg;
}

void
ht_nav_variables__msg__HtNavKalmanOut__destroy(ht_nav_variables__msg__HtNavKalmanOut * msg)
{
  if (msg) {
    ht_nav_variables__msg__HtNavKalmanOut__fini(msg);
  }
  free(msg);
}


bool
ht_nav_variables__msg__HtNavKalmanOut__Sequence__init(ht_nav_variables__msg__HtNavKalmanOut__Sequence * array, size_t size)
{
  if (!array) {
    return false;
  }
  ht_nav_variables__msg__HtNavKalmanOut * data = NULL;
  if (size) {
    data = (ht_nav_variables__msg__HtNavKalmanOut *)calloc(size, sizeof(ht_nav_variables__msg__HtNavKalmanOut));
    if (!data) {
      return false;
    }
    // initialize all array elements
    size_t i;
    for (i = 0; i < size; ++i) {
      bool success = ht_nav_variables__msg__HtNavKalmanOut__init(&data[i]);
      if (!success) {
        break;
      }
    }
    if (i < size) {
      // if initialization failed finalize the already initialized array elements
      for (; i > 0; --i) {
        ht_nav_variables__msg__HtNavKalmanOut__fini(&data[i - 1]);
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
ht_nav_variables__msg__HtNavKalmanOut__Sequence__fini(ht_nav_variables__msg__HtNavKalmanOut__Sequence * array)
{
  if (!array) {
    return;
  }
  if (array->data) {
    // ensure that data and capacity values are consistent
    assert(array->capacity > 0);
    // finalize all array elements
    for (size_t i = 0; i < array->capacity; ++i) {
      ht_nav_variables__msg__HtNavKalmanOut__fini(&array->data[i]);
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

ht_nav_variables__msg__HtNavKalmanOut__Sequence *
ht_nav_variables__msg__HtNavKalmanOut__Sequence__create(size_t size)
{
  ht_nav_variables__msg__HtNavKalmanOut__Sequence * array = (ht_nav_variables__msg__HtNavKalmanOut__Sequence *)malloc(sizeof(ht_nav_variables__msg__HtNavKalmanOut__Sequence));
  if (!array) {
    return NULL;
  }
  bool success = ht_nav_variables__msg__HtNavKalmanOut__Sequence__init(array, size);
  if (!success) {
    free(array);
    return NULL;
  }
  return array;
}

void
ht_nav_variables__msg__HtNavKalmanOut__Sequence__destroy(ht_nav_variables__msg__HtNavKalmanOut__Sequence * array)
{
  if (array) {
    ht_nav_variables__msg__HtNavKalmanOut__Sequence__fini(array);
  }
  free(array);
}
