# Copyright 2011 Brown University Robotics.
# Copyright 2017 Open Source Robotics Foundation, Inc.
# All rights reserved.
#
# Software License Agreement (BSD License 2.0)
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions
# are met:
#
#  * Redistributions of source code must retain the above copyright
#    notice, this list of conditions and the following disclaimer.
#  * Redistributions in binary form must reproduce the above
#    copyright notice, this list of conditions and the following
#    disclaimer in the documentation and/or other materials provided
#    with the distribution.
#  * Neither the name of the Willow Garage nor the names of its
#    contributors may be used to endorse or promote products derived
#    from this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
# "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
# LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS
# FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE
# COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT,
# INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING,
# BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
# LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
# CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT
# LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN
# ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.

import sys

import geometry_msgs.msg
import rclpy

if sys.platform == 'win32':
    import msvcrt
else:
    import termios
    import tty


msg = """
This node takes keypresses from the keyboard and publishes them
as Twist messages. It works best with a US keyboard layout.
---------------------------
Moving around:
        w     
   a    s    d

anything else : stop

t/y : increase/decrease acc limit by 10%
g/h : increase/decrease velocity increase limit by 10%

CTRL-C to quit
"""

velocityBindings = {
    'w': (1,  0,  0, 0, 1, 1),
    'a': (0,  0,  0, 1, 1, 1),
    's': (0, -1,  0, 0, 1, 1),
    'd': (0,  0, -1, 0, 1, 1),
    'q': (0,  0,  0, 0, 0, 1),
    'e': (0,  0,  0, 0, 1, 0),
}

accLimits = {
    't': (0.9,   1,   1,   1),
    'y': (  1, 1.1,   1,   1),
    'g': (  1,   1, 0.9,   1),
    'h': (  1,   1,   1, 1.1),
}




def getKey(settings):
    if sys.platform == 'win32':
        # getwch() returns a string on Windows
        key = msvcrt.getwch()
    else:
        tty.setraw(sys.stdin.fileno())
        # sys.stdin.read() returns a string on Linux
        key = sys.stdin.read(1)
        termios.tcsetattr(sys.stdin, termios.TCSADRAIN, settings)
    return key


def saveTerminalSettings():
    if sys.platform == 'win32':
        return None
    return termios.tcgetattr(sys.stdin)


def restoreTerminalSettings(old_settings):
    if sys.platform == 'win32':
        return
    termios.tcsetattr(sys.stdin, termios.TCSADRAIN, old_settings)


def vels(velocity, turn):
    return 'currently:\tvelocity %s\tturn %s ' % (velocity, turn)


def main():
    settings = saveTerminalSettings()

    rclpy.init()

    node = rclpy.create_node('teleop_controller')
    pub = node.create_publisher(geometry_msgs.msg.Twist, 'cmd_vel', 10)

    steering_angle = 0.0
    angle_scale_factor = 0.025
    velocity = 0.0
    veloity_scale_factor = 0.2
    acc_limit = 0.2
    jerk_limit = 0.0
    status = 0.0
    max_steer = 0.4 # 0.6458

    try:
        print(msg)
        print(vels(velocity, steering_angle))
        while True:
            key = getKey(settings)
            if key in velocityBindings.keys():
                velocity = velocity + veloity_scale_factor * velocityBindings[key][0]
                velocity = velocity + veloity_scale_factor * velocityBindings[key][1]
                    
                steering_angle = steering_angle + angle_scale_factor * velocityBindings[key][2]
                steering_angle = steering_angle + angle_scale_factor * velocityBindings[key][3]

                velocity        = velocity       * velocityBindings[key][4]
                steering_angle  = steering_angle * velocityBindings[key][5]

                if abs(steering_angle) < 1e-5:
                        steering_angle = 0.0

            elif key in accLimits.keys():
                acc_limit = acc_limit * accLimits[key][0]
                acc_limit = acc_limit * accLimits[key][1]
                 
                veloity_scale_factor = veloity_scale_factor * accLimits[key][2]
                veloity_scale_factor = veloity_scale_factor * accLimits[key][3]                 

                print(vels(velocity, steering_angle))
                if (status == 14):
                    print(msg)
                status = (status + 1) % 15
            else:
                velocity = 0.0
                acc_limit = 0.0
                jerk_limit = 0.0
                steering_angle = 0.0
                if (key == '\x03'):
                    break

            if abs(steering_angle) > max_steer:
                if (steering_angle < 0.0):
                    steering_angle = -max_steer
                else:
                    steering_angle = max_steer
            else:
                steering_angle = steering_angle

            twist = geometry_msgs.msg.Twist()
            twist.linear.x = velocity
            twist.linear.y = acc_limit
            twist.linear.z = jerk_limit
            twist.angular.x = 0.0
            twist.angular.y = 0.0
            twist.angular.z = steering_angle
            pub.publish(twist)

    except Exception as e:
        print(e)

    finally:
        twist = geometry_msgs.msg.Twist()
        twist.linear.x = 0.0
        twist.linear.y = 0.0
        twist.linear.z = 0.0
        twist.angular.x = 0.0
        twist.angular.y = 0.0
        twist.angular.z = 0.0
        pub.publish(twist)

        restoreTerminalSettings(settings)


if __name__ == '__main__':
    main()
