#!/usr/bin/python2
import rospy
from cal_service.srv import cal_service
from ros_homework.msg import cal
from std_msgs.msg import String

def client_request():
	rospy.wait_for_service('cal_service')
	client=rospy.ServiceProxy('cal_service',cal_service)
	print('Press plus or minus or exit')
	calculate=raw_input()
	if calculate=='exit':
		exit()
	elif calculate=='plus':
		calculate=String('+')
	elif calculate=='minus':
		calculate=String('-')
	print 'Number1',':'
	num1=int(input())
	print 'Number2',':'
	num2=int(input())
	num=client(calculate,num1,num2)
	print(num.responseNO)
	print "{} {} {}=" .format(num1,calculate.data,num2),num.responseNO

if __name__ == '__main__':
	rospy.init_node('node_client',anonymous=True)
	client_request()
