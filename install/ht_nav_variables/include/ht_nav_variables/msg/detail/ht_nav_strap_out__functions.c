// generated from rosidl_generator_c/resource/idl__functions.c.em
// with input from ht_nav_variables:msg/HtNavStrapOut.idl
// generated code does not contain a copyright notice
#include "ht_nav_variables/msg/detail/ht_nav_strap_out__functions.h"

#include <assert.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>


// Include directives for member types
// Member `pos`
#include "ht_nav_variables/msg/detail/ht_nav_point__functions.h"
// Member `vel`
#include "ht_nav_variables/msg/detail/ht_nav_vector3__functions.h"
// Member `euler`
#include "ht_nav_variables/msg/detail/ht_nav_euler__functions.h"
// Member `quaternion`
#include "ht_nav_variables/msg/detail/ht_nav_quaternion__functions.h"

bool
ht_nav_variables__msg__HtNavStrapOut__init(ht_nav_variables__msg__HtNavStrapOut * msg)
{
  if (!msg) {
    return false;
  }
  // pos
  if (!ht_nav_variables__msg__HtNavPoint__init(&msg->pos)) {
    ht_nav_variables__msg__HtNavStrapOut__fini(msg);
    return false;
  }
  // vel
  if (!ht_nav_variables__msg__HtNavVector3__init(&msg->vel)) {
    ht_nav_variables__msg__HtNavStrapOut__fini(msg);
    return false;
  }
  // euler
  if (!ht_nav_variables__msg__HtNavEuler__init(&msg->euler)) {
    ht_nav_variables__msg__HtNavStrapOut__fini(msg);
    return false;
  }
  // quaternion
  if (!ht_nav_variables__msg__HtNavQuaternion__init(&msg->quaternion)) {
    ht_nav_variables__msg__HtNavStrapOut__fini(msg);
    return false;
  }
  return true;
}

void
ht_nav_variables__msg__HtNavStrapOut__fini(ht_nav_variables__msg__HtNavStrapOut * msg)
{
  if (!msg) {
    return;
  }
  // pos
  ht_nav_variables__msg__HtNavPoint__fini(&msg->pos);
  // vel
  ht_nav_variables__msg__HtNavVector3__fini(&msg->vel);
  // euler
  ht_nav_variables__msg__HtNavEuler__fini(&msg->euler);
  // quaternion
  ht_nav_variables__msg__HtNavQuaternion__fini(&msg->quaternion);
}

ht_nav_variables__msg__HtNavStrapOut *
ht_nav_variables__msg__HtNavStrapOut__create()
{
  ht_nav_variables__msg__HtNavStrapOut * msg = (ht_nav_variables__msg__HtNavStrapOut *)malloc(sizeof(ht_nav_variables__msg__HtNavStrapOut));
  if (!msg) {
    return NULL;
  }
  memset(msg, 0, sizeof(ht_nav_variables__msg__HtNavStrapOut));
  bool success = ht_nav_variables__msg__HtNavStrapOut__init(msg);
  if (!success) {
    free(msg);
    return NULL;
  }
  return msg;
}

void
ht_nav_variables__msg__HtNavStrapOut__destroy(ht_nav_variables__msg__HtNavStrapOut * msg)
{
  if (msg) {
    ht_nav_variables__msg__HtNavStrapOut__fini(msg);
  }
  free(msg);
}


bool
ht_nav_variables__msg__HtNavStrapOut__Sequence__init(ht_nav_variables__msg__HtNavStrapOut__Sequence * array, size_t size)
{
  if (!array) {
    return false;
  }
  ht_nav_variables__msg__HtNavStrapOut * data = NULL;
  if (size) {
    data = (ht_nav_variables__msg__HtNavStrapOut *)calloc(size, sizeof(ht_nav_variables__msg__HtNavStrapOut));
    if (!data) {
      return false;
    }
    // initialize all array elements
    size_t i;
    for (i = 0; i < size; ++i) {
      bool success = ht_nav_variables__msg__HtNavStrapOut__init(&data[i]);
      if (!success) {
        break;
      }
    }
    if (i < size) {
      // if initialization failed finalize the already initialized array elements
      for (; i > 0; --i) {
        ht_nav_variables__msg__HtNavStrapOut__fini(&data[i - 1]);
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
ht_nav_variables__msg__HtNavStrapOut__Sequence__fini(ht_nav_variables__msg__HtNavStrapOut__Sequence * array)
{
  if (!array) {
    return;
  }
  if (array->data) {
    // ensure that data and capacity values are consistent
    assert(array->capacity > 0);
    // finalize all array elements
    for (size_t i = 0; i < array->capacity; ++i) {
      ht_nav_variables__msg__HtNavStrapOut__fini(&array->data[i]);
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

ht_nav_variables__msg__HtNavStrapOut__Sequence *
ht_nav_variables__msg__HtNavStrapOut__Sequence__create(size_t size)
{
  ht_nav_variables__msg__HtNavStrapOut__Sequence * array = (ht_nav_variables__msg__HtNavStrapOut__Sequence *)malloc(sizeof(ht_nav_variables__msg__HtNavStrapOut__Sequence));
  if (!array) {
    return NULL;
  }
  bool success = ht_nav_variables__msg__HtNavStrapOut__Sequence__init(array, size);
  if (!success) {
    free(array);
    return NULL;
  }
  return array;
}

void
ht_nav_variables__msg__HtNavStrapOut__Sequence__destroy(ht_nav_variables__msg__HtNavStrapOut__Sequence * array)
{
  if (array) {
    ht_nav_variables__msg__HtNavStrapOut__Sequence__fini(array);
  }
  free(array);
}
