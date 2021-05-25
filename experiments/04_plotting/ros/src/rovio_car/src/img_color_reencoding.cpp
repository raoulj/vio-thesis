
#include <ros/ros.h>
#include <std_msgs/Image.h>
#include <cv_bridge/cv_bridge.h>


void chatterCallback(const std_msgs::String::ConstPtr& msg)
{
  ROS_INFO("I heard: [%s]", msg->data.c_str());
}

int main(int argc, char **argv)
{
  ros::init(argc, argv, "listener");
  ros::NodeHandle n;
  ros::Subscriber sub = n.subscribe("cam0/color", 1000, chatterCallback);
  ros::Publisher pub = n.advertise<std_messages::Image>("cam0", 1000)
  ros::spin();

  return 0;
}
