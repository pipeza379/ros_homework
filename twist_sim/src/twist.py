#!/usr/bin/python2 

import rospy
from geometry_msgs.msg import Twist

# linear=Twist().linear
# angular=Twist().angular
# print('linear')
# print(linear)
# print('angular')
# print(angular)
class autorun:    
    global linears

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

if __name__ == '__main__':
    rospy.init_node('autorun',anonymous=True)
    autorun().run('left')
    #up,down,forward,back,left,right
    Twist().linear.x=0;Twist().linear.y=0;Twist().linear.z=0
    rospy.Publisher('/cmd_vel',Twist,queue_size=10).publish(Twist())
