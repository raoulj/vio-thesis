#!/usr/bin/env python

import logging
import rospy
from sensor_msgs.msg import Image
import cv2
from cv_bridge import CvBridge, CvBridgeError
import copy

class image_converter:
    def __init__(self, source, drain):
        self.sub = rospy.Subscriber(source, Image, self.convert_image)
        self.pub = rospy.Publisher(drain, Image, queue_size = 10)

        self.bridge = CvBridge()

    def convert_image(self, color_ros_image):
        original_header = copy.copy(color_ros_image.header)
        try:
            color_cv_image = self.bridge.imgmsg_to_cv2(color_ros_image, "bgr8")
            gray_cv_image = cv2.cvtColor(color_cv_image, cv2.COLOR_BGR2GRAY)
            grayscale_image = self.bridge.cv2_to_imgmsg(gray_cv_image, "mono8")
            
            grayscale_image.header = original_header

            self.pub.publish(grayscale_image)
        except CvBridgeError as e:
            print(e)
        
        

if __name__ == '__main__':
    # ROS Setup
    rospy.init_node('image_color_converter', anonymous=True)
    
    from_topic = rospy.get_param('~from_topic')
    to_topic = rospy.get_param('~to_topic')
    ic = image_converter(from_topic, to_topic)

    try:
        rospy.spin()
    except KeyboardInterrupt:
        print('Shutting Down')

    rospy.spin()

