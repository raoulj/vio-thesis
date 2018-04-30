
# If they are just sensors, we don't need to build ROVIO
catkin build --cmake-args -DCMAKE_BUILD_TYPE=Release -DCATKIN_BLACKLIST_PACKAGES="rovio"

export ROS_MASTER_URI=http://192.168.0.136:11311/
export ROS_IP=full_ip
export ROS_HOSTNAME=full_ip