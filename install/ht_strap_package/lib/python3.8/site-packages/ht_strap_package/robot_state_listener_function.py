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

#from ht_nav_variables.msg import HtNavDeneme
from ht_nav_variables.msg import HtNavEuler
from ht_nav_variables.msg import HtNavJointState
from ht_nav_variables.msg import HtNavStrapOut
from ht_nav_variables.msg import HtNavGpsData
from ht_nav_variables.msg import HtNavImuData

from ht_strap_package.config import base_path
from ht_strap_package.config import DEG2RAD
from ht_strap_package.config import delta_t

#base_path = Path("/home/temur/INS-GPS-ws/INS-GPS-Matlab/veriler/veri1_to_Dogukan/")           #Ubuntu Path

# out_data_path = base_path / "joint_states_gazebo.txt"
# out_data_txt = open(out_data_path, 'w')

# gps_data_path = base_path / "gps_data_ideal_gazebo.txt"
# gps_data_gazebo_txt = open(gps_data_path, 'w')

# out_data_ideal_path = base_path / "strap_data_ideal_gazebo.txt"
# out_data_ideal_txt = open(out_data_ideal_path, 'w')

class RobotStateListener(Node):

    def __init__(self,qos_profile):
        super().__init__('minimal_subscriber')
        
        self.joint_state_subscription = self.create_subscription(
            JointState, 
            'kobra_mk5/joint_states', 
            self.listener_callback, 
            qos_profile=qos_profile)
        
        # self.gps_ideal_subscription = self.create_subscription(
        #     NavSatFix,
        #     'kobra_mk5/ideal_gps_data',
        #     self.gps_sub_cb,
        #     qos_profile=qos_profile)
        
        self.strap_ideal_subscription = self.create_subscription(
            HtNavStrapOut,
            'ht_nav_strap_data_onlyins',
            self.onlyins_listener_callback,
            qos_profile=qos_profile)
            
        self.strap_ideal_subscription = self.create_subscription(
            HtNavStrapOut,
            'ht_nav_strap_data_ideal',
            self.ideal_listener_callback,
            qos_profile=qos_profile)

        self.strap_imu_sub = self.create_subscription(
            Imu, 
            'kobra_mk5/imu_data_ideal', 
            self.sub_cb_imu_data, 
            qos_profile=qos_profile)

        self.joint_state_subscription  # prevent unused variable warning
        # self.gps_ideal_subscription  # prevent unused variable warning
        self.strap_ideal_subscription  # prevent unused variable warning
        self.strap_imu_sub  # prevent unused variable warning

        self.joint_state = HtNavJointState()
        self.gps_data_ideal = HtNavGpsData()
        self.imu_data = HtNavImuData()

        self.zaman_ref = 0.0
        self.zaman_ilk = self.get_clock().now().nanoseconds * 1e-6 #msec

        self.gazebo_time  = 0.0

    def listener_callback(self, msg):
        # self.get_logger().info('I heard joint namse as: "%f"' % msg.velocity[1])
        self.zaman_ref = self.get_clock().now().nanoseconds * 1e-6 #msec
        self.zaman_ref = self.zaman_ref - self.zaman_ilk
        
        self.joint_state.steering_angle.w1 = msg.position[0]
        self.joint_state.steering_angle.w2 = msg.position[1]
        self.joint_state.steering_angle.w3 = msg.position[2]
        self.joint_state.steering_angle.w4 = msg.position[3]

        self.joint_state.wheel_rotation.w1 = msg.velocity[0]
        self.joint_state.wheel_rotation.w2 = msg.velocity[1]
        self.joint_state.wheel_rotation.w3 = msg.velocity[2]
        self.joint_state.wheel_rotation.w4 = msg.velocity[3]
        
        # print(str(self.zaman_ref), str(msg.position[0]), str(msg.velocity[0]), str(msg.position[1]), str(msg.velocity[1]), str(msg.position[2]), str(msg.velocity[2]), str(msg.position[3]), str(msg.velocity[3]), str(msg.position[4]), str(msg.velocity[4]), sep='\t', file=out_data_txt)

    def gps_sub_cb(self, msg):   

        temp_time_sec = float(msg.header.stamp.sec)
        temp_time_nsec = float(msg.header.stamp.nanosec)
        self.gazebo_time = temp_time_sec*1e6 + temp_time_nsec*1e-3

        self.gps_data_ideal.gps_pos.x = msg.latitude * DEG2RAD
        self.gps_data_ideal.gps_pos.y = msg.longitude * DEG2RAD
        self.gps_data_ideal.gps_pos.z = msg.altitude

        self.gps_data_ideal.gps_vel.x = 0.0
        self.gps_data_ideal.gps_vel.y = 0.0
        self.gps_data_ideal.gps_vel.z = 0.0

        self.zaman_ref = self.get_clock().now().nanoseconds * 1e-6 #msec
        self.zaman_ref = self.zaman_ref - self.zaman_ilk
        print(str(self.gazebo_time), str(self.gps_data_ideal.gps_pos.x), str(self.gps_data_ideal.gps_pos.y), str(self.gps_data_ideal.gps_pos.z), str(self.gps_data_ideal.gps_vel.x), str(self.gps_data_ideal.gps_vel.y), str(self.gps_data_ideal.gps_vel.z), sep='\t', file=gps_data_gazebo_txt)

    def ideal_listener_callback(self, msg):
        #self.get_logger().info('I heard x pos as: "%f"' % msg.pos.x)
        self.zaman_ref = self.get_clock().now().nanoseconds * 1e-6 #msec
        self.zaman_ref = self.zaman_ref - self.zaman_ilk
        # print(str(self.zaman_ref), str(msg.pos.x), str(msg.pos.y), str(msg.pos.z), str(msg.vel.x), str(msg.vel.y), str(msg.vel.z), str(msg.euler.roll), str(msg.euler.pitch), str(msg.euler.yaw), sep='\t', file=out_data_ideal_txt)

    def onlyins_listener_callback(self, msg):
        #self.get_logger().info('I heard x pos as: "%f"' % msg.pos.x)
        self.zaman_ref = self.get_clock().now().nanoseconds * 1e-6 #msec
        self.zaman_ref = self.zaman_ref - self.zaman_ilk
        # print(str(self.zaman_ref), str(msg.pos.x), str(msg.pos.y), str(msg.pos.z), str(msg.vel.x), str(msg.vel.y), str(msg.vel.z), str(msg.euler.roll), str(msg.euler.pitch), str(msg.euler.yaw), sep='\t', file=out_data_ideal_txt)


    def sub_cb_imu_data(self, msg):
        self.imu_data.vel_diff.x = -msg.linear_acceleration.y * delta_t 
        self.imu_data.vel_diff.y = -msg.linear_acceleration.x * delta_t
        self.imu_data.vel_diff.z = -msg.linear_acceleration.z * delta_t

        self.imu_data.ang_diff.x = -msg.angular_velocity.y * delta_t
        self.imu_data.ang_diff.y = -msg.angular_velocity.x * delta_t
        self.imu_data.ang_diff.z = -msg.angular_velocity.z * delta_t

        # self.zaman_ref = self.get_clock().now().nanoseconds * 1e-6 #msec
        # self.zaman_ref = self.zaman_ref - self.zaman_ilk
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
