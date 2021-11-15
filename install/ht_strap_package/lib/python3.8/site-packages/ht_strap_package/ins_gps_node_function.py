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
from ht_nav_variables.msg import HtNavKalmanOut 
from ht_strap_package.kalman_operations import f_matrix_construct, q_matrix_construct, p_update, kalman_update, p0_matrix_construct
from ht_strap_package.strapdown import strapdown
from ht_strap_package.strap_operations import euler2quaternion, quaternion2euler, quaternion_normalize 

from ht_strap_package.config import base_path
from ht_strap_package.config import buffer_size

base_path2 = base_path # Path("/home/temurtas/INS-GPS-ws/INS-GPS-Matlab/veriler/veri1_to_Dogukan/")           #Ubuntu Path
#kks_data_path = base_path2 / "kks_veri.txt"

out_data_ins_gps_mid_txt = base_path2 / "ros_mid_kalman_out.txt"
out_data_ins_gps_mid_ros_txt = open(out_data_ins_gps_mid_txt, 'w')

deneme_txt_1_path = base_path2 / "ros2_kks_veri.txt"
deneme_txt_1 = open(deneme_txt_1_path, 'w')


class INSGPSNode(Node):

    def __init__(self, qos_profile):
        ''' 
        Class constructor to initialise the class 
        '''
        super().__init__('ins_gps_node')
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
        self.ins_gps_pub = self.create_publisher(HtNavKalmanOut, 'ht_nav_ins_gps_data_topic', qos_profile=qos_profile)
        self.deneme_pub = self.create_publisher(HtNavKalmanOut, 'ht_nav_deneme_topic', qos_profile=qos_profile)
        # Initialise subscribers
        self.gps_sub = self.create_subscription(HtNavGpsData, 'ht_nav_gps_data_topic', self.sub_cb_gps_data, qos_profile=qos_profile)
        self.strap_sub = self.create_subscription(HtNavStrapOut, 'ht_nav_strap_w_kalman_topic', self.sub_cb_strap, qos_profile=qos_profile)

        self.zaman_ref = 0.0
        self.zaman_ilk = self.get_clock().now().nanoseconds * 1e-6 #msec
        self.ax = []
        self.gps_data = HtNavGpsData()
        self.gps_data.gps_pos.x = 0.0
        self.gps_data.gps_pos.y = 0.0
        self.gps_data.gps_pos.z = 0.0
        self.gps_data.gps_vel.x = 0.0
        self.gps_data.gps_vel.y = 0.0
        self.gps_data.gps_vel.z = 0.0

        self.old_duzeltme = HtNavKalmanOut()
        self.old_duzeltme.pos_err.x = 0.0
        self.old_duzeltme.pos_err.y = 0.0
        self.old_duzeltme.pos_err.z = 0.0
        self.old_duzeltme.vel_err.x = 0.0
        self.old_duzeltme.vel_err.y = 0.0
        self.old_duzeltme.vel_err.z = 0.0
        self.old_duzeltme.att_err.x = 0.0
        self.old_duzeltme.att_err.y = 0.0
        self.old_duzeltme.att_err.z = 0.0
        self.old_duzeltme.att_err.x = 0.0
        self.old_duzeltme.att_err.y = 0.0
        self.old_duzeltme.att_err.z = 0.0
        self.old_duzeltme.bias.x = 0.0
        self.old_duzeltme.bias.y = 0.0
        self.old_duzeltme.bias.z = 0.0
        self.old_duzeltme.drift.x = 0.0
        self.old_duzeltme.drift.y = 0.0
        self.old_duzeltme.drift.z = 0.0

        self.old_strap = HtNavStrapOut()
        self.old_strap.pos.x = 0.0 
        self.old_strap.pos.y = 0.0 
        self.old_strap.pos.z = 0.0 
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

        self.new_duzeltme = HtNavKalmanOut()
        self.new_duzeltme.pos_err.x = 0.0
        self.new_duzeltme.pos_err.y = 0.0
        self.new_duzeltme.pos_err.z = 0.0
        self.new_duzeltme.vel_err.x = 0.0
        self.new_duzeltme.vel_err.y = 0.0
        self.new_duzeltme.vel_err.z = 0.0
        self.new_duzeltme.att_err.x = 0.0
        self.new_duzeltme.att_err.y = 0.0
        self.new_duzeltme.att_err.z = 0.0
        self.new_duzeltme.att_err.x = 0.0
        self.new_duzeltme.att_err.y = 0.0
        self.new_duzeltme.att_err.z = 0.0
        self.new_duzeltme.bias.x = 0.0
        self.new_duzeltme.bias.y = 0.0
        self.new_duzeltme.bias.z = 0.0
        self.new_duzeltme.drift.x = 0.0
        self.new_duzeltme.drift.y = 0.0
        self.new_duzeltme.drift.z = 0.0

        self.p_matrix = np.zeros((15, 15))
        self.p_matrix = p0_matrix_construct()

        self.x_k = np.zeros((15,1))


    def sub_cb_gps_data(self, msg):
        self.gps_data.gps_pos = msg.gps_pos
        self.gps_data.gps_vel = msg.gps_vel
        print(str(self.gps_data.gps_pos.x), str(self.gps_data.gps_pos.y), str(self.gps_data.gps_pos.z), str(self.gps_data.gps_vel.x), str(self.gps_data.gps_vel.y), str(self.gps_data.gps_vel.z), sep='\t', file=deneme_txt_1)
        
        self.node_covariance_update()
        self.node_kalman_update()

        msg_pb = HtNavKalmanOut() 
        msg_pb.pos_err.x = float(self.x_k[0])
        msg_pb.pos_err.y = float(self.x_k[1])
        msg_pb.pos_err.z = float(self.x_k[2])

        msg_pb.vel_err.x = float(self.x_k[3])
        msg_pb.vel_err.y = float(self.x_k[4])
        msg_pb.vel_err.z = float(self.x_k[5])

        msg_pb.att_err.x = float(self.x_k[6])
        msg_pb.att_err.y = float(self.x_k[7])
        msg_pb.att_err.z = float(self.x_k[8])

        msg_pb.bias.x = float(self.x_k[9])
        msg_pb.bias.y = float(self.x_k[10])
        msg_pb.bias.z = float(self.x_k[11])

        msg_pb.drift.x = float(self.x_k[12])
        msg_pb.drift.y = float(self.x_k[13])
        msg_pb.drift.z = float(self.x_k[14])

        self.x_k = np.zeros((15,1))
        #self.get_logger().info('I received GPS Data')
        #self.get_logger().info('I publish x bias as: "%f"' % msg_pb.bias.x)
        self.deneme_pub.publish(msg_pb)
        self.pub_func(msg_pb)

    def sub_cb_strap(self, msg):
        self.old_strap.pos = msg.pos
        self.old_strap.vel = msg.vel
        self.old_strap.euler = msg.euler
        self.old_strap.quaternion = msg.quaternion


    def pub_func(self,msg):
        #self.get_logger().info('I want to publish Kalman Out')
        self.ins_gps_pub.publish(msg)
        #self.get_logger().info('I published x drift as: "%f"' % msg.drift.x)
        #self.get_logger().info('I publish z pos as: "%f"' % msg.pos.z)
        self.zaman_ref = self.get_clock().now().nanoseconds * 1e-6 #msec
        self.zaman_ref = self.zaman_ref - self.zaman_ilk
        print(self.zaman_ref, str(msg.bias.x), str(msg.bias.y), str(msg.bias.z), str(msg.drift.x), str(msg.drift.y), str(msg.drift.z), sep='\t', file=out_data_ins_gps_mid_ros_txt)

    def node_covariance_update(self):
    
        new_pos = np.zeros((3, 1))
        new_pos[0] = self.old_strap.pos.x
        new_pos[1] = self.old_strap.pos.y
        new_pos[2] = self.old_strap.pos.z

        new_vel = np.zeros((3, 1))
        new_vel[0] = self.old_strap.vel.x
        new_vel[1] = self.old_strap.vel.y
        new_vel[2] = self.old_strap.vel.z

        new_quaternion = np.zeros((4, 1))
        new_quaternion[0] = self.old_strap.quaternion.x
        new_quaternion[1] = self.old_strap.quaternion.y
        new_quaternion[2] = self.old_strap.quaternion.z        
        new_quaternion[3] = self.old_strap.quaternion.w

        f = f_matrix_construct(new_pos, new_vel, new_quaternion)
        q = q_matrix_construct()
        self.p_matrix = p_update(self.p_matrix, f, q)


    def node_kalman_update(self):

        gnss_pos = np.zeros((3, 1))
        gnss_pos[0] = self.gps_data.gps_pos.x  
        gnss_pos[1] = self.gps_data.gps_pos.y
        gnss_pos[2] = self.gps_data.gps_pos.z

        new_pos = np.zeros((3, 1))
        new_pos[0] = self.old_strap.pos.x
        new_pos[1] = self.old_strap.pos.y
        new_pos[2] = self.old_strap.pos.z

        self.p_matrix, self.x_k = kalman_update(self.p_matrix, self.x_k, gnss_pos, new_pos)



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