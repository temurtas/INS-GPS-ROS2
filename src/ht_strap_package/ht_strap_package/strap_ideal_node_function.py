#!/usr/bin/env python3

# We need install numpy in order to import it
import numpy as np
import math
import rclpy
from pathlib import Path

from rclpy.qos import qos_profile_sensor_data

from rclpy.node import Node
from geometry_msgs.msg import PoseStamped, Pose2D, Point
#from nav_msgs.msg import Path
from std_msgs.msg import Float64
from visualization_msgs.msg import Marker
from builtin_interfaces.msg import Duration
from std_msgs.msg import String
#from ht_nav_variables.msg import HtNavDeneme
from ht_nav_variables.msg import HtNavImuData
from ht_nav_variables.msg import HtNavGpsData
from ht_nav_variables.msg import HtNavQuaternion
from ht_nav_variables.msg import HtNavEuler
from ht_nav_variables.msg import HtNavStrapOut

from ht_strap_package.kalman_operations import f_matrix_construct, q_matrix_construct, p_update, kalman_update, p0_matrix_construct
from ht_strap_package.strapdown import strapdown
from ht_strap_package.strap_operations import euler2quaternion, quaternion2euler, quaternion_normalize 
from ht_strap_package.strap_operations import pos_update, vel_update, quaternion_update, quaternion2euler
from ht_strap_package.strapdown import strapdown
from ht_strap_package.kalman_operations import kalman_duzeltme

from ht_strap_package.config import base_path
from ht_strap_package.config import buffer_size
from ht_strap_package.config import DEG2RAD
from ht_strap_package.config import kalman_prop_const 

base_path2 = base_path # Path("/home/temur/INS-GPS-ws/INS-GPS-Matlab/veriler/veri1_to_Dogukan/")           #Ubuntu Path
#kks_data_path = base_path2 / "kks_veri.txt"


strap_data_ins_gps_mid_txt = base_path2 / "strap_data_gazebo_ros_kalman_out.txt"
strap_data_gazebo_ros_txt = open(strap_data_ins_gps_mid_txt, 'w')

ros_gazebo_kalman_out =  base_path2 / "ros_gazebo_kalman_out.txt"
out_data_strap_kalman_ros_txt = open(ros_gazebo_kalman_out, 'w')

