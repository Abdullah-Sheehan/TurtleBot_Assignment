#!/usr/bin/env python3 

import rospy
from std_msgs.msg import String


if __name__ == '__main__':
    rospy.init_node("turtlebot_commands", anonymous=True)

    pub = rospy.Publisher('command_taker', String, queue_size=10)
    rate = rospy.Rate(10)

    while not rospy.is_shutdown():
        command = input("Enter you command: ")

        pub.publish(command)
        rate.sleep()
    
    ## This node takes commands from the user -> publish it as "command_taker"