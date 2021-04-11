#!/bin/bash
# udevadm info --name=/dev/ttyACMx --attribute-walk
sudo cp udev/99-usb-serial.rules /etc/udev/rules.d/
sudo udevadm control --reload-rules