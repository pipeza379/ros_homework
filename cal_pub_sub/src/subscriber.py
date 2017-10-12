#!/usr/bin/env python
import rospy
from std_msgs.msg import String
from ros_homework.msg import cal

def callback(recieveData): 
	msg = recieveData
	cal = msg.cal
	num1 = msg.num1
	num2 = msg.num2
	rospy.loginfo('%d+%d=%d' %(num1,num2,num1+num2))

if __name__=='__main__':
	rospy.init_node('node_subscriber',anonymous=True)
	rospy.Subscriber('/topic_publisher',cal,callback)
	rospy.spin()
