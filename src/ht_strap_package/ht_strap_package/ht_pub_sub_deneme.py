#!/usr/bin/env python3

import rclpy

from rclpy.node import Node
from geometry_msgs.msg import PoseStamped, Pose2D, Point
from ht_nav_variables import *
from nav_msgs.msg import Path
from std_msgs.msg import Float64
from visualization_msgs.msg import Marker
from builtin_interfaces.msg import Duration
from std_msgs.msg import String
from ht_nav_variables.msg import HtNavDeneme


class DenemePubSub(Node):

    def __init__(self):
        ''' 
        Class constructor to initialise the class 
        '''

        super().__init__('deneme_ps')

        # Initialise publishers
        self.deneme_pub = self.create_publisher(HtNavDeneme, 'topic2', 10)

        # Initialise subscribers
        self.deneme_sub = self.create_subscription(HtNavDeneme, 'topic1', self.sub_cb, 10)

        self.ax = []


    def sub_cb(self, msg):
        self.ax.append(msg.num)
        self.pub_func(msg)

    def pub_func(self,x):
        self.deneme_pub.publish(x)

def main(args=None):
    ''' 
    Main function to initialise the class and node. 
    '''

    # Initialise the node
    rclpy.init(args=args)

    try:
        # Initialise the class
        deneme_ps = DenemePubSub()

        # Stop the node from exiting
        rclpy.spin(deneme_ps)

    finally:
        deneme_ps.destroy_node()
        rclpy.shutdown()

if __name__=="__main__":
    main()