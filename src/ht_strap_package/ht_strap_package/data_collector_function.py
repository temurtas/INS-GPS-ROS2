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

from gazebo_msgs.msg import ContactsState

from sensor_msgs.msg import NavSatFix
from sensor_msgs.msg import JointState
from sensor_msgs.msg import Imu

from ht_strap_package.config import base_path


# We need install numpy in order to import it
from cmath import pi
import numpy as np
import math
import ht_strap_package.config as config

from ht_nav_variables.msg import HtNavStrapOut, HtNavJointState, HtNavGpsData, HtNavImuData
from ht_strap_package.strap_tf_operations import *
from ht_strap_package.config import DEG2RAD
from ht_nav_variables.msg import HtNavContactState
from ht_nav_variables.msg import HtNavContactStates

# base_path = Path("/home/temur/INS-GPS-ws/INS-GPS-Matlab/veriler/veri1_to_Dogukan/")           #Ubuntu Path

# FRONT_RIGHT, 
# FRONT_LEFT, 
# REAR_RIGHT, 
# REAR_LEFT, 
# IMU_LINK  

fr_out_data_path = base_path / "front_right_wheel_pva_sync.txt"
fr_out_data_txt = open(fr_out_data_path, 'w')

fl_out_data_path = base_path / "front_left_wheel_pva_sync.txt"
fl_out_data_txt = open(fl_out_data_path, 'w')

rr_out_data_path = base_path / "rear_right_wheel_pva_sync.txt"
rr_out_data_txt = open(rr_out_data_path, 'w')

rl_out_data_path = base_path / "rear_left_wheel_pva_sync.txt"
rl_out_data_txt = open(rl_out_data_path, 'w')

imu_out_data_path = base_path / "imu_link_pva_sync.txt"
imu_out_data_txt = open(imu_out_data_path, 'w')

imu_link_data_path = base_path / "imu_link_data_sync.txt"
imu_link_data_txt = open(imu_link_data_path, 'w')

imu_link_data_path2 = base_path / "imu_data_link_body_sync.txt"
imu_link_data2_txt = open(imu_link_data_path2, 'w')

imu_data_path = base_path / "imu_data_sync.txt"
imu_data_txt = open(imu_data_path, 'w')

imu_ideal_data_path = base_path / "imu_data_ideal_sync.txt"
imu_data_ideal_txt = open(imu_ideal_data_path, 'w')

gps_link_data_path = base_path / "gps_link_data_sync.txt"
gps_link_data_txt = open(gps_link_data_path, 'w')

gps_data_path = base_path / "gps_data_sync.txt"
gps_data_txt = open(gps_data_path, 'w')

gps_data_ideal_path = base_path / "gps_data_ideal_sync.txt"
gps_data_ideal_txt = open(gps_data_ideal_path, 'w')

joint_state_data_path = base_path / "joint_states_sync.txt"
joint_input_data_txt = open(joint_state_data_path, 'w')

fl_contact_states_path = base_path / "fl_contact_states_sync.txt"
fl_contact_states_txt = open(fl_contact_states_path, 'w')

fr_contact_states_path = base_path / "fr_contact_states_sync.txt"
fr_contact_states_txt = open(fr_contact_states_path, 'w')

rl_contact_states_path = base_path / "rl_contact_states_sync.txt"
rl_contact_states_txt = open(rl_contact_states_path, 'w')

rr_contact_states_path = base_path / "rr_contact_states_sync.txt"
rr_contact_states_txt = open(rr_contact_states_path, 'w')

