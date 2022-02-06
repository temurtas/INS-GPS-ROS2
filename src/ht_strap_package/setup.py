from setuptools import setup
import os
from glob import glob

package_name = 'ht_strap_package'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name, 'launch'), glob('launch/*.launch.py')),
        (os.path.join('share', package_name, 'config'), glob('config/*.yaml'))
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='temur',
    maintainer_email='halil.temur@gmail.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
                'strap_node = ht_strap_package.strap_node_function:main',
                'strap_w_kalman_node = ht_strap_package.strap_with_kalman_node_function:main',
                'imu_data_publisher_node = ht_strap_package.imu_data_publisher_function:main',
                'imu_data_converter_node = ht_strap_package.imu_data_converter_function:main',
                'listener = ht_strap_package.subscriber_member_function:main',
                'pseudo_controller = ht_strap_package.pseudo_controller_function:main',
                'gps_data_publisher_node = ht_strap_package.gps_data_publisher_function:main',
                'gps_data_converter_node = ht_strap_package.gps_data_converter_function:main',
                'ideal_gps_data_converter_node = ht_strap_package.ideal_gps_data_converter_function:main',
                'ins_gps_node = ht_strap_package.ins_gps_node_function:main',
                'strap_ins_gps_node = ht_strap_package.ins_gps_strap_node_function:main',
                'my_teleop = ht_strap_package.my_teleop:main',
                'joint_listener_node = ht_strap_package.joint_message_subscriber_function:main'

        ],
    },
)
