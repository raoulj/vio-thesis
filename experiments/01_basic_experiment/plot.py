#!/usr/bin/env python

# Example execution:
# python plot.py /home/raoul/vio-thesis/experiments/01_basic_experiment 1.0


import os, sys, inspect
import numpy as np
import matplotlib.pyplot as plt

from trajectory_toolkit.TimedData import TimedData
from trajectory_toolkit.Plotter import Plotter
from trajectory_toolkit.VIEvaluator import VIEvaluator
from trajectory_toolkit import Quaternion
from trajectory_toolkit import Utils
from trajectory_toolkit import RosDataAcquisition


def load_one_comparison(bag_file_name, odometry_topic_name):
    td_visual = TimedData()
    td_vicon = TimedData()

    eval = VIEvaluator()
    eval.bag = bag_file_name
    eval.odomTopic = odometry_topic_name
    eval.gtFile = bag_file_name
    eval.gtTopic = '/vicon/firefly_sbx/firefly_sbx'
    eval.alignMode = 0     # Align body frames to the same inertial (not viceversa)
    eval.derMode = 0    # Compute analytical derivatives for visual data as well

    eval.initTimedData(td_visual)
    eval.initTimedDataGT(td_vicon)
    eval.acquireData()
    eval.acquireDataGT()
    eval.getAllDerivatives()
    eval.alignTime()
    eval.alignBodyFrame()
    eval.alignInertialFrame()
    eval.getYpr()
    eval.evaluateSigmaBounds()

    return td_visual, td_vicon


plotterPos = Plotter(-1, [1,1],'',['time[s]'],['x[m]'],10000)

assert len(sys.argv) > 1, 'Insufficient arguments.  Proper usage: python plot.py experiment_location rate'
experiment_path = sys.argv[1]
rate = sys.argv[2]

td_visual, td_vicon = load_one_comparison(os.path.join(experiment_path, 'results/rovio_traj_{}.bag'.format(rate)), '/rovio/odometry')
plotterPos.addDataToSubplot(td_visual, 1, 1, '', 'Rovio')
plotterPos.addDataToSubplot(td_vicon, 1, 1, '', 'Truth')

raw_input('Press enter to exit')

