#!/usr/bin/env python

import rospy
import math
from inverted_pendulum_sim.msg import ControlForce, CurrentState
from std_msgs.msg import Float64

class ForceController:

    def __init__(self):
        rospy.init_node('force_controller', anonymous=True)

        self.pub = rospy.Publisher('/inverted_pendulum/control_force', ControlForce, queue_size=1)
        rospy.Subscriber('/inverted_pendulum/current_state', CurrentState, self.current_state_callback)
        self.pose = 0
        self.angle = 0
        self.kp = 1.062
        self.ki = 0.0552
        self.kd = 0.462
        self.prev_error = 0
        self.integral = 0

    def current_state_callback(self, data):
        self.pose = data.curr_x
        self.angle = data.curr_theta
          
    def pid_control(self):
        rate = rospy.Rate(10)

        while not rospy.is_shutdown():
            setpoint = math.pi

            error = setpoint - self.angle
            self.integral += error
            derivative = error - self.prev_error

            control_effort = self.kp * error + self.ki * self.integral + self.kd * derivative
            print("error is = ", end='')
            print(error)
            if 0 <= self.angle <= math.pi:
                print("right")
                self.pub.publish(control_effort)
            else:
                print("left")
                self.pub.publish(-control_effort)

            self.prev_error = error

            rospy.loginfo("Angle: {:.3f}, Control Effort: {:.3f}".format(self.angle, control_effort))
            rate.sleep()

if __name__ == "__main__":
    controller = ForceController()
    controller.pid_control()
