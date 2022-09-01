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
import sys

from rclpy.qos import qos_profile_sensor_data

import geometry_msgs.msg

from ht_strap_package.config import base_path

gps_data_path = base_path / "teleop_time.txt"

gps_data_gazebo_txt = open(gps_data_path, 'w')

class TeleopScnPub(Node):

    def __init__(self):
        super().__init__('teleop_scn_pub')

        # Initialise publishers
        self.cmd_pub = self.create_publisher(geometry_msgs.msg.Twist, 'cmd_vel', 10)

        self.i = 0
        self.zaman_ref = 0.0
        self.zaman_ref_sec = 0.0
        self.zaman_ilk = self.get_clock().now().nanoseconds * 1e-6 #msec

        timer_period = 5e-3 # seconds

        self.delta_t = timer_period
        self.timer = self.create_timer(timer_period, self.timer_callback)

        self.in_velocity = 0.0
        self.in_steer_ang = 0.0

        self.velocity_ = 0.0
        self.steering_angle_ = 0.0

        self.scn_num_ = 1
        # 1 : Circular Motion with Constant Velocity
        # 2 : Straight Motion with Constant Acceleration
        # 3 : Circular Motion with Constant Acceleration
        # 4 : Slalom Motion with Constant Velocity
        # 5 : Slalom Motion with Constant Acceleration
        # 6 : Straight Motion with Constant Acceleration & Decelaration
        # 2 : Straight Motion with Constant Acceleration (no vel contr btw t=20-25 sec)

        self.steer_limit = 0.1
        self.steer_diff = 0.0
        self.vel_diff = 0.0
        self.max_velocity = 16.6 # 60 km/hr

        scn_num = self.scn_num_
        if (scn_num == 1):
            self.in_velocity = 10.0
            self.in_steer_ang = 0.15 
            self.velocity_ = self.delta_t * 0.5
            self.steering_angle_ = self.in_steer_ang
        elif (scn_num == 2):
            self.in_velocity = self.delta_t * 0.2
            self.in_steer_ang = 0.0 #self.delta_t * 2.0
            self.velocity_ = 0.0
            self.steering_angle_ = 0.0
        elif (scn_num == 3):
            self.in_velocity = 0.0
            self.in_steer_ang = 0.15
            self.velocity_ = 0.0
            self.steering_angle_ = 0.15
        elif (scn_num == 4):
            self.in_velocity = 20.0
            self.in_steer_ang = 0.0
            self.velocity_ = 0.0
            self.steering_angle_ = 0.0
        elif (scn_num == 5):
            self.in_velocity = 0.0
            self.in_steer_ang = 0.0
            self.velocity_ = 0.0
            self.steering_angle_ = 0.0   
        elif (scn_num == 6):
            self.in_velocity = self.delta_t * 0.2
            self.in_steer_ang = 0.0
            self.velocity_ = self.in_velocity
            self.steering_angle_ = 0.0    
        elif (scn_num == 7):
            self.in_velocity = self.delta_t * 0.2
            self.in_steer_ang = 0.0 #self.delta_t * 2.0
            self.velocity_ = 0.0
            self.steering_angle_ = 0.0
        elif (scn_num == 8):
            self.in_velocity = self.delta_t * 0.2
            self.in_steer_ang = 0.0 #self.delta_t * 2.0
            self.velocity_ = 0.0
            self.steering_angle_ = 0.0
        elif (scn_num == 9):
            self.in_velocity = 10.0
            self.in_steer_ang = 0.15 
            self.velocity_ = self.delta_t * 0.5
            self.steering_angle_ = self.in_steer_ang

        self.last_velocity_ = self.in_velocity
        # self.pub_func(msg_pb)

    def timer_callback(self):
        twist = geometry_msgs.msg.Twist()

        # velocity = 5.0
        # acc_limit = 0.0
        # jerk_limit = 0.0
        # steering_angle = 0.35 # 0.1745 # 0.52
        self.sim_time = self.get_clock().now().nanoseconds * 1e-6 #msec
        time_diff = self.sim_time - self.zaman_ilk

        twist.linear.x = 0.0
        twist.linear.y = 0.0
        twist.linear.z = 0.0
        twist.angular.x = 0.0
        twist.angular.y = 0.0
        twist.angular.z = 0.0

        scn_num = self.scn_num_
        if (scn_num == 1):
            if (self.velocity_ < self.in_velocity):
                self.velocity_ = self.velocity_ +  self.delta_t * 0.5
            else:
                self.velocity_ = self.in_velocity
            
            self.steering_angle_ = self.in_steer_ang
        elif (scn_num == 2):
            if (self.last_velocity_ < 16.6):
                self.velocity_ = self.in_velocity +  self.i * self.delta_t * 0.2
            else:
                self.velocity_ = self.last_velocity_
            self.steering_angle_ = self.in_steer_ang
        elif (scn_num == 3):
            if (self.last_velocity_ < 12.0):
                self.velocity_ = self.in_velocity +  self.i * self.delta_t * 0.2
            else:
                self.velocity_ = self.last_velocity_            
            self.steering_angle_ = self.in_steer_ang
        elif (scn_num == 4):   
            if (self.velocity_ < self.in_velocity):
                self.velocity_ = self.velocity_ +  self.delta_t * 0.5
            else:
                self.velocity_ = self.in_velocity

            # self.velocity_ = self.in_velocity

            old_steer = self.steering_angle_

            if (self.steering_angle_ > -1e-15 and  self.steering_angle_ < self.steer_limit and self.steer_diff > -1e-15):
                self.steering_angle_ = self.steering_angle_ +  self.delta_t * 0.1
            elif(self.steering_angle_ > self.steer_limit): 
                self.steering_angle_ = self.steering_angle_ - self.delta_t * 0.1
            elif (self.steering_angle_ > -1e-15 and  self.steering_angle_ < self.steer_limit and self.steer_diff < -1e-15):
                self.steering_angle_ = self.steering_angle_ -  self.delta_t * 0.1
            elif (self.steering_angle_ < -1e-15 and  self.steering_angle_ > -self.steer_limit and self.steer_diff < -1e-15):
                self.steering_angle_ = self.steering_angle_ -  self.delta_t * 0.1
            elif(self.steering_angle_ < -self.steer_limit): 
                self.steering_angle_ = self.steering_angle_ + self.delta_t * 0.1
            elif (self.steering_angle_ < -1e-15 and  self.steering_angle_ > -self.steer_limit and self.steer_diff > -1e-15):
                self.steering_angle_ = self.steering_angle_ + self.delta_t * 0.1
            
            self.steer_diff = self.steering_angle_ - old_steer

        elif (scn_num == 5):
            self.velocity_ = self.in_velocity +  self.i * self.delta_t * 0.5
            old_steer = self.steering_angle_

            if (self.steering_angle_ > -1e-15 and  self.steering_angle_ < self.steer_limit and self.steer_diff > -1e-15):
                self.steering_angle_ = self.steering_angle_ +  self.delta_t * 0.1
            elif(self.steering_angle_ > self.steer_limit): 
                self.steering_angle_ = self.steering_angle_ - self.delta_t * 0.1
            elif (self.steering_angle_ > -1e-15 and  self.steering_angle_ < self.steer_limit and self.steer_diff < -1e-15):
                self.steering_angle_ = self.steering_angle_ -  self.delta_t * 0.1
            elif (self.steering_angle_ < -1e-15 and  self.steering_angle_ > -self.steer_limit and self.steer_diff < -1e-15):
                self.steering_angle_ = self.steering_angle_ -  self.delta_t * 0.1
            elif(self.steering_angle_ < -self.steer_limit): 
                self.steering_angle_ = self.steering_angle_ + self.delta_t * 0.1
            elif (self.steering_angle_ < -1e-15 and  self.steering_angle_ > -self.steer_limit and self.steer_diff > -1e-15):
                self.steering_angle_ = self.steering_angle_ + self.delta_t * 0.1
            
            self.steer_diff = self.steering_angle_ - old_steer      
        
        elif (scn_num == 6):
            self.steering_angle_ = self.in_steer_ang
            old_vel = self.velocity_
            if(self.velocity_ > -1e-15 and self.velocity_ < self.max_velocity and self.vel_diff > -1e-15):
                self.velocity_ = self.velocity_ + self.delta_t * 0.2 
            elif(self.velocity_ > self.max_velocity): 
                self.velocity_ = self.velocity_ - self.delta_t * 0.2 
            elif (self.velocity_ > -1e-15 and  self.velocity_ < self.max_velocity and self.vel_diff < -1e-15):
                self.velocity_ = self.velocity_ - self.delta_t * 0.2 
            elif (self.velocity_ < -1e-15 ):
                self.velocity_ = self.velocity_ +  self.delta_t * 0.2

            self.vel_diff = self.velocity_ - old_vel      

        elif (scn_num == 7):
            if( (time_diff * 1e-3) > 20.0 and  (time_diff * 1e-3) < 25.0):
                self.velocity_ = self.last_velocity_   
                twist.linear.z  = 1.0  # for new ackermann plugin: lin_vel_stop_: stops the linear velocity controller 
                twist.angular.x = 1.0  # for new ackermann plugin: steer_stop_: stops the steering angle controller
            else:
                self.velocity_ = self.last_velocity_ + self.delta_t * 0.2
            self.steering_angle_ = self.in_steer_ang
    
        elif (scn_num == 8):
            if( (time_diff * 1e-3) > 50.0 and  (time_diff * 1e-3) < 55.0):
                self.velocity_ = self.last_velocity_   
                twist.linear.z  = 1.0  # for new ackermann plugin: lin_vel_stop_: stops the linear velocity controller 
                twist.angular.x = 1.0  # for new ackermann plugin: steer_stop_: stops the steering angle controller
            else:
                if(self.velocity_ > -1e-15 and self.velocity_ < 8.0):
                    self.velocity_ = self.last_velocity_ + self.delta_t * 0.2
                else:
                    self.velocity_ = self.last_velocity_
            self.steering_angle_ = self.in_steer_ang

        if (scn_num == 9):
            if( (time_diff * 1e-3) > 50.0 and  (time_diff * 1e-3) < 55.0):
                twist.linear.z  = 1.0  # for new ackermann plugin: lin_vel_stop_: stops the linear velocity controller 
                twist.angular.x = 1.0  # for new ackermann plugin: steer_stop_: stops the steering angle controller
            else:
                if (self.velocity_ < self.in_velocity):
                    self.velocity_ = self.velocity_ +  self.delta_t * 0.5
                else:
                    self.velocity_ = self.in_velocity
            
            self.steering_angle_ = self.in_steer_ang

        velocity = self.velocity_
        steering_angle = self.steering_angle_

        twist.linear.x = velocity
        twist.angular.z = steering_angle

        self.last_velocity_ = self.velocity_    

        self.cmd_pub.publish(twist)
        # self.get_logger().info('Publishing: "%s"' % msg.data)
        self.i += 1

    # def pub_func(self,msg):
        # self.gps_pub.publish(msg)
        # #self.get_logger().info('I publish lat as: "%f"' % msg.gps_pos.x)
        # self.zaman_ref = self.get_clock().now().nanoseconds * 1e-6 #msec
        # self.zaman_ref = self.zaman_ref - self.zaman_ilk
        # print(str(self.zaman_ref), str(msg.gps_pos.x), str(msg.gps_pos.y), str(msg.gps_pos.z), str(msg.gps_vel.x), str(msg.gps_vel.y), str(msg.gps_vel.z), sep='\t', file=gps_data_gazebo_txt)
 


def main(args=None):
    rclpy.init(args=args)

    teleop_scn_pub = TeleopScnPub()

    rclpy.spin(teleop_scn_pub)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    teleop_scn_pub.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()