#!/usr/bin/env python 

# Imports
import os, sys, inspect
import numpy as np
import rospy

from trajectory_toolkit.TimedData import TimedData
from trajectory_toolkit.Plotter import Plotter
from trajectory_toolkit import Quaternion
from trajectory_toolkit import Utils
from trajectory_toolkit import RosDataAcquisition
from trajectory_toolkit.VIEvaluator import VIEvaluator


class OdometryListener:
    td = TimedData(0)
    posId = [1, 2, 3]

    def __init__(self, td, topic, posId = [1,2,3])


def plot_single():
    rovioEvaluator = VIEvaluator()
    rovioEvaluator.bag = '/home/raoul/vio-thesis/experiments/01_basic_experiment/results/rovio_traj_1.0.bag'
    rovioEvaluator.odomTopic = '/rovio/odometry'
    rovioEvaluator.initTimedData(td3)

    rovioEvaluator.acquireData()
    # Position plotting
    plotterPos = Plotter(-1, [3,1],'Position',['','','time[s]'],['x[m]','y[m]','z[m]'],10000)
    plotterPos.addDataToSubplotMultiple(td3, 'pos', [1,2,3], ['r','r','r'], ['','',''])



td3 = TimedData(8)
rospy.init_node('example', anonymous=True)
rate = rospy.Rate(100)
tsl = RosDataAcquisition.TransformStampedListener(td3, "/rovio/transform", 1, 4)

"""
    Initialize the plotter as a live plot. Limit the maximal number of displayed points to 300.
"""
livePlotter = Plotter(1, [4,2], 300)
livePlotter.addDataToSubplot(td3, 1, 1, 'r', 'rx');
livePlotter.addDataToSubplot(td3, 2, 3, 'g', 'ry');
livePlotter.addDataToSubplot(td3, 3, 5, 'b', 'rz');

"""
    Run the node and refresh the live Plotter.
"""
while not rospy.is_shutdown():
    livePlotter.refresh()
    rate.sleep()
