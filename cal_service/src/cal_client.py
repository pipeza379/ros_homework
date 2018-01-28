#!/usr/bin/python2
import rospy
from cal_service.srv import cal2_service
from ros_homework.msg import cal
#from std_msgs.msg import String

def client_request():
	rospy.wait_for_service('cal_service')
	client=rospy.ServiceProxy('cal_service',cal2_service)
	call=cal2_service()
	print('Press plus or minus or exit')
	calculate=raw_input()
	if calculate=='exit':
		exit()
	elif calculate=='plus':
		call.cal=str('+')
	elif calculate=='minus':
		call.cal=str('-')
	print 'Number1',':'
	call.num1=int(input())
	print 'Number2',':'
	call.num2=int(input())
	num=client(call)
	print(num.responseNO)
	print "{} {} {}=" .format(call.num1,call.cal,call.num2),num.responseNO

if __name__ == '__main__':
	rospy.init_node('node_client',anonymous=True)
	client_request()
