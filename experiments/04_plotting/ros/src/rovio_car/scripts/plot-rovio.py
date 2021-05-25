# Imports
import os, sys, inspect
import numpy as np

from trajectory_toolkit.TimedData import TimedData
from trajectory_toolkit.Plotter import Plotter
from trajectory_toolkit import Quaternion
from trajectory_toolkit import Utils
from trajectory_toolkit import RosDataAcquisition
from trajectory_toolkit.VIEvaluator import VIEvaluator

plotRon = False
plotAtt = False
plotPos = True
plotVel = False
plotRor = False
plotYpr = False
plotExt = False

td_rovio = TimedData()
td_vicon = TimedData()

def plot_single():
    rovioEvaluator = VIEvaluator()
    rovioEvaluator.bag = '/home/raoul/vio-thesis/datasets/eval.bag'
    rovioEvaluator.odomTopic = '/rovio/odometry'
    rovioEvaluator.initTimedData(td_rovio)
    rovioEvaluator.acquireData()
    # Position plotting
    plotterPos = Plotter(-1, [3,1],'Position',['','','time[s]'],['x[m]','y[m]','z[m]'],10000)
    plotterPos.addDataToSubplotMultiple(td_rovio, 'pos', [1,2,3], ['r','r','r'], ['','',''])

def plot_with_truth():
    td_visual = TimedData()
    td_vicon = TimedData()

    eval = VIEvaluator()
    eval.bag = '/home/raoul/vio-thesis/datasets/eval.bag'
    eval.odomTopic = '/rovio/odometry'
    eval.gtFile = '/home/raoul/vio-thesis/datasets/eval.bag'
    eval.gtTopic = '/vicon/firefly_sbx/firefly_sbx'
    eval.alignMode = 0     # Align body frames to the same inertial (not viceversa)
    eval.derMode = 0    # Compute analytical derivatives for visual data as well

    eval.initTimedData(td_visual)
    eval.acquireData()
    
    eval.initTimedDataGT(td_vicon)
    eval.acquireDataGT()
    eval.getAllDerivatives()
    eval.alignTime()
    eval.alignBodyFrame()
    eval.alignInertialFrame()
    eval.getYpr()
    eval.evaluateSigmaBounds()

    plotterPos = Plotter(-1, [3,1],'Position',['','','time[s]'],['x[m]','y[m]','z[m]'],10000)
    plotterPos.addDataToSubplotMultiple(td_visual, 'pos', [1,2,3], ['r','r','r'], ['Rovio','Rovio','Rovio'])
    plotterPos.addDataToSubplotMultiple(td_vicon, 'pos', [1,2,3], ['g','g','g'], ['Truth','Truth','Truth'])
    # plotterPos.setAxis(1, y1=1000)
    # plotterPos.setAxis(2, y1=1000)
    # plotterPos.setAxis(3, y1=1000)

plot_single()

raw_input('press enter')
