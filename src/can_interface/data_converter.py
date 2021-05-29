import rospy
from ackermann_msgs.msg import AckermannDriveStamped
from std_msgs.msg import Float32
from os.path import dirname, abspath, join
from scipy import interpolate
import pandas as pd


class Converter:

    def __init__(self, file_path, csv_x, csv_y):

        # wczytanie danych z pliku csv
        with open(file_path, 'r') as f:
            lookup_table = pd.read_csv(f)

        # przypisanie funkcji interpolacji do zmiennej
        self.real2norm = interpolate.interp1d(
                                                lookup_table[csv_x],
                                                lookup_table[csv_y],
                                                fill_value='extrapolate',
                                                assume_sorted='false')
        self.norm2real = interpolate.interp1d(
                                                lookup_table[csv_y],
                                                lookup_table[csv_x],
                                                fill_value='extrapolate',
                                                assume_sorted='false')

    def real2norm(self, real_value):
        angle_converted = self.real2norm(real_value)
        return angle_converted

    def norm2real(self, norm_value):
        angle_converted = self.norm2real(norm_value)
        return angle_converted
