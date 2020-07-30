from __future__ import print_function
import can
import threading
import struct
import numpy
import binascii


class CanSubscriber:

    stop_event = threading.Event()
    MAX_DRIVE_MOTOR_SPEED = 600  # RPM (max 1000)
    MAX_STEERING_MOTOR_POSITION = 370  # impulsy

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
                    # print("Otrzymano dane z silnika napedowego")
                    drive_motor_speed = int(numpy.uint32(struct.unpack('<I', recv_frame.data[0:4])))
                    if drive_motor_speed > 2147483647:
                        # print("jedzie do przodu")
                        drive_motor_speed = int("FFFFFFFF", 16) - drive_motor_speed
                    else:
                        # print("jedzie do tylu")
                        drive_motor_speed = - drive_motor_speed
                    drive_motor_speed_norm = float(drive_motor_speed) / self.MAX_DRIVE_MOTOR_SPEED
                    self.drive_motor_speed = drive_motor_speed_norm
                    self.drive_motor_position = numpy.uint32(struct.unpack('<I', recv_frame.data[4:8]))  # TODO

                elif recv_id == int(str(self.steering_motor_frame_id), 0):
                    # print("Otrzymano dane z silnika ukladu kierowniczego)
                    self.steering_motor_speed = numpy.uint32(struct.unpack('<I', recv_frame.data[0:4]))  # TODO
                    steering_motor_position = float(numpy.int32(struct.unpack('<I', recv_frame.data[4:8])))
                    if steering_motor_position > 2147483647:
                        print("skreca w prawo")
                        steering_motor_position = int("FFFFFFFF", 16) - steering_motor_position
                    else:
                        print("skreca w lewo")
                        steering_motor_position = - steering_motor_position
                    steering_motor_position_norm = float(steering_motor_position) / self.MAX_STEERING_MOTOR_POSITION
                    self.steering_motor_position = steering_motor_position_norm
                    print(steering_motor_position)
                # else:
                #     print("Otrzymano nieznane dane")
                #     print(recv_id)
        print("Stopped receiving can_frames")

    def can_subscriber(self):
        t_receive = threading.Thread(target=self.receive, args=(self.bus, self.stop_event))
        t_receive.start()
