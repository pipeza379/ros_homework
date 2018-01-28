#!/usr/bin/python2
import rospy
from std_msgs.msg import String, Float64
from aicontrol import AIControl
import constants as cons
# import pinger as follow_pinger

class Flare(object):
    def __init__(self):
        print 'now do flare'
        
        ## vision service 

        gate_srv = 'gate'
        rospy.wait_for_service(flare_srv)
        print 'flare_srv start'
        self.detect_gate = rospy.ServiceProxy(flare_srv)
        self.check_flare = False
        self.pos_center = self.detect_gate.data_gate.pos_flare

        self.aicontrol = AIControl()

    def bump(self):
        auv = self.aicontrol
        count = 15

        print "mv to center"
        while rospy.is_shutdown() and self.aicontrol.isFail(count) :
            if self.pos_center >= 152 and self.pos_center <= 168:
                print("good aim")
                break
            elif self.pos_center < 152:
                auv.move('right',cons.AUV_SPEED)
            elif self.pos_center > 168:
                auv.move('left',cons.AUV_SPEED)
            count-=1
            ## move to center
        print "move complete"

        print "bump!!"
        while rospy.is_shutdown() and self.aicontrol.isFail(count)
        auv.move('forward',cons.FLARE_SPEED)
        ## bump flare
        auv.stop()
        
if __init__ == '__main__': 
    mission_gate = Flare()
    mission_gate.bump()
    print "finish gate"