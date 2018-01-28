#!/usr/bin/python2
import rospy 
from test_araikordai_msg.msg import robot_detail 

def callback(recieveData):
    msg = recieveData
    rospy.loginfo(msg) 
 
if __name__=='__main__': 
    rospy.init_node('node_subscriber', anonymous=True) 
    rospy.Subscriber('/publish', robot_detail, callback) 
    rospy.spin() 
    