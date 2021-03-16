# CAN Interface
CAN Interface package provides integration between ROS and CAN bus.

## CAN Node
`can_node` is a python script which implements bidirectional translation between ROS Topics and CAN frames.

### Subscribed topics
- `/drive` ([ackermann_msgs/AckermannDriveStamped](http://docs.ros.org/api/ackermann_msgs/html/msg/AckermannDriveStamped.html)) This topic contains speed and steering angle data. The data is used to control vehicle.

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

You have to install newest verion of `python-can` manually:

```
pip install python-can
```

### Testing
You can test functionality of this package by using virtual interface.
First you need to bring it up by using following commands:
```
sudo modprobe vcan
sudo ip link add dev vcan0 type vcan
sudo ip link set up vcan0
```
Then you can run python node:
```
rosrun can_interface can_node
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

### canplayer
```
canplayer vcan0=slcan0 -v -I name.log
```
### Linux static port
Execute following script to configure static port:
```
./port_setup.sh
```
### slcan
Plug in USB device and then:
```
ls /dev
sudo slcand -o -s8 -t hw -S 1000000 /dev/ttyACM8
sudo ip link set up slcan0
```
Alternatively, with linux static port setup you can execute following script:
```
./slcan.sh
```
## Diagnostic tools
```
candump slcan0,B1D:F00
cansniffer slcan0
```
If you run into error `sendto: No buffer space available` just type:
```
sudo ifconfig slcan0 txqueuelen 1000

```
## Additional Information
- https://elinux.org/Bringing_CAN_interface_up
- https://sgframework.readthedocs.io/en/latest/cantutorial.html
- https://python-can.readthedocs.io/en/master/
- https://msadowski.github.io/linux-static-port/
