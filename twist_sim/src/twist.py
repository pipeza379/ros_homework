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

    def up(msg):
        pub = rospy.Publisher('/cmd_vel',Twist,queue_size=10)
        msg=Twist()
        for i in range(100):
            msg.linear.z+=1
            rospy.loginfo("Linear Components: [%f, %f, %f]"%(msg.linear.x, msg.linear.y, msg.linear.z))
            pub.publish(msg)

    def down(msg):
        pub = rospy.Publisher('/cmd_vel',Twist,queue_size=10)
        msg=Twist()
        for i in range(100):
            msg.linear.z-=1
            rospy.loginfo("Linear Components: [%f, %f, %f]"%(msg.linear.x, msg.linear.y, msg.linear.z))
            pub.publish(msg)

    def left(msg):
        pub = rospy.Publisher('/cmd_vel',Twist,queue_size=10)
        msg=Twist()
        for i in range(100):
            msg.linear.y+=1
            rospy.loginfo("Linear Components: [%f, %f, %f]"%(msg.linear.x, msg.linear.y, msg.linear.z))
            pub.publish(msg)

    def right(msg):
        pub = rospy.Publisher('/cmd_vel',Twist,queue_size=10)
        msg=Twist()
        for i in range(100):
            msg.linear.y-=1
            rospy.loginfo("Linear Components: [%f, %f, %f]"%(msg.linear.x, msg.linear.y, msg.linear.z))
            pub.publish(msg)

    def forward(msg):
        pub = rospy.Publisher('/cmd_vel',Twist,queue_size=10)
        msg=Twist()
        for i in range(100):
            msg.linear.x+=1
            rospy.loginfo("Linear Components: [%f, %f, %f]"%(msg.linear.x, msg.linear.y, msg.linear.z))
            pub.publish(msg)

    def back(msg):
        from geometry_msgs.msg import Twist
        pub = rospy.Publisher('/cmd_vel',Twist,queue_size=10)
        msg=Twist()
        for i in range(100):
            msg.linear.x-=1
            rospy.loginfo("Linear Components: [%f, %f, %f]"%(msg.linear.x, msg.linear.y, msg.linear.z))
            pub.publish(msg)

if __name__ == '__main__':
    rospy.init_node('autorun',anonymous=True)
    autorun()).forward()
    # autorun().back()
    # autorun().up()
    # autorun().down()
    # autorun().right()
    # autorun().left()