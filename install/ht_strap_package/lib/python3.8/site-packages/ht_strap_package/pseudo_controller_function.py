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

#from ht_nav_variables.msg import HtNavDeneme
from ht_nav_variables.msg import HtNavEuler
from ht_nav_variables.msg import HtNavKalmanOut
from ht_nav_variables.msg import HtNavStrapOut
from ht_nav_variables.msg import HtNavGpsData
from ht_nav_variables.msg import HtNavTireOut

from ht_strap_package.config import base_path
from ht_strap_package.config import DEG2RAD

#base_path = Path("/home/temur/INS-GPS-ws/INS-GPS-Matlab/veriler/veri1_to_Dogukan/")           #Ubuntu Path

# out_data_path = base_path / "strap_data_controller_input.txt"
# out_data_txt = open(out_data_path, 'w')

# out_data_kalman_path = base_path / "kalman_out_controller_input.txt"
# out_data_kalman_txt = open(out_data_kalman_path, 'w')


class PseudoController(Node):

    def __init__(self,qos_profile):
        super().__init__('minimal_subscriber')
        self.strap_subscription = self.create_subscription(
            HtNavStrapOut,
            'ht_nav_strap_data',
            self.listener_callback,
            qos_profile=qos_profile)     

        self.kalman_subscription = self.create_subscription(
            HtNavKalmanOut,
            'ht_nav_kalman_out',
            self.kalman_listener_callback,
            qos_profile=qos_profile)

        self.tire_subscription = self.create_subscription(
            HtNavTireOut,
            'ht_nav_tire_data',
            self.tire_listener_callback,
            qos_profile=qos_profile)    

        self.strap_subscription  # prevent unused variable warning
        self.kalman_subscription  # prevent unused variable warning
        self.tire_subscription  # prevent unused variable warning

        self.strap_data = HtNavStrapOut()
        self.kalman_out = HtNavKalmanOut()
        self.tire_data  = HtNavTireOut()

        self.zaman_ref = 0.0
        self.zaman_ilk = self.get_clock().now().nanoseconds * 1e-6 #msec

    def listener_callback(self, msg):
        #self.get_logger().info('I heard x pos as: "%f"' % msg.pos.x)
        self.zaman_ref = self.get_clock().now().nanoseconds * 1e-6 #msec
        self.zaman_ref = self.zaman_ref - self.zaman_ilk
        
        self.strap_data.pos = msg.pos
        self.strap_data.vel = msg.vel
        self.strap_data.euler = msg.euler
        self.strap_data.quaternion = msg.quaternion

        # print(str(self.zaman_ref), str(msg.pos.x), str(msg.pos.y), str(msg.pos.z), str(msg.vel.x), str(msg.vel.y), str(msg.vel.z), str(msg.euler.roll), str(msg.euler.pitch), str(msg.euler.yaw), sep='\t', file=out_data_txt)

    def kalman_listener_callback(self, msg):
        #self.get_logger().info('I heard x pos as: "%f"' % msg.pos.x)
        self.zaman_ref = self.get_clock().now().nanoseconds * 1e-6 #msec
        self.zaman_ref = self.zaman_ref - self.zaman_ilk
        
        self.kalman_out.pos_err = msg.pos_err
        self.kalman_out.vel_err = msg.vel_err
        self.kalman_out.att_err = msg.att_err
        self.kalman_out.bias = msg.bias
        self.kalman_out.drift = msg.drift

        # print(str(self.zaman_ref), str(msg.bias.x), str(msg.bias.y), str(msg.bias.z), str(msg.drift.x), str(msg.drift.y), str(msg.drift.z), sep='\t', file=out_data_kalman_txt)

    def tire_listener_callback(self, msg):
        #self.get_logger().info('I heard x pos as: "%f"' % msg.pos.x)
        self.zaman_ref = self.get_clock().now().nanoseconds * 1e-6 #msec
        self.zaman_ref = self.zaman_ref - self.zaman_ilk

        self.tire_data.effective_radius_est = msg.effective_radius_est
        self.tire_data.vehicle_mass_est = msg.vehicle_mass_est
        self.tire_data.wheel_side_slip_ang = msg.wheel_side_slip_ang
        self.tire_data.wheel_longitudinal_slip_ratio = msg.wheel_longitudinal_slip_ratio
        self.tire_data.tire_lateral_forces = msg.tire_lateral_forces
        self.tire_data.tire_longitudinal_forces = msg.tire_longitudinal_forces  


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
