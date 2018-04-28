#!/bin/sh

# Description: 
# Start the ROS system and verify that plotting works.

PROJECT_HOME=/home/raoul/vio-thesis
EXPERIMENT_HOME=$PROJECT_HOME/experiments/04_plotting
PROCESS_RATE=1.0

echo "===================="
echo " Running experiment"
echo "===================="
mkdir -p $EXPERIMENT_HOME/results
roslaunch rovio.launch PROCESS_RATE:=$PROCESS_RATE PROJECT_HOME:=$PROJECT_HOME EXPERIMENT_HOME:=$EXPERIMENT_HOME