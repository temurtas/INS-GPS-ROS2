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
from sensor_msgs.msg import Imu
from sensor_msgs.msg import NavSatFix
from sensor_msgs.msg import JointState
#from ht_nav_variables.msg import HtNavDeneme
from ht_nav_variables.msg import HtNavImuData
from ht_nav_variables.msg import HtNavGpsData
from ht_nav_variables.msg import HtNavQuaternion
from ht_nav_variables.msg import HtNavEuler
from ht_nav_variables.msg import HtNavStrapOut
from ht_nav_variables.msg import HtNavKalmanOut 

from ht_strap_package.strap_tf_operations import *
from ht_strap_package.kalman_operations_cartesian import *
from ht_strap_package.strap_operations_cartesian import *

from ht_strap_package.config import base_path
from ht_strap_package.config import buffer_size
from ht_strap_package.config import DEG2RAD
from ht_strap_package.config import kalman_prop_const 
from ht_strap_package.config import delta_t

from cmath import pi

base_path2 = base_path 
strap_data_ins_gps_mid_txt = base_path2 / "strap_data_cartesian_pv.txt"
strap_data_gazebo_ros_txt = open(strap_data_ins_gps_mid_txt, 'w')

ros_gazebo_kalman_out =  base_path2 / "kalman_out_cartesian_pv.txt"
out_data_strap_kalman_ros_txt = open(ros_gazebo_kalman_out, 'w')

imu_data_path = base_path2 / "imu_data_cartesian_pv_gazebo.txt"
imu_data_gazebo_txt = open(imu_data_path, 'w')

imu_data_calib_path = base_path2 / "imu_data_calibrated_cartesian_pv_gazebo.txt"
imu_data_calib_txt = open(imu_data_calib_path, 'w')

gps_data_path = base_path2 / "gps_data_link_cartesian_pv_gazebo.txt"
gps_data_gazebo_txt = open(gps_data_path, 'w')

kalman_p_diag_path = base_path2 / "kalman_p_diag_cartesian_pv.txt"
kalman_p_diag_txt = open(kalman_p_diag_path, 'w')

kalman_dx_path = base_path2 / "kalman_dx_cartesian_pv.txt"
kalman_dx_txt = open(kalman_dx_path, 'w')

kalman_y_path = base_path2 / "kalman_y_cartesian_pv.txt"
kalman_y_txt = open(kalman_y_path, 'w')

