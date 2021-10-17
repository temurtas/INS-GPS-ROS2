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
    listener_node = Node(
        package = 'ht_strap_package',
        name = 'listener',
        executable = 'listener',
    )

    ps_node = Node(
        package = 'ht_strap_package',
        name = 'strap_node',
        executable = 'strap_node',
        parameters = [config]
    )

    gps_talker_node = Node(
        package = 'ht_strap_package',
        name = 'gps_data_publisher_node',
        executable = 'gps_data_publisher_node',
    )

    kalman_ps_node = Node(
        package = 'ht_strap_package',
        name = 'ins_gps_node',
        executable = 'ins_gps_node',
        parameters = [config]
    )

    ps_node2 = Node(
        package = 'ht_strap_package',
        name = 'strap_w_kalman_node',
        executable = 'strap_w_kalman_node',
    )

    talker_node = Node(
        package = 'ht_strap_package',
        name = 'imu_data_publisher_node',
        executable = 'imu_data_publisher_node',
    )



    #ld.add_action(bagfile)
    ld.add_action(listener_node)
    ld.add_action(ps_node)
    ld.add_action(ps_node2)
    ld.add_action(gps_talker_node)
    ld.add_action(kalman_ps_node)
    ld.add_action(talker_node)

    return ld