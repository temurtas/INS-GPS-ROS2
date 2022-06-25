# We need install numpy in order to import it
import numpy as np
from ht_strap_package.strap_tf_operations import *
from ht_strap_package.strap_operations import pos_update, vel_update, quaternion_update
from ht_nav_variables.msg import HtNavTireOut, HtNavStrapOut
from ht_nav_variables.msg import HtNavVehicleDebug, HtNavWheelVector
import ht_strap_package.config as config
from ht_strap_package.tire_operations_cartesian import *

# def tire_force_calc_old(strap_data, imu_data, joint_state):
#     DELTA_T = config.delta_t
#     rh = config.vehicle_rear_half_m              
#     fh = config.vehicle_front_half_m            
#     wl = config.vehicle_width_m     
#     R_0 = config.R_0
#     R_eff = R_0
#     vehicle_mass = config.vehicle_mass

#     # Convert your custom variable types (float) to np variables (float) 
#     vel_diff = np.zeros((3, 1))
#     vel_diff[0] = imu_data.vel_diff.x
#     vel_diff[1] = imu_data.vel_diff.y
#     vel_diff[2] = imu_data.vel_diff.z

#     ang_diff = np.zeros((3, 1))
#     ang_diff[0] = imu_data.ang_diff.x
#     ang_diff[1] = imu_data.ang_diff.y
#     ang_diff[2] = imu_data.ang_diff.z

#     quaternion = np.zeros((4, 1))
#     quaternion[0] = strap_data.quaternion.x
#     quaternion[1] = strap_data.quaternion.y
#     quaternion[2] = strap_data.quaternion.z
#     quaternion[3] = strap_data.quaternion.w

#     euler = quaternion2euler(quaternion)

#     vel = np.zeros((3, 1))
#     vel[0] = strap_data.vel.x
#     vel[1] = strap_data.vel.y
#     vel[2] = strap_data.vel.z

#     pos = np.zeros((3, 1))
#     pos[0] = strap_data.pos.x
#     pos[1] = strap_data.pos.y
#     pos[2] = strap_data.pos.z

#     steer_angs = np.zeros((4, 1))
#     steer_angs[0] = joint_state.steering_angle.w1
#     steer_angs[1] = joint_state.steering_angle.w2
#     steer_angs[2] = joint_state.steering_angle.w3
#     steer_angs[3] = joint_state.steering_angle.w4

#     wheel_rots = np.zeros((4, 1))
#     wheel_rots[0] = joint_state.wheel_rotation.w1
#     wheel_rots[1] = joint_state.wheel_rotation.w2
#     wheel_rots[2] = joint_state.wheel_rotation.w3
#     wheel_rots[3] = joint_state.wheel_rotation.w4

#     v_et = np.zeros((3,8))
#     v_et_n = np.zeros((3,4))

#     v_et = body2wheels(ang_diff, pos, vel, euler, steer_angs)
    
#     v_et1 = np.zeros((3,1))
#     v_et2 = np.zeros((3,1))
#     v_et3 = np.zeros((3,1))
#     v_et4 = np.zeros((3,1))

#     v_et1 = v_et[0:3, 0]
#     v_et2 = v_et[0:3, 1]
#     v_et3 = v_et[0:3, 2]
#     v_et4 = v_et[0:3, 3]

#     v_et1_n = np.zeros((3,1))
#     v_et2_n = np.zeros((3,1))
#     v_et3_n = np.zeros((3,1))
#     v_et4_n = np.zeros((3,1))

#     v_et1_n = v_et[0:3, 4]
#     v_et2_n = v_et[0:3, 5]
#     v_et3_n = v_et[0:3, 6]
#     v_et4_n = v_et[0:3, 7]

#     v_et_n = np.c_[v_et1_n, v_et2_n, v_et3_n, v_et4_n]

#     alpha = np.zeros((4,1))
#     sigma = np.zeros((4,1))

#     yaw_rate = yaw_rate_calc(ang_diff, pos, vel, euler)
#     yaw_rate = 0.0
#     alpha = tire_sideslip_angle_calc_old(v_et_n, euler, steer_angs, yaw_rate)

