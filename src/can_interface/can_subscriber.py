from __future__ import print_function
import can
import threading
import struct
import numpy

class CanSubscriber:

    bus = can.interface.Bus(bustype='socketcan', channel='vcan0', bitrate=250000)
    stop_event = threading.Event()

    def __init__(self, speed_frame_id, angle_frame_id, distance_frame_id):
        self.speed_frame_id = speed_frame_id
        self.angle_frame_id = angle_frame_id
        self.distance_frame_id = distance_frame_id
        self.received_speed = 0.0
        self.received_distance = 0.0
        self.received_angle = 0.0

    def receive(self, bus, stop_event):
        print("Start receiving can_frames")
        while not stop_event.is_set():
            recv_frame = bus.recv(1)
            if recv_frame is not None:
                recv_id = recv_frame.arbitration_id
                if recv_id == int(str(self.speed_frame_id), 0):
                    # print("Otrzymano dane predkosci")
                    self.received_speed = numpy.float64(struct.unpack('>d', recv_frame.data))
                elif recv_id == int(str(self.distance_frame_id), 0):
                    # print("Otrzymano dane dystansu")
                    self.received_distance = numpy.float64(struct.unpack('>d', recv_frame.data))
                elif recv_id == int(str(self.angle_frame_id), 0):
                    # print("Otrzymano dane kata skretu")
                    self.received_angle = numpy.float64(struct.unpack('>d', recv_frame.data))
                # else:
                #     print("Otrzymano nieznane dane")
                #     print(recv_id)
        print("Stopped receiving can_frames")

    def can_subscriber(self):
        t_receive = threading.Thread(target=self.receive, args=(self.bus, self.stop_event))
        t_receive.start()
