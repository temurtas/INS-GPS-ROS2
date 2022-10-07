#!/bin/bash
# A sample Bash script, by Ryan

cd ~/INS-GPS-ROS2
rosdep install -i --from-path src --rosdistro foxy -y
export RMW_IMPLEMENTATION=rmw_cyclonedds_cpp

export GAZEBO_PLUGIN_PATH=${GAZEBO_PLUGIN_PATH}:~/ws/src/gazebo_ros_pkgs/build/gazebo_plugins
export GAZEBO_PLUGIN_PATH=${GAZEBO_PLUGIN_PATH}:~/gazebo_wheel_slip_plugin/build

colcon build --allow-overriding ht_nav_variables ht_strap_package

. install/setup.bash

RMW_IMPLEMENTATION=rmw_cyclonedds_cpp ros2 launch ht_strap_package ht_gazebo_constant_circle.launch.py
killall -9 gzserver gzclient
