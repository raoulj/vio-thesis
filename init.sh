echo "====================="
echo " Increase Swap Space"
echo "====================="

swapsize=4000

# does the swap file already exist?
grep -q "swapfile" /etc/fstab

# if not then create it
if [ $? -ne 0 ]; then
  echo 'swapfile not found. Adding swapfile.'
  fallocate -l ${swapsize}M /swapfile
  chmod 600 /swapfile
  mkswap /swapfile
  swapon /swapfile
  echo '/swapfile none swap defaults 0 0' >> /etc/fstab
else
  echo 'swapfile found. No changes made.'
fi

echo "Updated swap size to $swapsize"

echo "============"
echo " Intall ROS"
echo "============"
sudo sh -c 'echo "deb http://packages.ros.org/ros/ubuntu $(lsb_release -sc) main" > /etc/apt/sources.list.d/ros-latest.list'
sudo apt-key adv --keyserver hkp://ha.pool.sks-keyservers.net:80 --recv-key 421C365BD9FF1F717815A3895523BAEEB01FA116# sudo apt-get install ros-kinetic-desktop-full
sudo apt-get update
sudo apt-get install ros-indigo-desktop-full

echo "======================"
echo " Installing catkin..."
echo "======================"

sudo apt-get update
sudo apt-get --yes --force-yes install python-catkin-tools

echo "========================="
echo " Setting up workspace..."
echo "========================="

mkdir test
cd test
catkin init
source /opt/ros/indigo/setup.bash
mkdir src

echo "====================="
echo " Installing ROVIO..."
echo "====================="
cd src
git clone https://github.com/ethz-asl/rovio.git > /dev/null
cd rovio
sudo add-apt-repository ppa:ethz-asl/common
sudo apt-get update
sudo apt-get install ros-indigo-kindr-*
git submodule update --init --recursive
cd ../../..
pwd

echo "=================================="
echo " Installing trajectory_toolkit..."
echo "=================================="
cd test/src
git clone https://github.com/ethz-asl/trajectory_toolkit.git

echo "================="
echo " Build Workspace"
echo "================="
cd ..
catkin build --cmake-args -DCMAKE_BUILD_TYPE=Release
source devel/setup.bash

echo "======================="
echo " Pull in launch script"
echo "======================="
wget -nc https://raw.githubusercontent.com/raoulj/vslam_evaluation/master/launch/rovio.launch
roslaunch -v rovio.launch


echo "======================="
echo " View how we did..."
echo "======================="
python plot.py


