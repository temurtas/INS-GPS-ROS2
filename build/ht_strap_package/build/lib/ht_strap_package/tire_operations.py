# We need install numpy in order to import it
import numpy as np
import math
import ht_strap_package.config as config

from ht_strap_package.strap_operations import euler2cbn, earth_rate_calc, craft_rate_calc, cbn2euler


def steering2Cwb(steer_ang):
    wheel_euler = np.zeros((3,1))

    c_wb = np.zeros((3, 3))

    wheel_euler[0] = 0.0
    wheel_euler[1] = 0.0
    wheel_euler[2] = steer_ang

    c_wb = euler2cbn(wheel_euler)

    return c_wb

def wheel_lever_arm_calc(x_len, y_len, z_len):
    r_wb = np.zeros((3,1))
    
    r_wb[0] = x_len
    r_wb[1] = y_len
    r_wb[2] = z_len

    return r_wb

def yaw_rate_calc(delta_ang, pos, vel, euler):
    DELTA_T = config.delta_t

    w_ib_b = np.zeros((3,1))
    w_ib_n = np.zeros((3,1))
    w_ie_n = np.zeros((3,1))
    w_en_n = np.zeros((3,1))
    w_nb_n = np.zeros((3,1))
    w_in_n = np.zeros((3,1))

    c_bn = np.zeros((3, 3))

    w_ib_b = delta_ang * DELTA_T

    c_bn = euler2cbn(euler)
    w_ib_n = np.dot(c_bn , w_ib_b)
    w_ie_n = earth_rate_calc(pos)
    w_en_n = craft_rate_calc(vel, pos)
    
    w_in_n = w_ie_n + w_en_n
    w_nb_n = w_ib_n - w_in_n

    yaw_rate = w_nb_n[2]
    
    return yaw_rate


def body2wheels(delta_ang, pos, v_eb_n, euler, steer_ip):
    DELTA_T = config.delta_t
    rh = config.vehicle_rear_half_m              
    fh = config.vehicle_front_half_m            
    wl = config.vehicle_width_m       

    r_bt1_n = np.zeros((3,1))
    r_bt2_n = np.zeros((3,1))
    r_bt3_n = np.zeros((3,1))
    r_bt4_n = np.zeros((3,1))
    
    w_ib_b = np.zeros((3,1))
    w_ib_n = np.zeros((3,1))
    w_ie_n = np.zeros((3,1))
    w_eb_n = np.zeros((3,1))

    temp_vel_t1 = np.zeros((3,1))
    temp_vel_t2 = np.zeros((3,1))
    temp_vel_t3 = np.zeros((3,1))
    temp_vel_t4 = np.zeros((3,1))

    v_et1_n = np.zeros((3,1))
    v_et2_n = np.zeros((3,1))
    v_et3_n = np.zeros((3,1))
    v_et4_n = np.zeros((3,1))

    v_et = np.zeros((3,8))

    c_bn = np.zeros((3, 3))
    c_nb = np.zeros((3, 3))

    C_t1_b = np.zeros((3, 3))
    C_t2_b = np.zeros((3, 3))
    C_t3_b = np.zeros((3, 3))
    C_t4_b = np.zeros((3, 3))

    C_b_t1 = np.zeros((3, 3))
    C_b_t2 = np.zeros((3, 3))
    C_b_t3 = np.zeros((3, 3))
    C_b_t4 = np.zeros((3, 3))

    C_t1_b = steering2Cwb(steer_ip[0])
    C_t2_b = steering2Cwb(steer_ip[1])
    C_t3_b = steering2Cwb(steer_ip[2])
    C_t4_b = steering2Cwb(steer_ip[3])    

    C_b_t1 = C_t1_b.transpose()
    C_b_t2 = C_t2_b.transpose()
    C_b_t3 = C_t3_b.transpose()
    C_b_t4 = C_t4_b.transpose()

    r_bt1_b = wheel_lever_arm_calc(fh,  -wl/2, 0)
    r_bt2_b = wheel_lever_arm_calc(fh,   wl/2, 0)
    r_bt3_b = wheel_lever_arm_calc(-rh, -wl/2, 0)
    r_bt4_b = wheel_lever_arm_calc(-rh,  wl/2, 0)

    w_ib_b = delta_ang * DELTA_T

    c_bn = euler2cbn(euler)

    c_nb = c_bn.transpose()
    
    w_ib_n = np.dot(c_bn , w_ib_b)
    w_ie_n = earth_rate_calc(pos)
    w_eb_n = w_ib_n - w_ie_n

    r_bt1_n = np.dot(c_bn , r_bt1_b)
    r_bt2_n = np.dot(c_bn , r_bt2_b)
    r_bt3_n = np.dot(c_bn , r_bt3_b)
    r_bt4_n = np.dot(c_bn , r_bt4_b)

    temp_vel_t1 = np.cross(w_eb_n, r_bt1_n ,axis=0)
    temp_vel_t2 = np.cross(w_eb_n, r_bt2_n ,axis=0)
    temp_vel_t3 = np.cross(w_eb_n, r_bt3_n ,axis=0)
    temp_vel_t4 = np.cross(w_eb_n, r_bt4_n ,axis=0)

    v_et1_n = v_eb_n + temp_vel_t1
    v_et2_n = v_eb_n + temp_vel_t2
    v_et3_n = v_eb_n + temp_vel_t3
    v_et4_n = v_eb_n + temp_vel_t4

    temp_vel_t1 = np.dot(c_nb, v_et1_n)
    temp_vel_t2 = np.dot(c_nb, v_et2_n)
    temp_vel_t3 = np.dot(c_nb, v_et3_n)
    temp_vel_t4 = np.dot(c_nb, v_et4_n)

    v_et1_t1 =  np.dot(C_b_t1 , temp_vel_t1)
    v_et2_t2 =  np.dot(C_b_t2 , temp_vel_t2)
    v_et3_t3 =  np.dot(C_b_t3 , temp_vel_t3)
    v_et4_t4 =  np.dot(C_b_t4 , temp_vel_t4)

    v_et = np.c_[v_et1_t1, v_et2_t2, v_et3_t3, v_et4_t4, v_et1_n, v_et2_n, v_et3_n, v_et4_n]

    return v_et

