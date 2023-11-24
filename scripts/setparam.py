#!/usr/bin/env python

import rospy
import time
from math import pi
from inverted_pendulum_sim.srv import SetParams


def master_node():
    rospy.wait_for_service('/inverted_pendulum/set_params')
    try:
        pendulum_mass=2.0 
        pendulum_length=300.0 
        cart_mass=0.5 
        theta_0=pi
        theta_dot_0=0.0
        theta_dot_dot_0=0.0 
        cart_x_0=0.0 
        cart_x_dot_0=0.0 
        cart_x_dot_dot_0=0.0
        param= rospy.ServiceProxy('/inverted_pendulum/set_params', SetParams)
        result = param(pendulum_mass, pendulum_length, cart_mass, theta_0, theta_dot_0, theta_dot_dot_0, cart_x_0, cart_x_dot_0, cart_x_dot_dot_0)
        print(result.success)
        print(result.message)

    except rospy.ServiceException as e:
        print("Service call failed:", e)

if __name__ == "__main__":
    rospy.init_node('master_node')
    master_node()