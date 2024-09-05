#!/usr/bin/env python3 

import rospy
from std_msgs.msg import String

pub = rospy.Publisher('/turtle_pos_xy', String, queue_size=10)


if __name__ == '__main__':
    rospy.init_node('position_turtle', anonymous=True)

    # rospy.Subscriber(???, ???, console position data from fnc) 
    # How to get robot position data :( if i get it should be printed from callback fnc 
    # in subscriber call :)
    
    rate = rospy.Rate(0.2) # This is for 1 Message in each 5 Second

    while not rospy.is_shutdown():
        rate.sleep()