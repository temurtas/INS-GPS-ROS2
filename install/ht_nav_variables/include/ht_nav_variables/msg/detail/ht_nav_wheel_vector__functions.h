// generated from rosidl_generator_c/resource/idl__functions.h.em
// with input from ht_nav_variables:msg/HtNavWheelVector.idl
// generated code does not contain a copyright notice

#ifndef HT_NAV_VARIABLES__MSG__DETAIL__HT_NAV_WHEEL_VECTOR__FUNCTIONS_H_
#define HT_NAV_VARIABLES__MSG__DETAIL__HT_NAV_WHEEL_VECTOR__FUNCTIONS_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stdlib.h>

#include "rosidl_runtime_c/visibility_control.h"
#include "ht_nav_variables/msg/rosidl_generator_c__visibility_control.h"

#include "ht_nav_variables/msg/detail/ht_nav_wheel_vector__struct.h"

/// Initialize msg/HtNavWheelVector message.
/**
 * If the init function is called twice for the same message without
 * calling fini inbetween previously allocated memory will be leaked.
 * \param[in,out] msg The previously allocated message pointer.
 * Fields without a default value will not be initialized by this function.
 * You might want to call memset(msg, 0, sizeof(
 * ht_nav_variables__msg__HtNavWheelVector
 * )) before or use
 * ht_nav_variables__msg__HtNavWheelVector__create()
 * to allocate and initialize the message.
 * \return true if initialization was successful, otherwise false
 */
ROSIDL_GENERATOR_C_PUBLIC_ht_nav_variables
bool
ht_nav_variables__msg__HtNavWheelVector__init(ht_nav_variables__msg__HtNavWheelVector * msg);

/// Finalize msg/HtNavWheelVector message.
/**
 * \param[in,out] msg The allocated message pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_ht_nav_variables
void
ht_nav_variables__msg__HtNavWheelVector__fini(ht_nav_variables__msg__HtNavWheelVector * msg);

/// Create msg/HtNavWheelVector message.
/**
 * It allocates the memory for the message, sets the memory to zero, and
 * calls
 * ht_nav_variables__msg__HtNavWheelVector__init().
 * \return The pointer to the initialized message if successful,
 * otherwise NULL
 */
ROSIDL_GENERATOR_C_PUBLIC_ht_nav_variables
ht_nav_variables__msg__HtNavWheelVector *
ht_nav_variables__msg__HtNavWheelVector__create();

/// Destroy msg/HtNavWheelVector message.
/**
 * It calls
 * ht_nav_variables__msg__HtNavWheelVector__fini()
 * and frees the memory of the message.
 * \param[in,out] msg The allocated message pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_ht_nav_variables
void
ht_nav_variables__msg__HtNavWheelVector__destroy(ht_nav_variables__msg__HtNavWheelVector * msg);


/// Initialize array of msg/HtNavWheelVector messages.
/**
 * It allocates the memory for the number of elements and calls
 * ht_nav_variables__msg__HtNavWheelVector__init()
 * for each element of the array.
 * \param[in,out] array The allocated array pointer.
 * \param[in] size The size / capacity of the array.
 * \return true if initialization was successful, otherwise false
 * If the array pointer is valid and the size is zero it is guaranteed
 # to return true.
 */
ROSIDL_GENERATOR_C_PUBLIC_ht_nav_variables
bool
ht_nav_variables__msg__HtNavWheelVector__Sequence__init(ht_nav_variables__msg__HtNavWheelVector__Sequence * array, size_t size);

/// Finalize array of msg/HtNavWheelVector messages.
/**
 * It calls
 * ht_nav_variables__msg__HtNavWheelVector__fini()
 * for each element of the array and frees the memory for the number of
 * elements.
 * \param[in,out] array The initialized array pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_ht_nav_variables
void
ht_nav_variables__msg__HtNavWheelVector__Sequence__fini(ht_nav_variables__msg__HtNavWheelVector__Sequence * array);

/// Create array of msg/HtNavWheelVector messages.
/**
 * It allocates the memory for the array and calls
 * ht_nav_variables__msg__HtNavWheelVector__Sequence__init().
 * \param[in] size The size / capacity of the array.
 * \return The pointer to the initialized array if successful, otherwise NULL
 */
ROSIDL_GENERATOR_C_PUBLIC_ht_nav_variables
ht_nav_variables__msg__HtNavWheelVector__Sequence *
ht_nav_variables__msg__HtNavWheelVector__Sequence__create(size_t size);

/// Destroy array of msg/HtNavWheelVector messages.
/**
 * It calls
 * ht_nav_variables__msg__HtNavWheelVector__Sequence__fini()
 * on the array,
 * and frees the memory of the array.
 * \param[in,out] array The initialized array pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_ht_nav_variables
void
ht_nav_variables__msg__HtNavWheelVector__Sequence__destroy(ht_nav_variables__msg__HtNavWheelVector__Sequence * array);

#ifdef __cplusplus
}
#endif

#endif  // HT_NAV_VARIABLES__MSG__DETAIL__HT_NAV_WHEEL_VECTOR__FUNCTIONS_H_
