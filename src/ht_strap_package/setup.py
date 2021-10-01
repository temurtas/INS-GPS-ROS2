from setuptools import setup

package_name = 'ht_strap_package'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
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
                'middle_man = ht_strap_package.ht_pub_sub_deneme:main',
                'talker = ht_strap_package.publisher_member_function:main',
                'listener = ht_strap_package.subscriber_member_function:main',
        ],
    },
)
