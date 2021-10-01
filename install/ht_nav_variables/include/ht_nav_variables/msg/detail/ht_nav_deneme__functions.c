// generated from rosidl_generator_c/resource/idl__functions.c.em
// with input from ht_nav_variables:msg/HtNavDeneme.idl
// generated code does not contain a copyright notice
#include "ht_nav_variables/msg/detail/ht_nav_deneme__functions.h"

#include <assert.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>


bool
ht_nav_variables__msg__HtNavDeneme__init(ht_nav_variables__msg__HtNavDeneme * msg)
{
  if (!msg) {
    return false;
  }
  // num
  return true;
}

void
ht_nav_variables__msg__HtNavDeneme__fini(ht_nav_variables__msg__HtNavDeneme * msg)
{
  if (!msg) {
    return;
  }
  // num
}

ht_nav_variables__msg__HtNavDeneme *
ht_nav_variables__msg__HtNavDeneme__create()
{
  ht_nav_variables__msg__HtNavDeneme * msg = (ht_nav_variables__msg__HtNavDeneme *)malloc(sizeof(ht_nav_variables__msg__HtNavDeneme));
  if (!msg) {
    return NULL;
  }
  memset(msg, 0, sizeof(ht_nav_variables__msg__HtNavDeneme));
  bool success = ht_nav_variables__msg__HtNavDeneme__init(msg);
  if (!success) {
    free(msg);
    return NULL;
  }
  return msg;
}

void
ht_nav_variables__msg__HtNavDeneme__destroy(ht_nav_variables__msg__HtNavDeneme * msg)
{
  if (msg) {
    ht_nav_variables__msg__HtNavDeneme__fini(msg);
  }
  free(msg);
}


bool
ht_nav_variables__msg__HtNavDeneme__Sequence__init(ht_nav_variables__msg__HtNavDeneme__Sequence * array, size_t size)
{
  if (!array) {
    return false;
  }
  ht_nav_variables__msg__HtNavDeneme * data = NULL;
  if (size) {
    data = (ht_nav_variables__msg__HtNavDeneme *)calloc(size, sizeof(ht_nav_variables__msg__HtNavDeneme));
    if (!data) {
      return false;
    }
    // initialize all array elements
    size_t i;
    for (i = 0; i < size; ++i) {
      bool success = ht_nav_variables__msg__HtNavDeneme__init(&data[i]);
      if (!success) {
        break;
      }
    }
    if (i < size) {
      // if initialization failed finalize the already initialized array elements
      for (; i > 0; --i) {
        ht_nav_variables__msg__HtNavDeneme__fini(&data[i - 1]);
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
ht_nav_variables__msg__HtNavDeneme__Sequence__fini(ht_nav_variables__msg__HtNavDeneme__Sequence * array)
{
  if (!array) {
    return;
  }
  if (array->data) {
    // ensure that data and capacity values are consistent
    assert(array->capacity > 0);
    // finalize all array elements
    for (size_t i = 0; i < array->capacity; ++i) {
      ht_nav_variables__msg__HtNavDeneme__fini(&array->data[i]);
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

ht_nav_variables__msg__HtNavDeneme__Sequence *
ht_nav_variables__msg__HtNavDeneme__Sequence__create(size_t size)
{
  ht_nav_variables__msg__HtNavDeneme__Sequence * array = (ht_nav_variables__msg__HtNavDeneme__Sequence *)malloc(sizeof(ht_nav_variables__msg__HtNavDeneme__Sequence));
  if (!array) {
    return NULL;
  }
  bool success = ht_nav_variables__msg__HtNavDeneme__Sequence__init(array, size);
  if (!success) {
    free(array);
    return NULL;
  }
  return array;
}

void
ht_nav_variables__msg__HtNavDeneme__Sequence__destroy(ht_nav_variables__msg__HtNavDeneme__Sequence * array)
{
  if (array) {
    ht_nav_variables__msg__HtNavDeneme__Sequence__fini(array);
  }
  free(array);
}
