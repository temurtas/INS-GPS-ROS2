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
from sensor_msgs.msg import JointState
from sensor_msgs.msg import Imu

from ht_strap_package.config import base_path


# We need install numpy in order to import it
from cmath import pi
import numpy as np
import math
import ht_strap_package.config as config

from ht_nav_variables.msg import HtNavStrapOut, HtNavJointState, HtNavVehicleDebug, HtNavWheelVector, HtNavTireOut, HtNavImuData
from ht_strap_package.strap_tf_operations import *
from ht_strap_package.tire_operations_cartesian import *

# base_path = Path("/home/temur/INS-GPS-ws/INS-GPS-Matlab/veriler/veri1_to_Dogukan/")           #Ubuntu Path

# FRONT_RIGHT, 
# FRONT_LEFT, 
# REAR_RIGHT, 
# REAR_LEFT, 
# IMU_LINK  

fr_out_data_path = base_path / "front_right_wheel_pva.txt"
fr_out_data_txt = open(fr_out_data_path, 'w')

fl_out_data_path = base_path / "front_left_wheel_pva.txt"
fl_out_data_txt = open(fl_out_data_path, 'w')

rr_out_data_path = base_path / "rear_right_wheel_pva.txt"
rr_out_data_txt = open(rr_out_data_path, 'w')

rl_out_data_path = base_path / "rear_left_wheel_pva.txt"
rl_out_data_txt = open(rl_out_data_path, 'w')

imu_out_data_path = base_path / "imu_link_pva.txt"
imu_out_data_txt = open(imu_out_data_path, 'w')

fr_calc_data_path = base_path / "front_right_wheel_pva_calc.txt"
fr_calc_data_txt = open(fr_calc_data_path, 'w')

fl_calc_data_path = base_path / "front_left_wheel_pva_calc.txt"
fl_calc_data_txt = open(fl_calc_data_path, 'w')

rr_calc_data_path = base_path / "rear_right_wheel_pva_calc.txt"
rr_calc_data_txt = open(rr_calc_data_path, 'w')

rl_calc_data_path = base_path / "rear_left_wheel_pva_calc.txt"
rl_calc_data_txt = open(rl_calc_data_path, 'w')

# gps_data_path = base_path / "gps_data_ideal_gazebo.txt"
# gps_data_gazebo_txt = open(gps_data_path, 'w')

tire_out_data_ideal_path = base_path / "tire_variables_ideal_gazebo.txt"
tire_out_data_ideal_txt = open(tire_out_data_ideal_path, 'w')

joint_state_data_path = base_path / "joint_states.txt"
joint_input_data_txt = open(joint_state_data_path, 'w')

yaw_rate_path = base_path / "yaw_rate_debug.txt"
yaw_rate_txt = open(yaw_rate_path, 'w')

