import os
from ament_index_python.packages import get_package_share_directory
import launch
from launch import LaunchDescription
from launch_ros.actions import Node
def generate_launch_description():
    ld = LaunchDescription()
    config = os.path.join(
        get_package_share_directory('ht_strap_package'),
        'config',
        'params.yaml'
        )
        
    #bagfile = launch.actions.ExecuteProcess(
    #    cmd=['rm', '-rf', '~/INS-GPS-ROS2/imu_strap_data_only',';','.', '~/INS-GPS-ROS2/install/setup.bash', ';','ros2', 'bag', 'record', '-o', '~/INS-GPS-ROS2/imu_strap_data_only', '/ht_nav_imu_data_topic', '/ht_nav_strap_topic'],
    #    prefix = 'xterm -e',
    #    output='screen' 
    #)

    gazebo = launch.actions.ExecuteProcess(
        cmd=['gazebo', '--verbose', '-s', 'libgazebo_ros_factory.so',
            # 'worlds/city_mk5.world'],
        #  'worlds/new_city_2.world'],
         'worlds/empty_mk5.world'],
        output='screen'
    )

    teleop = Node(
        package='ht_strap_package',
        #namespace='my_teleop',
        # executable='teleop_controller',
        # name='teleop_controller',
        executable='teleop_constant',
        name='teleop_constant',
        prefix = 'xterm -e',
        output='screen',        
        remappings=[
            ('cmd_vel', '/kobra_mk5/cmd_vel')
        ]
    )


    data_collector = Node(
        package = 'ht_strap_package',
        name = 'data_collector',
        executable = 'data_collector'
        )

    ld.add_action(gazebo)
    ld.add_action(teleop)
    ld.add_action(data_collector)

    return ld