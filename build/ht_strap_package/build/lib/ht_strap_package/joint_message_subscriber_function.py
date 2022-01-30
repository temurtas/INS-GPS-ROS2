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


from sensor_msgs.msg import JointState
#from ht_nav_variables.msg import HtNavDeneme
from ht_nav_variables.msg import HtNavEuler
from ht_nav_variables.msg import HtNavStrapOut
from ht_strap_package.config import base_path

#base_path = Path("/home/temurtas/INS-GPS-ws/INS-GPS-Matlab/veriler/veri1_to_Dogukan/")           #Ubuntu Path

out_data_path = base_path / "gazebo_joint_states.txt"
out_data_txt = open(out_data_path, 'w')

class MinimalSubscriber(Node):

    def __init__(self,qos_profile):
        super().__init__('minimal_subscriber')
        self.subscription = self.create_subscription(JointState, 'kobra_mk5/joint_states', self.listener_callback, qos_profile=qos_profile)
        self.subscription  # prevent unused variable warning
        self.zaman_ref = 0.0
        self.zaman_ilk = self.get_clock().now().nanoseconds * 1e-6 #msec

    def listener_callback(self, msg):
        # self.get_logger().info('I heard joint namse as: "%f"' % msg.velocity[1])
        self.zaman_ref = self.get_clock().now().nanoseconds * 1e-6 #msec
        self.zaman_ref = self.zaman_ref - self.zaman_ilk
        print(str(self.zaman_ref), str(msg.position[0]), str(msg.velocity[0]), str(msg.position[1]), str(msg.velocity[1]), str(msg.position[2]), str(msg.velocity[2]), str(msg.position[3]), str(msg.velocity[3]), str(msg.position[4]), str(msg.velocity[4]), sep='\t', file=out_data_txt)

def main(args=None):
    rclpy.init(args=args)

    custom_qos_profile = qos_profile_sensor_data

    minimal_subscriber = MinimalSubscriber(custom_qos_profile)

    rclpy.spin(minimal_subscriber)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    minimal_subscriber.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
