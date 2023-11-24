#!/usr/bin/env python

import rospy
import matplotlib.pyplot as plt
from inverted_pendulum_sim.msg import ControlForce, CurrentState

class force():

    def __init__(self):
        super(force, self).__init__()
        rospy.init_node('force',anonymous=True)

        self.pub = rospy.Publisher('/inverted_pendulum/control_force', ControlForce, queue_size=1)
        rospy.Subscriber('/inverted_pendulum/current_state', CurrentState, self.currect_state_callback)
        self.pose = 0

    def currect_state_callback(self,data):
        self.pose = data.curr_x
        print(data.curr_x)

    def force(self):
        while not rospy.is_shutdown():
            if self.pose < 200:
                while self.pose < 200:
                    # print(self.pose)
                    print("----------")
                    force_pub = abs(200 - self.pose)*0.01
                    print(force_pub)
                    self.pub.publish(force_pub)
            elif self.pose > -200:
                while self.pose > -200:
                    # print(self.pose)
                    print("+++++++++++++++")    
                    force_pub = -abs(-20 - self.pose)*0.01
                    print(force_pub)
                    self.pub.publish(force_pub)

if __name__ == "__main__":
    
    object = force()
    object.force()