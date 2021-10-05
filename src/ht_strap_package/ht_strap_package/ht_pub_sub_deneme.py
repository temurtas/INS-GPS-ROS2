#!/usr/bin/env python3

# We need install numpy in order to import it
import numpy as np
import math
import rclpy
from pathlib import Path

from rclpy.node import Node
from geometry_msgs.msg import PoseStamped, Pose2D, Point
#from nav_msgs.msg import Path
from std_msgs.msg import Float64
from visualization_msgs.msg import Marker
from builtin_interfaces.msg import Duration
from std_msgs.msg import String
#from ht_nav_variables.msg import HtNavDeneme
from ht_nav_variables.msg import HtNavImuData
from ht_nav_variables.msg import HtNavEuler
from ht_nav_variables.msg import HtNavStrapOut
from ht_strap_package.strapdown import strapdown
from ht_strap_package.strap_operations import euler2quaternion, quaternion_normalize 

from ht_strap_package.config import base_path

base_path2 = base_path # Path("/home/temurtas/INS-GPS-ws/INS-GPS-Matlab/veriler/veri1_to_Dogukan/")           #Ubuntu Path
initial_data_path = base_path2 / "ilk_deger.txt"

out_data_mid_txt = base_path2 / "ros_mid_strap_out.txt"

out_data_mid_ros_txt = open(out_data_mid_txt, 'w')

