cmake_minimum_required(VERSION 2.8.3)
project(can_interface)

find_package(catkin REQUIRED COMPONENTS
  rospy
  roslint
  std_msgs
  ackermann_msgs
)

catkin_package(
  std_msgs
  ackermann_msgs
)

roslint_python(scripts/can_node)

include_directories(
  ${catkin_INCLUDE_DIRS}
)
