#!/usr/bin/env python2

import rospy
from test_araikordai_msg.msg import robot_detail
from std_msgs.msg import String,Float32
def sender(name):
    zeabus_i = robot_detail()
    zeabus_i.name = name
    zeabus_i.year = 2016
    zeabus_i.weight = 50
    return zeabus_i

def reciever(data):
    robot_detail_obj=data
    print(robot_detail_obj)
    print(robot_detail_obj.name)

def test_std_msg():
    name = String(sender('ZeabusI').name)
    print(name)
    print(robot_detail()7)


if __name__ == '__main__':
    rospy.init_node("test_message")
    data = sender("ZeabusI")
    #reciever(data)
    #while not rospy.is_shutdown():
     #   rospy.sleep(0.1)
    test_std_msg()