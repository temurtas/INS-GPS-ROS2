# Copyright 2016 Open Source Robotics Foundation, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import rclpy
from rclpy.node import Node
from pathlib import Path

from rclpy.qos import qos_profile_sensor_data

from sensor_msgs.msg import NavSatFix
from sensor_msgs.msg import JointState
from sensor_msgs.msg import Imu

from ht_strap_package.config import base_path

# base_path = Path("/home/temur/INS-GPS-ws/INS-GPS-Matlab/veriler/veri1_to_Dogukan/")           #Ubuntu Path

# FRONT_RIGHT, 
# FRONT_LEFT, 
# REAR_RIGHT, 
# REAR_LEFT, 
# IMU_LINK  

fr_out_data_path = base_path / "front_right_wheel_pva.txt"
fr_out_data_txt = open(fr_out_data_path, 'w')

fl_out_data_path = base_path / "front_left_wheel_pva.txt"
fl_out_data_txt = open(fl_out_data_path, 'w')

rr_out_data_path = base_path / "rear_right_wheel_pva.txt"
rr_out_data_txt = open(rr_out_data_path, 'w')

rl_out_data_path = base_path / "rear_left_wheel_pva.txt"
rl_out_data_txt = open(rl_out_data_path, 'w')

imu_out_data_path = base_path / "imu_link_pva.txt"
imu_out_data_txt = open(imu_out_data_path, 'w')

# gps_data_path = base_path / "gps_data_ideal_gazebo.txt"
# gps_data_gazebo_txt = open(gps_data_path, 'w')

joint_state_data_path = base_path / "joint_states.txt"
joint_input_data_txt = open(joint_state_data_path, 'w')

