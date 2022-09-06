#!/usr/bin/env python3
import rospy
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose
from math import pow, atan2, sqrt


def pose_upgrade(msg: Pose):
    global pose
    pose = msg
    

rospy.init_node('turtle_controller')

pub = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
sub = rospy.Subscriber('/turtle1/pose', Pose, callback=pose_upgrade)
rate = rospy.Rate(10)


def set_beta():
    rospy.set_param('/beta', beta)
    return rospy.get_param('/beta')

def set_phi():
    rospy.set_param('/phi', phi)
    return rospy.get_param('/phi')

def distance():
    return sqrt(pow((x_goal - pose.x), 2) + pow((y_goal - pose.y), 2))

def linear_vel():
    return set_beta() * distance()

def angular_vel():
    return set_phi() * (atan2(y_goal - pose.y, x_goal - pose.x) - pose.theta)


def go_to_goal():
    global x_goal, y_goal, beta, phi
    x_goal = rospy.get_param('/x_goal')
    y_goal = rospy.get_param('/y_goal')
    beta = float(input('Enter Beta value: '))
    phi = float(input('Enter Phi value: '))

    while distance() >= 0.1:
        vel =  Twist()

        vel.linear.x = linear_vel()
        vel.linear.y = 0
        vel.linear.z = 0

        vel.angular.x = 0
        vel.angular.y = 0
        vel.angular.z = angular_vel()
        pub.publish(vel)

        rate.sleep()

    vel.linear.x = 0
    vel.angular.z = 0
    pub.publish(vel)
    print("Arrived to the goal!")

    rospy.spin()


go_to_goal()
