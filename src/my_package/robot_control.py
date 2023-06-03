#!/usr/bin/env python

import rospy
from geometry_msgs.msg import Twist

def twist_callback(msg):
    # Process the twist message and perform the desired robot motions
    # Example: Update the robot's velocity based on the received twist
    robot_velocity = msg.linear.x
    robot_angular_velocity = msg.angular.z
    # Perform further actions based on the twist message

if __name__ == '__main__':
    rospy.init_node('robot_control_node')
    rospy.Subscriber('/cmd_vel', Twist, twist_callback)
    rospy.spin()
