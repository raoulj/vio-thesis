#!/bin/sh
# Description: Install ROS Indigo on a Raspbian Jessie.
# Adapted from installation steps found in:
# http://wiki.ros.org/ROSberryPi/
# ... Installing%20ROS%20Indigo%20on%20Raspberry%20Pi

# 1: prerequisites

# a: add repositories
sudo sh -c 'echo "deb http://packages.ros.org/ros/ubuntu jessie main" > /etc/apt/sources.list.d/ros-latest.list'
wget https://raw.githubusercontent.com/ros/rosdistro/master/ros.key -O - | sudo apt-key add -
sudo apt-get update -y
sudo apt-get upgrade -y

# b: install bootstrap dependencies
sudo apt-get install python-pip python-setuptools python-yaml python-distribute python-docutils python-dateutil python-six
sudo pip install rosdep rosinstall_generator wstool rosinstall
sudo rosdep init
rosdep update

#2: installation
mkdir ~/ros_catkin_ws
cd ~/ros_catkin_ws

# (installing ROS-COMM)
rosinstall_generator ros_comm --rosdistro indigo --deps --wet-only --exclude roslisp --tar > indigo-ros_comm-wet.rosinstall
wstool init src indigo-ros_comm-wet.rosinstall

# dependency resolution
mkdir ~/ros_catkin_ws/external_src
sudo apt-get install checkinstall cmake -y
sudo sh -c 'echo "deb-src http://mirrordirector.raspbian.org/raspbian/ testing main contrib non-free rpi" >> /etc/apt/sources.list'
sudo apt-get update

cd ~/ros_catkin_ws/external_src
sudo apt-get install libboost-filesystem-dev libxml2-dev -y
wget "http://downloads.sourceforge.net/project/collada-dom/"\
    "Collada%20DOM/Collada%20DOM%202.4/collada-dom-2.4.0.tgz"
tar -xzf collada-dom-2.4.0.tgz
cd collada-dom-2.4.0
cmake .
echo "need to change name (choice 2) to 'collada-dom-dev'"
sudo checkinstall make install

cd ~/ros_catkin_ws
rosdep install --from-paths src --ignore-src --rosdistro indigo -y -r --os=debian:jessie

# Build
sudo ./src/catkin/bin/catkin_make_isolated --install -DCMAKE_BUILD_TYPE=Release --install-space /opt/ros/indigo

# 3. post-installation
echo "source /opt/ros/indigo/setup.bash" >> ~/.bashrc
echo "export LC_ALL=C" >> ~/.bashrc
source ~/.bashrc