class DataCollector(Node):

    def __init__(self,qos_profile):
        super().__init__('minimal_subscriber')
        
        self.joint_state_subscription = self.create_subscription(
            JointState, 
            'kobra_mk5/joint_states', 
            self.joint_listener_callback, 
            qos_profile=qos_profile)
        
        self.fr_link_subscription = self.create_subscription(
            JointState, 
            'kobra_mk5/front_right_link_states', 
            self.front_right_link_listener_callback, 
            qos_profile=qos_profile)

        self.fl_link_subscription = self.create_subscription(
            JointState, 
            'kobra_mk5/front_left_link_states', 
            self.front_left_link_listener_callback, 
            qos_profile=qos_profile)

        self.rr_link_subscription = self.create_subscription(
            JointState, 
            'kobra_mk5/rear_right_link_states', 
            self.rear_right_link_listener_callback, 
            qos_profile=qos_profile)

        self.rl_link_subscription = self.create_subscription(
            JointState, 
            'kobra_mk5/rear_left_link_states', 
            self.rear_left_link_listener_callback, 
            qos_profile=qos_profile)

        self.imu_link_subscription = self.create_subscription(
            JointState, 
            'kobra_mk5/imu_link_states', 
            self.imu_link_listener_callback, 
            qos_profile=qos_profile)

        self.imu_link_meas_subscription = self.create_subscription(
            JointState, 
            'kobra_mk5/imu_link_measurements', 
            self.imu_link_meas_listener_callback, 
            qos_profile=qos_profile)

        self.imu_link_meas_subscription2 = self.create_subscription(
            JointState, 
            'kobra_mk5/imu_data_link_body', 
            self.imu_link_meas_listener_callback2, 
            qos_profile=qos_profile)

        # Initialise subscribers
        # self.gps_sub = self.create_subscription(
        #     NavSatFix, 
        #     'kobra_mk5/gps_data', 
        #     self.sub_cb_gps_data, 
        #     qos_profile=qos_profile)
        
        self.strap_imu_sub = self.create_subscription(
            Imu, 
            'kobra_mk5/imu_data_body', 
            self.sub_cb_imu_data, 
            qos_profile=qos_profile)

        # self.strap_imu_sub = self.create_subscription(
        #     Imu, 
        #     'kobra_mk5/imu_data', 
        #     self.sub_cb_imu_data, 
        #     qos_profile=qos_profile)

        # self.gps_ideal_subscription = self.create_subscription(
        #     NavSatFix,
        #     'kobra_mk5/ideal_gps_data',
        #     self.ideal_gps_sub_cb,
        #     qos_profile=qos_profile)
        
        self.strap_imu_sub = self.create_subscription(
            Imu, 
            'kobra_mk5/imu_data_body_ideal', 
            self.sub_cb_imu_data_ideal, 
            qos_profile=qos_profile)

        # self.strap_imu_sub = self.create_subscription(
        #     Imu, 
        #     'kobra_mk5/imu_data_ideal', 
        #     self.sub_cb_imu_data_ideal, 
        #     qos_profile=qos_profile)

        self.gps_link_sub = self.create_subscription(
            JointState, 
            'kobra_mk5/link_gps_data', 
            self.gps_link_cb, 
            qos_profile=qos_profile)

        # self.fl_contact_sub = self.create_subscription(
        #     ContactsState, 
        #     'kobra_mk5/front_left_contact_forces', 
        #     self.fl_contact_cb, 
        #     qos_profile=qos_profile)

        # self.fr_contact_sub = self.create_subscription(
        #     ContactsState, 
        #     'kobra_mk5/front_right_contact_forces', 
        #     self.fr_contact_cb, 
        #     qos_profile=qos_profile)

        # self.rl_contact_sub = self.create_subscription(
        #     ContactsState, 
        #     'kobra_mk5/rear_left_contact_forces', 
        #     self.rl_contact_cb, 
        #     qos_profile=qos_profile)

        # self.rr_contact_sub = self.create_subscription(
        #     ContactsState, 
        #     'kobra_mk5/rear_right_contact_forces', 
        #     self.rr_contact_cb, 
        #     qos_profile=qos_profile)

        self.fl_surface_sub = self.create_subscription(
            JointState, 
            'kobra_mk5/front_left_wheel_contact_states', 
            self.fl_contact_surface_listener_callback, 
            qos_profile=qos_profile)
        
        self.fr_surface_sub = self.create_subscription(
            JointState, 
            'kobra_mk5/front_right_wheel_contact_states', 
            self.fr_contact_surface_listener_callback, 
            qos_profile=qos_profile)

        self.rl_surface_sub = self.create_subscription(
            JointState, 
            'kobra_mk5/rear_left_wheel_contact_states', 
            self.rl_contact_surface_listener_callback, 
            qos_profile=qos_profile)

        self.rr_surface_sub = self.create_subscription(
            JointState, 
            'kobra_mk5/rear_right_wheel_contact_states', 
            self.rr_contact_surface_listener_callback, 
            qos_profile=qos_profile)

        self.contact_states = HtNavContactStates()

        self.fl_surface_sub  # prevent unused variable warning
        self.fr_surface_sub  # prevent unused variable warning
        self.rl_surface_sub  # prevent unused variable warning
        self.rr_surface_sub  # prevent unused variable warning
        
        # self.fl_contact_sub  # prevent unused variable warning
        # self.fr_contact_sub  # prevent unused variable warning
        # self.rl_contact_sub  # prevent unused variable warning
        # self.rr_contact_sub  # prevent unused variable warning

        self.fr_link_subscription  # prevent unused variable warning
        self.fl_link_subscription  # prevent unused variable warning
        self.rr_link_subscription  # prevent unused variable warning
        self.fl_link_subscription  # prevent unused variable warning
        self.imu_link_subscription  # prevent unused variable warning
        self.gps_link_sub  # prevent unused variable warning

        self.imu_link_meas_subscription  # prevent unused variable warning

        self.joint_state_subscription  # prevent unused variable warning
        # self.gps_ideal_subscription  # prevent unused variable warning
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

        self.imu_link_meas2 = HtNavStrapOut()
        self.imu_link_meas = HtNavStrapOut()
        self.imu_link_pva  = HtNavStrapOut()
        self.fl_wheel_pva  = HtNavStrapOut()
        self.fr_wheel_pva  = HtNavStrapOut()
        self.rl_wheel_pva  = HtNavStrapOut()
        self.rr_wheel_pva  = HtNavStrapOut()

        self.joint_state = HtNavJointState()
        self.joint_state.steering_angle.w1 = 0.0
        self.joint_state.steering_angle.w2 = 0.0
        self.joint_state.steering_angle.w3 = 0.0
        self.joint_state.steering_angle.w4 = 0.0

        self.joint_state.wheel_rotation.w1 = 0.0
        self.joint_state.wheel_rotation.w2 = 0.0
        self.joint_state.wheel_rotation.w3 = 0.0
        self.joint_state.wheel_rotation.w4 = 0.0

        self.gps_link_data = HtNavGpsData()
        self.gps_link_data.gps_pos.x = 0.0
        self.gps_link_data.gps_pos.y = 0.0
        self.gps_link_data.gps_pos.z = 0.0
        self.gps_link_data.gps_vel.x = 0.0
        self.gps_link_data.gps_vel.y = 0.0
        self.gps_link_data.gps_vel.z = 0.0

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

        self.gps_data_ideal = HtNavGpsData()
        self.gps_data_ideal.gps_pos.x = 0.0
        self.gps_data_ideal.gps_pos.y = 0.0
        self.gps_data_ideal.gps_pos.z = 0.0
        self.gps_data_ideal.gps_vel.x = 0.0
        self.gps_data_ideal.gps_vel.y = 0.0
        self.gps_data_ideal.gps_vel.z = 0.0

        self.imu_data_ideal = HtNavImuData()
        self.imu_data_ideal.vel_diff.x = 0.0
        self.imu_data_ideal.vel_diff.y = 0.0
        self.imu_data_ideal.vel_diff.z = 0.0
        self.imu_data_ideal.ang_diff.x = 0.0
        self.imu_data_ideal.ang_diff.y = 0.0
        self.imu_data_ideal.ang_diff.z = 0.0
    
        self.gazebo_time = 0.0
    

    def fl_contact_surface_listener_callback(self, msg):
        temp_time_sec = float(msg.header.stamp.sec)
        temp_time_nsec = float(msg.header.stamp.nanosec)
        self.gazebo_time = temp_time_sec*1e6 + temp_time_nsec*1e-3        
        
        wheel_contact_state = HtNavContactState()
        wheel_contact_state.time = self.gazebo_time

        wheel_contact_state.ideal_contact_forces.x = msg.position[0]
        wheel_contact_state.ideal_contact_forces.y = msg.position[1]
        wheel_contact_state.ideal_contact_forces.z = msg.position[2]
        
        wheel_contact_state.ideal_pacejka_forces.x = msg.effort[0]
        wheel_contact_state.ideal_pacejka_forces.y = msg.effort[1]
        wheel_contact_state.ideal_pacejka_forces.z = msg.position[2] # Pacejka inputs the normal force

        wheel_contact_state.ideal_slip.x = msg.velocity[1] # sigma_x
        wheel_contact_state.ideal_slip.y = msg.velocity[0] # alpha_x
        wheel_contact_state.ideal_slip.z = 0.0             # camber angle slip (gamma_x) is assummed to be zero

        # self.joint_state.normal_force.w1 = abs(wheel_contact_state.ideal_contact_forces.z)
        self.contact_states.fl_wheel_contact_states = wheel_contact_state
        
        print(str(wheel_contact_state.time), str(wheel_contact_state.ideal_contact_forces.x), str(wheel_contact_state.ideal_contact_forces.y), str(wheel_contact_state.ideal_contact_forces.z), \
                str(wheel_contact_state.ideal_slip.x), str(wheel_contact_state.ideal_slip.y), str(wheel_contact_state.ideal_slip.z), sep='\t', file=fl_contact_states_txt) 

    def fr_contact_surface_listener_callback(self, msg):
        temp_time_sec = float(msg.header.stamp.sec)
        temp_time_nsec = float(msg.header.stamp.nanosec)
        self.gazebo_time = temp_time_sec*1e6 + temp_time_nsec*1e-3        
        
        wheel_contact_state = HtNavContactState()
        wheel_contact_state.time = self.gazebo_time

        wheel_contact_state.ideal_contact_forces.x = msg.position[0]
        wheel_contact_state.ideal_contact_forces.y = msg.position[1]
        wheel_contact_state.ideal_contact_forces.z = msg.position[2]
        
        wheel_contact_state.ideal_pacejka_forces.x = msg.effort[0]
        wheel_contact_state.ideal_pacejka_forces.y = msg.effort[1]
        wheel_contact_state.ideal_pacejka_forces.z = msg.position[2] # Pacejka inputs the normal force

        wheel_contact_state.ideal_slip.x = msg.velocity[1] # sigma_x
        wheel_contact_state.ideal_slip.y = msg.velocity[0] # alpha_x
        wheel_contact_state.ideal_slip.z = 0.0             # camber angle slip (gamma_x) is assummed to be zero

        # self.joint_state.normal_force.w2 = abs(wheel_contact_state.ideal_contact_forces.z)
        self.contact_states.fr_wheel_contact_states = wheel_contact_state
        print(str(wheel_contact_state.time), str(wheel_contact_state.ideal_contact_forces.x), str(wheel_contact_state.ideal_contact_forces.y), str(wheel_contact_state.ideal_contact_forces.z), \
                str(wheel_contact_state.ideal_slip.x), str(wheel_contact_state.ideal_slip.y), str(wheel_contact_state.ideal_slip.z), sep='\t', file=fr_contact_states_txt) 

    def rl_contact_surface_listener_callback(self, msg):
        temp_time_sec = float(msg.header.stamp.sec)
        temp_time_nsec = float(msg.header.stamp.nanosec)
        self.gazebo_time = temp_time_sec*1e6 + temp_time_nsec*1e-3        
        
        wheel_contact_state = HtNavContactState()
        wheel_contact_state.time = self.gazebo_time

        wheel_contact_state.ideal_contact_forces.x = msg.position[0]
        wheel_contact_state.ideal_contact_forces.y = msg.position[1]
        wheel_contact_state.ideal_contact_forces.z = msg.position[2]
        
        wheel_contact_state.ideal_pacejka_forces.x = msg.effort[0]
        wheel_contact_state.ideal_pacejka_forces.y = msg.effort[1]
        wheel_contact_state.ideal_pacejka_forces.z = msg.position[2] # Pacejka inputs the normal force

        wheel_contact_state.ideal_slip.x = msg.velocity[1] # sigma_x
        wheel_contact_state.ideal_slip.y = msg.velocity[0] # alpha_x
        wheel_contact_state.ideal_slip.z = 0.0             # camber angle slip (gamma_x) is assummed to be zero

        # self.joint_state.normal_force.w3 = abs(wheel_contact_state.ideal_contact_forces.z)
        self.contact_states.rl_wheel_contact_states = wheel_contact_state
        print(str(wheel_contact_state.time), str(wheel_contact_state.ideal_contact_forces.x), str(wheel_contact_state.ideal_contact_forces.y), str(wheel_contact_state.ideal_contact_forces.z), \
                str(wheel_contact_state.ideal_slip.x), str(wheel_contact_state.ideal_slip.y), str(wheel_contact_state.ideal_slip.z), sep='\t', file=rl_contact_states_txt) 

    def rr_contact_surface_listener_callback(self, msg):
        temp_time_sec = float(msg.header.stamp.sec)
        temp_time_nsec = float(msg.header.stamp.nanosec)
        self.gazebo_time = temp_time_sec*1e6 + temp_time_nsec*1e-3        
        
        wheel_contact_state = HtNavContactState()
        wheel_contact_state.time = self.gazebo_time

        wheel_contact_state.ideal_contact_forces.x = msg.position[0]
        wheel_contact_state.ideal_contact_forces.y = msg.position[1]
        wheel_contact_state.ideal_contact_forces.z = msg.position[2]
        
        wheel_contact_state.ideal_pacejka_forces.x = msg.effort[0]
        wheel_contact_state.ideal_pacejka_forces.y = msg.effort[1]
        wheel_contact_state.ideal_pacejka_forces.z = msg.position[2] # Pacejka inputs the normal force

        wheel_contact_state.ideal_slip.x = msg.velocity[1] # sigma_x
        wheel_contact_state.ideal_slip.y = msg.velocity[0] # alpha_x
        wheel_contact_state.ideal_slip.z = 0.0             # camber angle slip (gamma_x) is assummed to be zero

        # self.joint_state.normal_force.w4 = abs(wheel_contact_state.ideal_contact_forces.z)
        self.contact_states.rr_wheel_contact_states = wheel_contact_state
        print(str(wheel_contact_state.time), str(wheel_contact_state.ideal_contact_forces.x), str(wheel_contact_state.ideal_contact_forces.y), str(wheel_contact_state.ideal_contact_forces.z), \
                str(wheel_contact_state.ideal_slip.x), str(wheel_contact_state.ideal_slip.y), str(wheel_contact_state.ideal_slip.z), sep='\t', file=rr_contact_states_txt) 

    def joint_listener_callback(self, msg):
        # self.get_logger().info('I heard joint namse as: "%f"' % msg.velocity[1])
        self.zaman_ref = self.get_clock().now().nanoseconds * 1e-6 #msec
        self.zaman_ref = self.zaman_ref - self.zaman_ilk

        temp_time_sec = float(msg.header.stamp.sec)
        temp_time_nsec = float(msg.header.stamp.nanosec)
        self.gazebo_time = temp_time_sec*1e6 + temp_time_nsec*1e-3
        
        self.joint_state.time = self.gazebo_time

        self.joint_state.steering_angle.w1 = msg.position[0]
        self.joint_state.steering_angle.w2 = msg.position[1]
        self.joint_state.steering_angle.w3 = 0.0 # msg.position[2]
        self.joint_state.steering_angle.w4 = 0.0 # msg.position[3]

        self.joint_state.wheel_rotation.w1 = msg.velocity[0]
        self.joint_state.wheel_rotation.w2 = msg.velocity[1]
        self.joint_state.wheel_rotation.w3 = msg.velocity[2]
        self.joint_state.wheel_rotation.w4 = msg.velocity[3]

        print(str(self.joint_state.time), str(self.joint_state.steering_angle.w1), str(self.joint_state.wheel_rotation.w1), str(self.joint_state.steering_angle.w2), str(self.joint_state.wheel_rotation.w2), str(self.joint_state.steering_angle.w3), str(self.joint_state.wheel_rotation.w3), str(self.joint_state.steering_angle.w4), str(self.joint_state.wheel_rotation.w4), str(msg.position[4]), str(msg.velocity[4]), sep='\t', file=joint_input_data_txt)
        
    def front_right_link_listener_callback(self, msg):
        # self.get_logger().info('I heard joint namse as: "%f"' % msg.velocity[1])
        self.zaman_ref = self.get_clock().now().nanoseconds * 1e-6 #msec
        self.zaman_ref = self.zaman_ref - self.zaman_ilk

        temp_time_sec = float(msg.header.stamp.sec)
        temp_time_nsec = float(msg.header.stamp.nanosec)
        self.gazebo_time = temp_time_sec*1e6 + temp_time_nsec*1e-3

        self.fr_wheel_pva.time = self.gazebo_time

        temp_pos = np.zeros((3, 1))
        temp_pos2 = np.zeros((3, 1))
        temp_pos[0] = msg.position[0]
        temp_pos[1] = msg.position[1]
        temp_pos[2] = msg.position[2]

        temp_pos2 = np.dot(self.CRef2NED , temp_pos)

        self.fr_wheel_pva.pos.x = float(temp_pos2[0])
        self.fr_wheel_pva.pos.y = float(temp_pos2[1])
        self.fr_wheel_pva.pos.z = float(temp_pos2[2])

        temp_vel = np.zeros((3, 1))
        temp_vel2 = np.zeros((3, 1))
        temp_vel[0] = msg.velocity[0]
        temp_vel[1] = msg.velocity[1]
        temp_vel[2] = msg.velocity[2]

        temp_vel2 = np.dot(self.CRef2NED , temp_vel)

        self.fr_wheel_pva.vel.x = float(temp_vel2[0])
        self.fr_wheel_pva.vel.y = float(temp_vel2[1])
        self.fr_wheel_pva.vel.z = float(temp_vel2[2])
        
        temp_euler = np.zeros((3, 1))
        temp_euler2 = np.zeros((3, 1))
        temp_euler[0] = msg.effort[0]
        temp_euler[1] = msg.effort[1]
        temp_euler[2] = msg.effort[2]

        temp_euler2 = np.dot(self.CENU2NED , temp_euler)

        self.fr_wheel_pva.euler.roll  = float(temp_euler2[0])
        self.fr_wheel_pva.euler.pitch = float(temp_euler2[1])
        self.fr_wheel_pva.euler.yaw   = float(temp_euler2[2])

        print(str(self.fr_wheel_pva.time), str(self.fr_wheel_pva.pos.x), str(self.fr_wheel_pva.pos.y), str(self.fr_wheel_pva.pos.z), str(self.fr_wheel_pva.vel.x), str(self.fr_wheel_pva.vel.y), str(self.fr_wheel_pva.vel.z), str(self.fr_wheel_pva.euler.roll), str(self.fr_wheel_pva.euler.pitch), str(self.fr_wheel_pva.euler.yaw), sep='\t', file=fr_out_data_txt)

    def front_left_link_listener_callback(self, msg):
        # self.get_logger().info('I heard joint namse as: "%f"' % msg.velocity[1])
        self.zaman_ref = self.get_clock().now().nanoseconds * 1e-6 #msec
        self.zaman_ref = self.zaman_ref - self.zaman_ilk
        
        temp_time_sec = float(msg.header.stamp.sec)
        temp_time_nsec = float(msg.header.stamp.nanosec)
        self.gazebo_time = temp_time_sec*1e6 + temp_time_nsec*1e-3

        self.fl_wheel_pva.time = self.gazebo_time

        temp_pos = np.zeros((3, 1))
        temp_pos2 = np.zeros((3, 1))
        temp_pos[0] = msg.position[0]
        temp_pos[1] = msg.position[1]
        temp_pos[2] = msg.position[2]

        temp_pos2 = np.dot(self.CRef2NED , temp_pos)

        self.fl_wheel_pva.pos.x = float(temp_pos2[0])
        self.fl_wheel_pva.pos.y = float(temp_pos2[1])
        self.fl_wheel_pva.pos.z = float(temp_pos2[2])

        temp_vel = np.zeros((3, 1))
        temp_vel2 = np.zeros((3, 1))
        temp_vel[0] = msg.velocity[0]
        temp_vel[1] = msg.velocity[1]
        temp_vel[2] = msg.velocity[2]

        temp_vel2 = np.dot(self.CRef2NED , temp_vel)

        self.fl_wheel_pva.vel.x = float(temp_vel2[0])
        self.fl_wheel_pva.vel.y = float(temp_vel2[1])
        self.fl_wheel_pva.vel.z = float(temp_vel2[2])
        
        temp_euler = np.zeros((3, 1))
        temp_euler2 = np.zeros((3, 1))
        temp_euler[0] = msg.effort[0]
        temp_euler[1] = msg.effort[1]
        temp_euler[2] = msg.effort[2]

        temp_euler2 = np.dot(self.CENU2NED , temp_euler)

        self.fl_wheel_pva.euler.roll  = float(temp_euler2[0])
        self.fl_wheel_pva.euler.pitch = float(temp_euler2[1])
        self.fl_wheel_pva.euler.yaw   = float(temp_euler2[2])
        
        print(str(self.fl_wheel_pva.time), str(self.fl_wheel_pva.pos.x), str(self.fl_wheel_pva.pos.y), str(self.fl_wheel_pva.pos.z), str(self.fl_wheel_pva.vel.x), str(self.fl_wheel_pva.vel.y), str(self.fl_wheel_pva.vel.z), str(self.fl_wheel_pva.euler.roll), str(self.fl_wheel_pva.euler.pitch), str(self.fl_wheel_pva.euler.yaw), sep='\t', file=fl_out_data_txt)

    def rear_right_link_listener_callback(self, msg):
        # self.get_logger().info('I heard joint namse as: "%f"' % msg.velocity[1])
        self.zaman_ref = self.get_clock().now().nanoseconds * 1e-6 #msec
        self.zaman_ref = self.zaman_ref - self.zaman_ilk
        
        temp_time_sec = float(msg.header.stamp.sec)
        temp_time_nsec = float(msg.header.stamp.nanosec)
        self.gazebo_time = temp_time_sec*1e6 + temp_time_nsec*1e-3

        self.rr_wheel_pva.time = self.gazebo_time

        temp_pos = np.zeros((3, 1))
        temp_pos2 = np.zeros((3, 1))
        temp_pos[0] = msg.position[0]
        temp_pos[1] = msg.position[1]
        temp_pos[2] = msg.position[2]

        temp_pos2 = np.dot(self.CRef2NED , temp_pos)

        self.rr_wheel_pva.pos.x = float(temp_pos2[0])
        self.rr_wheel_pva.pos.y = float(temp_pos2[1])
        self.rr_wheel_pva.pos.z = float(temp_pos2[2])

        temp_vel = np.zeros((3, 1))
        temp_vel2 = np.zeros((3, 1))
        temp_vel[0] = msg.velocity[0]
        temp_vel[1] = msg.velocity[1]
        temp_vel[2] = msg.velocity[2]

        temp_vel2 = np.dot(self.CRef2NED , temp_vel)

        self.rr_wheel_pva.vel.x = float(temp_vel2[0])
        self.rr_wheel_pva.vel.y = float(temp_vel2[1])
        self.rr_wheel_pva.vel.z = float(temp_vel2[2])
        
        temp_euler = np.zeros((3, 1))
        temp_euler2 = np.zeros((3, 1))
        temp_euler[0] = msg.effort[0]
        temp_euler[1] = msg.effort[1]
        temp_euler[2] = msg.effort[2]

        temp_euler2 = np.dot(self.CENU2NED , temp_euler)

        self.rr_wheel_pva.euler.roll  = float(temp_euler2[0])
        self.rr_wheel_pva.euler.pitch = float(temp_euler2[1])
        self.rr_wheel_pva.euler.yaw   = float(temp_euler2[2])        
        
        print(str(self.rr_wheel_pva.time), str(self.rr_wheel_pva.pos.x), str(self.rr_wheel_pva.pos.y), str(self.rr_wheel_pva.pos.z), str(self.rr_wheel_pva.vel.x), str(self.rr_wheel_pva.vel.y), str(self.rr_wheel_pva.vel.z), str(self.rr_wheel_pva.euler.roll), str(self.rr_wheel_pva.euler.pitch), str(self.rr_wheel_pva.euler.yaw), sep='\t', file=rr_out_data_txt)

    def rear_left_link_listener_callback(self, msg):
        # self.get_logger().info('I heard joint namse as: "%f"' % msg.velocity[1])
        self.zaman_ref = self.get_clock().now().nanoseconds * 1e-6 #msec
        self.zaman_ref = self.zaman_ref - self.zaman_ilk

        temp_time_sec = float(msg.header.stamp.sec)
        temp_time_nsec = float(msg.header.stamp.nanosec)
        self.gazebo_time = temp_time_sec*1e6 + temp_time_nsec*1e-3

        self.rl_wheel_pva.time = self.gazebo_time

        temp_pos = np.zeros((3, 1))
        temp_pos2 = np.zeros((3, 1))
        temp_pos[0] = msg.position[0]
        temp_pos[1] = msg.position[1]
        temp_pos[2] = msg.position[2]

        temp_pos2 = np.dot(self.CRef2NED , temp_pos)

        self.rl_wheel_pva.pos.x = float(temp_pos2[0])
        self.rl_wheel_pva.pos.y = float(temp_pos2[1])
        self.rl_wheel_pva.pos.z = float(temp_pos2[2])

        temp_vel = np.zeros((3, 1))
        temp_vel2 = np.zeros((3, 1))
        temp_vel[0] = msg.velocity[0]
        temp_vel[1] = msg.velocity[1]
        temp_vel[2] = msg.velocity[2]

        temp_vel2 = np.dot(self.CRef2NED , temp_vel)

        self.rl_wheel_pva.vel.x = float(temp_vel2[0])
        self.rl_wheel_pva.vel.y = float(temp_vel2[1])
        self.rl_wheel_pva.vel.z = float(temp_vel2[2])
        
        temp_euler = np.zeros((3, 1))
        temp_euler2 = np.zeros((3, 1))
        temp_euler[0] = msg.effort[0]
        temp_euler[1] = msg.effort[1]
        temp_euler[2] = msg.effort[2]

        temp_euler2 = np.dot(self.CENU2NED , temp_euler)

        self.rl_wheel_pva.euler.roll  = float(temp_euler2[0])
        self.rl_wheel_pva.euler.pitch = float(temp_euler2[1])
        self.rl_wheel_pva.euler.yaw   = float(temp_euler2[2])

        print(str(self.rl_wheel_pva.time), str(self.rl_wheel_pva.pos.x), str(self.rl_wheel_pva.pos.y), str(self.rl_wheel_pva.pos.z), str(self.rl_wheel_pva.vel.x), str(self.rl_wheel_pva.vel.y), str(self.rl_wheel_pva.vel.z), str(self.rl_wheel_pva.euler.roll), str(self.rl_wheel_pva.euler.pitch), str(self.rl_wheel_pva.euler.yaw), sep='\t', file=rl_out_data_txt)

    def imu_link_listener_callback(self, msg):
        # self.get_logger().info('I heard joint namse as: "%f"' % msg.velocity[1])
        self.zaman_ref = self.get_clock().now().nanoseconds * 1e-6 #msec
        self.zaman_ref = self.zaman_ref - self.zaman_ilk
        
        temp_time_sec = float(msg.header.stamp.sec)
        temp_time_nsec = float(msg.header.stamp.nanosec)
        self.gazebo_time = temp_time_sec*1e6 + temp_time_nsec*1e-3

        self.imu_link_pva.time = self.gazebo_time

        temp_pos = np.zeros((3, 1))
        temp_pos2 = np.zeros((3, 1))
        temp_pos[0] = msg.position[0]
        temp_pos[1] = msg.position[1]
        temp_pos[2] = msg.position[2]

        temp_pos2 = np.dot(self.CRef2NED , temp_pos)

        self.imu_link_pva.pos.x = float(temp_pos2[0])
        self.imu_link_pva.pos.y = float(temp_pos2[1])
        self.imu_link_pva.pos.z = float(temp_pos2[2])

        temp_vel = np.zeros((3, 1))
        temp_vel2 = np.zeros((3, 1))
        temp_vel[0] = msg.velocity[0]
        temp_vel[1] = msg.velocity[1]
        temp_vel[2] = msg.velocity[2]

        temp_vel2 = np.dot(self.CRef2NED , temp_vel)

        self.imu_link_pva.vel.x = float(temp_vel2[0])
        self.imu_link_pva.vel.y = float(temp_vel2[1])
        self.imu_link_pva.vel.z = float(temp_vel2[2])
        
        temp_euler = np.zeros((3, 1))
        temp_euler2 = np.zeros((3, 1))
        temp_euler[0] = msg.effort[0]
        temp_euler[1] = msg.effort[1]
        temp_euler[2] = msg.effort[2]

        temp_euler2 = np.dot(self.CENU2NED , temp_euler)

        self.imu_link_pva.euler.roll  = float(temp_euler2[0])
        self.imu_link_pva.euler.pitch = float(temp_euler2[1])
        self.imu_link_pva.euler.yaw   = float(temp_euler2[2])        
        
        print(str(self.imu_link_pva.time), str(self.imu_link_pva.pos.x), str(self.imu_link_pva.pos.y), str(self.imu_link_pva.pos.z), str(self.imu_link_pva.vel.x), str(self.imu_link_pva.vel.y), str(self.imu_link_pva.vel.z), str(self.imu_link_pva.euler.roll), str(self.imu_link_pva.euler.pitch), str(self.imu_link_pva.euler.yaw), sep='\t', file=imu_out_data_txt)

    def imu_link_meas_listener_callback(self, msg):
        # self.get_logger().info('I heard joint namse as: "%f"' % msg.velocity[1])
        self.zaman_ref = self.get_clock().now().nanoseconds * 1e-6 #msec
        self.zaman_ref = self.zaman_ref - self.zaman_ilk
        
        temp_time_sec = float(msg.header.stamp.sec)
        temp_time_nsec = float(msg.header.stamp.nanosec)
        self.gazebo_time = temp_time_sec*1e6 + temp_time_nsec*1e-3

        self.imu_link_meas.time = self.gazebo_time

        #   pos   : ang_vel  = link->WorldAngularVel();
        #   vel   : lin_acc  = link->WorldLinearAccel ();
        #   euler : ang_acc  = link->WorldAngularAccel();

        self.imu_link_meas.pos.x = -float(msg.position[1])
        self.imu_link_meas.pos.y = -float(msg.position[0])
        self.imu_link_meas.pos.z = -float(msg.position[2])

        self.imu_link_meas.vel.x = -float(msg.velocity[1])
        self.imu_link_meas.vel.y = -float(msg.velocity[0])
        self.imu_link_meas.vel.z = -float(msg.velocity[2])
    
        self.imu_link_meas.euler.roll  = -float(msg.effort[1])
        self.imu_link_meas.euler.pitch = -float(msg.effort[0])
        self.imu_link_meas.euler.yaw   = -float(msg.effort[2])        
        
        print(str(self.imu_link_meas.time), str(self.imu_link_meas.pos.x), str(self.imu_link_meas.pos.y), str(self.imu_link_meas.pos.z), str(self.imu_link_meas.vel.x), str(self.imu_link_meas.vel.y), str(self.imu_link_meas.vel.z), str(self.imu_link_meas.euler.roll), str(self.imu_link_meas.euler.pitch), str(self.imu_link_meas.euler.yaw), sep='\t', file=imu_link_data_txt)


    def imu_link_meas_listener_callback2(self, msg):
        # self.get_logger().info('I heard joint namse as: "%f"' % msg.velocity[1])
        self.zaman_ref = self.get_clock().now().nanoseconds * 1e-6 #msec
        self.zaman_ref = self.zaman_ref - self.zaman_ilk
        
        temp_time_sec = float(msg.header.stamp.sec)
        temp_time_nsec = float(msg.header.stamp.nanosec)
        self.gazebo_time = temp_time_sec*1e6 + temp_time_nsec*1e-3

        self.imu_link_meas2.time = self.gazebo_time

        #   pos   : ang_vel  = link->WorldAngularVel();
        #   vel   : lin_acc  = link->WorldLinearAccel ();
        #   euler : ang_acc  = link->WorldAngularAccel();

        self.imu_link_meas2.pos.x = float(msg.position[0])
        self.imu_link_meas2.pos.y = float(msg.position[1])
        self.imu_link_meas2.pos.z = float(msg.position[2])

        self.imu_link_meas2.vel.x = float(msg.velocity[0])
        self.imu_link_meas2.vel.y = float(msg.velocity[1])
        self.imu_link_meas2.vel.z = float(msg.velocity[2])
    
        self.imu_link_meas2.euler.roll  = float(msg.effort[0])
        self.imu_link_meas2.euler.pitch = float(msg.effort[1])
        self.imu_link_meas2.euler.yaw   = float(msg.effort[2])        
        
        print(str(self.imu_link_meas2.time), str(self.imu_link_meas2.pos.x), str(self.imu_link_meas2.pos.y), str(self.imu_link_meas2.pos.z), str(self.imu_link_meas2.vel.x), str(self.imu_link_meas2.vel.y), str(self.imu_link_meas2.vel.z), str(self.imu_link_meas2.euler.roll), str(self.imu_link_meas2.euler.pitch), str(self.imu_link_meas2.euler.yaw), sep='\t', file=imu_link_data2_txt)

    def sub_cb_imu_data(self, msg):
        temp_time_sec = float(msg.header.stamp.sec)
        temp_time_nsec = float(msg.header.stamp.nanosec)
        self.gazebo_time = temp_time_sec*1e6 + temp_time_nsec*1e-3

        self.imu_data.time = self.gazebo_time
        
        self.imu_data.vel_diff.x = -msg.linear_acceleration.y 
        self.imu_data.vel_diff.y = -msg.linear_acceleration.x 
        self.imu_data.vel_diff.z = -msg.linear_acceleration.z  

        self.imu_data.ang_diff.x = -msg.angular_velocity.y 
        self.imu_data.ang_diff.y = -msg.angular_velocity.x 
        self.imu_data.ang_diff.z = -msg.angular_velocity.z 
        
        self.zaman_ref = self.get_clock().now().nanoseconds * 1e-6 #msec
        self.zaman_ref = self.zaman_ref - self.zaman_ilk

        print(str(self.imu_data.time), str(self.imu_data.ang_diff.x), str(self.imu_data.ang_diff.y), str(self.imu_data.ang_diff.z), str(self.imu_data.vel_diff.x), str(self.imu_data.vel_diff.y), str(self.imu_data.vel_diff.z), sep='\t', file=imu_data_txt)


    def gps_link_cb(self, msg):       
        temp_time_sec = float(msg.header.stamp.sec)
        temp_time_nsec = float(msg.header.stamp.nanosec)
        self.gazebo_time = temp_time_sec*1e6 + temp_time_nsec*1e-3

        self.gps_link_data.time = self.gazebo_time

        self.gps_link_data.gps_pos.x = float(msg.position[0])
        self.gps_link_data.gps_pos.y = float(msg.position[1])
        self.gps_link_data.gps_pos.z = float(msg.position[2])

        self.gps_link_data.gps_vel.x = float(msg.velocity[0])
        self.gps_link_data.gps_vel.y = float(msg.velocity[1])
        self.gps_link_data.gps_vel.z = float(msg.velocity[2])

        self.zaman_ref = self.get_clock().now().nanoseconds * 1e-6 #msec
        self.zaman_ref = self.zaman_ref - self.zaman_ilk

        print(str(self.gps_link_data.time), str(self.gps_link_data.gps_pos.x), str(self.gps_link_data.gps_pos.y), str(self.gps_link_data.gps_pos.z), str(self.gps_link_data.gps_vel.x), str(self.gps_link_data.gps_vel.y), str(self.gps_link_data.gps_vel.z), sep='\t', file=gps_link_data_txt)


    def sub_cb_gps_data(self, msg):       
        temp_time_sec = float(msg.header.stamp.sec)
        temp_time_nsec = float(msg.header.stamp.nanosec)
        self.gazebo_time = temp_time_sec*1e6 + temp_time_nsec*1e-3

        self.gps_data.time = self.gazebo_time

        self.gps_data.gps_pos.x = msg.latitude * DEG2RAD
        self.gps_data.gps_pos.y = msg.longitude * DEG2RAD
        self.gps_data.gps_pos.z = msg.altitude

        self.gps_data.gps_vel.x = 0.0
        self.gps_data.gps_vel.y = 0.0
        self.gps_data.gps_vel.z = 0.0

        self.zaman_ref = self.get_clock().now().nanoseconds * 1e-6 #msec
        self.zaman_ref = self.zaman_ref - self.zaman_ilk

        print(str(self.gps_data.time), str(self.gps_data.gps_pos.x), str(self.gps_data.gps_pos.y), str(self.gps_data.gps_pos.z), str(self.gps_data.gps_vel.x), str(self.gps_data.gps_vel.y), str(self.gps_data.gps_vel.z), sep='\t', file=gps_data_txt)

    def ideal_gps_sub_cb(self, msg):   

        temp_time_sec = float(msg.header.stamp.sec)
        temp_time_nsec = float(msg.header.stamp.nanosec)
        self.gazebo_time = temp_time_sec*1e6 + temp_time_nsec*1e-3

        self.gps_data_ideal.time = self.gazebo_time

        self.gps_data_ideal.gps_pos.x = msg.latitude * DEG2RAD
        self.gps_data_ideal.gps_pos.y = msg.longitude * DEG2RAD
        self.gps_data_ideal.gps_pos.z = msg.altitude

        self.gps_data_ideal.gps_vel.x = 0.0
        self.gps_data_ideal.gps_vel.y = 0.0
        self.gps_data_ideal.gps_vel.z = 0.0

        self.zaman_ref = self.get_clock().now().nanoseconds * 1e-6 #msec
        self.zaman_ref = self.zaman_ref - self.zaman_ilk
        print(str(self.gps_data_ideal.time), str(self.gps_data_ideal.gps_pos.x), str(self.gps_data_ideal.gps_pos.y), str(self.gps_data_ideal.gps_pos.z), str(self.gps_data_ideal.gps_vel.x), str(self.gps_data_ideal.gps_vel.y), str(self.gps_data_ideal.gps_vel.z), sep='\t', file=gps_data_ideal_txt)

    def sub_cb_imu_data_ideal(self, msg):
        temp_time_sec = float(msg.header.stamp.sec)
        temp_time_nsec = float(msg.header.stamp.nanosec)
        self.gazebo_time = temp_time_sec*1e6 + temp_time_nsec*1e-3

        self.imu_data_ideal.time = self.gazebo_time
        
        self.imu_data_ideal.vel_diff.x = -msg.linear_acceleration.y 
        self.imu_data_ideal.vel_diff.y = -msg.linear_acceleration.x 
        self.imu_data_ideal.vel_diff.z = -msg.linear_acceleration.z  

        self.imu_data_ideal.ang_diff.x = -msg.angular_velocity.y 
        self.imu_data_ideal.ang_diff.y = -msg.angular_velocity.x 
        self.imu_data_ideal.ang_diff.z = -msg.angular_velocity.z 
        
        self.zaman_ref = self.get_clock().now().nanoseconds * 1e-6 #msec
        self.zaman_ref = self.zaman_ref - self.zaman_ilk

        print(str(self.imu_data_ideal.time), str(self.imu_data_ideal.ang_diff.x), str(self.imu_data_ideal.ang_diff.y), str(self.imu_data_ideal.ang_diff.z), str(self.imu_data_ideal.vel_diff.x), str(self.imu_data_ideal.vel_diff.y), str(self.imu_data_ideal.vel_diff.z), sep='\t', file=imu_data_ideal_txt)


    def fl_contact_cb(self, msg):
        temp_time_sec = float(msg.header.stamp.sec)
        temp_time_nsec = float(msg.header.stamp.nanosec)
        self.gazebo_time = temp_time_sec*1e6 + temp_time_nsec*1e-3

        # self.get_logger().info('I heard fl contact force x as: 1')
        # self.get_logger().info('I heard fl contact size as: "%f"' % len(msg.states))

        # self.get_logger().info('I heard fl contact info as: "%s"' % msg.states[0].info)

        # self.get_logger().info('I heard fl contact pos size: "%f"' % len(msg.states[0].contact_positions))

        # self.get_logger().info('I heard fl contact pos x: "%f"' % msg.states[0].contact_positions[0].x)

        # self.get_logger().info('I heard fl contact force 1 x as: "%f"' % msg.states[0].wrenches[0].force.x)
        # self.get_logger().info('I heard fl contact force 2 x as: "%f"' % msg.states[1].wrenches[0].force.x)

        ix = 0
        while ix < len(msg.states):
            print(str(self.imu_data_ideal.time), str(ix+1), str(msg.states[ix].contact_positions[0].x), str(msg.states[ix].contact_positions[0].y), str(msg.states[ix].contact_positions[0].z), \
                str(msg.states[ix].wrenches[0].force.x), str(msg.states[ix].wrenches[0].force.y), str(msg.states[ix].wrenches[0].force.z), sep='\t', file=fl_contact_states_txt) 
            ix = ix + 1


    def fr_contact_cb(self, msg):
        temp_time_sec = float(msg.header.stamp.sec)
        temp_time_nsec = float(msg.header.stamp.nanosec)
        self.gazebo_time = temp_time_sec*1e6 + temp_time_nsec*1e-3

        ix = 0
        while ix < len(msg.states):
            print(str(self.imu_data_ideal.time), str(ix+1), str(msg.states[ix].contact_positions[0].x), str(msg.states[ix].contact_positions[0].y), str(msg.states[ix].contact_positions[0].z), \
                str(msg.states[ix].wrenches[0].force.x), str(msg.states[ix].wrenches[0].force.y), str(msg.states[ix].wrenches[0].force.z), sep='\t', file=fr_contact_states_txt) 
            ix = ix + 1

    def rl_contact_cb(self, msg):
        temp_time_sec = float(msg.header.stamp.sec)
        temp_time_nsec = float(msg.header.stamp.nanosec)
        self.gazebo_time = temp_time_sec*1e6 + temp_time_nsec*1e-3

        ix = 0
        while ix < len(msg.states):
            print(str(self.imu_data_ideal.time), str(ix+1), str(msg.states[ix].contact_positions[0].x), str(msg.states[ix].contact_positions[0].y), str(msg.states[ix].contact_positions[0].z), \
                str(msg.states[ix].wrenches[0].force.x), str(msg.states[ix].wrenches[0].force.y), str(msg.states[ix].wrenches[0].force.z), sep='\t', file=rl_contact_states_txt) 
            ix = ix + 1

    def rr_contact_cb(self, msg):
        temp_time_sec = float(msg.header.stamp.sec)
        temp_time_nsec = float(msg.header.stamp.nanosec)
        self.gazebo_time = temp_time_sec*1e6 + temp_time_nsec*1e-3

        ix = 0
        while ix < len(msg.states):
            print(str(self.imu_data_ideal.time), str(ix+1), str(msg.states[ix].contact_positions[0].x), str(msg.states[ix].contact_positions[0].y), str(msg.states[ix].contact_positions[0].z), \
                str(msg.states[ix].wrenches[0].force.x), str(msg.states[ix].wrenches[0].force.y), str(msg.states[ix].wrenches[0].force.z), sep='\t', file=rr_contact_states_txt) 
            ix = ix + 1

def main(args=None):
    rclpy.init(args=args)

    custom_qos_profile = qos_profile_sensor_data

    minimal_subscriber = DataCollector(custom_qos_profile)

    rclpy.spin(minimal_subscriber)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    minimal_subscriber.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
