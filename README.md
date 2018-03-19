## Requirements

The current setup assumes you're on MacOS for your base station and your sensors are [Raspberry Pi Zero W's with the V2 camera module](https://www.adafruit.com/product/3415) and [9DoF IMU sensor](https://www.adafruit.com/product/2472).

## Sensor Installation

To add a sensor to the network:

1. Burn [latest Raspian release](https://www.raspberrypi.org/downloads/raspbian/) to your SD.  For this project I used Raspian Stretch.  I recommend [Etcher](https://etcher.io/).
2. If using Etcher, reinsert the SD because it was auto-ejected.  Then run init-sensor.py in the sensor directory.

## Computer/Base Station installation

To configure your computer to run the project:

1. Run `vagrant up` in the computer directory.