def tire_sideslip_angle_calc(v_et_n, euler, steer_ip, yaw_rate):
    DELTA_T = config.delta_t
    rh = config.vehicle_rear_half_m              
    fh = config.vehicle_front_half_m            
    wl = config.vehicle_width_m         

    C_t1_b = np.zeros((3, 3))
    C_t2_b = np.zeros((3, 3))
    C_t3_b = np.zeros((3, 3))
    C_t4_b = np.zeros((3, 3))

    C_t1_n = np.zeros((3, 3))
    C_t2_n = np.zeros((3, 3))
    C_t3_n = np.zeros((3, 3))
    C_t4_n = np.zeros((3, 3))

    euler_w1 = np.zeros((3, 1))
    euler_w2 = np.zeros((3, 1))
    euler_w3 = np.zeros((3, 1))
    euler_w4 = np.zeros((3, 1))
    
    C_t1_b = steering2Cwb(steer_ip[0])
    C_t2_b = steering2Cwb(steer_ip[1])
    C_t3_b = steering2Cwb(steer_ip[2])
    C_t4_b = steering2Cwb(steer_ip[3])    
    
    C_b_n = np.zeros((3, 3))
    C_b_n = euler2cbn(euler)

    C_t1_n = np.dot(C_b_n, C_t1_b)
    C_t2_n = np.dot(C_b_n, C_t2_b)
    C_t3_n = np.dot(C_b_n, C_t3_b)
    C_t4_n = np.dot(C_b_n, C_t4_b)

    euler_w1 =  cbn2euler(C_t1_n)
    euler_w2 =  cbn2euler(C_t2_n)
    euler_w3 =  cbn2euler(C_t3_n)
    euler_w4 =  cbn2euler(C_t4_n)
    
    alpha = np.zeros((4,1))

    v_et1_n = np.zeros((3,1))
    v_et2_n = np.zeros((3,1))
    v_et3_n = np.zeros((3,1))
    v_et4_n = np.zeros((3,1))

    v_et1_n = v_et_n[0:3 , 0]
    v_et2_n = v_et_n[0:3 , 1]
    v_et3_n = v_et_n[0:3 , 2]
    v_et4_n = v_et_n[0:3 , 3]

    # yaw_rate = (v_et4_n[2] - v_et3_n[2])/wl

    alpha_t1 = euler_w1[2] - math.atan2(v_et1_n[1] + fh * yaw_rate, v_et1_n[0] - wl/2 * yaw_rate)
    alpha_t2 = euler_w2[2] - math.atan2(v_et2_n[1] + fh * yaw_rate, v_et2_n[0] + wl/2 * yaw_rate)
    alpha_t3 = euler_w3[2] - math.atan2(v_et3_n[1] + rh * yaw_rate, v_et3_n[0] - wl/2 * yaw_rate)
    alpha_t4 = euler_w4[2] - math.atan2(v_et4_n[1] + rh * yaw_rate, v_et4_n[0] + wl/2 * yaw_rate)

    alpha = np.concatenate((alpha_t1, alpha_t2, alpha_t3, alpha_t4), axis = 0)

    return alpha

def longitudinal_tire_slip_calc(w_tk, v_tk_x):
    R_0 = config.R_0

    # to-do eff_radius_calc()
    R_eff = R_0

    if ( math.fabs(v_tk_x) > math.fabs(R_eff*w_tk) ):   # During Braking
        sigma_x = (math.fabs(R_eff * w_tk) - math.fabs(v_tk_x)) / math.fabs(v_tk_x)
    else:
        sigma_x = (math.fabs(R_eff * w_tk) - math.fabs(v_tk_x)) / math.fabs(R_eff * w_tk)

    return sigma_x

 

