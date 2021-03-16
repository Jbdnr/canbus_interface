#!/bin/bash
echo "Hello there, prepare to reinstall Ubuntu"
echo ""
sudo slcand -o -s8 -t hw -S 1000000 /dev/emaks/can_usb
sudo ip link set up slcan0
echo ""
echo "Ubuntu reinstall is now necessary"