class DenemePubSub(Node):

    def __init__(self):
        ''' 
        Class constructor to initialise the class 
        '''
        super().__init__('strap_node')
        self.declare_parameters(
            namespace='',
            parameters=[
                ('pos_std', None),
                ('h_std', None),
                ('vel_std', None),
                ('att_std', None),
                ('bias_std', None),
                ('drift_std', None),
                ('tau_i', None),
                ('tau_bad', None),
                ('sigma_ra', None),
                ('sigma_rg', None),
                ('sigma_bad', None),
                ('sigma_bgd', None)
            ])

        self.lines = String()
        with open(initial_data_path) as initial_data_txt: # open the file for reading
            self.lines = initial_data_txt.readlines()

        line = self.lines[0]
        p1, p2, p3, v1, v2, v3, e1, e2, e3 = line.split() # split it by whitespace
       
        self.pos_std = float(self.get_parameter("pos_std").value)
        self.h_std = float(self.get_parameter("h_std").value)
        self.vel_std = float(self.get_parameter("vel_std").value)
        self.att_std = float(self.get_parameter("att_std").value)
        self.bias_std = float(self.get_parameter("bias_std").value)
        self.drift_std = float(self.get_parameter("drift_std").value)
        self.tau_i = float(self.get_parameter("tau_i").value)
        self.tau_bad = float(self.get_parameter("tau_bad").value)
        self.sigma_ra = float(self.get_parameter("sigma_ra").value)
        self.sigma_rg = float(self.get_parameter("sigma_rg").value)
        self.sigma_bad = float(self.get_parameter("sigma_bad").value)
        self.sigma_bgd = float(self.get_parameter("sigma_bgd").value)

        # Initialise publishers
        self.deneme_pub = self.create_publisher(HtNavStrapOut, 'ht_nav_strap_topic', 10)
        # Initialise subscribers
        self.deneme_sub = self.create_subscription(HtNavImuData, 'ht_nav_imu_data_topic', self.sub_cb, 10)

        self.zaman_ref = 0.0
        self.zaman_ilk = self.get_clock().now().nanoseconds * 1e-6 #msec
        self.ax = []
        self.imu_data = HtNavImuData()
        self.imu_data.vel_diff.x = 0.0
        self.imu_data.vel_diff.y = 0.0
        self.imu_data.vel_diff.z = 0.0
        self.imu_data.ang_diff.x = 0.0
        self.imu_data.ang_diff.y = 0.0
        self.imu_data.ang_diff.z = 0.0

        self.old_strap = HtNavStrapOut()

        initial_euler_temp = [0, 0, 0]
        initial_euler_temp[0] = float(e1) # convert bs from string to float
        initial_euler_temp[0] = float(e1) # convert bs from string to float
        initial_euler_temp[0] = float(e1) # convert bs from string to float

        initial_quaternion_temp = euler2quaternion(initial_euler_temp)
        initial_quaternion_temp2 = quaternion_normalize(initial_quaternion_temp)

        self.old_strap.pos.x = float(p1) # convert bs from string to float
        self.old_strap.pos.y = float(p2) # convert bs from string to float
        self.old_strap.pos.z = float(p3) # convert bs from string to float
        self.old_strap.vel.x = float(v1) # convert bs from string to float
        self.old_strap.vel.y = float(v2) # convert bs from string to float
        self.old_strap.vel.z = float(v3) # convert bs from string to float
        self.old_strap.euler.roll = float(e1) # convert bs from string to float
        self.old_strap.euler.pitch = float(e2) # convert bs from string to float
        self.old_strap.euler.yaw = float(e3) # convert bs from string to float
        self.old_strap.quaternion.x = float(initial_quaternion_temp2[0])
        self.old_strap.quaternion.y = float(initial_quaternion_temp2[1])
        self.old_strap.quaternion.z = float(initial_quaternion_temp2[2])
        self.old_strap.quaternion.w = float(initial_quaternion_temp2[3])

        self.new_strap = HtNavStrapOut()
        self.new_strap.pos.x = 0.0
        self.new_strap.pos.y = 0.0
        self.new_strap.pos.z = 0.0
        self.new_strap.vel.x = 0.0
        self.new_strap.vel.y = 0.0
        self.new_strap.vel.z = 0.0
        self.new_strap.euler.roll = 0.0
        self.new_strap.euler.pitch = 0.0
        self.new_strap.euler.yaw = 0.0
        self.new_strap.quaternion.x = 1.0
        self.new_strap.quaternion.y = 0.0
        self.new_strap.quaternion.z = 0.0
        self.new_strap.quaternion.w = 0.0

    def sub_cb(self, msg):
        self.ax.append(msg.vel_diff.x)
        self.get_logger().info('I heard vel_diff x as: "%f"' % msg.vel_diff.x)
        
        self.imu_data.vel_diff = msg.vel_diff
        self.imu_data.ang_diff = msg.ang_diff

        self.new_strap = strapdown(self.old_strap, self.imu_data)

        self.old_strap = self.new_strap

        msg_pb = HtNavStrapOut()
        msg_pb.pos = self.new_strap.pos
        msg_pb.vel = self.new_strap.vel
        msg_pb.euler = self.new_strap.euler
        msg_pb.quaternion = self.new_strap.quaternion

        #msg_pb = HtNavEuler() 
        #msg_pb.roll = self.att_std
        #msg_pb.pitch = msg.ang_diff.y
        #msg_pb.yaw = msg.ang_diff.z
        self.pub_func(msg_pb)

    def pub_func(self,msg):
        self.deneme_pub.publish(msg)
        self.get_logger().info('I publish z pos as: "%f"' % msg.pos.z)
        self.zaman_ref = self.get_clock().now().nanoseconds * 1e-6 #msec
        self.zaman_ref = self.zaman_ref - self.zaman_ilk
        print(self.zaman_ref, str(msg.pos.x), str(msg.pos.y), str(msg.pos.z), str(msg.vel.x), str(msg.vel.y), str(msg.vel.z), str(msg.euler.roll), str(msg.euler.pitch), str(msg.euler.yaw), sep='\t', file=out_data_mid_ros_txt)



def main(args=None):
    ''' 
    Main function to initialise the class and node. 
    '''

    # Initialise the node
    rclpy.init(args=args)

    try:
        # Initialise the class
        strap_node = DenemePubSub()

        # Stop the node from exiting
        rclpy.spin(strap_node)

    finally:
        strap_node.destroy_node()
        rclpy.shutdown()

if __name__=="__main__":
    main()