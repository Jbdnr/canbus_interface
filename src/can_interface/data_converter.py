import rospy
from ackermann_msgs.msg import AckermannDriveStamped
from std_msgs.msg import Float32
from os.path import dirname, abspath, join
from scipy import interpolate
import pandas as pd

class Converter:
    def __init__(self, angle_file_path, angle_ref):
        # Zaladowanie danych .csv do zmiennych
        with open(angle_file_path, 'r') as f:
            angle_lookup_table = pd.read_csv(f)

        self.function_angle_conv = interpolate.interp1d(angle_lookup_table['angle_measured'], angle_lookup_table['angle_ref'], fill_value='extrapolate', assume_sorted='false')
        self.angle_ref = angle_ref

    def angle_converter(self):
        self.angle_coverted = self.function_angle_conv(self.angle_ref)
