#!/usr/bin/python2
import rospy
from cal_service.srv import cal2_service
#from ros_homework.msg import cal

def callback(req):
	req_cal=req.call.cal
	req_num1=req.call.num1
	req_num2=req.call.num2
	if req_cal =='+':
		responseNO=req_num1+req_num2
	elif req_cal =='-':
		responseNO=req_num1-req_num2
	print(responseNO)
	return responseNO
if __name__ == '__main__':
	rospy.init_node('node_service', anonymous=True)
	service = rospy.Service('cal_service', cal2_service, callback)
	rospy.spin()
