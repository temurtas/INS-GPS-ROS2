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
from ht_nav_variables.msg import HtNavQuaternion
from ht_nav_variables.msg import HtNavEuler
from ht_nav_variables.msg import HtNavStrapOut
from ht_nav_variables.msg import HtNavKalmanOut
from ht_strap_package.strap_operations import pos_update, vel_update, quaternion_update, quaternion2euler
from ht_strap_package.strapdown import strapdown
from ht_strap_package.strap_operations import euler2quaternion, quaternion2euler, quaternion_normalize 
from ht_strap_package.kalman_operations import kalman_duzeltme

from ht_strap_package.config import base_path

base_path2 = base_path # Path("/home/temurtas/INS-GPS-ws/INS-GPS-Matlab/veriler/veri1_to_Dogukan/")           #Ubuntu Path
initial_data_path = base_path2 / "ilk_deger.txt"

out_data_mid_txt = base_path2 / "ros_mid_strap_w_kalman_out.txt"
out_data_mid_strap_txt = base_path2 / "ros_mid_strap_w_kalman_strap_out.txt"

out_data_mid_ros_txt = open(out_data_mid_txt, 'w')
out_data_mid_strap_ros_txt = open(out_data_mid_strap_txt, 'w')

class StrapKalmanPubSub(Node):

    def __init__(self):
        ''' 
        Class constructor to initialise the class 
        '''
        super().__init__('strap_w_kalman_node')
        

        self.lines = String()
        with open(initial_data_path) as initial_data_txt: # open the file for reading
            self.lines = initial_data_txt.readlines()

        line = self.lines[0]
        p1, p2, p3, v1, v2, v3, e1, e2, e3 = line.split() # split it by whitespace
       
        # Initialise publishers
        self.strap_w_kalman_pub = self.create_publisher(HtNavStrapOut, 'ht_nav_strap_w_kalman_topic', 10)
        # Initialise subscribers

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

        self.duzeltme_vector = HtNavKalmanOut()
        self.duzeltme_vector.pos_err.x = 0.0
        self.duzeltme_vector.pos_err.y = 0.0
        self.duzeltme_vector.pos_err.z = 0.0
        self.duzeltme_vector.vel_err.x = 0.0
        self.duzeltme_vector.vel_err.y = 0.0
        self.duzeltme_vector.vel_err.z = 0.0
        self.duzeltme_vector.att_err.x = 0.0
        self.duzeltme_vector.att_err.y = 0.0
        self.duzeltme_vector.att_err.z = 0.0
        self.duzeltme_vector.bias.x = 0.0
        self.duzeltme_vector.bias.y = 0.0
        self.duzeltme_vector.bias.z = 0.0
        self.duzeltme_vector.drift.x = 0.0
        self.duzeltme_vector.drift.y = 0.0
        self.duzeltme_vector.drift.z = 0.0


        self.x_k = np.zeros((15, 1))
        self.old_strap = HtNavStrapOut()

        initial_euler_temp = [0, 0, 0]
        initial_euler_temp[0] = float(e1) # convert bs from string to float
        initial_euler_temp[1] = float(e2) # convert bs from string to float
        initial_euler_temp[2] = float(e3) # convert bs from string to float

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
        print(self.zaman_ref, str(self.old_strap.pos.x), str(self.old_strap.pos.y), str(self.old_strap.pos.z), str(self.old_strap.vel.x), str(self.old_strap.vel.y), str(self.old_strap.vel.z), str(self.old_strap.euler.roll), str(self.old_strap.euler.pitch), str(self.old_strap.euler.yaw), sep='\t', file=out_data_mid_ros_txt)

        self.strap_imu_sub = self.create_subscription(HtNavImuData, 'ht_nav_imu_data_topic', self.sub_cb_imu_data, 10)
        self.strap_kalman_sub = self.create_subscription(HtNavImuData, 'ht_nav_ins_gps_data_topic', self.sub_cb_duzeltme, 10)


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

        self.pub_func(msg_pb)

    def sub_cb_duzeltme(self, msg):
        self.get_logger().info('I heard pos_err x as: "%f"' % msg.pos_err.x)

        self.duzetme_vector.pos_err = msg.pos_err
        self.duzetme_vector.vel_err = msg.vel_err
        self.duzetme_vector.att_err = msg.att_err
        self.duzeltme_vector.bias = msg.bias
        self.duzeltme_vector.drift = msg.drift

        self.x_k[0] = msg.pos_err.x
        self.x_k[1] = msg.pos_err.y
        self.x_k[2] = msg.pos_err.z
        self.x_k[3] = msg.vel_err.x
        self.x_k[4] = msg.vel_err.y
        self.x_k[5] = msg.vel_err.z
        self.x_k[6] = msg.att_err.x
        self.x_k[7] = msg.att_err.y
        self.x_k[8] = msg.att_err.z
        self.x_k[9] = msg.bias.x
        self.x_k[10] = msg.bias.y
        self.x_k[11] = msg.bias.z
        self.x_k[12] = msg.drift.x
        self.x_k[13] = msg.drift.y
        self.x_k[14] = msg.drift.z

        self.new_strap = kalman_duzeltme(self.old_strap, self.x_k)
        self.old_strap = self.new_strap

        self.zaman_ref = self.get_clock().now().nanoseconds * 1e-6 #msec
        self.zaman_ref = self.zaman_ref - self.zaman_ilk
        print(self.zaman_ref, str(self.new_strap.pos.x), str(self.new_strap.pos.y), str(self.new_strap.pos.z), str(self.new_strap.vel.x), str(self.new_strap.vel.y), str(self.new_strap.vel.z), str(self.new_strap.euler.roll), str(self.new_strap.euler.pitch), str(self.new_strap.euler.yaw), sep='\t', file=out_data_mid_strap_ros_txt)

        

    def pub_func(self,msg):
        self.strap_w_kalman_pub.publish(msg)
        #self.get_logger().info('I publish z pos as: "%f"' % msg.pos.z)
        self.zaman_ref = self.get_clock().now().nanoseconds * 1e-6 #msec
        self.zaman_ref = self.zaman_ref - self.zaman_ilk
        print(self.zaman_ref, str(msg.pos.x), str(msg.pos.y), str(msg.pos.z), str(msg.vel.x), str(msg.vel.y), str(msg.vel.z), str(msg.euler.roll), str(msg.euler.pitch), str(msg.euler.yaw), sep='\t', file=out_data_mid_ros_txt)

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


        #self.get_logger().info('internal old q1: "%f"' % old_quaternion_temp[0])
        #self.get_logger().info('internal old q2: "%f"' % old_quaternion_temp[1])
        #self.get_logger().info('internal old q3: "%f"' % old_quaternion_temp[2])
        #self.get_logger().info('internal old q4: "%f"' % old_quaternion_temp[3])

        # ATTITUDE UPDATE
        new_quaternion_temp = quaternion_update(old_quaternion_temp, ang_diff_temp, new_pos_temp, new_vel_temp)
        new_euler_temp = quaternion2euler(new_quaternion_temp)

        #self.get_logger().info('internal q1: "%f"' % new_quaternion_temp[0])
        #self.get_logger().info('internal q2: "%f"' % new_quaternion_temp[1])
        #self.get_logger().info('internal q3: "%f"' % new_quaternion_temp[2])
        #self.get_logger().info('internal q4: "%f"' % new_quaternion_temp[3])

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

    try:
        # Initialise the class
        strap_w_kalman_node = StrapKalmanPubSub()

        # Stop the node from exiting
        rclpy.spin(strap_w_kalman_node)

    finally:
        strap_w_kalman_node.destroy_node()
        rclpy.shutdown()

if __name__=="__main__":
    main()