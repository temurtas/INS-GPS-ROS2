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

from sensor_msgs.msg import Imu
from sensor_msgs.msg import JointState
#from ht_nav_variables.msg import HtNavDeneme
from ht_nav_variables.msg import HtNavTireOut
from ht_nav_variables.msg import HtNavImuData
from ht_nav_variables.msg import HtNavJointState
from ht_nav_variables.msg import HtNavStrapOut
from ht_strap_package.config import base_path
from ht_strap_package.config import delta_t

from ht_strap_package.tire_force_calc import tire_force_calc

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
        # Initialise subscribers
        self.imu_sub = self.create_subscription(
            Imu, 
            'kobra_mk5/imu_data', 
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
        
        # Iniitalize variables
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
        
        self.strap_data.pos = msg.pos
        self.strap_data.vel = msg.vel
        self.strap_data.euler = msg.euler
        self.strap_data.quaternion = msg.quaternion

        # print(str(self.zaman_ref), str(msg.pos.x), str(msg.pos.y), str(msg.pos.z), str(msg.vel.x), str(msg.vel.y), str(msg.vel.z), str(msg.euler.roll), str(msg.euler.pitch), str(msg.euler.yaw), sep='\t', file=strap_input_data_txt)


    def joint_listener_callback(self, msg):
        # self.get_logger().info('I heard joint namse as: "%f"' % msg.velocity[1])
        self.zaman_ref = self.get_clock().now().nanoseconds * 1e-6 #msec
        self.zaman_ref = self.zaman_ref - self.zaman_ilk
        
        self.joint_state.steering_angle.w1 = msg.position[0]
        self.joint_state.steering_angle.w2 = msg.position[1]
        self.joint_state.steering_angle.w3 = 0.0 # msg.position[2]
        self.joint_state.steering_angle.w4 = 0.0 # msg.position[3]

        self.joint_state.wheel_rotation.w1 = msg.velocity[0]
        self.joint_state.wheel_rotation.w2 = msg.velocity[1]
        self.joint_state.wheel_rotation.w3 = msg.velocity[2]
        self.joint_state.wheel_rotation.w4 = msg.velocity[3]

        print(str(self.zaman_ref), str(msg.position[0]), str(msg.velocity[0]), str(msg.position[1]), str(msg.velocity[1]), str(msg.position[2]), str(msg.velocity[2]), str(msg.position[3]), str(msg.velocity[3]), str(msg.position[4]), str(msg.velocity[4]), sep='\t', file=joint_input_data_txt)

        self.tire_out = tire_force_calc(self.strap_data, self.imu_data, self.joint_state)
        msg_pb = self.tire_out

        self.pub_func(msg_pb)

    def pub_func(self,msg):
        self.tire_pub.publish(msg)
        #self.get_logger().info('I publish x vel_diff as: "%f"' % msg.vel_diff.x)
        self.zaman_ref = self.get_clock().now().nanoseconds * 1e-6 #msec
        self.zaman_ref = self.zaman_ref - self.zaman_ilk
        
        print(str(self.zaman_ref), str(msg.wheel_side_slip_ang.w1), str(msg.wheel_side_slip_ang.w2) , str(msg.wheel_side_slip_ang.w3), str(msg.wheel_side_slip_ang.w4), str(msg.wheel_longitudinal_slip_ratio.w1), str(msg.wheel_longitudinal_slip_ratio.w2) , str(msg.wheel_longitudinal_slip_ratio.w3), str(msg.wheel_longitudinal_slip_ratio.w4) , sep='\t', file=tire_out_data_txt)



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
