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
    maintainer='temurtas',
    maintainer_email='halil.temurtas@gmail.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
                'strap_node = ht_strap_package.ht_pub_sub_deneme:main',
                'imu_data_publisher_node = ht_strap_package.imu_data_publisher_function:main',
                'listener = ht_strap_package.subscriber_member_function:main',
        ],
    },
)
