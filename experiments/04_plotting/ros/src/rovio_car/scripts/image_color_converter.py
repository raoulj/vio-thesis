#!/usr/bin/env python

import logging
import rospy
from sensor_msgs.msg import Image
import cv2
from cv_bridge import CvBridge, CvBridgeError

class image_converter:
    def __init__(self):
        self.pub = rospy.Publisher('cam0/image_raw', Image, queue_size = 100)
        self.sub = rospy.Subscriber("colored_cam0", Image, self.convert_image)

        self.bridge = CvBridge()

    def convert_image(self, color_ros_image):
        try:
            color_cv_image = self.bridge.imgmsg_to_cv2(color_ros_image, "bgr8")
            gray_cv_image = cv2.cvtColor(color_cv_image, cv2.COLOR_BGR2GRAY)
            grayscale_image = self.bridge.cv2_to_imgmsg(gray_cv_image, "mono8")
            self.pub.publish(grayscale_image)
        except CvBridgeError as e:
            print(e)
        
        

if __name__ == '__main__':
    # ROS Setup
    ic = image_converter()
    rospy.init_node('image_color_converter', anonymous=True)

    try:
        rospy.spin()
    except KeyboardInterrupt:
        print('Shutting Down')

    rospy.spin()

