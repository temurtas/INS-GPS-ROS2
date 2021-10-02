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
        
    bagfile = launch.actions.ExecuteProcess(
         cmd=['ros2', 'bag', 'record', '-o', 'imu_strap_data_only', '/ht_nav_imu_data_topic', '/ht_nav_strap_topic'],
        output='screen'
    )

    ps_node = Node(
        package = 'ht_strap_package',
        name = 'strap_node',
        executable = 'strap_node',
        parameters = [config]
    )

    talker_node = Node(
        package = 'ht_strap_package',
        name = 'imu_data_publisher_node',
        executable = 'imu_data_publisher_node',
    )

    listener_node = Node(
        package = 'ht_strap_package',
        name = 'listener',
        executable = 'listener',
    )

    ld.add_action(bagfile)
    ld.add_action(ps_node)
    ld.add_action(talker_node)
    ld.add_action(listener_node)

    return ld