from __future__ import print_function
import can
import threading
import struct
import numpy
import binascii
import sys


class CanSubscriber:

    stop_event = threading.Event()
    MAX_DRIVE_MOTOR_SPEED = 600  # RPM (max 1000)
    MAX_STEERING_MOTOR_POSITION = 370  # impulsy
    DISTANCE_MECH_CONST = 0.0180963046
    MAX_DISTANCE = DISTANCE_MECH_CONST * 2147483647
    MIN_DISTANCE = DISTANCE_MECH_CONST * (-2147483648)

    def __init__(self, drive_motor_frame_id, steering_motor_frame_id, bustype, channel, bitrate):
        self.drive_motor_frame_id = drive_motor_frame_id
        self.steering_motor_frame_id = steering_motor_frame_id
        self.drive_motor_speed = 0.0
        self.drive_motor_position = 0.0
        self.steering_motor_speed = 0.0
        self.steering_motor_position = 0.0
        self.bus = can.interface.Bus(bustype=bustype, channel=channel, bitrate=bitrate)

    def receive(self, bus, stop_event):
        print("Start receiving can_frames")
        while not stop_event.is_set():
            recv_frame = bus.recv(1)
            if recv_frame is not None:
                recv_id = recv_frame.arbitration_id

                if recv_id == int(str(self.drive_motor_frame_id), 0):
                    # self.drive_motor_speed = - float(numpy.int32(struct.unpack('<I', recv_frame.data[0:4])))\
                    # / self.MAX_DRIVE_MOTOR_SPEED
                    self.drive_motor_position = - numpy.int32(struct.unpack('<I', recv_frame.data[4:8]))\
                        * self.DISTANCE_MECH_CONST

                elif recv_id == int(str(self.steering_motor_frame_id), 0):
                    # self.steering_motor_speed = numpy.uint32(struct.unpack('<I', recv_frame.data[0:4]))
                    self.steering_motor_position = float(numpy.int32(struct.unpack('<I', recv_frame.data[4:8])))\
                        / self.MAX_STEERING_MOTOR_POSITION

        print("Stopped receiving can_frames")

    def can_subscriber(self):
        t_receive = threading.Thread(target=self.receive, args=(self.bus, self.stop_event))
        t_receive.start()
