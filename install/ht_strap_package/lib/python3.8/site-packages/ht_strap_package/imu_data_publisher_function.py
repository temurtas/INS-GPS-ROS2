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

from std_msgs.msg import String
#from ht_nav_variables.msg import HtNavDeneme
from ht_nav_variables.msg import HtNavImuData
from ht_nav_variables.msg import HtNavPoint
#base_path = Path("/home/temurtas/INS-GPS-ws/INS-GPS-Matlab/veriler/veri2/input/")           #Ubuntu Path
base_path = Path("/home/temurtas/INS-GPS-ws/INS-GPS-Matlab/veriler/veri1_to_Dogukan/")           #Ubuntu Path
imu_data_path = base_path / "aob_veri.txt"

class IMUDataPublisher(Node):

    def __init__(self):
        super().__init__('imu_data_publisher')
        self.imu_data = HtNavImuData()

        self.lines = String()
        with open(imu_data_path) as imu_data_txt: # open the file for reading
            self.lines = imu_data_txt.readlines()

        self.publisher_ = self.create_publisher(HtNavImuData, 'ht_nav_imu_data_topic', 10)
        timer_period = 1/1000  # seconds
        self.timer = self.create_timer(timer_period, self.timer_callback)
        self.i = 0

    def timer_callback(self):
        line = self.lines[self.i]
        #for line in lines: # iterate over each line
        w1, w2, w3, a1, a2, a3 = line.split() # split it by whitespace
        self.imu_data.ang_diff.x = float(w1) # convert bs from string to float
        self.imu_data.ang_diff.y = float(w2) # convert bs from string to float
        self.imu_data.ang_diff.z = float(w3) # convert bs from string to float

        self.imu_data.vel_diff.x = float(a1) # convert bs from string to float
        self.imu_data.vel_diff.y = float(a2) # convert bs from string to float
        self.imu_data.vel_diff.z = float(a3) # convert bs from string to float

        msg = HtNavImuData()
        msg.vel_diff.x = self.imu_data.vel_diff.x
        msg.vel_diff.y = self.imu_data.vel_diff.y
        msg.vel_diff.z = self.imu_data.vel_diff.z
        msg.ang_diff.x = self.imu_data.vel_diff.x
        msg.ang_diff.y = self.imu_data.vel_diff.y
        msg.ang_diff.z = self.imu_data.vel_diff.z
        self.publisher_.publish(msg)
        self.get_logger().info('Publishing vel_diff x as: "%f"' % msg.vel_diff.x)
        self.i += 1


def main(args=None):
    rclpy.init(args=args)

    imu_data_publisher = IMUDataPublisher()

    rclpy.spin(imu_data_publisher)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    imu_data_publisher.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
