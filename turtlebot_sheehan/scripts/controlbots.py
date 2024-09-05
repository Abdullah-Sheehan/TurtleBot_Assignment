#!/usr/bin/env python3 

import rospy
from std_msgs.msg import String
from geometry_msgs.msg import Twist

pub = rospy.Publisher('/cmd_vel', Twist, queue_size=10)
# This publishes the twist data into turtlebot cmd_vel

def movethebot(data):
    # print(data)
    direction, speed = data.data.split()
    # speed *= 1.00
    speed = float(speed)
    # print(direction, speed)
    current_position = Twist()
    if direction == 'Move' or direction == 'Forward' or direction == 'Up':
        current_position.linear.x = speed
    elif direction == 'Backward' or direction == 'Down':
        current_position.linear.x = -speed
    elif direction == 'Left':
        current_position.angular.z = speed
    elif direction == 'Right':
        current_position.angular.z = -speed
    
    pub.publish(current_position)


if __name__ == '__main__':
    rospy.init_node('control_node', anonymous=True)

    rospy.Subscriber('command_taker', String, movethebot)
    # subscribes input from 'command_taker' of the previous script and handle the process
    # of the moving

    # I have some problem understanding the motion axis of this turtle bot 3 :(((
    rospy.spin()