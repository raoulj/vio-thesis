## Requirements

The current setup assumes you're on Ubuntu 14.04 for your base station and your sensors are [Raspberry Pi Zero W's with the V2 camera module](https://www.adafruit.com/product/3415) and [9DoF IMU sensor](https://www.adafruit.com/product/2472).

## Base Station Setup

If you're a Mac user like me, you have two options to run this project:
1. VM
2. Dual Boot

I recommend first trying a VirtualBox VM before doing Dual Boot.  Unfortunately, I found that dual booting was necessary because the VM was too slow, and because of this ROS messages would be droppped.

### VM
I absolutely recommend using vagrant to set up your VM.  Use the included Vagrantfile.

### Dual Booting
If you need to set up a dual boot into Linux, check out [this good tutorial](https://www.youtube.com/watch?v=IQIaDO9nR6Y) which got me booting just fine into Ubuntu with MacOS Sierra.  The tutorial-maker's [Bootable Drive Maker](https://github.com/GregoryConrad/BootableDriveMaker) is a handy tool to get a boot on a flash drive. As always, be careful with partitioning!


## Sensor Setup

To add a sensor to the network:

1. Burn [latest Raspian release](https://www.raspberrypi.org/downloads/raspbian/) to your SD.  For this project I used Raspian Stretch.  I recommend [Etcher](https://etcher.io/).
2. If using Etcher, reinsert the SD because it was auto-ejected.  Then run `python init-sensor.py` in the `sensor` directory.

## Datasets
## Computer/Base Station Installation

To configure your computer to run the project:

If you lack a suitable setup for collecting data yourself, you can use [ETH ASL's datasets](https://projects.asl.ethz.ch/datasets/doku.php?id=kmavvisualinertialdatasets) for testing and benchmarking.