#     sigma[0] = longitudinal_tire_slip_calc(wheel_rots[0], v_et1[0])
#     sigma[1] = longitudinal_tire_slip_calc(wheel_rots[1], v_et2[0])
#     sigma[2] = longitudinal_tire_slip_calc(wheel_rots[2], v_et3[0])
#     sigma[3] = longitudinal_tire_slip_calc(wheel_rots[3], v_et4[0])


#     F_z = 1326.0/4 * 9.81
#     mu = 0.7; # Dry Asphalt %http://hyperphysics.phy-astr.gsu.edu/
#     C_sigma = 1.98e5
#     C_alpha = 1.56e5
#     F_x_t = np.zeros((4,1))
#     F_y_t = np.zeros((4,1))

#     for i in range(4):
#         lambda_temp = (mu * F_z * (1 + sigma[i])) / (2 * np.sqrt( np.power(C_sigma * sigma[i],2) + np.power(C_alpha * np.tan(alpha[i]),2) ) )
#         if lambda_temp >= 1:
#             f_lambda = 1
#         else:
#             f_lambda = (2 - lambda_temp)*lambda_temp
#         F_x_t[i] = C_sigma * sigma[i] / (1 + sigma[i]) * f_lambda
#         F_y_t[i] = C_alpha * np.tan(alpha[i]) / (1 + sigma[i]) * f_lambda

#     # Convert your np variables (float) to custom variable types (float)
#     tire_out = HtNavTireOut()
    
#     tire_out.effective_radius_est             = float(R_eff)
#     tire_out.vehicle_mass_est                 = float(vehicle_mass)

#     tire_out.wheel_side_slip_ang.w1           = float(alpha[0])
#     tire_out.wheel_side_slip_ang.w2           = float(alpha[1])
#     tire_out.wheel_side_slip_ang.w3           = float(alpha[2])
#     tire_out.wheel_side_slip_ang.w4           = float(alpha[3])

#     tire_out.wheel_longitudinal_slip_ratio.w1 = float(sigma[0])
#     tire_out.wheel_longitudinal_slip_ratio.w2 = float(sigma[1])
#     tire_out.wheel_longitudinal_slip_ratio.w3 = float(sigma[2])
#     tire_out.wheel_longitudinal_slip_ratio.w4 = float(sigma[3])

#     tire_out.tire_lateral_forces.w1           = float(F_y_t[0])
#     tire_out.tire_lateral_forces.w2           = float(F_y_t[1])
#     tire_out.tire_lateral_forces.w3           = float(F_y_t[2])
#     tire_out.tire_lateral_forces.w4           = float(F_y_t[3])

#     tire_out.tire_longitudinal_forces.w1      = float(F_x_t[0])
#     tire_out.tire_longitudinal_forces.w2      = float(F_x_t[1])
#     tire_out.tire_longitudinal_forces.w3      = float(F_x_t[2])
#     tire_out.tire_longitudinal_forces.w4      = float(F_x_t[3])

#     return tire_out
    
