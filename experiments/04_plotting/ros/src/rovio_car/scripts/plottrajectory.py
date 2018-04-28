#!/usr/bin/env python 

# Adapted from: https://answers.ros.org/question/264767/plotting-real-time-data/

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import rospy
from nav_msgs.msg import Odometry
from trajectory_toolkit.VIEvaluator import VIEvaluator
from trajectory_toolkit import Quaternion
from trajectory_toolkit import Utils
from trajectory_toolkit import RosDataAcquisition


def processOdomData(dat):
    td_visual = TimedData()
    eval = VIEvaluator()
    eval.bag = bag_file_name
    eval.odomTopic = odometry_topic_name
    eval.alignMode = 0 
    eval.derMode = 0
    eval.initTimedData(td_visual)
    eval.acquireData()
    eval.getAllDerivatives()
    eval.alignTime()
    eval.alignBodyFrame()
    eval.alignInertialFrame()
    eval.getYpr()
    eval.evaluateSigmaBounds()

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