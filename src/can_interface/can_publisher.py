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
        # pierwsze 2 bajty odpowiadaja za znak
        if data >= 0:
            sign = ['\x00', '\x01']
        elif data < 0:
            sign = ['\x00', '\x00']
        # nastepne 2 bajty odpowiadaja za znormalizowane wychylenie drazka
        # 0x0000 to stan neutralny
        # 0xC800 (51 200) to max wychylenie
        data = int(abs(data) * 51200) # dostajemy 0-1 a chcemy 0-51200
        bytes = struct.pack('<H', data) # little-endian unsigned short
        data_frame = sign + list(bytes) # znak na poczatku ramki danych
        return bytearray(data_frame)    # ostatecznie dostajemy ramke 4 bajtowa

    def can_publisher(self):
        try:
            self.bus.send(self.frame)
        except can.CanError:
            print("Message NOT sent")
