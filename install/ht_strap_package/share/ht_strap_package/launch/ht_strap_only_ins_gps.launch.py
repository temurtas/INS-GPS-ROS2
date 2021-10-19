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

    #ld.add_action(bagfile)
    ld.add_action(ps_node2)
    ld.add_action(kalman_ps_node)

    return ld