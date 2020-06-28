from __future__ import print_function
import can
import numpy
import struct

class CanPublisher:

    bus = can.interface.Bus(bustype='socketcan', channel='vcan0', bitrate=250000)

    def __init__(self, frame_id, frame_data):
        self.frame_id = frame_id
        self.frame_data = self.get_pathology_data_frame(frame_data)
        self.frame = can.Message(arbitration_id=self.frame_id, data=self.frame_data)

    def get_pathology_data_frame(self, data):
        if data >= 0:
            sign = ['\x00', '\x01']
        elif data < 0:
            sign = ['\x00', '\x00']
        # TODO normalizacja
        data = int(abs(data))
        # TODO normalizacja
        bytes = struct.pack('>H', data)  # big-endian unsigned short
        data_frame = sign + list(bytes)  # znak na poczatku ramki danych
        return bytearray(data_frame)

    def can_publisher(self):
        try:
            self.bus.send(self.frame)
        except can.CanError:
            print("Message NOT sent")
