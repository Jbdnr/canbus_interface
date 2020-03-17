#include "ros/ros.h"
#include "std_msgs/Float32.h"
#include "ackermann_msgs/AckermannDriveStamped.h"
#include <sstream>
#include <std_msgs/String.h>

std_msgs::Float32 msg;
// publikowane
float speed;
float distance;
float steering_angle;
// subskrybowane
float ackermann_angle;
float ackermann_speed;

void ackermanCallback(const ackermann_msgs::AckermannDriveStamped::ConstPtr& msg)
{
  ackermann_angle = -msg->drive.steering_angle;
  ackermann_speed = msg->drive.speed;
}


int main(int argc, char **argv)
{

  ros::init(argc, argv, "can_node");
  ros::NodeHandle n;

  ros::Publisher speed_pub = n.advertise<std_msgs::Float32>("speed", 50);
  ros::Publisher distance_pub = n.advertise<std_msgs::Float32>("distance", 50);
  ros::Publisher angle_pub = n.advertise<std_msgs::Float32>("steering_angle", 50);
  ros::Subscriber ackerman_subscriber = n.subscribe("drive", 1, ackermanCallback);

  ros::Time begin = ros::Time::now();
  ros::Rate rate(10);

  while (ros::ok())
  {
    ros::Time now = ros::Time::now();
    
    //send speed to msg
    std_msgs::Float32 speed_msg;
    speed = ackermann_speed; //test
    speed_msg.data = speed;

    //send distance to msg
    std_msgs::Float32 distance_msg;
    distance = 21.37; //test
    distance_msg.data = distance;

    //send angle to msg
    std_msgs::Float32 angle_msg;
    steering_angle = ackermann_angle; //test
    angle_msg.data = steering_angle;

    //publishing msg
    speed_pub.publish(speed_msg);
    distance_pub.publish(distance_msg);
    angle_pub.publish(angle_msg);

    ros::spinOnce();
    rate.sleep();
  }
}
