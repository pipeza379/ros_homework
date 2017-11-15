#!/usr/bin/python2 
from std_msgs.msg import Float64, Bool
import rospy
from geometry_msgs.msg import Twist
import math


# linear=Twist().linear
# angular=Twist().angular
# print('linear');print(linear) /fix/rel/yaw
# print('angular');print(angular)
class Autorun:    
    global linears
    global angulars
    global check_stop

    def __init__(self):
        
    def run(msg,move):
        pub = rospy.Publisher('/cmd_vel',Twist,queue_size=10)
        msg=Twist()
        for _ in range(100):
            msg=linears(move)
            rospy.loginfo("Linear Components: [%f, %f, %f]"%(msg.linear.x, msg.linear.y, msg.linear.z))
            pub.publish(msg)
        rospy.sleep(5)

    def linears(move):
        msg=Twist()
        if move=='back':
            msg.linear.x-=1
        elif move=='forward':
            msg.linear.x+=1
        elif move=='up':
            msg.linear.z+=1
        elif move=='down':
            msg.linear.z-=1
        elif move=='right':
            msg.linear.y-=1
        elif move=='left':
            msg.linear.y+=1
        return msg

    def stop(msg):
        msg=Twist()
        msg.linear.x=0;msg.linear.y=0;msg.linear.z=0
        rospy.Publisher('/cmd_vel',Twist,queue_size=10).publish(Twist())

    def turn_yaw(msg,rad):
        pub = rospy.Publisher('/fix/rel/yaw',Float64,queue_size=10)
        msg=Float64(math.radians(rad))
        while not rospy.is_shutdown():
            pub.publish(msg)

    # def turn_x(msg,rad):
    #     pub = rospy.Publisher('/fix/rel/x',Float64,queue_size=10)
    #     msg=Float64(math.radians(rad))
    #     while not rospy.is_shutdown():
    #         pub.publish(msg)

    # def turn_y(msg,rad):
    #     pub = rospy.Publisher('/fix/rel/y',Float64,queue_size=10)
    #     msg=Float64(math.radians(rad))
    #     while not rospy.is_shutdown():
    #         pub.publish(msg)

    def check_turn(data):
        # print(data)
        check_stop=data.data

if __name__ == '__main__':
    check_stop = True
    rospy.init_node('autorun',anonymous=True)
    # up,down,forward,back,left,right
    # autorun().run('right')
    # autorun().stop()
    # rospy.Subscriber('/zeabus_controller/is_at_fix_orientation',Bool, Autorun().check_turn()) 
    Autorun().turn_yaw(90)
    