#!/usr/bin/python2

import rospy
from test_service.srv import robot_service
from test_araikordai_msg.msg import robot_detail


def client():
    rospy.wait_for_service('robot_service_name')
    client = rospy.ServiceProxy('robot_service_name', robot_service)
    data = client('zeabusI')
    print(data.response.name)
    


if __name__ == '__main__':
    rospy.init_node('node_client')
    client()