def tire_force_calc(strap_data, imu_data, joint_state):
    DELTA_T = config.delta_t
    rh = config.vehicle_rear_half_m              
    fh = config.vehicle_front_half_m            
    wl = config.vehicle_width_m     

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

    # Create lever-arms and rotation matrices
    r_bt1_n = np.zeros((3,1))
    r_bt2_n = np.zeros((3,1))
    r_bt3_n = np.zeros((3,1))
    r_bt4_n = np.zeros((3,1))

    C_t1_b = np.zeros((3, 3))
    C_t2_b = np.zeros((3, 3))
    C_t3_b = np.zeros((3, 3))
    C_t4_b = np.zeros((3, 3))

    C_b_t1 = np.zeros((3, 3))
    C_b_t2 = np.zeros((3, 3))
    C_b_t3 = np.zeros((3, 3))
    C_b_t4 = np.zeros((3, 3))

    C_t1_b = steering2Cwb(steer_angs[0])
    C_t2_b = steering2Cwb(steer_angs[1])
    C_t3_b = steering2Cwb(steer_angs[2])
    C_t4_b = steering2Cwb(steer_angs[3])    

    C_b_t1 = C_t1_b.transpose()
    C_b_t2 = C_t2_b.transpose()
    C_b_t3 = C_t3_b.transpose()
    C_b_t4 = C_t4_b.transpose()

    r_bt1_b = wheel_lever_arm_calc(fh,  -wl/2, 0)
    r_bt2_b = wheel_lever_arm_calc(fh,   wl/2, 0)
    r_bt3_b = wheel_lever_arm_calc(-rh, -wl/2, 0)
    r_bt4_b = wheel_lever_arm_calc(-rh,  wl/2, 0)

    # Transfer navigation solution to wheel base
    v_et1 = np.zeros((3,1))
    v_et2 = np.zeros((3,1))
    v_et3 = np.zeros((3,1))
    v_et4 = np.zeros((3,1))

    fl_wheel_pva = HtNavStrapOut()
    fl_wheel_pva = tire_pva_calc(ang_diff, pos, vel, euler, C_t1_b, r_bt1_b)
    v_et1 = nav2wheels(euler, C_t1_b, fl_wheel_pva)

    fr_wheel_pva = HtNavStrapOut()
    fr_wheel_pva = tire_pva_calc(ang_diff, pos, vel, euler, C_t2_b, r_bt2_b)
    v_et2 = nav2wheels(euler, C_t2_b, fr_wheel_pva)

    rl_wheel_pva = HtNavStrapOut()
    rl_wheel_pva = tire_pva_calc(ang_diff, pos, vel, euler, C_t3_b, r_bt3_b)
    v_et3 = nav2wheels(euler, C_t3_b, rl_wheel_pva)

    rr_wheel_pva = HtNavStrapOut()
    rr_wheel_pva = tire_pva_calc(ang_diff, pos, vel, euler, C_t4_b, r_bt4_b)
    v_et4 = nav2wheels(euler, C_t4_b, rr_wheel_pva)

    tire_debug = HtNavVehicleDebug()

    # float64       time
    # HtNavTireOut  wheel_variables
    # HtNavStrapOut imu_link_pva
    # HtNavStrapOut fl_wheel_pva
    # HtNavStrapOut fr_wheel_pva
    # HtNavStrapOut rl_wheel_pva
    # HtNavStrapOut rr_wheel_pva

    tire_debug.fl_wheel_pva = fl_wheel_pva
    tire_debug.fr_wheel_pva = fr_wheel_pva
    tire_debug.rl_wheel_pva = rl_wheel_pva
    tire_debug.rr_wheel_pva = rr_wheel_pva

    # Calculate Slip ratio and Slip Angles     
    alpha_t = HtNavWheelVector()
    sigma_t = HtNavWheelVector()

    yaw_rate = yaw_rate_calc(ang_diff, pos, vel, euler)
    yaw_rate = 0.0
    alpha_t = tire_sideslip_angle_calc(tire_debug)

    sigma_t.w1 = float(longitudinal_tire_slip_calc(wheel_rots[0], v_et1[0]))
    sigma_t.w2 = float(longitudinal_tire_slip_calc(wheel_rots[1], v_et2[0]))
    sigma_t.w3 = float(longitudinal_tire_slip_calc(wheel_rots[2], v_et3[0]))
    sigma_t.w4 = float(longitudinal_tire_slip_calc(wheel_rots[3], v_et4[0]))

    # Calculate Tire Forces
    tire_out = HtNavTireOut()
    tire_out = tire_dugoff_force_calc(alpha_t, sigma_t)
    
    # float64          effective_radius_est
    # float64          vehicle_mass_est
    # HtNavWheelVector wheel_side_slip_ang
    # HtNavWheelVector wheel_longitudinal_slip_ratio
    # HtNavWheelVector tire_lateral_forces
    # HtNavWheelVector tire_longitudinal_forces

    tire_debug.wheel_variables = tire_out

    return tire_debug