class RobotStateListener(Node):

    def __init__(self,qos_profile):
        super().__init__('minimal_subscriber')
        
        self.joint_state_subscription = self.create_subscription(
            JointState, 
            'kobra_mk5/joint_states', 
            self.joint_listener_callback, 
            qos_profile=qos_profile)
        
        self.joint_state_subscription = self.create_subscription(
            JointState, 
            'kobra_mk5/front_right_link_states', 
            self.front_right_link_listener_callback, 
            qos_profile=qos_profile)

        self.joint_state_subscription = self.create_subscription(
            JointState, 
            'kobra_mk5/front_left_link_states', 
            self.front_left_link_listener_callback, 
            qos_profile=qos_profile)

        self.joint_state_subscription = self.create_subscription(
            JointState, 
            'kobra_mk5/rear_right_link_states', 
            self.rear_right_link_listener_callback, 
            qos_profile=qos_profile)

        self.joint_state_subscription = self.create_subscription(
            JointState, 
            'kobra_mk5/rear_left_link_states', 
            self.rear_left_link_listener_callback, 
            qos_profile=qos_profile)

        self.joint_state_subscription = self.create_subscription(
            JointState, 
            'kobra_mk5/imu_link_states', 
            self.imu_link_listener_callback, 
            qos_profile=qos_profile)

        # FRONT_RIGHT, # Front right wheel # front_right_link_states
        # FRONT_LEFT,  # Front left wheel  # front_left_link_states
        # REAR_RIGHT,  # Rear right wheel  # rear_right_link_states
        # REAR_LEFT,   # Rear left wheel   # rear_left_link_states
        # IMU_LINK     # Steering wheel    # imu_link_states
        
        self.gps_ideal_subscription = self.create_subscription(
            NavSatFix,
            'kobra_mk5/ideal_gps_data',
            self.gps_sub_cb,
            qos_profile=qos_profile)
                  
        self.strap_imu_sub = self.create_subscription(
            Imu, 
            'kobra_mk5/imu_data_ideal', 
            self.sub_cb_imu_data, 
            qos_profile=qos_profile)

        self.joint_state_subscription  # prevent unused variable warning
        self.gps_ideal_subscription  # prevent unused variable warning
        self.strap_imu_sub  # prevent unused variable warning

        self.zaman_ref = 0.0
        self.zaman_ilk = self.get_clock().now().nanoseconds * 1e-6 #msec

    def joint_listener_callback(self, msg):
        # self.get_logger().info('I heard joint namse as: "%f"' % msg.velocity[1])
        self.zaman_ref = self.get_clock().now().nanoseconds * 1e-6 #msec
        self.zaman_ref = self.zaman_ref - self.zaman_ilk
        print(str(self.zaman_ref), str(msg.position[0]), str(msg.velocity[0]), str(msg.position[1]), str(msg.velocity[1]), str(msg.position[2]), str(msg.velocity[2]), str(msg.position[3]), str(msg.velocity[3]), str(msg.position[4]), str(msg.velocity[4]), sep='\t', file=joint_input_data_txt)
        
    def front_right_link_listener_callback(self, msg):
        # self.get_logger().info('I heard joint namse as: "%f"' % msg.velocity[1])
        self.zaman_ref = self.get_clock().now().nanoseconds * 1e-6 #msec
        self.zaman_ref = self.zaman_ref - self.zaman_ilk
        print(str(self.zaman_ref), str(msg.position[0]), str(msg.position[1]), str(msg.position[2]), str(msg.velocity[0]), str(msg.velocity[1]), str(msg.velocity[2]), str(msg.effort[0]), str(msg.effort[1]), str(msg.effort[2]), sep='\t', file=fr_out_data_txt)

    def front_left_link_listener_callback(self, msg):
        # self.get_logger().info('I heard joint namse as: "%f"' % msg.velocity[1])
        self.zaman_ref = self.get_clock().now().nanoseconds * 1e-6 #msec
        self.zaman_ref = self.zaman_ref - self.zaman_ilk
        print(str(self.zaman_ref), str(msg.position[0]), str(msg.position[1]), str(msg.position[2]), str(msg.velocity[0]), str(msg.velocity[1]), str(msg.velocity[2]), str(msg.effort[0]), str(msg.effort[1]), str(msg.effort[2]), sep='\t', file=fl_out_data_txt)

    def rear_right_link_listener_callback(self, msg):
        # self.get_logger().info('I heard joint namse as: "%f"' % msg.velocity[1])
        self.zaman_ref = self.get_clock().now().nanoseconds * 1e-6 #msec
        self.zaman_ref = self.zaman_ref - self.zaman_ilk
        print(str(self.zaman_ref), str(msg.position[0]), str(msg.position[1]), str(msg.position[2]), str(msg.velocity[0]), str(msg.velocity[1]), str(msg.velocity[2]), str(msg.effort[0]), str(msg.effort[1]), str(msg.effort[2]), sep='\t', file=rr_out_data_txt)

    def rear_left_link_listener_callback(self, msg):
        # self.get_logger().info('I heard joint namse as: "%f"' % msg.velocity[1])
        self.zaman_ref = self.get_clock().now().nanoseconds * 1e-6 #msec
        self.zaman_ref = self.zaman_ref - self.zaman_ilk
        print(str(self.zaman_ref), str(msg.position[0]), str(msg.position[1]), str(msg.position[2]), str(msg.velocity[0]), str(msg.velocity[1]), str(msg.velocity[2]), str(msg.effort[0]), str(msg.effort[1]), str(msg.effort[2]), sep='\t', file=rl_out_data_txt)

    def imu_link_listener_callback(self, msg):
        # self.get_logger().info('I heard joint namse as: "%f"' % msg.velocity[1])
        self.zaman_ref = self.get_clock().now().nanoseconds * 1e-6 #msec
        self.zaman_ref = self.zaman_ref - self.zaman_ilk
        print(str(self.zaman_ref), str(msg.position[0]), str(msg.position[1]), str(msg.position[2]), str(msg.velocity[0]), str(msg.velocity[1]), str(msg.velocity[2]), str(msg.effort[0]), str(msg.effort[1]), str(msg.effort[2]), sep='\t', file=imu_out_data_txt)


    def gps_sub_cb(self, msg):      
        # self.gps_data_ideal.gps_pos.x = msg.latitude 
        # self.gps_data_ideal.gps_pos.y = msg.longitude
        # self.gps_data_ideal.gps_pos.z = msg.altitude

        # self.gps_data_ideal.gps_vel.x = 0.0
        # self.gps_data_ideal.gps_vel.y = 0.0
        # self.gps_data_ideal.gps_vel.z = 0.0

        self.zaman_ref = self.get_clock().now().nanoseconds * 1e-6 #msec
        self.zaman_ref = self.zaman_ref - self.zaman_ilk
        # print(str(self.zaman_ref), str(self.gps_data_ideal.gps_pos.x), str(self.gps_data_ideal.gps_pos.y), str(self.gps_data_ideal.gps_pos.z), str(self.gps_data_ideal.gps_vel.x), str(self.gps_data_ideal.gps_vel.y), str(self.gps_data_ideal.gps_vel.z), sep='\t', file=gps_data_gazebo_txt)


    def sub_cb_imu_data(self, msg):
        # self.imu_data.vel_diff.x = -msg.linear_acceleration.y  
        # self.imu_data.vel_diff.y = -msg.linear_acceleration.x 
        # self.imu_data.vel_diff.z = -msg.linear_acceleration.z 

        # self.imu_data.ang_diff.x = -msg.angular_velocity.y 
        # self.imu_data.ang_diff.y = -msg.angular_velocity.x 
        # self.imu_data.ang_diff.z = -msg.angular_velocity.z 

        self.zaman_ref = self.get_clock().now().nanoseconds * 1e-6 #msec
        self.zaman_ref = self.zaman_ref - self.zaman_ilk
        # print(str(self.zaman_ref), str(self.imu_data.ang_diff.x), str(self.imu_data.ang_diff.y), str(self.imu_data.ang_diff.z), str(self.imu_data.vel_diff.x), str(self.imu_data.vel_diff.y), str(self.imu_data.vel_diff.z), sep='\t', file=imu_data_gazebo_txt)


def main(args=None):
    rclpy.init(args=args)

    custom_qos_profile = qos_profile_sensor_data

    minimal_subscriber = RobotStateListener(custom_qos_profile)

    rclpy.spin(minimal_subscriber)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    minimal_subscriber.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
