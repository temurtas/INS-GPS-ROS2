cmake_minimum_required(VERSION 3.5)
project(ht_nav_variables)

# Default to C99
if(NOT CMAKE_C_STANDARD)
  set(CMAKE_C_STANDARD 99)
endif()

# Default to C++14
if(NOT CMAKE_CXX_STANDARD)
  set(CMAKE_CXX_STANDARD 14)
endif()

if(CMAKE_COMPILER_IS_GNUCXX OR CMAKE_CXX_COMPILER_ID MATCHES "Clang")
  add_compile_options(-Wall -Wextra -Wpedantic)
endif()

# find dependencies
find_package(ament_cmake REQUIRED)
# uncomment the following section in order to fill in
# further dependencies manually.
# find_package(<dependency> REQUIRED)
find_package(rosidl_default_generators REQUIRED)
find_package(rclcpp REQUIRED)

rosidl_generate_interfaces(${PROJECT_NAME}
  "msg/HtNavErrorVector.msg"
  "msg/HtNavEuler.msg"
  "msg/HtNavGpsData.msg"
  "msg/HtNavImuData.msg"
  "msg/HtNavKalmanOut.msg"
  "msg/HtNavStrapOut.msg"
  "msg/HtNavStrapCarOut.msg"
  "msg/HtNavPoint.msg"
  "msg/HtNavVector3.msg"
  "msg/HtNavQuaternion.msg"
  "msg/HtNavDeneme.msg"
  "msg/HtNavWheelVector.msg"
  "msg/HtNavJointState.msg"
  "msg/HtNavTireOut.msg"
  "msg/HtNavVehicleDebug.msg"
  )

#set(msg_files
#  "msg/ht_error_vector.msg.msg"
#  "msg/ht_euler.msg"
#  "msg/ht_gps_data.msg"
#  "msg/ht_imu_data.msg"
#  "msg/ht_kalman_out.msg"
#  "msg/ht_strap_out.msg"
#)

#set(srv_files
#  "srv/Service1.srv"
#  "srv/Service2.srv"
#   # etc
#  )

#rosidl_generate_interfaces(${PROJECT_NAME}
#  ${msg_files}
#  #${srv_files}
#)

if(BUILD_TESTING)
  find_package(ament_lint_auto REQUIRED)
  # the following line skips the linter which checks for copyrights
  # uncomment the line when a copyright and license is not present in all source files
  #set(ament_cmake_copyright_FOUND TRUE)
  # the following line skips cpplint (only works in a git repo)
  # uncomment the line when this package is not in a git repo
  #set(ament_cmake_cpplint_FOUND TRUE)
  ament_lint_auto_find_test_dependencies()
endif()

ament_package()
