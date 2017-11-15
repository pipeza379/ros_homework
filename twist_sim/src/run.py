#!/usr/bin/python2 

import rospy
from twist import autorun as move

if __name__ == '__main__':
    rospy.init_node('autorun',anonymous=True)
    move().run('right')
    move().stop()
