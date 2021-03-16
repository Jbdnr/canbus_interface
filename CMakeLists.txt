cmake_minimum_required(VERSION 2.8.3)
project(can_interface)

find_package(catkin REQUIRED COMPONENTS
  rospy
  roslint
  std_msgs
  ackermann_msgs
)

catkin_python_setup()

roslint_python(
  scripts/can_node
  src/${}/)

catkin_package(CATKIN_DEPENDS std_msgs ackermann_msgs)

install(PROGRAMS scripts/can_node slcan.sh port_setup.sh
  DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
)

include_directories(
  ${catkin_INCLUDE_DIRS}
)
