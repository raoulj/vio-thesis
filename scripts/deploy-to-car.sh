
# If they are just sensors, we don't need to build ROVIO
catkin build --cmake-args -DCMAKE_BUILD_TYPE=Release -DCATKIN_BLACKLIST_PACKAGES="rovio"