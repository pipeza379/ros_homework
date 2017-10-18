#!/usr/bin/python2
import rospy
from cal_service.srv import cal_service
from ros_homework.msg import cal

def callback(req):
	req_cal=req.request.data
	req_num1=req.requestNO1
	req_num2=req.requestNO2
	if req_cal =='+':
		responseNO=req_num1+req_num2
	elif req_cal =='-':
		responseNO=req_num1-req_num2
	print(responseNO)
	return responseNO
if __name__ == '__main__':
	rospy.init_node('node_service', anonymous=True)
	service = rospy.Service('cal_service', cal_service, callback)
	rospy.spin()
