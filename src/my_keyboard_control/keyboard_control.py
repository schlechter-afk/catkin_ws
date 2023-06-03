#!/usr/bin/env python

import rospy
from geometry_msgs.msg import Twist
from pynput import keyboard

linear_vel = 0.2
angular_vel = 0.2

twist_msg = Twist()

def on_press(key):
    global twist_msg

    if key == keyboard.Key.up:
        twist_msg.linear.x = linear_vel
    elif key == keyboard.Key.down:
        twist_msg.linear.x = -linear_vel
    elif key == keyboard.Key.left:
        twist_msg.angular.z = angular_vel
    elif key == keyboard.Key.right:
        twist_msg.angular.z = -angular_vel

def on_release(key):
    global twist_msg

    if key == keyboard.Key.up or key == keyboard.Key.down:
        twist_msg.linear.x = 0.0
    elif key == keyboard.Key.left or key == keyboard.Key.right:
        twist_msg.angular.z = 0.0

def keyboard_control():
    rospy.init_node('keyboard_control')
    pub = rospy.Publisher('/cmd_vel', Twist, queue_size=10)

    listener = keyboard.Listener(on_press=on_press, on_release=on_release)
    listener.start()

    rate = rospy.Rate(10)  # 10 Hz

    while not rospy.is_shutdown():
        pub.publish(twist_msg)
        rate.sleep()

if __name__ == '__main__':
    try:
        keyboard_control()
    except rospy.ROSInterruptException:
        pass