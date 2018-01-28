#!/usr/bin/python2

class Robot():
    weight = 50
    no_of_thruster = 0
    speed = 5
    name ='zeabus'
    def show_name(self):
        print(self.name)

if __name__=='__main__':
    zeabus_i = Robot()
    zeabus_ii = Robot()
    zeabus_i.name = 'zeabusI'
    zeabus_ii.name = 'zeabusII'
    print(zeabus_i.name)
    zeabus_ii.show_name()
