#!/bin/sh

# Description: 
# Start the ROS system and verify that plotting works.

PROJECT_HOME=/home/raoul/vio-thesis
EXPERIMENT_HOME=$PROJECT_HOME/experiments/01_basic_experiment
PROCESS_RATE=1.0

echo "======================="
echo " Pull in launch script"
echo "======================="
cd $PROJECT_HOME/test
#rm rovio.launch
#cp $PROJECT_HOME/rovio_template.launch ./rovio.launch

echo "===================="
echo " Running experiment"
echo "===================="

mkdir $EXPERIMENT_HOME/results
roslaunch rovio.launch PROCESS_RATE:=$PROCESS_RATE PROJECT_HOME:=$PROJECT_HOME EXPERIMENT_HOME:=$EXPERIMENT_HOME
echo "======================="
echo " View how we did..."
echo "======================="
python $EXPERIMENT_HOME/plot.py $EXPERIMENT_HOME $PROCESS_RATE
