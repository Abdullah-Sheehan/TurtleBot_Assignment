#!/usr/bin/env python3 

import rospy
from std_msgs.msg import String
from geometry_msgs.msg import Twist

cmd_list = []

def cmd_clbk(data):
    cmd = data.data
    cmd_list.append(cmd)

    rospy.loginfo(f"Command History: {cmd_list}") # Prints the whole history


if __name__ == '__main__':
    rospy.init_node('command_history', anonymous=True)

    rospy.Subscriber('/turtlebot_commands', String, cmd_clbk)
    rospy.spin()
