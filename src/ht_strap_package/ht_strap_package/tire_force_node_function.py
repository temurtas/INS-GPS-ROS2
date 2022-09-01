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
import math

from sensor_msgs.msg import Imu
from sensor_msgs.msg import JointState
#from ht_nav_variables.msg import HtNavDeneme
from ht_nav_variables.msg import HtNavTireOut
from ht_nav_variables.msg import HtNavVehicleDebug
from ht_nav_variables.msg import HtNavImuData
from ht_nav_variables.msg import HtNavJointState
from ht_nav_variables.msg import HtNavStrapOut
from ht_nav_variables.msg import HtNavContactState
from ht_nav_variables.msg import HtNavContactStates
from ht_strap_package.config import base_path
from ht_strap_package.config import delta_t

from ht_strap_package.tire_force_calc import *

#base_path = Path("/home/temur/INS-GPS-ws/INS-GPS-Matlab/veriler/veri1_to_Dogukan/")           #Ubuntu Path

# out_data_path = base_path / "strap_data_tire_input.txt"
# strap_input_data_txt = open(out_data_path, 'w')

out_data_path = base_path / "joint_states_tire_input.txt"
joint_input_data_txt = open(out_data_path, 'w')

tire_out_data_path = base_path / "tire_variables_gazebo.txt"
tire_out_data_txt = open(tire_out_data_path, 'w')

