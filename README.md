# CAN Interface
CAN Interface package provides integration between ROS and CAN bus.

# CAN Node
`can_node` is a python script which implements bidirectional translation between ROS Topics and CAN frames.

### Subscribed topics
- `/drive` ([ackermann_msgs/AckermannDrive](http://docs.ros.org/api/ackermann_msgs/html/msg/AckermannDrive.html)) This topic contains speed and steering angle data. The data is used to control vehicle.

### Published topics
- `/speed` ([std_msgs/Float64](http://docs.ros.org/melodic/api/std_msgs/html/msg/Float64.html))[10 Hz] Speed feedback received from can bus.
- `/distance` ([std_msgs/Float64](http://docs.ros.org/melodic/api/std_msgs/html/msg/Float64.html))[10 Hz] Distance feedback received from can bus.
- `/steering_angle` ([std_msgs/Float64](http://docs.ros.org/melodic/api/std_msgs/html/msg/Float64.html))[10 Hz] Steering angle feedback received from can bus.

## Getting Started

### Prerequisites
Install required software by typing following command:
```
rosdep install can_interface
```

### Testing
You can test functionality of this package by using virtual interface.
First you need to bring it up by using following commands:
```
sudo modprobe vcan
sudo ip link add dev vcan0 type vcan
sudo ip link set up vcan0
```
##### Sending CAN frames
You can generate CAN frame by using following command:
```
cansend vcan0 31d#11223344AABBCCDD
```
Number before hashtag is frame id.
Number after hashtag is frame data.

##### Receiving CAN frames
You can print all data that is being received by a CAN interface by using following command:
```
candump vcan0
```

##### Monitoring ROS topics
Using [rqt](http://wiki.ros.org/rqt) package is good option to sending and receiving ROS topics.

## Additional Information
- https://elinux.org/Bringing_CAN_interface_up
- https://sgframework.readthedocs.io/en/latest/cantutorial.html
- https://python-can.readthedocs.io/en/master/
