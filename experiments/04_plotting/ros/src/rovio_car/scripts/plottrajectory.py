#!/usr/bin/env python 

# Adapted from: https://answers.ros.org/question/264767/plotting-real-time-data/

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import rospy
from nav_msgs.msg import Odometry

def plotData(msg):
    global ax
    pos = msg.pose.pose.position
    ax.scatter3D(pos.x, pos.y, pos.z, cmap='Greens');
    plt.draw()
    plt.pause(0.02)

if __name__ == '__main__':
    rospy.init_node("plottrajectory")
    rospy.Subscriber("rovio/odometry", Odometry, plotData)

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    plt.ion()
    plt.show(block=True)
    #rospy.spin()