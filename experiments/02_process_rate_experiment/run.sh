#!/bin/sh

# Description: 
# Get the trajectories for various experiment rates.

PROJECT_HOME=/home/raoul/vio-thesis
EXPERIMENT_HOME=$PROJECT_HOME/experiments/02_process_rate_experiment

echo "===================="
echo " Running experiment"
echo "===================="

FIRST=0.1
STEP=0.1
LAST=6.0

cd $PROJECT_HOME/test
rm rovio.launch
cp $PROJECT_HOME/rovio_template.launch ./rovio.launch
mkdir $EXPERIMENT_HOME/results

for rate in $(seq $FIRST $STEP $LAST) 
do
    echo "Rate: $rate"
    roslaunch rovio.launch PROCESS_RATE:=$rate PROJECT_HOME:=$PROJECT_HOME EXPERIMENT_HOME:=$EXPERIMENT_HOME
done

echo "======================="
echo " Finished..."
echo "======================="