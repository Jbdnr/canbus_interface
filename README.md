# CAN Interface
CAN Interface package provides integration between ROS and CAN bus.
## Getting Started

### Prerequisites
You need to install following software:
- `sudo apt install ros-melodic-ackermann-msgs`
- `pip install python-can`
- `sudo apt install can-utils`

### Testing
You can test functionality of this package by using virtual interface.
First you need to bring it up by using following commands:
```
sudo modprobe vcan
sudo ip link add dev vcan0 type vcan
sudo ip link set up vcan
```
#### Sending data_frames
You can generate CAN frame by using following command:
-`cansend vcan0 31d#11223344AABBCCDD`
Number before hashtag is frame id.
Number after hashtag is frame data.

#### Receiving data_frames
You can print all data that is being received by a CAN interface by using following command:
-`candump vcan0`

#### Monitoring ROS topics
Using rqt package is good option to sending and receiving ROS topics.

## Subscribed topics
- `/drive`

## Published topics
- `/speed`
- `/distance`
- `/steering_angle`

## Additional Information
- https://elinux.org/Bringing_CAN_interface_up
- https://sgframework.readthedocs.io/en/latest/cantutorial.html
- https://python-can.readthedocs.io/en/master/
