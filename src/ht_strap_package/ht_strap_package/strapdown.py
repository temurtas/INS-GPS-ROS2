# We need install numpy in order to import it
import numpy as np

from ht_strap_package.strap_tf_operations import *
from ht_strap_package.strap_operations import pos_update, vel_update, quaternion_update
from ht_nav_variables.msg import HtNavStrapOut

def strapdown(old_strap, imu_data):
    
    # Convert your custom variable types (float) to np variables (float) 
    vel_diff_temp = np.zeros((3, 1))
    vel_diff_temp[0] = imu_data.vel_diff.x
    vel_diff_temp[1] = imu_data.vel_diff.y
    vel_diff_temp[2] = imu_data.vel_diff.z

    ang_diff_temp = np.zeros((3, 1))
    ang_diff_temp[0] = imu_data.ang_diff.x
    ang_diff_temp[1] = imu_data.ang_diff.y
    ang_diff_temp[2] = imu_data.ang_diff.z

    old_quaternion_temp = np.zeros((4, 1))
    old_quaternion_temp[0] = old_strap.quaternion.x
    old_quaternion_temp[1] = old_strap.quaternion.y
    old_quaternion_temp[2] = old_strap.quaternion.z
    old_quaternion_temp[3] = old_strap.quaternion.w

    old_vel_temp = np.zeros((3, 1))
    old_vel_temp[0] = old_strap.vel.x
    old_vel_temp[1] = old_strap.vel.y
    old_vel_temp[2] = old_strap.vel.z

    old_pos_temp = np.zeros((3, 1))
    old_pos_temp[0] = old_strap.pos.x
    old_pos_temp[1] = old_strap.pos.y
    old_pos_temp[2] = old_strap.pos.z

    new_vel_temp = np.zeros((3, 1))
    new_pos_temp = np.zeros((3, 1))
    new_quaternion_temp = np.zeros((4, 1))

    # VELOCITY UPDATE
    new_vel_temp = vel_update(old_vel_temp, vel_diff_temp, old_pos_temp, old_quaternion_temp)

    # POSITION UPDATE
    new_pos_temp = pos_update(new_vel_temp, old_pos_temp)

    # ATTITUDE UPDATE
    new_quaternion_temp = quaternion_update(old_quaternion_temp, ang_diff_temp, new_pos_temp, new_vel_temp)
    new_euler_temp = quaternion2euler(new_quaternion_temp)

    # Convert your np variables (float) to custom variable types (float)
    new_strap = HtNavStrapOut()
    
    new_strap.pos.x = float(new_pos_temp[0])
    new_strap.pos.y = float(new_pos_temp[1])
    new_strap.pos.z = float(new_pos_temp[2])

    new_strap.vel.x = float(new_vel_temp[0])
    new_strap.vel.y = float(new_vel_temp[1])
    new_strap.vel.z = float(new_vel_temp[2])

    new_strap.euler.roll = float(new_euler_temp[0])
    new_strap.euler.pitch = float(new_euler_temp[1])
    new_strap.euler.yaw = float(new_euler_temp[2])

    new_strap.quaternion.x = float(new_quaternion_temp[0])
    new_strap.quaternion.y = float(new_quaternion_temp[1])
    new_strap.quaternion.z = float(new_quaternion_temp[2])
    new_strap.quaternion.w = float(new_quaternion_temp[3])
    
    return new_strap
