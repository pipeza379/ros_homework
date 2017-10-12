#!/usr/bin/python2
import rospy

from ros_homework.msg import cal
def publisher():
	t=cal()
	t.cal='plus'
	t.num1= 1
	t.num2= 3
	pub = rospy.Publisher('/topic_publisher',cal,queue_size=10)
	while not rospy.is_shutdown():
		pub.publish(t)
if __name__ =='__main__':
	rospy.init_node('node_publisher',anonymous=True)
	publisher()
