#!/usr/bin/env python3 

import rospy
from std_msgs.msg import String
from geometry_msgs.msg import Twist

pub = rospy.Publisher('/obstacle', String, queue_size=10)

if __name__ == '__main__':
    rospy.init_node('obstacle_identifier', anonymous=True)

    # What to Subscribe and How to get obstacle data?
    # if found log the data from callback fnc
    # :(((
    
    rospy.spin()
