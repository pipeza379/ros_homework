#!/usr/bin/python2 

import rospy 
from test_araikordai_msg.msg import robot_detail 

def publisher(): 
    pub = rospy.Publisher('/publish', robot_detail, queue_size=10) 
    while not rospy.is_shutdown(): 
        zeabus_ii = robot_detail()
        zeabus_ii.name = 'zeabusII'
        zeabus_ii.weight = 50
        zeabus_ii.year = 2016
        pub.publish(zeabus_ii)

if __name__=='__main__': 
    rospy.init_node('node_publisher', anonymous=True) 
    publisher()