class TireForceCalculator(Node):

    def __init__(self,qos_profile):
        super().__init__('tire_force_calc_node')

       # Initialise publishers
        self.tire_pub = self.create_publisher(HtNavTireOut, 'ht_nav_tire_data', qos_profile=qos_profile)
        
        self.fl_pva_pub = self.create_publisher(JointState, 'front_left_calc_link_states', qos_profile=qos_profile)
        self.fr_pva_pub = self.create_publisher(JointState, 'front_right_calc_link_states', qos_profile=qos_profile)
        self.rl_pva_pub = self.create_publisher(JointState, 'rear_left_calc_link_states', qos_profile=qos_profile)
        self.rr_pva_pub = self.create_publisher(JointState, 'rear_right_calc_link_states', qos_profile=qos_profile)

        # Initialise subscribers
        # self.imu_sub = self.create_subscription(
        #     Imu, 
        #     'kobra_mk5/imu_data', 
        #     self.imu_data_sub_cb, 
        #     qos_profile=qos_profile)

        self.imu_sub = self.create_subscription(
            Imu, 
            'kobra_mk5/imu_data_body', 
            self.imu_data_sub_cb, 
            qos_profile=qos_profile)

        self.strap_sub = self.create_subscription(
            HtNavStrapOut,
            'ht_nav_strap_data',
            self.strap_listener_callback,
            qos_profile=qos_profile)

        self.joint_sub = self.create_subscription(
            JointState, 
            'kobra_mk5/joint_states', 
            self.joint_listener_callback, 
            qos_profile=qos_profile)
        
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


        self.fl_surface_sub  # prevent unused variable warning
        self.fr_surface_sub  # prevent unused variable warning
        self.rl_surface_sub  # prevent unused variable warning
        self.rr_surface_sub  # prevent unused variable warning

        # Iniitalize variables
        self.tire_pub  # prevent unused variable warning
        self.fl_pva_pub  # prevent unused variable warning
        self.fr_pva_pub  # prevent unused variable warning
        self.rl_pva_pub  # prevent unused variable warning
        self.rr_pva_pub  # prevent unused variable warning
        self.imu_sub  # prevent unused variable warning
        self.strap_sub  # prevent unused variable warning
        self.joint_sub  # prevent unused variable warning
        self.zaman_ref = 0.0
        self.zaman_ilk = self.get_clock().now().nanoseconds * 1e-6 #msec

        self.imu_data = HtNavImuData()
        self.imu_data.vel_diff.x = 0.0  
        self.imu_data.vel_diff.y = 0.0 
        self.imu_data.vel_diff.z = 0.0 
        self.imu_data.ang_diff.x = 0.0 
        self.imu_data.ang_diff.y = 0.0 
        self.imu_data.ang_diff.z = 0.0 

        self.strap_data = HtNavStrapOut()
        self.strap_data.pos.x = 0.0 
        self.strap_data.pos.y = 0.0 
        self.strap_data.pos.z = 0.0 
        self.strap_data.vel.x = 0.0
        self.strap_data.vel.y = 0.0
        self.strap_data.vel.z = 0.0
        self.strap_data.euler.roll =  0.0 
        self.strap_data.euler.pitch = 0.0 
        self.strap_data.euler.yaw =   0.0
        self.strap_data.quaternion.x = 1.0
        self.strap_data.quaternion.y = 0.0
        self.strap_data.quaternion.z = 0.0
        self.strap_data.quaternion.w = 0.0

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

        self.tire_out = HtNavTireOut()
        self.tire_out.effective_radius_est = 0.0
        self.tire_out.vehicle_mass_est = 0.0
        self.tire_out.wheel_side_slip_ang.w1 = 0.0
        self.tire_out.wheel_side_slip_ang.w2 = 0.0
        self.tire_out.wheel_side_slip_ang.w3 = 0.0
        self.tire_out.wheel_side_slip_ang.w4 = 0.0
        self.tire_out.wheel_longitudinal_slip_ratio.w1 = 0.0
        self.tire_out.wheel_longitudinal_slip_ratio.w2 = 0.0
        self.tire_out.wheel_longitudinal_slip_ratio.w3 = 0.0
        self.tire_out.wheel_longitudinal_slip_ratio.w4 = 0.0
        self.tire_out.tire_lateral_forces.w1 = 0.0
        self.tire_out.tire_lateral_forces.w2 = 0.0
        self.tire_out.tire_lateral_forces.w3 = 0.0
        self.tire_out.tire_lateral_forces.w4 = 0.0
        self.tire_out.tire_longitudinal_forces.w1 = 0.0
        self.tire_out.tire_longitudinal_forces.w2 = 0.0
        self.tire_out.tire_longitudinal_forces.w3 = 0.0
        self.tire_out.tire_longitudinal_forces.w4 = 0.0

        self.contact_states = HtNavContactStates()

        self.gazebo_time = 0.0

        
    def imu_data_sub_cb(self, msg):      
        self.imu_data.vel_diff.x = -msg.linear_acceleration.y * delta_t 
        self.imu_data.vel_diff.y = -msg.linear_acceleration.x * delta_t
        self.imu_data.vel_diff.z = -msg.linear_acceleration.z * delta_t

        self.imu_data.ang_diff.x = -msg.angular_velocity.y * delta_t
        self.imu_data.ang_diff.y = -msg.angular_velocity.x * delta_t
        self.imu_data.ang_diff.z = -msg.angular_velocity.z * delta_t

    def strap_listener_callback(self, msg):
        #self.get_logger().info('I heard x pos as: "%f"' % msg.pos.x)
        self.zaman_ref = self.get_clock().now().nanoseconds * 1e-6 #msec
        self.zaman_ref = self.zaman_ref - self.zaman_ilk

        self.strap_data.time = msg.time
        self.strap_data.pos = msg.pos
        self.strap_data.vel = msg.vel
        self.strap_data.euler = msg.euler
        self.strap_data.quaternion = msg.quaternion

        # self.get_logger().info('I heard x pos as: "%f"' % self.strap_data.pos.x)

        # print(str(self.zaman_ref), str(msg.pos.x), str(msg.pos.y), str(msg.pos.z), str(msg.vel.x), str(msg.vel.y), str(msg.vel.z), str(msg.euler.roll), str(msg.euler.pitch), str(msg.euler.yaw), sep='\t', file=strap_input_data_txt)


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

        self.joint_state.normal_force.w1 = abs(wheel_contact_state.ideal_contact_forces.z)
        self.contact_states.fl_wheel_contact_states = wheel_contact_state

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

        self.joint_state.normal_force.w2 = abs(wheel_contact_state.ideal_contact_forces.z)
        self.contact_states.fr_wheel_contact_states = wheel_contact_state

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

        self.joint_state.normal_force.w3 = abs(wheel_contact_state.ideal_contact_forces.z)
        self.contact_states.rl_wheel_contact_states = wheel_contact_state

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

        self.joint_state.normal_force.w4 = abs(wheel_contact_state.ideal_contact_forces.z)
        self.contact_states.rr_wheel_contact_states = wheel_contact_state


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

        print(str(self.gazebo_time), str(msg.position[0]), str(msg.velocity[0]), str(msg.position[1]), str(msg.velocity[1]), str(msg.position[2]), str(msg.velocity[2]), str(msg.position[3]), str(msg.velocity[3]), str(msg.position[4]), str(msg.velocity[4]), sep='\t', file=joint_input_data_txt)

        msg_pb = HtNavVehicleDebug()

        # self.get_logger().info('I sent x vel as: "%f"' % self.strap_data.vel.x)

        self.tire_debug = tire_force_calc(self.strap_data, self.imu_data, self.joint_state)
        msg_pb = self.tire_debug
        msg_pb.time = self.gazebo_time

        # msg_pb = HtNavVehicleDebug()
        # self.tire_debug.wheel_variables = tire_force_calc_old(self.strap_data, self.imu_data, self.joint_state)
        # msg_pb = self.tire_debug
        
        # msg_pb = HtNavTireOut()
        # self.tire_out = tire_force_calc_old(self.strap_data, self.imu_data, self.joint_state)
        # msg_pb = self.tire_out       

        self.pub_func(msg_pb)

    def pub_func(self,msg):
        # HtNavTireOut  wheel_variables
        # HtNavStrapOut imu_link_pva
        # HtNavStrapOut fl_wheel_pva
        # HtNavStrapOut fr_wheel_pva
        # HtNavStrapOut rl_wheel_pva
        # HtNavStrapOut rr_wheel_pva
        
        msg_tire_out = msg.wheel_variables
        # msg_tire_out = HtNavTireOut()
        # msg_tire_out = msg
        self.tire_pub.publish(msg_tire_out)

        msg_fl = JointState()
        msg_fr = JointState()
        msg_rl = JointState()
        msg_rr = JointState()
        
        # Publish Calculated Front-Left Wheel Link States
        msg_fl.position = [msg.fl_wheel_pva.pos.x, msg.fl_wheel_pva.pos.y, msg.fl_wheel_pva.pos.z]
        msg_fl.velocity = [msg.fl_wheel_pva.vel.x, msg.fl_wheel_pva.vel.y, msg.fl_wheel_pva.vel.z]
        msg_fl.effort = [msg.fl_wheel_pva.euler.roll, msg.fl_wheel_pva.euler.pitch, msg.fl_wheel_pva.euler.yaw]
                
        self.fl_pva_pub.publish(msg_fl)

        # Publish Calculated Front-Right Wheel Link States
        msg_fr.position = [msg.fr_wheel_pva.pos.x, msg.fr_wheel_pva.pos.y, msg.fr_wheel_pva.pos.z]
        msg_fr.velocity = [msg.fr_wheel_pva.vel.x, msg.fr_wheel_pva.vel.y, msg.fr_wheel_pva.vel.z]
        msg_fr.effort = [msg.fr_wheel_pva.euler.roll, msg.fr_wheel_pva.euler.pitch, msg.fr_wheel_pva.euler.yaw]
                
        self.fr_pva_pub.publish(msg_fr)

        # Publish Calculated Rear-Left Wheel Link States
        msg_rl.position = [msg.rl_wheel_pva.pos.x, msg.rl_wheel_pva.pos.y, msg.rl_wheel_pva.pos.z]
        msg_rl.velocity = [msg.rl_wheel_pva.vel.x, msg.rl_wheel_pva.vel.y, msg.rl_wheel_pva.vel.z]
        msg_rl.effort = [msg.rl_wheel_pva.euler.roll, msg.rl_wheel_pva.euler.pitch, msg.rl_wheel_pva.euler.yaw]

        self.rl_pva_pub.publish(msg_rl)

        # Publish Calculated Rear-Right Wheel Link States
        msg_rr.position = [msg.rr_wheel_pva.pos.x, msg.rr_wheel_pva.pos.y, msg.rr_wheel_pva.pos.z]
        msg_rr.velocity = [msg.rr_wheel_pva.vel.x, msg.rr_wheel_pva.vel.y, msg.rr_wheel_pva.vel.z]
        msg_rr.effort = [msg.rr_wheel_pva.euler.roll, msg.rr_wheel_pva.euler.pitch, msg.rr_wheel_pva.euler.yaw]
        
        self.rr_pva_pub.publish(msg_rr)

        #self.get_logger().info('I publish x vel_diff as: "%f"' % msg.vel_diff.x)
        self.zaman_ref = self.get_clock().now().nanoseconds * 1e-6 #msec
        self.zaman_ref = self.zaman_ref - self.zaman_ilk
        
        print(str(msg.time), str(msg_tire_out.wheel_side_slip_ang.w1), str(msg_tire_out.wheel_side_slip_ang.w2) , str(msg_tire_out.wheel_side_slip_ang.w3), str(msg_tire_out.wheel_side_slip_ang.w4), str(msg_tire_out.wheel_longitudinal_slip_ratio.w1), str(msg_tire_out.wheel_longitudinal_slip_ratio.w2) , str(msg_tire_out.wheel_longitudinal_slip_ratio.w3), str(msg_tire_out.wheel_longitudinal_slip_ratio.w4) , \
            str(msg_tire_out.tire_lateral_forces.w1), str(msg_tire_out.tire_lateral_forces.w2) , str(msg_tire_out.tire_lateral_forces.w3), str(msg_tire_out.tire_lateral_forces.w4), str(msg_tire_out.tire_longitudinal_forces.w1), str(msg_tire_out.tire_longitudinal_forces.w2) , str(msg_tire_out.tire_longitudinal_forces.w3), str(msg_tire_out.tire_longitudinal_forces.w4) , sep='\t', file=tire_out_data_txt)



def main(args=None):
    rclpy.init(args=args)

    custom_qos_profile = qos_profile_sensor_data

    pseudo_controller = TireForceCalculator(custom_qos_profile)

    rclpy.spin(pseudo_controller)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    pseudo_controller.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
