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

from std_msgs.msg import String
from ht_nav_variables.msg import HtNavImuData
from sensor_msgs.msg import Imu

from ht_strap_package.config import base_path
from ht_strap_package.config import buffer_size
from ht_strap_package.config import imu_pub_freq
from ht_strap_package.config import delta_t

imu_data_path = base_path / "imu_data_ideal_gazebo.txt"

imu_data_gazebo_txt = open(imu_data_path, 'w')

class IMUDataIdealConverter(Node):

    def __init__(self,qos_profile):
        super().__init__('imu_data_converter')
        self.imu_data_out = HtNavImuData()
        self.imu_data_in = Imu()

        # Initialise publishers
        self.imu_pub = self.create_publisher(HtNavImuData, 'ht_nav_imu_data_ideal_topic', qos_profile=qos_profile)
        # Initialise subscribers
        self.imu_sub = self.create_subscription(Imu, 'kobra_mk5/imu_data_ideal', self.sub_cb, qos_profile=qos_profile)

        self.i = 0
        self.zaman_ref = 0.0
        self.zaman_ref_sec = 0.0
        self.zaman_ilk = self.get_clock().now().nanoseconds * 1e-6 #msec

    def sub_cb(self, msg):      
        self.imu_data_out.vel_diff.x = -msg.linear_acceleration.y * delta_t 
        self.imu_data_out.vel_diff.y = -msg.linear_acceleration.x * delta_t
        self.imu_data_out.vel_diff.z = -msg.linear_acceleration.z * delta_t

        self.imu_data_out.ang_diff.x = -msg.angular_velocity.y * delta_t
        self.imu_data_out.ang_diff.y = -msg.angular_velocity.x * delta_t
        self.imu_data_out.ang_diff.z = -msg.angular_velocity.z * delta_t

        #self.get_logger().info('I received x lin_acc as: "%f"' % msg.linear_acceleration.x)
       
        msg_pb = HtNavImuData()
        msg_pb.vel_diff = self.imu_data_out.vel_diff
        msg_pb.ang_diff = self.imu_data_out.ang_diff

        self.pub_func(msg_pb)

    def pub_func(self,msg):
        self.imu_pub.publish(msg)
        #self.get_logger().info('I publish x vel_diff as: "%f"' % msg.vel_diff.x)
        self.zaman_ref = self.get_clock().now().nanoseconds * 1e-6 #msec
        self.zaman_ref = self.zaman_ref - self.zaman_ilk
        print(str(self.zaman_ref), str(msg.ang_diff.x), str(msg.ang_diff.y), str(msg.ang_diff.z), str(msg.vel_diff.x), str(msg.vel_diff.y), str(msg.vel_diff.z), sep='\t', file=imu_data_gazebo_txt)
 


def main(args=None):
    rclpy.init(args=args)

    custom_qos_profile = qos_profile_sensor_data

    imu_data_converter = IMUDataIdealConverter(custom_qos_profile)

    rclpy.spin(imu_data_converter)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    imu_data_converter.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
