# We need install numpy in order to import it
import numpy as np
from ht_strap_package.strap_operations import pos_update, vel_update, quaternion_update, quaternion2euler
from ht_nav_variables.msg import HtNavTireOut
import ht_strap_package.config as config
from ht_strap_package.tire_operations import body2wheels, tire_sideslip_angle_calc, longitudinal_tire_slip_calc

def tire_force_calc(strap_data, imu_data, joint_state):
    DELTA_T = config.delta_t
    rh = config.vehicle_rear_half_m              
    fh = config.vehicle_front_half_m            
    wl = config.vehicle_width_m     
    R_0 = config.R_0
    R_eff = R_0
    vehicle_mass = config.vehicle_mass

    # Convert your custom variable types (float) to np variables (float) 
    vel_diff = np.zeros((3, 1))
    vel_diff[0] = imu_data.vel_diff.x
    vel_diff[1] = imu_data.vel_diff.y
    vel_diff[2] = imu_data.vel_diff.z

    ang_diff = np.zeros((3, 1))
    ang_diff[0] = imu_data.ang_diff.x
    ang_diff[1] = imu_data.ang_diff.y
    ang_diff[2] = imu_data.ang_diff.z

    quaternion = np.zeros((4, 1))
    quaternion[0] = strap_data.quaternion.x
    quaternion[1] = strap_data.quaternion.y
    quaternion[2] = strap_data.quaternion.z
    quaternion[3] = strap_data.quaternion.w

    euler = quaternion2euler(quaternion)

    vel = np.zeros((3, 1))
    vel[0] = strap_data.vel.x
    vel[1] = strap_data.vel.y
    vel[2] = strap_data.vel.z

    pos = np.zeros((3, 1))
    pos[0] = strap_data.pos.x
    pos[1] = strap_data.pos.y
    pos[2] = strap_data.pos.z

    steer_angs = np.zeros((4, 1))
    steer_angs[0] = joint_state.steering_angle.w1
    steer_angs[1] = joint_state.steering_angle.w2
    steer_angs[2] = joint_state.steering_angle.w3
    steer_angs[3] = joint_state.steering_angle.w4

    wheel_rots = np.zeros((4, 1))
    wheel_rots[0] = joint_state.wheel_rotation.w1
    wheel_rots[1] = joint_state.wheel_rotation.w2
    wheel_rots[2] = joint_state.wheel_rotation.w3
    wheel_rots[3] = joint_state.wheel_rotation.w4

    v_et = np.zeros((3,4))

    v_et = body2wheels(ang_diff, pos, vel, euler, steer_angs)
    
    v_et1_n = np.zeros((3,1))
    v_et2_n = np.zeros((3,1))
    v_et3_n = np.zeros((3,1))
    v_et4_n = np.zeros((3,1))

    v_et1_n = v_et[0:3, 0]
    v_et2_n = v_et[0:3, 1]
    v_et3_n = v_et[0:3, 2]
    v_et4_n = v_et[0:3, 3]

    alpha = np.zeros((4,1))
    sigma = np.zeros((4,1))

    alpha = tire_sideslip_angle_calc(v_et, euler, steer_angs)

    sigma[0] = longitudinal_tire_slip_calc(wheel_rots[0], v_et1_n[0])
    sigma[1] = longitudinal_tire_slip_calc(wheel_rots[1], v_et2_n[0])
    sigma[2] = longitudinal_tire_slip_calc(wheel_rots[2], v_et3_n[0])
    sigma[3] = longitudinal_tire_slip_calc(wheel_rots[3], v_et4_n[0])


    # Convert your np variables (float) to custom variable types (float)
    tire_out = HtNavTireOut()
    
    tire_out.effective_radius_est             = float(R_eff)
    tire_out.vehicle_mass_est                 = float(vehicle_mass)

    tire_out.wheel_side_slip_ang.w1           = float(alpha[0])
    tire_out.wheel_side_slip_ang.w2           = float(alpha[1])
    tire_out.wheel_side_slip_ang.w3           = float(alpha[2])
    tire_out.wheel_side_slip_ang.w4           = float(alpha[3])

    tire_out.wheel_longitudinal_slip_ratio.w1 = float(sigma[0])
    tire_out.wheel_longitudinal_slip_ratio.w2 = float(sigma[1])
    tire_out.wheel_longitudinal_slip_ratio.w3 = float(sigma[2])
    tire_out.wheel_longitudinal_slip_ratio.w4 = float(sigma[3])

    tire_out.tire_lateral_forces.w1           = float(alpha[0])
    tire_out.tire_lateral_forces.w2           = float(alpha[1])
    tire_out.tire_lateral_forces.w3           = float(alpha[2])
    tire_out.tire_lateral_forces.w4           = float(alpha[3])

    tire_out.tire_longitudinal_forces.w1      = float(sigma[0])
    tire_out.tire_longitudinal_forces.w2      = float(sigma[1])
    tire_out.tire_longitudinal_forces.w3      = float(sigma[2])
    tire_out.tire_longitudinal_forces.w4      = float(sigma[3])
    
    return tire_out
