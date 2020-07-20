## ! DO NOT MANUALLY INVOKE THIS setup.py, USE CATKIN INSTEAD

from distutils.core import setup
from catkin_pkg.python_setup import generate_distutils_setup

# fetch values from package.xml
setup_args = generate_distutils_setup(
    packages=['can_interface'],
    package_dir={'': 'src'},
    # package_data={'': ['data/angle_data.csv', 'data/speed_data.csv']},
    data_files=[('data', ['data/angle_data.csv', 'data/speed_data.csv'])],
)

setup(**setup_args)
