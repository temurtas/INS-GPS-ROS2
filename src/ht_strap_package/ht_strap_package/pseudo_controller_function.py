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


#from ht_nav_variables.msg import HtNavDeneme
from ht_nav_variables.msg import HtNavEuler
from ht_nav_variables.msg import HtNavKalmanOut
from ht_nav_variables.msg import HtNavStrapOut
from ht_strap_package.config import base_path

#base_path = Path("/home/temur/INS-GPS-ws/INS-GPS-Matlab/veriler/veri1_to_Dogukan/")           #Ubuntu Path

out_data_path = base_path / "strap_data_controller_input.txt"
out_data_txt = open(out_data_path, 'w')

out_data_kalman_path = base_path / "kalman_out_controller_input.txt"
out_data_kalman_txt = open(out_data_kalman_path, 'w')


class PseudoController(Node):

    def __init__(self,qos_profile):
        super().__init__('minimal_subscriber')
        self.subscription = self.create_subscription(
            HtNavStrapOut,
            'ht_nav_strap_w_kalman_topic',
            self.listener_callback,
            qos_profile=qos_profile)

        self.subscription = self.create_subscription(
            HtNavKalmanOut,
            'ht_nav_ins_gps_data_topic',
            self.kalman_listener_callback,
            qos_profile=qos_profile)

        self.subscription  # prevent unused variable warning
        self.zaman_ref = 0.0
        self.zaman_ilk = self.get_clock().now().nanoseconds * 1e-6 #msec

    def listener_callback(self, msg):
        #self.get_logger().info('I heard x pos as: "%f"' % msg.pos.x)
        self.zaman_ref = self.get_clock().now().nanoseconds * 1e-6 #msec
        self.zaman_ref = self.zaman_ref - self.zaman_ilk
        print(str(self.zaman_ref), str(msg.pos.x), str(msg.pos.y), str(msg.pos.z), str(msg.vel.x), str(msg.vel.y), str(msg.vel.z), str(msg.euler.roll), str(msg.euler.pitch), str(msg.euler.yaw), sep='\t', file=out_data_txt)

    def kalman_listener_callback(self, msg):
        #self.get_logger().info('I heard x pos as: "%f"' % msg.pos.x)
        self.zaman_ref = self.get_clock().now().nanoseconds * 1e-6 #msec
        self.zaman_ref = self.zaman_ref - self.zaman_ilk
        print(str(self.zaman_ref), str(msg.bias.x), str(msg.bias.y), str(msg.bias.z), str(msg.drift.x), str(msg.drift.y), str(msg.drift.z), sep='\t', file=out_data_kalman_txt)


def main(args=None):
    rclpy.init(args=args)

    custom_qos_profile = qos_profile_sensor_data

    pseudo_controller = PseudoController(custom_qos_profile)

    rclpy.spin(pseudo_controller)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    pseudo_controller.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