class INSGPSNode(Node):

    def __init__(self, qos_profile):
        ''' 
        Class constructor to initialise the class 
        '''
        super().__init__('ins_gps_node')

        # Initialise publishers
        self.ins_gps_pub = self.create_publisher(HtNavKalmanOut, 'ht_nav_kalman_out', qos_profile=qos_profile)
        self.strap_w_kalman_pub = self.create_publisher(HtNavStrapOut, 'ht_nav_strap_data', qos_profile=qos_profile)
        # Initialise subscribers
        # self.gps_sub = self.create_subscription(NavSatFix, 'kobra_mk5/gps_data', self.sub_cb_gps_data, qos_profile=qos_profile)
        self.gps_sub = self.create_subscription(JointState, 'kobra_mk5/link_gps_data', self.sub_cb_gps_data, qos_profile=qos_profile)
        self.strap_imu_sub = self.create_subscription(Imu,  'kobra_mk5/imu_data_body', self.sub_cb_imu_data, qos_profile=qos_profile)
        # self.strap_imu_sub = self.create_subscription(Imu, 'kobra_mk5/imu_data', self.sub_cb_imu_data, qos_profile=qos_profile)

        self.strap_sayac = 0
        self.kalman_sayac = 0

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

        self.imu_data = HtNavImuData()
        self.imu_data.vel_diff.x = 0.0
        self.imu_data.vel_diff.y = 0.0
        self.imu_data.vel_diff.z = 0.0
        self.imu_data.ang_diff.x = 0.0
        self.imu_data.ang_diff.y = 0.0
        self.imu_data.ang_diff.z = 0.0

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
        self.new_strap = HtNavStrapOut()

        # initialization 
        # self.old_strap.pos.x = 39.89044287479834 * DEG2RAD
        # self.old_strap.pos.y = 32.781467396951804 * DEG2RAD
        # self.old_strap.pos.z = 934.00
        # self.old_strap.pos.x = 0.696218877917194
        # self.old_strap.pos.y = 0.572145046188725
        # self.old_strap.pos.z = 934.011640024371
        # self.old_strap.car_pos.x = 0.0
        # self.old_strap.car_pos.y = 0.0
        # self.old_strap.car_pos.z = 0.0
        self.old_strap.pos.x = - 1.45
        self.old_strap.pos.y = + 0.00
        self.old_strap.pos.z = - 0.30
        
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
        
        init_pos_err = 5 * np.random.randn(3)
        init_vel_err = 0.2 * np.random.randn(3)
        init_att_err = 10e-3 * np.random.randn(3)
        
        self.old_strap.pos.x = self.old_strap.pos.x + init_pos_err[0]
        self.old_strap.pos.y = self.old_strap.pos.y + init_pos_err[1]
        self.old_strap.pos.z = self.old_strap.pos.z + init_pos_err[2]

        self.old_strap.vel.x = self.old_strap.vel.x + init_vel_err[0]
        self.old_strap.vel.y = self.old_strap.vel.y + init_vel_err[1]
        self.old_strap.vel.z = self.old_strap.vel.z + init_vel_err[2]

        self.old_strap.euler.roll  = self.old_strap.euler.roll  + init_att_err[0]
        self.old_strap.euler.pitch = self.old_strap.euler.pitch + init_att_err[1]
        self.old_strap.euler.yaw   = self.old_strap.euler.yaw   + init_att_err[2]

        err_euler = np.zeros((3,1))
        err_quat  = np.zeros((4,1))

        err_euler[0] = self.old_strap.euler.roll 
        err_euler[1] = self.old_strap.euler.pitch
        err_euler[2] = self.old_strap.euler.yaw 
        err_quat = euler2quaternion(err_euler)

        self.old_strap.quaternion.x = float(err_quat[0])
        self.old_strap.quaternion.y = float(err_quat[1])
        self.old_strap.quaternion.z = float(err_quat[2])
        self.old_strap.quaternion.w = float(err_quat[3])

        self.new_strap = self.old_strap

        self.p_matrix = np.zeros((15, 15))
        self.p_matrix = p0_matrix_construct()

        self.f_matrix = np.zeros((15, 15))
        self.q_matrix = np.zeros((15, 15))
        
        self.x_k = np.zeros((15,1))
        self.y   = np.zeros((6, 1))

        self.total_vel_inc = np.zeros((3,1))
        self.total_ang_inc = np.zeros((3,1))

        self.imu_bias_est  = np.zeros((3,1))
        self.imu_drift_est = np.zeros((3,1))

        self.gazebo_time = 0.0

        Ref2NedEuler = np.zeros((3, 1))
        self.CRef2NED = np.zeros((3, 3))

        Ref2NedEuler[0] = pi
        Ref2NedEuler[1] = 0.0
        Ref2NedEuler[2] = - pi / 2
        self.CRef2NED = euler2cbn(Ref2NedEuler)

        Enu2NEDEuler = np.zeros((3, 1))
        self.CENU2NED = np.zeros((3, 3))

        Enu2NEDEuler[0] = pi
        Enu2NEDEuler[1] = 0.0
        Enu2NEDEuler[2] = - pi / 2
        self.CENU2NED = euler2cbn(Enu2NEDEuler)

    def sub_cb_imu_data(self, msg):
        #self.get_logger().info('I heard vel_diff x as: "%f"' % msg.vel_diff.x)
        
        # self.imu_data.vel_diff = msg.vel_diff
        # self.imu_data.ang_diff = msg.ang_diff
        temp_time_sec = float(msg.header.stamp.sec)
        temp_time_nsec = float(msg.header.stamp.nanosec)
        self.gazebo_time = temp_time_sec*1e6 + temp_time_nsec*1e-3

        self.imu_data.time = self.gazebo_time
        
        # Tranform measurements from IMU-frame to Vehicle Body Frame
        self.imu_data.vel_diff.x = -msg.linear_acceleration.y * delta_t # m/s
        self.imu_data.vel_diff.y = -msg.linear_acceleration.x * delta_t # m/s
        self.imu_data.vel_diff.z = -msg.linear_acceleration.z * delta_t # m/s

        self.imu_data.ang_diff.x = -msg.angular_velocity.y * delta_t # rad
        self.imu_data.ang_diff.y = -msg.angular_velocity.x * delta_t # rad
        self.imu_data.ang_diff.z = -msg.angular_velocity.z * delta_t # rad
        
        print(str(self.imu_data.time), str(self.imu_data.ang_diff.x), str(self.imu_data.ang_diff.y), str(self.imu_data.ang_diff.z), str(self.imu_data.vel_diff.x), str(self.imu_data.vel_diff.y), str(self.imu_data.vel_diff.z), sep='\t', file=imu_data_gazebo_txt)

        # Calibrate the measurements using the estimated IMU bias and drift
        self.imu_data.vel_diff.x = self.imu_data.vel_diff.x - float(self.imu_bias_est[0]) * delta_t # m/s
        self.imu_data.vel_diff.y = self.imu_data.vel_diff.y - float(self.imu_bias_est[1]) * delta_t # m/s
        self.imu_data.vel_diff.z = self.imu_data.vel_diff.z - float(self.imu_bias_est[2]) * delta_t # m/s

        self.imu_data.ang_diff.x = self.imu_data.ang_diff.x - float(self.imu_drift_est[0]) * delta_t # rad
        self.imu_data.ang_diff.y = self.imu_data.ang_diff.y - float(self.imu_drift_est[1]) * delta_t # rad
        self.imu_data.ang_diff.z = self.imu_data.ang_diff.z - float(self.imu_drift_est[2]) * delta_t # rad

        print(str(self.imu_data.time), str(self.imu_data.ang_diff.x), str(self.imu_data.ang_diff.y), str(self.imu_data.ang_diff.z), str(self.imu_data.vel_diff.x), str(self.imu_data.vel_diff.y), str(self.imu_data.vel_diff.z), sep='\t', file=imu_data_calib_txt)

        # Calculate the velocity and angle increments
        self.total_vel_inc[0] = self.total_vel_inc[0] + self.imu_data.vel_diff.x # m/s
        self.total_vel_inc[1] = self.total_vel_inc[1] + self.imu_data.vel_diff.y # m/s
        self.total_vel_inc[2] = self.total_vel_inc[2] + self.imu_data.vel_diff.z # m/s

        self.total_ang_inc[0] = self.total_ang_inc[0] + self.imu_data.ang_diff.x # rad
        self.total_ang_inc[1] = self.total_ang_inc[1] + self.imu_data.ang_diff.y # rad
        self.total_ang_inc[2] = self.total_ang_inc[2] + self.imu_data.ang_diff.z # rad

        # Strapdown Inertail Navigation Algoritm
        self.new_strap = self.node_strapdown(self.old_strap, self.imu_data)
        self.old_strap = self.new_strap

        # Construct the message to be published
        msg_pb = HtNavStrapOut()
        msg_pb.time  = self.gazebo_time
        msg_pb.pos   = self.new_strap.pos
        msg_pb.vel   = self.new_strap.vel
        msg_pb.euler = self.new_strap.euler
        msg_pb.quaternion = self.new_strap.quaternion

        if (self.strap_sayac % kalman_prop_const  == 0):
            self.node_covariance_update()
            self.total_vel_inc[0] = 0.0
            self.total_vel_inc[1] = 0.0
            self.total_vel_inc[2] = 0.0

            self.total_ang_inc[0] = 0.0
            self.total_ang_inc[1] = 0.0
            self.total_ang_inc[2] = 0.0

        self.strap_sayac = self.strap_sayac + 1

        self.strap_pub_func(msg_pb)
        
        self.zaman_ref = self.get_clock().now().nanoseconds * 1e-6 #msec
        self.zaman_ref = self.zaman_ref - self.zaman_ilk
        # print(str(self.imu_data.time), str(self.imu_data.ang_diff.x), str(self.imu_data.ang_diff.y), str(self.imu_data.ang_diff.z), str(self.imu_data.vel_diff.x), str(self.imu_data.vel_diff.y), str(self.imu_data.vel_diff.z), sep='\t', file=imu_data_gazebo_txt)


    def sub_cb_gps_data(self, msg):
        # self.gps_data.gps_pos = msg.gps_pos
        # self.gps_data.gps_vel = msg.gps_vel
        
        temp_time_sec = float(msg.header.stamp.sec)
        temp_time_nsec = float(msg.header.stamp.nanosec)
        self.gazebo_time = temp_time_sec*1e6 + temp_time_nsec*1e-3

        self.gps_data.time = self.gazebo_time

        self.gps_data.gps_pos.x = float(msg.position[0])
        self.gps_data.gps_pos.y = float(msg.position[1])
        self.gps_data.gps_pos.z = float(msg.position[2])

        self.gps_data.gps_vel.x = float(msg.velocity[0])
        self.gps_data.gps_vel.y = float(msg.velocity[1])
        self.gps_data.gps_vel.z = float(msg.velocity[2])

        #print(str(self.gps_data.gps_pos.x), str(self.gps_data.gps_pos.y), str(self.gps_data.gps_pos.z), str(self.gps_data.gps_vel.x), str(self.gps_data.gps_vel.y), str(self.gps_data.gps_vel.z), sep='\t', file=deneme_txt_1)

        self.node_kalman_update()
        self.kalkman_sayac = self.kalman_sayac + 1

        msg_pb = HtNavKalmanOut() 

        msg_pb.time = self.gazebo_time

        msg_pb.pos_err.x = float(self.x_k[0])
        msg_pb.pos_err.y = float(self.x_k[1])
        msg_pb.pos_err.z = float(self.x_k[2])

        msg_pb.vel_err.x = float(self.x_k[3])
        msg_pb.vel_err.y = float(self.x_k[4])
        msg_pb.vel_err.z = float(self.x_k[5])

        msg_pb.att_err.x = float(self.x_k[6])
        msg_pb.att_err.y = float(self.x_k[7])
        msg_pb.att_err.z = float(self.x_k[8])

        self.imu_bias_est[0] = self.imu_bias_est[0] + float(self.x_k[9])
        self.imu_bias_est[1] = self.imu_bias_est[1] + float(self.x_k[10])
        self.imu_bias_est[2] = self.imu_bias_est[2] + float(self.x_k[11])

        self.imu_drift_est[0] = self.imu_drift_est[0] + float(self.x_k[12])
        self.imu_drift_est[1] = self.imu_drift_est[1] + float(self.x_k[13])
        self.imu_drift_est[2] = self.imu_drift_est[2] + float(self.x_k[14])

        msg_pb.bias.x = float(self.imu_bias_est[0])
        msg_pb.bias.y = float(self.imu_bias_est[1])
        msg_pb.bias.z = float(self.imu_bias_est[2])

        msg_pb.drift.x = float(self.imu_drift_est[0])
        msg_pb.drift.y = float(self.imu_drift_est[1])
        msg_pb.drift.z = float(self.imu_drift_est[2])

        self.x_k = np.zeros((15,1))
        self.kalman_pub_func(msg_pb)

        self.zaman_ref = self.get_clock().now().nanoseconds * 1e-6 #msec
        self.zaman_ref = self.zaman_ref - self.zaman_ilk
        print(str(self.gps_data.time), str(self.gps_data.gps_pos.x), str(self.gps_data.gps_pos.y), str(self.gps_data.gps_pos.z), str(self.gps_data.gps_vel.x), str(self.gps_data.gps_vel.y), str(self.gps_data.gps_vel.z), sep='\t', file=gps_data_gazebo_txt)


    def kalman_pub_func(self,msg):
        #self.get_logger().info('I want to publish Kalman Out')
        self.ins_gps_pub.publish(msg)
        #self.get_logger().info('I published x drift as: "%f"' % msg.drift.x)
        #self.get_logger().info('I publish z pos as: "%f"' % msg.pos.z)
        self.zaman_ref = self.get_clock().now().nanoseconds * 1e-6 #msec
        self.zaman_ref = self.zaman_ref - self.zaman_ilk
        print(str(msg.time), str(msg.bias.x), str(msg.bias.y), str(msg.bias.z), str(msg.drift.x), str(msg.drift.y), str(msg.drift.z), sep='\t', file=out_data_strap_kalman_ros_txt)

    def node_covariance_update(self):
    
        new_pos = np.zeros((3, 1))
        new_pos[0] = self.new_strap.pos.x
        new_pos[1] = self.new_strap.pos.y
        new_pos[2] = self.new_strap.pos.z

        new_vel = np.zeros((3, 1))
        new_vel[0] = self.new_strap.vel.x
        new_vel[1] = self.new_strap.vel.y
        new_vel[2] = self.new_strap.vel.z

        new_quaternion = np.zeros((4, 1))
        new_quaternion[0] = self.new_strap.quaternion.x
        new_quaternion[1] = self.new_strap.quaternion.y
        new_quaternion[2] = self.new_strap.quaternion.z        
        new_quaternion[3] = self.new_strap.quaternion.w

        self.f_matrix = f_matrix_construct_pv(new_quaternion, self.total_vel_inc)
        self.q_matrix = q_matrix_construct_pv(new_quaternion, self.total_vel_inc, self.total_ang_inc)
        self.p_matrix = p_update(self.p_matrix, self.f_matrix, self.q_matrix)

        print(str(self.imu_data.time), str(self.p_matrix[0,0]), str(self.p_matrix[1,1]), str(self.p_matrix[2,2]), str(self.p_matrix[3,3]), str(self.p_matrix[4,4]), str(self.p_matrix[5,5]), str(self.p_matrix[6,6]), str(self.p_matrix[7,7]), str(self.p_matrix[8,8]), str(self.p_matrix[9,9]), str(self.p_matrix[10,10]), str(self.p_matrix[11,11]), str(self.p_matrix[12,12]), str(self.p_matrix[13,13]), str(self.p_matrix[14,14]), sep='\t', file=kalman_p_diag_txt)

    def node_kalman_update(self):

        gnss_pos = np.zeros((3, 1))
        gnss_pos[0] = self.gps_data.gps_pos.x  
        gnss_pos[1] = self.gps_data.gps_pos.y
        gnss_pos[2] = self.gps_data.gps_pos.z

        gnss_vel = np.zeros((3, 1))
        gnss_vel[0] = self.gps_data.gps_vel.x  
        gnss_vel[1] = self.gps_data.gps_vel.y
        gnss_vel[2] = self.gps_data.gps_vel.z

        new_pos = np.zeros((3, 1))
        new_pos[0] = self.new_strap.pos.x
        new_pos[1] = self.new_strap.pos.y
        new_pos[2] = self.new_strap.pos.z

        new_vel = np.zeros((3, 1))
        new_vel[0] = self.new_strap.vel.x
        new_vel[1] = self.new_strap.vel.y
        new_vel[2] = self.new_strap.vel.z

        self.y[0] = gnss_pos[0] - new_pos[0] 
        self.y[1] = gnss_pos[1] - new_pos[1] 
        self.y[2] = gnss_pos[2] - new_pos[2] 
        self.y[3] = gnss_vel[0] - new_vel[0] 
        self.y[4] = gnss_vel[1] - new_vel[1] 
        self.y[5] = gnss_vel[2] - new_vel[2] 

        self.p_matrix, self.x_k = kalman_update_pv(self.p_matrix, self.x_k, self.y)

        print(str(self.gps_data.time), str(self.x_k[0,0]), str(self.x_k[1,0]), str(self.x_k[2,0]), str(self.x_k[3,0]), str(self.x_k[4,0]), str(self.x_k[5,0]), str(self.x_k[6,0]), str(self.x_k[7,0]), str(self.x_k[8,0]), str(self.x_k[9,0]), str(self.x_k[10,0]), str(self.x_k[11,0]), str(self.x_k[12,0]), str(self.x_k[13,0]), str(self.x_k[14,0]), sep='\t', file=kalman_dx_txt)
        print(str(self.gps_data.time), str(float(self.y[0])), str(float(self.y[1])), str(float(self.y[2])), str(float(self.y[3])), str(float(self.y[4])), str(float(self.y[5])), sep='\t', file=kalman_y_txt)

        self.new_strap = kalman_duzeltme_pv(self.old_strap, self.x_k)
        self.old_strap = self.new_strap


    def strap_pub_func(self,msg):
        self.strap_w_kalman_pub.publish(msg)
        #self.get_logger().info('I publish z pos as: "%f"' % msg.pos.z)
        self.zaman_ref = self.get_clock().now().nanoseconds * 1e-6 #msec
        self.zaman_ref = self.zaman_ref - self.zaman_ilk
        print(str(msg.time), str(msg.pos.x), str(msg.pos.y), str(msg.pos.z), str(msg.vel.x), str(msg.vel.y), str(msg.vel.z), str(msg.euler.roll), str(msg.euler.pitch), str(msg.euler.yaw), sep='\t', file=strap_data_gazebo_ros_txt)

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