class INSGPSNode(Node):

    def __init__(self, qos_profile):
        ''' 
        Class constructor to initialise the class 
        '''
        super().__init__('ins_gps_node')

        # Initialise publishers
        self.strap_w_kalman_pub = self.create_publisher(HtNavStrapOut, 'ht_nav_strap_w_kalman_topic', qos_profile=qos_profile)
        # Initialise subscribers
        self.strap_imu_sub = self.create_subscription(HtNavImuData, 'ht_nav_imu_data_topic', self.sub_cb_imu_data, qos_profile=qos_profile)

        self.strap_sayac = 0
        self.zaman_ref = 0.0
        self.zaman_ilk = self.get_clock().now().nanoseconds * 1e-6 #msec

        self.imu_data = HtNavImuData()
        self.imu_data.vel_diff.x = 0.0
        self.imu_data.vel_diff.y = 0.0
        self.imu_data.vel_diff.z = 0.0
        self.imu_data.ang_diff.x = 0.0
        self.imu_data.ang_diff.y = 0.0
        self.imu_data.ang_diff.z = 0.0

        self.old_strap = HtNavStrapOut()
        self.new_strap = HtNavStrapOut()

        # initialization 
        self.old_strap.pos.x = 39.89044287479834 * DEG2RAD
        self.old_strap.pos.y = 32.781467396951804 * DEG2RAD
        self.old_strap.pos.z = 934.0
        self.old_strap.vel.x = 0.0
        self.old_strap.vel.y = 0.0
        self.old_strap.vel.z = 0.0
        self.old_strap.euler.roll =  0.0 
        self.old_strap.euler.pitch = 0.0 
        self.old_strap.euler.yaw =   0.0
        self.old_strap.quaternion.x = 1.0
        self.old_strap.quaternion.y = 0.0
        self.old_strap.quaternion.z = 0.0
        self.old_strap.quaternion.w = 0.0

        self.new_strap = self.old_strap

    def sub_cb_imu_data(self, msg):
        #self.get_logger().info('I heard vel_diff x as: "%f"' % msg.vel_diff.x)
        
        self.imu_data.vel_diff = msg.vel_diff
        self.imu_data.ang_diff = msg.ang_diff

        self.new_strap = self.node_strapdown(self.old_strap, self.imu_data)

        self.old_strap = self.new_strap

        msg_pb = HtNavStrapOut()
        msg_pb.pos = self.new_strap.pos
        msg_pb.vel = self.new_strap.vel
        msg_pb.euler = self.new_strap.euler
        msg_pb.quaternion = self.new_strap.quaternion

        self.strap_sayac = self.strap_sayac + 1

        self.strap_pub_func(msg_pb)


    def strap_pub_func(self,msg):
        self.strap_w_kalman_pub.publish(msg)
        #self.get_logger().info('I publish z pos as: "%f"' % msg.pos.z)
        self.zaman_ref = self.get_clock().now().nanoseconds * 1e-6 #msec
        self.zaman_ref = self.zaman_ref - self.zaman_ilk
        print(self.zaman_ref, str(msg.pos.x), str(msg.pos.y), str(msg.pos.z), str(msg.vel.x), str(msg.vel.y), str(msg.vel.z), str(msg.euler.roll), str(msg.euler.pitch), str(msg.euler.yaw), sep='\t', file=strap_data_gazebo_ros_txt)

    def node_strapdown(self, old_strap, imu_data):
    
        # Convert your custom variable types (float) to np variables (float) 
        vel_diff_temp = np.zeros((3, 1))
        vel_diff_temp[0] = imu_data.vel_diff.x
        vel_diff_temp[1] = imu_data.vel_diff.y
        vel_diff_temp[2] = imu_data.vel_diff.z

        ang_diff_temp = np.zeros((3, 1))
        ang_diff_temp[0] = imu_data.ang_diff.x
        ang_diff_temp[1] = imu_data.ang_diff.y
        ang_diff_temp[2] = imu_data.ang_diff.z

        old_quaternion_temp = np.zeros((4, 1))
        old_quaternion_temp[0] = old_strap.quaternion.x
        old_quaternion_temp[1] = old_strap.quaternion.y
        old_quaternion_temp[2] = old_strap.quaternion.z
        old_quaternion_temp[3] = old_strap.quaternion.w

        old_vel_temp = np.zeros((3, 1))
        old_vel_temp[0] = old_strap.vel.x
        old_vel_temp[1] = old_strap.vel.y
        old_vel_temp[2] = old_strap.vel.z

        old_pos_temp = np.zeros((3, 1))
        old_pos_temp[0] = old_strap.pos.x
        old_pos_temp[1] = old_strap.pos.y
        old_pos_temp[2] = old_strap.pos.z

        new_vel_temp = np.zeros((3, 1))
        new_pos_temp = np.zeros((3, 1))
        new_quaternion_temp = np.zeros((4, 1))

        # VELOCITY UPDATE
        new_vel_temp = vel_update(old_vel_temp, vel_diff_temp, old_pos_temp, old_quaternion_temp)

        # POSITION UPDATE
        new_pos_temp = pos_update(new_vel_temp, old_pos_temp)

        # ATTITUDE UPDATE
        new_quaternion_temp = quaternion_update(old_quaternion_temp, ang_diff_temp, new_pos_temp, new_vel_temp)
        new_euler_temp = quaternion2euler(new_quaternion_temp)
        # Convert your np variables (float) to custom variable types (float)
        new_strap = HtNavStrapOut()
        
        new_strap.pos.x = float(new_pos_temp[0])
        new_strap.pos.y = float(new_pos_temp[1])
        new_strap.pos.z = float(new_pos_temp[2])

        new_strap.vel.x = float(new_vel_temp[0])
        new_strap.vel.y = float(new_vel_temp[1])
        new_strap.vel.z = float(new_vel_temp[2])

        new_strap.euler.roll = float(new_euler_temp[0])
        new_strap.euler.pitch = float(new_euler_temp[1])
        new_strap.euler.yaw = float(new_euler_temp[2])

        new_strap.quaternion.x = float(new_quaternion_temp[0])
        new_strap.quaternion.y = float(new_quaternion_temp[1])
        new_strap.quaternion.z = float(new_quaternion_temp[2])
        new_strap.quaternion.w = float(new_quaternion_temp[3])
        
        return new_strap

def main(args=None):
    ''' 
    Main function to initialise the class and node. 
    '''

    # Initialise the node
    rclpy.init(args=args)

    custom_qos_profile = qos_profile_sensor_data

    try:
        # Initialise the class
        ins_gps_node = INSGPSNode(custom_qos_profile)

        # Stop the node from exiting
        rclpy.spin(ins_gps_node)

    finally:
        ins_gps_node.destroy_node()
        rclpy.shutdown()

if __name__=="__main__":
    main()