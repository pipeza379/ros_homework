#!/usr/bin/python2 
import rospy 
from test_service.srv import robot_service
from test_araikordai_msg.msg import robot_detail

def callback(req):
    print(req)
    name = req.name

    zeabus_i = robot_detail()
    zeabus_i.name = 'zeabusI'
    zeabus_i.year = 2015
    zeabus_i.weight = 60 

    zeabus_ii = robot_detail()
    zeabus_ii.name = 'zeabusII'
    zeabus_ii.year = 2016
    zeabus_ii.weight = 55 

    if name == 'zeabusI':
        return zeabus_i
    else:
        return zeabus_ii
 
if __name__ == '__main__': 
    rospy.init_node('node_service', anonymous=True) 
    service = rospy.Service('robot_service_name', robot_service, callback) 
    rospy.spin() 
