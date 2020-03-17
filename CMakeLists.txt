cmake_minimum_required(VERSION 2.8.3)
project(can_interface)
add_compile_options(-std=c++11)

find_package(catkin REQUIRED COMPONENTS
  roscpp
  std_msgs
  ackermann_msgs
)

catkin_package(
  INCLUDE_DIRS include
)

include_directories(
  include
  ${catkin_INCLUDE_DIRS}
)


add_executable(can_node src/can_node.cpp )
target_link_libraries(can_node ${catkin_LIBRARIES})
