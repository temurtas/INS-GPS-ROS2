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
from ht_nav_variables.msg import HtNavGpsData
from sensor_msgs.msg import NavSatFix

from ht_strap_package.config import base_path
from ht_strap_package.config import delta_t
from ht_strap_package.config import DEG2RAD

gps_data_path = base_path / "ideal_gps_veri_gazebo.txt"

gps_data_gazebo_txt = open(gps_data_path, 'w')

class GPSDataConverter(Node):

    def __init__(self,qos_profile):
        super().__init__('ideal_gps_data_converter')
        self.gps_data_out = HtNavGpsData()
        self.gps_data_in = NavSatFix()

        # Initialise publishers
        self.gps_sub = self.create_subscription(NavSatFix, 'kobra_mk5/ideal_gps_data', self.sub_cb, qos_profile=qos_profile)

        self.i = 0
        self.zaman_ref = 0.0
        self.zaman_ref_sec = 0.0
        self.zaman_ilk = self.get_clock().now().nanoseconds * 1e-6 #msec

    def sub_cb(self, msg):      
        self.gps_data_out.gps_pos.x = msg.latitude * DEG2RAD
        self.gps_data_out.gps_pos.y = msg.longitude * DEG2RAD
        self.gps_data_out.gps_pos.z = msg.altitude

        self.gps_data_out.gps_vel.x = 0.0
        self.gps_data_out.gps_vel.y = 0.0
        self.gps_data_out.gps_vel.z = 0.0

        #self.get_logger().info('I received lat as: "%f"' % msg.latitude)
       
        msg_pb = HtNavGpsData()
        msg_pb.gps_pos = self.gps_data_out.gps_pos
        msg_pb.gps_vel = self.gps_data_out.gps_vel

        self.pub_func(msg_pb)

    def pub_func(self,msg):
        #self.get_logger().info('I publish lat as: "%f"' % msg.gps_pos.x)
        self.zaman_ref = self.get_clock().now().nanoseconds * 1e-6 #msec
        self.zaman_ref = self.zaman_ref - self.zaman_ilk
        print(str(self.zaman_ref), str(msg.gps_pos.x), str(msg.gps_pos.y), str(msg.gps_pos.z), str(msg.gps_vel.x), str(msg.gps_vel.y), str(msg.gps_vel.z), sep='\t', file=gps_data_gazebo_txt)
 


def main(args=None):
    rclpy.init(args=args)

    custom_qos_profile = qos_profile_sensor_data

    gps_data_converter = GPSDataConverter(custom_qos_profile)

    rclpy.spin(gps_data_converter)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    gps_data_converter.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
