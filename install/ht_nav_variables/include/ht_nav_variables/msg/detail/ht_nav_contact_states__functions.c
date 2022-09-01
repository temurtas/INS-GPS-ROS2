// generated from rosidl_generator_c/resource/idl__functions.c.em
// with input from ht_nav_variables:msg/HtNavContactStates.idl
// generated code does not contain a copyright notice
#include "ht_nav_variables/msg/detail/ht_nav_contact_states__functions.h"

#include <assert.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>


// Include directives for member types
// Member `fl_wheel_contact_states`
// Member `fr_wheel_contact_states`
// Member `rl_wheel_contact_states`
// Member `rr_wheel_contact_states`
#include "ht_nav_variables/msg/detail/ht_nav_contact_state__functions.h"

bool
ht_nav_variables__msg__HtNavContactStates__init(ht_nav_variables__msg__HtNavContactStates * msg)
{
  if (!msg) {
    return false;
  }
  // time
  // fl_wheel_contact_states
  if (!ht_nav_variables__msg__HtNavContactState__init(&msg->fl_wheel_contact_states)) {
    ht_nav_variables__msg__HtNavContactStates__fini(msg);
    return false;
  }
  // fr_wheel_contact_states
  if (!ht_nav_variables__msg__HtNavContactState__init(&msg->fr_wheel_contact_states)) {
    ht_nav_variables__msg__HtNavContactStates__fini(msg);
    return false;
  }
  // rl_wheel_contact_states
  if (!ht_nav_variables__msg__HtNavContactState__init(&msg->rl_wheel_contact_states)) {
    ht_nav_variables__msg__HtNavContactStates__fini(msg);
    return false;
  }
  // rr_wheel_contact_states
  if (!ht_nav_variables__msg__HtNavContactState__init(&msg->rr_wheel_contact_states)) {
    ht_nav_variables__msg__HtNavContactStates__fini(msg);
    return false;
  }
  return true;
}

void
ht_nav_variables__msg__HtNavContactStates__fini(ht_nav_variables__msg__HtNavContactStates * msg)
{
  if (!msg) {
    return;
  }
  // time
  // fl_wheel_contact_states
  ht_nav_variables__msg__HtNavContactState__fini(&msg->fl_wheel_contact_states);
  // fr_wheel_contact_states
  ht_nav_variables__msg__HtNavContactState__fini(&msg->fr_wheel_contact_states);
  // rl_wheel_contact_states
  ht_nav_variables__msg__HtNavContactState__fini(&msg->rl_wheel_contact_states);
  // rr_wheel_contact_states
  ht_nav_variables__msg__HtNavContactState__fini(&msg->rr_wheel_contact_states);
}

ht_nav_variables__msg__HtNavContactStates *
ht_nav_variables__msg__HtNavContactStates__create()
{
  ht_nav_variables__msg__HtNavContactStates * msg = (ht_nav_variables__msg__HtNavContactStates *)malloc(sizeof(ht_nav_variables__msg__HtNavContactStates));
  if (!msg) {
    return NULL;
  }
  memset(msg, 0, sizeof(ht_nav_variables__msg__HtNavContactStates));
  bool success = ht_nav_variables__msg__HtNavContactStates__init(msg);
  if (!success) {
    free(msg);
    return NULL;
  }
  return msg;
}

void
ht_nav_variables__msg__HtNavContactStates__destroy(ht_nav_variables__msg__HtNavContactStates * msg)
{
  if (msg) {
    ht_nav_variables__msg__HtNavContactStates__fini(msg);
  }
  free(msg);
}


bool
ht_nav_variables__msg__HtNavContactStates__Sequence__init(ht_nav_variables__msg__HtNavContactStates__Sequence * array, size_t size)
{
  if (!array) {
    return false;
  }
  ht_nav_variables__msg__HtNavContactStates * data = NULL;
  if (size) {
    data = (ht_nav_variables__msg__HtNavContactStates *)calloc(size, sizeof(ht_nav_variables__msg__HtNavContactStates));
    if (!data) {
      return false;
    }
    // initialize all array elements
    size_t i;
    for (i = 0; i < size; ++i) {
      bool success = ht_nav_variables__msg__HtNavContactStates__init(&data[i]);
      if (!success) {
        break;
      }
    }
    if (i < size) {
      // if initialization failed finalize the already initialized array elements
      for (; i > 0; --i) {
        ht_nav_variables__msg__HtNavContactStates__fini(&data[i - 1]);
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
ht_nav_variables__msg__HtNavContactStates__Sequence__fini(ht_nav_variables__msg__HtNavContactStates__Sequence * array)
{
  if (!array) {
    return;
  }
  if (array->data) {
    // ensure that data and capacity values are consistent
    assert(array->capacity > 0);
    // finalize all array elements
    for (size_t i = 0; i < array->capacity; ++i) {
      ht_nav_variables__msg__HtNavContactStates__fini(&array->data[i]);
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

ht_nav_variables__msg__HtNavContactStates__Sequence *
ht_nav_variables__msg__HtNavContactStates__Sequence__create(size_t size)
{
  ht_nav_variables__msg__HtNavContactStates__Sequence * array = (ht_nav_variables__msg__HtNavContactStates__Sequence *)malloc(sizeof(ht_nav_variables__msg__HtNavContactStates__Sequence));
  if (!array) {
    return NULL;
  }
  bool success = ht_nav_variables__msg__HtNavContactStates__Sequence__init(array, size);
  if (!success) {
    free(array);
    return NULL;
  }
  return array;
}

void
ht_nav_variables__msg__HtNavContactStates__Sequence__destroy(ht_nav_variables__msg__HtNavContactStates__Sequence * array)
{
  if (array) {
    ht_nav_variables__msg__HtNavContactStates__Sequence__fini(array);
  }
  free(array);
}