class RobotStateListener(Node):

    def __init__(self,qos_profile):
        super().__init__('minimal_subscriber')
        
        self.joint_state_subscription = self.create_subscription(
            JointState, 
            'kobra_mk5/joint_states', 
            self.joint_listener_callback, 
            qos_profile=qos_profile)
        
        self.joint_state_subscription = self.create_subscription(
            JointState, 
            'kobra_mk5/front_right_link_states', 
            self.front_right_link_listener_callback, 
            qos_profile=qos_profile)

        self.joint_state_subscription = self.create_subscription(
            JointState, 
            'kobra_mk5/front_left_link_states', 
            self.front_left_link_listener_callback, 
            qos_profile=qos_profile)

        self.joint_state_subscription = self.create_subscription(
            JointState, 
            'kobra_mk5/rear_right_link_states', 
            self.rear_right_link_listener_callback, 
            qos_profile=qos_profile)

        self.joint_state_subscription = self.create_subscription(
            JointState, 
            'kobra_mk5/rear_left_link_states', 
            self.rear_left_link_listener_callback, 
            qos_profile=qos_profile)

        self.joint_state_subscription = self.create_subscription(
            JointState, 
            'kobra_mk5/imu_link_states', 
            self.imu_link_listener_callback, 
            qos_profile=qos_profile)

        # Calculated States

        self.joint_state_subscription = self.create_subscription(
            JointState, 
            'front_left_calc_link_states', 
            self.front_left_link_calc_listener_callback, 
            qos_profile=qos_profile)

        self.joint_state_subscription = self.create_subscription(
            JointState, 
            'front_right_calc_link_states', 
            self.front_right_link_calc_listener_callback, 
            qos_profile=qos_profile)

        self.joint_state_subscription = self.create_subscription(
            JointState, 
            'rear_left_calc_link_states', 
            self.rear_left_link_calc_listener_callback, 
            qos_profile=qos_profile)

        self.joint_state_subscription = self.create_subscription(
            JointState, 
            'rear_right_calc_link_states', 
            self.rear_right_link_calc_listener_callback, 
            qos_profile=qos_profile)

        # FRONT_RIGHT, # Front right wheel # front_right_link_states
        # FRONT_LEFT,  # Front left wheel  # front_left_link_states
        # REAR_RIGHT,  # Rear right wheel  # rear_right_link_states
        # REAR_LEFT,   # Rear left wheel   # rear_left_link_states
        # IMU_LINK     # Steering wheel    # imu_link_states
        
        self.gps_ideal_subscription = self.create_subscription(
            NavSatFix,
            'kobra_mk5/ideal_gps_data',
            self.gps_sub_cb,
            qos_profile=qos_profile)
                  
        self.strap_imu_sub = self.create_subscription(
            Imu, 
            'kobra_mk5/imu_data_ideal', 
            self.sub_cb_imu_data, 
            qos_profile=qos_profile)

        self.joint_state_subscription  # prevent unused variable warning
        self.gps_ideal_subscription  # prevent unused variable warning
        self.strap_imu_sub  # prevent unused variable warning

        self.zaman_ref = 0.0
        self.zaman_ilk = self.get_clock().now().nanoseconds * 1e-6 #msec

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

        self.imu_link_pva = HtNavStrapOut()
        self.fl_wheel_pva = HtNavStrapOut()
        self.fr_wheel_pva = HtNavStrapOut()
        self.rl_wheel_pva = HtNavStrapOut()
        self.rr_wheel_pva = HtNavStrapOut()

        self.joint_state = HtNavJointState()
        self.joint_state.steering_angle.w1 = 0.0
        self.joint_state.steering_angle.w2 = 0.0
        self.joint_state.steering_angle.w3 = 0.0
        self.joint_state.steering_angle.w4 = 0.0

        self.joint_state.wheel_rotation.w1 = 0.0
        self.joint_state.wheel_rotation.w2 = 0.0
        self.joint_state.wheel_rotation.w3 = 0.0
        self.joint_state.wheel_rotation.w4 = 0.0
 
        self.tire_debug = HtNavVehicleDebug()

        self.imu_data = HtNavImuData()
        self.imu_data.vel_diff.x = 0.0
        self.imu_data.vel_diff.y = 0.0
        self.imu_data.vel_diff.z = 0.0
        self.imu_data.ang_diff.x = 0.0
        self.imu_data.ang_diff.y = 0.0
        self.imu_data.ang_diff.z = 0.0

        self.gazebo_time = 0.0
    

    def joint_listener_callback(self, msg):
        # self.get_logger().info('I heard joint namse as: "%f"' % msg.velocity[1])
        self.zaman_ref = self.get_clock().now().nanoseconds * 1e-6 #msec
        self.zaman_ref = self.zaman_ref - self.zaman_ilk

        temp_time_sec = float(msg.header.stamp.sec)
        temp_time_nsec = float(msg.header.stamp.nanosec)
        self.gazebo_time = temp_time_sec*1e6 + temp_time_nsec*1e-3
        
        self.joint_state.steering_angle.w1 = msg.position[0]
        self.joint_state.steering_angle.w2 = msg.position[1]
        self.joint_state.steering_angle.w3 = 0.0 # msg.position[2]
        self.joint_state.steering_angle.w4 = 0.0 # msg.position[3]

        self.joint_state.wheel_rotation.w1 = msg.velocity[0]
        self.joint_state.wheel_rotation.w2 = msg.velocity[1]
        self.joint_state.wheel_rotation.w3 = msg.velocity[2]
        self.joint_state.wheel_rotation.w4 = msg.velocity[3]

        wheel_rots = np.zeros((4, 1))
        wheel_rots[0] = self.joint_state.wheel_rotation.w1
        wheel_rots[1] = self.joint_state.wheel_rotation.w2
        wheel_rots[2] = self.joint_state.wheel_rotation.w3
        wheel_rots[3] = self.joint_state.wheel_rotation.w4
   
        steer_angs = np.zeros((4, 1))
        steer_angs[0] = self.joint_state.steering_angle.w1
        steer_angs[1] = self.joint_state.steering_angle.w2
        steer_angs[2] = self.joint_state.steering_angle.w3
        steer_angs[3] = self.joint_state.steering_angle.w4

        C_t1_b = np.zeros((3, 3))
        C_t2_b = np.zeros((3, 3))
        C_t3_b = np.zeros((3, 3))
        C_t4_b = np.zeros((3, 3))

        C_t1_b = steering2Cwb(steer_angs[0])
        C_t2_b = steering2Cwb(steer_angs[1])
        C_t3_b = steering2Cwb(steer_angs[2])
        C_t4_b = steering2Cwb(steer_angs[3])  

        # float64       time
        # HtNavTireOut  wheel_variables
        # HtNavStrapOut imu_link_pva
        # HtNavStrapOut fl_wheel_pva
        # HtNavStrapOut fr_wheel_pva
        # HtNavStrapOut rl_wheel_pva
        # HtNavStrapOut rr_wheel_pva

        self.tire_debug.fl_wheel_pva = self.fl_wheel_pva
        self.tire_debug.fr_wheel_pva = self.fr_wheel_pva
        self.tire_debug.rl_wheel_pva = self.rl_wheel_pva
        self.tire_debug.rr_wheel_pva = self.rr_wheel_pva

        # Calculate Slip ratio and Slip Angles     
        alpha_t = HtNavWheelVector()
        sigma_t = HtNavWheelVector()

        pos = np.zeros((3,1))
        pos[0] = self.imu_link_pva.pos.x
        pos[1] = self.imu_link_pva.pos.y
        pos[2] = self.imu_link_pva.pos.z

        vel = np.zeros((3,1))
        vel[0] = self.imu_link_pva.vel.x
        vel[1] = self.imu_link_pva.vel.y
        vel[2] = self.imu_link_pva.vel.z

        euler = np.zeros((3,1))
        euler[0] = self.imu_link_pva.euler.roll
        euler[1] = self.imu_link_pva.euler.pitch
        euler[2] = self.imu_link_pva.euler.yaw

        delta_ang = np.zeros((3,1))
        delta_ang[0] = self.imu_data.ang_diff.x
        delta_ang[1] = self.imu_data.ang_diff.y
        delta_ang[2] = self.imu_data.ang_diff.z

        # self.get_logger().info('I heard z delta_ang as: "%f"' % delta_ang[2])

        # yaw_rate = 0.0
        yaw_rate = yaw_rate_calc(delta_ang, pos, vel, euler)
        DELTA_T = config.delta_t

        w_ib_b = np.zeros((3,1))
        
        euler_rate = np.zeros((3,1))
        w_ib_b = delta_ang / DELTA_T # rad/sec

        euler_rate = euler_rate_calc(euler, w_ib_b)

        rh = config.vehicle_cg_2_rear_half_m              
        fh = config.vehicle_cg_2_front_half_m            
        wl = config.vehicle_width_m       


        alpha_t = tire_sideslip_angle_calc(self.tire_debug)

        # Transfer navigation solution to wheel base
        v_et1 = np.zeros((3,1))
        v_et2 = np.zeros((3,1))
        v_et3 = np.zeros((3,1))
        v_et4 = np.zeros((3,1))

        v_et1 = nav2wheels(euler, C_t1_b, self.fl_wheel_pva)
        v_et2 = nav2wheels(euler, C_t2_b, self.fr_wheel_pva)
        v_et3 = nav2wheels(euler, C_t3_b, self.rl_wheel_pva)
        v_et4 = nav2wheels(euler, C_t4_b, self.rr_wheel_pva)

        v_etk_n = np.zeros((3,1)) 
        v_etk_tk = np.zeros((3,1)) 
        C_b_tk = np.zeros((3,3)) 

        c_bn = euler2cbn(euler)
        c_nb = c_bn.transpose()

        C_b_tk = C_t1_b.transpose()

        v_etk_n[0] = self.fl_wheel_pva.vel.x
        v_etk_n[1] = self.fl_wheel_pva.vel.y
        v_etk_n[2] = self.fl_wheel_pva.vel.z
        
        temp_vel_t1 = np.dot(c_nb, v_etk_n)
        v_etk_tk =  np.dot(C_b_tk , temp_vel_t1)

        print(str(self.gazebo_time), str(float(v_etk_n[0])), str(float(v_etk_n[1])), str(float(v_etk_n[2])), str(float(v_etk_tk[0])), str(float(v_etk_tk[1])), str(float(v_etk_tk[2])),  sep='\t', file=yaw_rate_txt)

        sigma_t.w1 = float(longitudinal_tire_slip_calc(wheel_rots[0], v_et1[0]))
        sigma_t.w2 = float(longitudinal_tire_slip_calc(wheel_rots[1], v_et2[0]))
        sigma_t.w3 = float(longitudinal_tire_slip_calc(wheel_rots[2], v_et3[0]))
        sigma_t.w4 = float(longitudinal_tire_slip_calc(wheel_rots[3], v_et4[0]))

        # Calculate Tire Forces
        tire_out = HtNavTireOut()
        tire_out = tire_dugoff_force_calc(alpha_t, sigma_t)
        
        # float64          effective_radius_est
        # float64          vehicle_mass_est
        # HtNavWheelVector wheel_side_slip_ang
        # HtNavWheelVector wheel_longitudinal_slip_ratio
        # HtNavWheelVector tire_lateral_forces
        # HtNavWheelVector tire_longitudinal_forces

        self.tire_debug.wheel_variables = tire_out
    
        msg_tire_out = self.tire_debug.wheel_variables
        print(str(self.zaman_ref), str(msg_tire_out.wheel_side_slip_ang.w1), str(msg_tire_out.wheel_side_slip_ang.w2) , str(msg_tire_out.wheel_side_slip_ang.w3), str(msg_tire_out.wheel_side_slip_ang.w4), str(msg_tire_out.wheel_longitudinal_slip_ratio.w1), str(msg_tire_out.wheel_longitudinal_slip_ratio.w2) , str(msg_tire_out.wheel_longitudinal_slip_ratio.w3), str(msg_tire_out.wheel_longitudinal_slip_ratio.w4) , \
            str(msg_tire_out.tire_lateral_forces.w1), str(msg_tire_out.tire_lateral_forces.w2) , str(msg_tire_out.tire_lateral_forces.w3), str(msg_tire_out.tire_lateral_forces.w4), str(msg_tire_out.tire_longitudinal_forces.w1), str(msg_tire_out.tire_longitudinal_forces.w2) , str(msg_tire_out.tire_longitudinal_forces.w3), str(msg_tire_out.tire_longitudinal_forces.w4) , sep='\t', file=tire_out_data_ideal_txt)

        print(str(self.gazebo_time), str(msg.position[0]), str(msg.velocity[0]), str(msg.position[1]), str(msg.velocity[1]), str(msg.position[2]), str(msg.velocity[2]), str(msg.position[3]), str(msg.velocity[3]), str(msg.position[4]), str(msg.velocity[4]), sep='\t', file=joint_input_data_txt)
        
    def front_right_link_listener_callback(self, msg):
        # self.get_logger().info('I heard joint namse as: "%f"' % msg.velocity[1])
        self.zaman_ref = self.get_clock().now().nanoseconds * 1e-6 #msec
        self.zaman_ref = self.zaman_ref - self.zaman_ilk

        temp_time_sec = float(msg.header.stamp.sec)
        temp_time_nsec = float(msg.header.stamp.nanosec)
        self.gazebo_time = temp_time_sec*1e6 + temp_time_nsec*1e-3

        self.fr_wheel_pva.pos.x = -float(msg.position[1])
        self.fr_wheel_pva.pos.y = -float(msg.position[0])
        self.fr_wheel_pva.pos.z = -float(msg.position[2])

        # temp_vel = np.zeros((3, 1))
        # temp_vel2 = np.zeros((3, 1))
        # temp_vel[0] = msg.velocity[0]
        # temp_vel[1] = msg.velocity[1]
        # temp_vel[2] = msg.velocity[2]

        # temp_vel2 = np.dot(self.CRef2NED , temp_vel)

        self.fr_wheel_pva.vel.x = -float(msg.velocity[1]) # float(temp_vel[0])
        self.fr_wheel_pva.vel.y = -float(msg.velocity[0]) # float(temp_vel[1])
        self.fr_wheel_pva.vel.z = -float(msg.velocity[2]) # float(temp_vel[2])
        
        # temp_euler = np.zeros((3, 1))
        # temp_euler2 = np.zeros((3, 1))
        # temp_euler[0] = msg.effort[0]
        # temp_euler[1] = msg.effort[1]
        # temp_euler[2] = msg.effort[2]

        # temp_euler2 = np.dot(self.CENU2NED , temp_euler)

        self.fr_wheel_pva.euler.roll  = -float(msg.effort[1]) # float(temp_euler2[0])
        self.fr_wheel_pva.euler.pitch = -float(msg.effort[0]) # float(temp_euler2[1])
        self.fr_wheel_pva.euler.yaw   = -float(msg.effort[2]) # float(temp_euler2[2])

        print(str(self.gazebo_time), str(msg.position[0]), str(msg.position[1]), str(msg.position[2]), str(msg.velocity[0]), str(msg.velocity[1]), str(msg.velocity[2]), str(msg.effort[0]), str(msg.effort[1]), str(msg.effort[2]), sep='\t', file=fr_out_data_txt)

    def front_left_link_listener_callback(self, msg):
        # self.get_logger().info('I heard joint namse as: "%f"' % msg.velocity[1])
        self.zaman_ref = self.get_clock().now().nanoseconds * 1e-6 #msec
        self.zaman_ref = self.zaman_ref - self.zaman_ilk
        
        temp_time_sec = float(msg.header.stamp.sec)
        temp_time_nsec = float(msg.header.stamp.nanosec)
        self.gazebo_time = temp_time_sec*1e6 + temp_time_nsec*1e-3

        # ENU --> NED
        self.fl_wheel_pva.pos.x = -float(msg.position[1])
        self.fl_wheel_pva.pos.y = -float(msg.position[0])
        self.fl_wheel_pva.pos.z = -float(msg.position[2])

        # temp_vel = np.zeros((3, 1))
        # temp_vel2 = np.zeros((3, 1))
        # temp_vel[0] = msg.velocity[1]
        # temp_vel[1] = msg.velocity[0]
        # temp_vel[2] = - msg.velocity[2]

        self.fl_wheel_pva.vel.x = -float(msg.velocity[1]) # float(temp_vel[0])
        self.fl_wheel_pva.vel.y = -float(msg.velocity[0]) # float(temp_vel[1])
        self.fl_wheel_pva.vel.z = -float(msg.velocity[2]) # float(temp_vel[2])
        
        # temp_euler = np.zeros((3, 1))
        # temp_euler2 = np.zeros((3, 1))
        # temp_euler[0] = msg.effort[0]
        # temp_euler[1] = msg.effort[1]
        # temp_euler[2] = msg.effort[2]

        # temp_euler2 = np.dot(self.CENU2NED , temp_euler)

        self.fl_wheel_pva.euler.roll  = -float(msg.effort[1]) # float(temp_euler2[0])
        self.fl_wheel_pva.euler.pitch = -float(msg.effort[0]) # float(temp_euler2[1])
        self.fl_wheel_pva.euler.yaw   = -float(msg.effort[2]) # float(temp_euler2[2])
        
        print(str(self.gazebo_time), str(msg.position[0]), str(msg.position[1]), str(msg.position[2]), str(msg.velocity[0]), str(msg.velocity[1]), str(msg.velocity[2]), str(msg.effort[0]), str(msg.effort[1]), str(msg.effort[2]), sep='\t', file=fl_out_data_txt)

    def rear_right_link_listener_callback(self, msg):
        # self.get_logger().info('I heard joint namse as: "%f"' % msg.velocity[1])
        self.zaman_ref = self.get_clock().now().nanoseconds * 1e-6 #msec
        self.zaman_ref = self.zaman_ref - self.zaman_ilk
        
        temp_time_sec = float(msg.header.stamp.sec)
        temp_time_nsec = float(msg.header.stamp.nanosec)
        self.gazebo_time = temp_time_sec*1e6 + temp_time_nsec*1e-3

        self.rr_wheel_pva.pos.x = -float(msg.position[1])
        self.rr_wheel_pva.pos.y = -float(msg.position[0])
        self.rr_wheel_pva.pos.z = -float(msg.position[2])

        # temp_vel = np.zeros((3, 1))
        # temp_vel2 = np.zeros((3, 1))
        # temp_vel[0] = msg.velocity[0]
        # temp_vel[1] = msg.velocity[1]
        # temp_vel[2] = msg.velocity[2]

        # temp_vel2 = np.dot(self.CRef2NED , temp_vel)

        self.rr_wheel_pva.vel.x = -float(msg.velocity[1]) # float(temp_vel[0])
        self.rr_wheel_pva.vel.y = -float(msg.velocity[0]) # float(temp_vel[1])
        self.rr_wheel_pva.vel.z = -float(msg.velocity[2]) # float(temp_vel[2])
        
        # temp_euler = np.zeros((3, 1))
        # temp_euler2 = np.zeros((3, 1))
        # temp_euler[0] = msg.effort[0]
        # temp_euler[1] = msg.effort[1]
        # temp_euler[2] = msg.effort[2]

        # temp_euler2 = np.dot(self.CENU2NED , temp_euler)

        self.rr_wheel_pva.euler.roll  = -float(msg.effort[1]) # float(temp_euler2[0])
        self.rr_wheel_pva.euler.pitch = -float(msg.effort[0]) # float(temp_euler2[1])
        self.rr_wheel_pva.euler.yaw   = -float(msg.effort[2]) # float(temp_euler2[2])        
        
        print(str(self.gazebo_time), str(msg.position[0]), str(msg.position[1]), str(msg.position[2]), str(msg.velocity[0]), str(msg.velocity[1]), str(msg.velocity[2]), str(msg.effort[0]), str(msg.effort[1]), str(msg.effort[2]), sep='\t', file=rr_out_data_txt)

    def rear_left_link_listener_callback(self, msg):
        # self.get_logger().info('I heard joint namse as: "%f"' % msg.velocity[1])
        self.zaman_ref = self.get_clock().now().nanoseconds * 1e-6 #msec
        self.zaman_ref = self.zaman_ref - self.zaman_ilk

        temp_time_sec = float(msg.header.stamp.sec)
        temp_time_nsec = float(msg.header.stamp.nanosec)
        self.gazebo_time = temp_time_sec*1e6 + temp_time_nsec*1e-3

        self.rl_wheel_pva.pos.x = -float(msg.position[1])
        self.rl_wheel_pva.pos.y = -float(msg.position[0])
        self.rl_wheel_pva.pos.z = -float(msg.position[2])

        # temp_vel = np.zeros((3, 1))
        # temp_vel2 = np.zeros((3, 1))
        # temp_vel[0] = msg.velocity[0]
        # temp_vel[1] = msg.velocity[1]
        # temp_vel[2] = msg.velocity[2]

        # temp_vel2 = np.dot(self.CRef2NED , temp_vel)

        self.rl_wheel_pva.vel.x = -float(msg.velocity[1]) # float(temp_vel[0])
        self.rl_wheel_pva.vel.y = -float(msg.velocity[0]) # float(temp_vel[1])
        self.rl_wheel_pva.vel.z = -float(msg.velocity[2]) # float(temp_vel[2])
        
        # temp_euler = np.zeros((3, 1))
        # temp_euler2 = np.zeros((3, 1))
        # temp_euler[0] = msg.effort[0]
        # temp_euler[1] = msg.effort[1]
        # temp_euler[2] = msg.effort[2]

        # temp_euler2 = np.dot(self.CENU2NED , temp_euler)

        self.rl_wheel_pva.euler.roll  = -float(msg.effort[1]) # float(temp_euler2[0])
        self.rl_wheel_pva.euler.pitch = -float(msg.effort[0]) # float(temp_euler2[1])
        self.rl_wheel_pva.euler.yaw   = -float(msg.effort[2]) # float(temp_euler2[2])

        print(str(self.gazebo_time), str(msg.position[0]), str(msg.position[1]), str(msg.position[2]), str(msg.velocity[0]), str(msg.velocity[1]), str(msg.velocity[2]), str(msg.effort[0]), str(msg.effort[1]), str(msg.effort[2]), sep='\t', file=rl_out_data_txt)

    def imu_link_listener_callback(self, msg):
        # self.get_logger().info('I heard joint namse as: "%f"' % msg.velocity[1])
        self.zaman_ref = self.get_clock().now().nanoseconds * 1e-6 #msec
        self.zaman_ref = self.zaman_ref - self.zaman_ilk
        
        temp_time_sec = float(msg.header.stamp.sec)
        temp_time_nsec = float(msg.header.stamp.nanosec)
        self.gazebo_time = temp_time_sec*1e6 + temp_time_nsec*1e-3

        self.imu_link_pva.pos.x = -float(msg.position[1])
        self.imu_link_pva.pos.y = -float(msg.position[0])
        self.imu_link_pva.pos.z = -float(msg.position[2])

        # temp_vel = np.zeros((3, 1))
        # temp_vel2 = np.zeros((3, 1))
        # temp_vel[0] = msg.velocity[0]
        # temp_vel[1] = msg.velocity[1]
        # temp_vel[2] = msg.velocity[2]

        # temp_vel2 = np.dot(self.CRef2NED , temp_vel)

        self.imu_link_pva.vel.x = -float(msg.velocity[1]) # float(temp_vel[0])
        self.imu_link_pva.vel.y = -float(msg.velocity[0]) # float(temp_vel[1])
        self.imu_link_pva.vel.z = -float(msg.velocity[2]) # float(temp_vel[2])
        
        # temp_euler = np.zeros((3, 1))
        # temp_euler2 = np.zeros((3, 1))
        # temp_euler[0] = msg.effort[0]
        # temp_euler[1] = msg.effort[1]
        # temp_euler[2] = msg.effort[2]

        # temp_euler2 = np.dot(self.CENU2NED , temp_euler)

        self.imu_link_pva.euler.roll  = -float(msg.effort[1]) # float(temp_euler2[0])
        self.imu_link_pva.euler.pitch = -float(msg.effort[0]) # float(temp_euler2[1])
        self.imu_link_pva.euler.yaw   = -float(msg.effort[2]) # float(temp_euler2[2])        
        
        print(str(self.gazebo_time), str(msg.position[0]), str(msg.position[1]), str(msg.position[2]), str(msg.velocity[0]), str(msg.velocity[1]), str(msg.velocity[2]), str(msg.effort[0]), str(msg.effort[1]), str(msg.effort[2]), sep='\t', file=imu_out_data_txt)

    def front_right_link_calc_listener_callback(self, msg):
        # self.get_logger().info('I heard joint namse as: "%f"' % msg.velocity[1])
        self.zaman_ref = self.get_clock().now().nanoseconds * 1e-6 #msec
        self.zaman_ref = self.zaman_ref - self.zaman_ilk
        print(str(self.zaman_ref), str(msg.position[0]), str(msg.position[1]), str(msg.position[2]), str(msg.velocity[0]), str(msg.velocity[1]), str(msg.velocity[2]), str(msg.effort[0]), str(msg.effort[1]), str(msg.effort[2]), sep='\t', file=fr_calc_data_txt)

    def front_left_link_calc_listener_callback(self, msg):
        # self.get_logger().info('I heard joint namse as: "%f"' % msg.velocity[1])
        self.zaman_ref = self.get_clock().now().nanoseconds * 1e-6 #msec
        self.zaman_ref = self.zaman_ref - self.zaman_ilk
        print(str(self.zaman_ref), str(msg.position[0]), str(msg.position[1]), str(msg.position[2]), str(msg.velocity[0]), str(msg.velocity[1]), str(msg.velocity[2]), str(msg.effort[0]), str(msg.effort[1]), str(msg.effort[2]), sep='\t', file=fl_calc_data_txt)

    def rear_right_link_calc_listener_callback(self, msg):
        self.zaman_ref = self.get_clock().now().nanoseconds * 1e-6 #msec
        self.zaman_ref = self.zaman_ref - self.zaman_ilk
        print(str(self.zaman_ref), str(msg.position[0]), str(msg.position[1]), str(msg.position[2]), str(msg.velocity[0]), str(msg.velocity[1]), str(msg.velocity[2]), str(msg.effort[0]), str(msg.effort[1]), str(msg.effort[2]), sep='\t', file=rr_calc_data_txt)

    def rear_left_link_calc_listener_callback(self, msg):
        # self.get_logger().info('I heard joint namse as: "%f"' % msg.velocity[1])
        self.zaman_ref = self.get_clock().now().nanoseconds * 1e-6 #msec
        self.zaman_ref = self.zaman_ref - self.zaman_ilk
        print(str(self.zaman_ref), str(msg.position[0]), str(msg.position[1]), str(msg.position[2]), str(msg.velocity[0]), str(msg.velocity[1]), str(msg.velocity[2]), str(msg.effort[0]), str(msg.effort[1]), str(msg.effort[2]), sep='\t', file=rl_calc_data_txt)


    def gps_sub_cb(self, msg):      
        # self.gps_data_ideal.gps_pos.x = msg.latitude 
        # self.gps_data_ideal.gps_pos.y = msg.longitude
        # self.gps_data_ideal.gps_pos.z = msg.altitude

        # self.gps_data_ideal.gps_vel.x = 0.0
        # self.gps_data_ideal.gps_vel.y = 0.0
        # self.gps_data_ideal.gps_vel.z = 0.0

        self.zaman_ref = self.get_clock().now().nanoseconds * 1e-6 #msec
        self.zaman_ref = self.zaman_ref - self.zaman_ilk
        # print(str(self.zaman_ref), str(self.gps_data_ideal.gps_pos.x), str(self.gps_data_ideal.gps_pos.y), str(self.gps_data_ideal.gps_pos.z), str(self.gps_data_ideal.gps_vel.x), str(self.gps_data_ideal.gps_vel.y), str(self.gps_data_ideal.gps_vel.z), sep='\t', file=gps_data_gazebo_txt)


    def sub_cb_imu_data(self, msg):
        DELTA_T = config.delta_t

        self.imu_data.vel_diff.x = -msg.linear_acceleration.y * DELTA_T
        self.imu_data.vel_diff.y = -msg.linear_acceleration.x * DELTA_T
        self.imu_data.vel_diff.z = -msg.linear_acceleration.z * DELTA_T

        # self.get_logger().info('I heard z gyro as: "%f"' % msg.angular_velocity.z)

        self.imu_data.ang_diff.x = -msg.angular_velocity.y * DELTA_T
        self.imu_data.ang_diff.y = -msg.angular_velocity.x * DELTA_T
        self.imu_data.ang_diff.z = -msg.angular_velocity.z * DELTA_T

        self.zaman_ref = self.get_clock().now().nanoseconds * 1e-6 #msec
        self.zaman_ref = self.zaman_ref - self.zaman_ilk
        # print(str(self.zaman_ref), str(self.imu_data.ang_diff.x), str(self.imu_data.ang_diff.y), str(self.imu_data.ang_diff.z), str(self.imu_data.vel_diff.x), str(self.imu_data.vel_diff.y), str(self.imu_data.vel_diff.z), sep='\t', file=imu_data_gazebo_txt)


def main(args=None):
    rclpy.init(args=args)

    custom_qos_profile = qos_profile_sensor_data

    minimal_subscriber = RobotStateListener(custom_qos_profile)

    rclpy.spin(minimal_subscriber)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    minimal_subscriber.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
