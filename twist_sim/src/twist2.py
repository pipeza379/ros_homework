#!/usr/bin/python2
import rospy, math, tf
from std_msgs.msg import Float64, Bool
from geometry_msgs.msg import Twist, Pose
from nav_msgs.msg import Odometry

class Zeabuscontrol:
    def __init__(self):
        rospy.init_node('autorun',anonymous=True)
        self.drive = Twist()
        self.pose = Pose()
        self.pub_vel = rospy.Publisher('/cmd_vel',Twist,queue_size=10)
        self.pub_yaw = rospy.Publisher('/fix/rel/yaw',Float64,queue_size=10)
        self.pub_abs_yaw = rospy.Publisher('/fix/abs/yaw',Float64,queue_size=10)
        self.pub_abs_depth = rospy.Publisher('/fix/abs/depth',Float64,queue_size=10)
        self.auv_state = [0,0,0,0,0,0]
        rospy.Subscriber('/auv/state',Odometry,self.getState)

    def getState(self,data):
        self.pose=data.pose.pose
        pose = self.pose
        temp = (pose.orientation.x,pose.orientation.y,pose.orientation.z,pose.orientation.w)
        euler_angular =tf.transformations.euler_from_quaternion(temp)
        self.auv_state[0] = pose.position.x
        self.auv_state[1] = pose.position.y
        self.auv_state[2] = pose.position.z

        self.auv_state[3] = euler_angular[0]
        self.auv_state[4] = euler_angular[1]
        self.auv_state[5] = euler_angular[2]

    # def run(self,move):
    #     for i in range(30):
    #         self.linears(move)
    #         rospy.loginfo("Linear Components: [%f, %f, %f]"%(self.drive.linear.x, self.drive.linear.y, self.drive.linear.z))
    #     rospy.sleep(3)
    #     self.stop()
       
    # def linears(self,move):
    #     if move == 'forward':
    #         self.drive.linear.x+=1
    #     elif move == 'back':
    #         self.drive.linear.x-=1
    #     elif move == 'up':
    #         self.drive.linear.z+=1
    #     elif move == 'down':
    #         self.drive.linear.z-=1
    #     elif move == 'left':
    #         self.drive.linear.y+=1
    #     elif move == 'right':
    #         self.drive.linear.y-=1
    #     self.pub_vel.publish(self.drive)


    def run(self,position):
        here = (self.auv_state[0],self.auv_state[1],self.auv_state[2])
        for j in range(len(position)):
            rospy.Subscriber('/auv/state',Odometry,self.getState)
            if position[j] == 777:
                continue
            if j == 0:
                error=0.6
            elif j == 1:
                error=0.33
            # elif j == 2:
            #     error =0
            self.linears(position[j],j,error)
            self.stop()
            
    def linears(self,position,pose,error):
        while self.auv_state[pose] < position-error:
            # print self.auv_state
            if pose == 0:
                self.drive.linear.x+=1
            elif pose == 1:                    
                self.drive.linear.y+=1
            elif pose == 2:
                self.drive.linear.z+=1
            self.pub_vel.publish(self.drive)
        while self.auv_state[pose] > position+error:
            # print self.auv_state
            if pose == 0:
                self.drive.linear.x-=1
            elif pose == 1:
                self.drive.linear.y-=1
            elif pose == 2:
                self.drive.linear.z-=1
            self.pub_vel.publish(self.drive)
        print self.auv_state
    def stop(self):
        self.drive.linear.x=0 
        self.drive.linear.y=0 
        self.drive.linear.z=0
        self.pub_vel.publish(self.drive)
        rospy.sleep(0.5)
        

    def turn_yaw(self,rad):
        self.stop()
        self.pub_yaw.publish(Float64(math.radians(rad)))
        rospy.sleep(2)

    def turn_abs_yaw(self,rad):
        self.stop()
        self.pub_abs_yaw.publish(Float64(math.radians(rad)))
        rospy.sleep(2)

    def depth(self,high):
        self.stop()
        self.pub_abs_depth.publish(high)

if __name__ == '__main__':
    position = [int(input('x: ')),int(input('y: '))]#,int(input())]
    control=Zeabuscontrol()
    control.turn_abs_yaw(0)
    control.run(position)
    control.stop()
    print control.auv_state

    # control.turn_yaw(-90)
    # control.depth(0.5)