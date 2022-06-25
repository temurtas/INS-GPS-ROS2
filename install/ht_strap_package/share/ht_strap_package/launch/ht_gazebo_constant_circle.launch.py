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
        # executable='teleop_constant',
        # name='teleop_constant',
        executable='teleop_scn_pub',
        name='teleop_scn_pub',
        prefix = 'xterm -e',
        output='screen',        
        remappings=[
            ('cmd_vel', '/kobra_mk5/cmd_vel')
        ]
    )

    listener_node = Node(
        package = 'ht_strap_package',
        name = 'pseudo_controller',
        executable = 'pseudo_controller',
    )

    # gps_talker_node = Node(
    #     package = 'ht_strap_package',
    #     name = 'gps_data_converter_node',
    #     executable = 'gps_data_converter_node',
    # )

    # ideal_gps_talker_node = Node(
    #     package = 'ht_strap_package',
    #     name = 'ideal_gps_data_converter_node',
    #     executable = 'ideal_gps_data_converter_node',
    # )


    # strap_kalman_ps_node = Node(
    #     package = 'ht_strap_package',
    #     name = 'strap_ins_gps_node',
    #     executable = 'strap_ins_gps_node',
    #     parameters = [config]
    # )

    strap_kalman_cartesian_node = Node(
        package = 'ht_strap_package',
        name = 'strap_ins_gps_cartesian_pv_node',
        executable = 'strap_ins_gps_cartesian_pv_node',
    )

    # talker_node = Node(
    #     package = 'ht_strap_package',
    #     name = 'imu_data_converter_node',
    #     executable = 'imu_data_converter_node',
    # )

    # talker_ideal_node = Node(
    #     package = 'ht_strap_package',
    #     name = 'imu_data_ideal_converter_node',
    #     executable = 'imu_data_ideal_converter_node',
    # )

    # strap_ideal_node =  Node(
    #     package = 'ht_strap_package',
    #     name = 'strap_ideal_node',
    #     executable = 'strap_ideal_node',
    # )

    # strap_onlyins_node =  Node(
    #     package = 'ht_strap_package',
    #     name = 'strap_onlyins_node',
    #     executable = 'strap_onlyins_node',
    # )
    
    # robot_state_listener = Node(
    #     package = 'ht_strap_package',
    #     name = 'robot_state_listener',
    #     executable = 'robot_state_listener'
    #     )

    robot_listener = Node(
        package = 'ht_strap_package',
        name = 'robot_listener',
        executable = 'robot_listener'
        )

    tire_force_calc_node = Node(
        package = 'ht_strap_package',
        name = 'tire_force_calc_node',
        executable = 'tire_force_calc_node'
    )

    data_collector = Node(
        package = 'ht_strap_package',
        name = 'data_collector',
        executable = 'data_collector'
    )

    # ld.add_action(talker_node)
    # ld.add_action(talker_ideal_node)
    # ld.add_action(bagfile)
    # ld.add_action(gps_talker_node)
    # ld.add_action(ideal_gps_talker_node)
    
    ld.add_action(gazebo)
    ld.add_action(teleop)
    ld.add_action(listener_node)
    # ld.add_action(strap_kalman_ps_node)
    # ld.add_action(robot_state_listener)
    ld.add_action(robot_listener)
    ld.add_action(tire_force_calc_node)
    # ld.add_action(strap_ideal_node)
    # ld.add_action(strap_onlyins_node)
    ld.add_action(strap_kalman_cartesian_node)
    ld.add_action(data_collector)

    return ld