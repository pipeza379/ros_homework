#!/usr/bin/python2 
import rospy
cal = str(input())
num1 = float(input())
num2 = float(input())
rospy.init_node('hello_program')
if cal == '1':
        print(num1+num2)        
if cal == '2':
        print(num1-num2)


