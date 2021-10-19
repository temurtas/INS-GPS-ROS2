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
from ht_nav_variables.msg import HtNavGpsData
from ht_nav_variables.msg import HtNavPoint
#base_path = Path("/home/temurtas/INS-GPS-ws/INS-GPS-Matlab/veriler/veri2/input/")           #Ubuntu Path
#base_path = Path("/home/temurtas/INS-GPS-ws/INS-GPS-Matlab/veriler/veri1_to_Dogukan/")           #Ubuntu Path

from ht_strap_package.config import base_path
from ht_strap_package.config import buffer_size

gps_data_path = base_path / "kks_veri.txt"
gps_data_ros_path = base_path / "kks_veri_ros2.txt"

gps_data_ros_txt = open(gps_data_ros_path, 'w')

class GPSDataPublisher(Node):

    def __init__(self):
        super().__init__('gps_data_publisher')
        self.gps_data = HtNavGpsData()

        self.lines = String()
        with open(gps_data_path) as gps_data_ros_txt: # open the file for reading
            self.lines = gps_data_ros_txt.readlines()

        self.publisher_ = self.create_publisher(HtNavGpsData, 'ht_nav_gps_data_topic', buffer_size)
        timer_period = 1/50  # seconds
        self.timer = self.create_timer(timer_period, self.timer_callback)
        self.i = 0
        self.zaman_ref = 0.0
        self.zaman_ref_sec = 0.0
        self.zaman_ilk = self.get_clock().now().nanoseconds * 1e-6 #msec

    def timer_callback(self):
        line = self.lines[self.i]
        #for line in lines: # iterate over each line
        w1, w2, w3, a1, a2, a3 = line.split() # split it by whitespace
        self.gps_data.gps_pos.x = float(w1) # convert bs from string to float
        self.gps_data.gps_pos.y = float(w2) # convert bs from string to float
        self.gps_data.gps_pos.z = float(w3) # convert bs from string to float

        self.gps_data.gps_vel.x = float(a1) # convert bs from string to float
        self.gps_data.gps_vel.y = float(a2) # convert bs from string to float
        self.gps_data.gps_vel.z = float(a3) # convert bs from string to float

        msg = HtNavGpsData()
        msg.gps_pos.x = self.gps_data.gps_pos.x
        msg.gps_pos.y = self.gps_data.gps_pos.y
        msg.gps_pos.z = self.gps_data.gps_pos.z
        msg.gps_vel.x = self.gps_data.gps_vel.x
        msg.gps_vel.y = self.gps_data.gps_vel.y
        msg.gps_vel.z = self.gps_data.gps_vel.z
        self.publisher_.publish(msg)
        #self.get_logger().info('Publishing vel_diff x as: "%f"' % msg.vel_diff.x)
        self.zaman_ref = self.get_clock().now().nanoseconds * 1e-6 #msec
        self.zaman_ref = self.zaman_ref - self.zaman_ilk
        self.zaman_ref_sec = self.zaman_ref*1e-3
        print(str(self.zaman_ref), str(msg.gps_pos.x), str(msg.gps_pos.y), str(msg.gps_pos.z), str(msg.gps_vel.x), str(msg.gps_vel.y), str(msg.gps_vel.z), sep='\t', file=gps_data_ros_txt)
        self.i += 1
        #if(self.i % 100 == 0):
        #    self.get_logger().info('time: "%f"' % self.zaman_ref_sec)



def main(args=None):
    rclpy.init(args=args)

    gps_data_publisher = GPSDataPublisher()

    rclpy.spin(gps_data_publisher)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    gps_data_publisher.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
