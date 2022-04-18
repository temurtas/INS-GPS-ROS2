# We need install numpy in order to import it
from cmath import pi
import numpy as np
import math
import ht_strap_package.config as config

from ht_strap_package.strap_operations import euler2cbn, earth_rate_calc, craft_rate_calc, cbn2euler, euler_rate_calc, calc_rn_re
from ht_nav_variables.msg import HtNavStrapOut, HtNavWheelVector, HtNavVehicleDebug, HtNavTireOut
from ht_strap_package.config import base_path


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
    w_nb_b = np.zeros((3,1))
    w_in_b = np.zeros((3,1))
    euler_rate = np.zeros((3,1))

    c_bn = np.zeros((3, 3))

    w_ib_b = delta_ang / DELTA_T # rad/sec

    c_bn = euler2cbn(euler)
    w_ib_n = np.dot(c_bn , w_ib_b)
    w_ie_n = earth_rate_calc(pos)
    w_en_n = craft_rate_calc(vel, pos)
    
    w_in_n = w_en_n # w_ie_n + w_en_n
    w_nb_n = w_ib_n - w_in_n

    c_nb = np.transpose(c_bn)
    w_in_b = np.dot(c_nb, w_in_n)

    w_nb_b = w_ib_b - w_in_b

    euler_rate = euler_rate_calc(euler, w_ib_b)
    # euler_rate = euler_rate_calc(euler, w_nb_b)

    yaw_rate = euler_rate[2]
    
    return yaw_rate

def nav2wheels(euler, C_tk_b, tire_pva):
    v_etk_n = np.zeros((3,1)) 
    v_etk_tk = np.zeros((3,1)) 
    C_b_tk = np.zeros((3,3)) 

    c_bn = euler2cbn(euler)
    c_nb = c_bn.transpose()

    C_b_tk = C_tk_b.transpose()

    v_etk_n[0] = tire_pva.vel.x
    v_etk_n[1] = tire_pva.vel.y
    v_etk_n[2] = tire_pva.vel.z
    
    temp_vel_t1 = np.dot(c_nb, v_etk_n)
    v_etk_tk =  np.dot(C_b_tk , temp_vel_t1)

    return v_etk_tk


def body2wheels(delta_ang, pos, v_eb_n, euler, steer_ip):

    # out_data_path = base_path / "debug_wheel_vel.txt"
    # wheel_vel = open(out_data_path, 'a')

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

    w_ib_b = delta_ang / DELTA_T

    c_bn = euler2cbn(euler)

    c_nb = c_bn.transpose()
    
    w_ib_n = np.dot(c_bn , w_ib_b)
    w_ie_n = earth_rate_calc(pos)
    w_eb_n = w_ib_n # - w_ie_n

    r_bt1_n = np.dot(c_bn , r_bt1_b)
    r_bt2_n = np.dot(c_bn , r_bt2_b)
    r_bt3_n = np.dot(c_bn , r_bt3_b)
    r_bt4_n = np.dot(c_bn , r_bt4_b)

    temp_vel_t1 = np.cross(w_eb_n, r_bt1_n ,axis=0)
    temp_vel_t2 = np.cross(w_eb_n, r_bt2_n ,axis=0)
    temp_vel_t3 = np.cross(w_eb_n, r_bt3_n ,axis=0)
    temp_vel_t4 = np.cross(w_eb_n, r_bt4_n ,axis=0)

    # print(str(r_bt1_b[0,0]), str(r_bt1_b[1,0]), str(r_bt1_b[2,0]), str(r_bt2_b[0,0]), str(r_bt2_b[1,0]), str(r_bt2_b[2,0]), str(pos[0,0]), str(pos[1,0]), str(pos[2,0]), sep='\t', file=wheel_vel)
    # print(str(r_bt3_b[0,0]), str(r_bt3_b[1,0]), str(r_bt3_b[2,0]), str(r_bt4_b[0,0]), str(r_bt4_b[1,0]), str(r_bt4_b[2,0]), str(euler[0,0]), str(euler[1,0]), str(euler[2,0]), sep='\t', file=wheel_vel)
    # print(str(w_ib_b[0,0]), str(w_ib_b[1,0]), str(w_ib_b[2,0]), str(w_eb_n[0,0]), str(w_eb_n[1,0]), str(w_eb_n[2,0]), sep='\t', file=wheel_vel)
    # print(str(temp_vel_t1[0,0]), str(temp_vel_t1[1,0]), str(temp_vel_t1[2,0]), str(temp_vel_t2[0,0]), str(temp_vel_t2[1,0]), str(temp_vel_t2[2,0]), sep='\t', file=wheel_vel)
    # print(str(temp_vel_t3[0,0]), str(temp_vel_t3[1,0]), str(temp_vel_t3[2,0]), str(temp_vel_t4[0,0]), str(temp_vel_t4[1,0]), str(temp_vel_t4[2,0]), sep='\t', file=wheel_vel)
    # print(str(v_eb_n[0,0]), str(v_eb_n[1,0]), str(v_eb_n[2,0]), sep='\t', file=wheel_vel)

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

    # print(str(v_et1_t1[0,0]), str(v_et1_t1[1,0]), str(v_et1_t1[2,0]), str(v_et2_t2[0,0]), str(v_et2_t2[1,0]), str(v_et2_t2[2,0]), \
    #     str(v_et3_t3[0,0]), str(v_et3_t3[1,0]), str(v_et3_t3[2,0]), str(v_et4_t4[0,0]), str(v_et4_t4[1,0]), str(v_et4_t4[2,0]), \
    #     str(v_et1_n[0,0]), str(v_et1_n[1,0]), str(v_et1_n[2,0]), str(v_et2_n[0,0]), str(v_et2_n[1,0]), str(v_et2_n[2,0]), \
    #     str(v_et3_n[0,0]), str(v_et3_n[1,0]), str(v_et3_n[2,0]), str(v_et4_n[0,0]), str(v_et4_n[1,0]), str(v_et4_n[2,0]), sep='\t', file=wheel_vel)

    v_et = np.c_[v_et1_t1, v_et2_t2, v_et3_t3, v_et4_t4, v_et1_n, v_et2_n, v_et3_n, v_et4_n]

    return v_et
    

def tire_sideslip_angle_calc_old(v_et_n, euler, steer_ip, yaw_rate):
    DELTA_T = config.delta_t
    rh = config.vehicle_rear_half_m              
    fh = config.vehicle_front_half_m            
    wl = config.vehicle_width_m         

    # out_data_path = base_path / "debug_tire_lin_vel.txt"
    # tire_lin_vel = open(out_data_path, 'a')

    alpha_t = np.zeros((4, 1))

    C_b_t1 = np.zeros((3, 3))
    C_b_t2 = np.zeros((3, 3))
    C_b_t3 = np.zeros((3, 3))
    C_b_t4 = np.zeros((3, 3))

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

    C_b_t1 = C_t1_b.transpose()
    C_b_t2 = C_t2_b.transpose()
    C_b_t3 = C_t3_b.transpose()
    C_b_t4 = C_t4_b.transpose()
    
    C_b_n = np.zeros((3, 3))
    C_b_n = euler2cbn(euler)

    # C_t1_n = np.dot(C_b_n, C_t1_b)
    # C_t2_n = np.dot(C_b_n, C_t2_b)
    # C_t3_n = np.dot(C_b_n, C_t3_b)
    # C_t4_n = np.dot(C_b_n, C_t4_b)

    C_t1_n = np.dot(C_b_n, C_b_t1)
    C_t2_n = np.dot(C_b_n, C_b_t2)
    C_t3_n = np.dot(C_b_n, C_b_t3)
    C_t4_n = np.dot(C_b_n, C_b_t4)

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

    alpha_t[0] = euler_w1[2, 0] - math.atan2(v_et1_n[1] + fh * yaw_rate, v_et1_n[0] - wl/2 * yaw_rate)
    alpha_t[1] = euler_w2[2, 0] - math.atan2(v_et2_n[1] + fh * yaw_rate, v_et2_n[0] + wl/2 * yaw_rate)
    alpha_t[2] = euler_w3[2, 0] - math.atan2(v_et3_n[1] + rh * yaw_rate, v_et3_n[0] - wl/2 * yaw_rate)
    alpha_t[3] = euler_w4[2, 0] - math.atan2(v_et4_n[1] + rh * yaw_rate, v_et4_n[0] + wl/2 * yaw_rate)

    # print(str(steer_ip[0,0]), str(steer_ip[1,0]), str(steer_ip[2,0]), str(steer_ip[3,0]), str(euler[0,0]), str(euler[1,0]), str(euler[2,0]), sep='\t', file=tire_lin_vel)

    # print(str(v_et1_n[0]), str(v_et1_n[1]), str(v_et1_n[2]), str(v_et2_n[0]), str(v_et2_n[1]), str(v_et2_n[2]), \
    #     str(v_et3_n[0]), str(v_et3_n[1]), str(v_et3_n[2]), str(v_et4_n[0]), str(v_et4_n[1]), str(v_et4_n[2]),  \
    #     str(euler_w1[0,0]), str(euler_w1[1,0]), str(euler_w1[2,0]), str(euler_w2[0,0]), str(euler_w2[1,0]), str(euler_w2[2,0]), \
    #     str(euler_w3[0,0]), str(euler_w3[1,0]), str(euler_w3[2,0]), str(euler_w4[0,0]), str(euler_w4[1,0]), str(euler_w4[2,0]), sep='\t', file=tire_lin_vel)
    # print(str(euler_w1[2,0]), str(euler_w2[2,0]), str(euler_w3[2,0]), str(euler_w4[2,0]), str(C_b_t1[0,0]), str(C_b_t1[1,1]), str(C_b_t1[2,2]), str(v_et4_n[1]), sep='\t', file=tire_lin_vel)


    for x in range(4):
        if(alpha_t[x] > 6.0):
            alpha_t[x] = alpha_t[x] - 2*pi
        elif(alpha_t[x] < -6.0):
            alpha_t[x] = alpha_t[x] + 2*pi


    alpha = np.concatenate((alpha_t[0], alpha_t[1], alpha_t[2], alpha_t[3]), axis = 0)

    return alpha

def longitudinal_tire_slip_calc_old(w_tk, v_tk_x):
    R_0 = config.R_0

    # to-do eff_radius_calc()
    R_eff = R_0

    if ( math.fabs(v_tk_x) > math.fabs(R_eff*w_tk) ):   # During Braking
        sigma_x = (math.fabs(R_eff * w_tk) - math.fabs(v_tk_x)) / math.fabs(v_tk_x)
    else:
        sigma_x = (math.fabs(R_eff * w_tk) - math.fabs(v_tk_x)) / math.fabs(R_eff * w_tk)

    return sigma_x


def tire_sideslip_angle_calc(tire_debug, yaw_rate):
    DELTA_T = config.delta_t
    rh = config.vehicle_rear_half_m              
    fh = config.vehicle_front_half_m            
    wl = config.vehicle_width_m         

    # tire_debug = HtNavVehicleDebug()

    # float64       time
    # HtNavTireOut  wheel_variables
    # HtNavStrapOut imu_link_pva
    # HtNavStrapOut fl_wheel_pva
    # HtNavStrapOut fr_wheel_pva
    # HtNavStrapOut rl_wheel_pva
    # HtNavStrapOut rr_wheel_pva

    # tire_pva = HtNavStrapOut()
    # HtNavVector3          pos
    # HtNavVector3          vel
    # HtNavEuler            euler
    # HtNavQuaternion       quaternion

    alpha = HtNavWheelVector()

    alpha_t = np.zeros((4,1))
    alpha_t[0] = tire_debug.fl_wheel_pva.euler.yaw - math.atan2(tire_debug.fl_wheel_pva.vel.y + fh * yaw_rate, tire_debug.fl_wheel_pva.vel.x - wl/2 * yaw_rate)
    alpha_t[1] = tire_debug.fr_wheel_pva.euler.yaw - math.atan2(tire_debug.fr_wheel_pva.vel.y + fh * yaw_rate, tire_debug.fr_wheel_pva.vel.x + wl/2 * yaw_rate)
    alpha_t[2] = tire_debug.rl_wheel_pva.euler.yaw - math.atan2(tire_debug.rl_wheel_pva.vel.y + rh * yaw_rate, tire_debug.rl_wheel_pva.vel.x - wl/2 * yaw_rate)
    alpha_t[3] = tire_debug.rr_wheel_pva.euler.yaw - math.atan2(tire_debug.rr_wheel_pva.vel.y + rh * yaw_rate, tire_debug.rr_wheel_pva.vel.x + wl/2 * yaw_rate)

    for x in range(4):
        if(alpha_t[x] > 6.0):
            alpha_t[x] = alpha_t[x] - 2*pi
        elif(alpha_t[x] < -6.0):
            alpha_t[x] = alpha_t[x] + 2*pi


    alpha.w1 = float(alpha_t[0])
    alpha.w2 = float(alpha_t[1])
    alpha.w3 = float(alpha_t[2])
    alpha.w4 = float(alpha_t[3])

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

 
def tire_pva_calc(delta_ang, pos, v_eb_n, euler, C_tk_b, r_btk_b):
    # out_data_path = base_path / "debug_wheel_vel.txt"
    # wheel_vel = open(out_data_path, 'a')
    DELTA_T = config.delta_t

    r_btk_n = np.zeros((3,1))
    w_ib_b = np.zeros((3,1))
    w_ib_n = np.zeros((3,1))
    
    temp_vel_tk = np.zeros((3,1))
    v_etk_n = np.zeros((3,1))
    c_bn = np.zeros((3, 3))
    c_nb = np.zeros((3, 3))

    C_b_tk = np.zeros((3, 3))
    C_tk_n = np.zeros((3, 3))
    euler_wk = np.zeros((3,1))
    pos_wk = np.zeros((3,1))

    # transport euler solution from IMU to wheel
    C_b_tk = C_tk_b.transpose()
    w_ib_b = delta_ang / DELTA_T

    c_bn = euler2cbn(euler)
    c_nb = c_bn.transpose()

    C_tk_n = np.dot(c_bn, C_b_tk)
    euler_wk =  cbn2euler(C_tk_n)
    
    # transport velocity solution from IMU to wheel
    w_ib_n = np.dot(c_bn , w_ib_b)

    r_btk_n = np.dot(c_bn , r_btk_b)
    temp_vel_tk = np.cross(w_ib_n, r_btk_n ,axis=0)  
    v_etk_n = v_eb_n + temp_vel_tk
    # temp_vel_tk = np.dot(c_nb, v_etk_n)
    # v_etk_tk =  np.dot(C_b_tk , temp_vel_tk)

    # transport position solution from IMU to wheel
    rn, re = calc_rn_re(pos[0])
    rn = rn + pos[2]
    re = re + pos[2]

    pos_wk[0] = pos[0] + r_btk_n[0] / rn
    pos_wk[1] = pos[1] + r_btk_n[1] / re / np.cos(pos[0])
    pos_wk[2] = pos[2] + r_btk_n[2] 

    tire_pva = HtNavStrapOut()
    # HtNavVector3          pos
    # HtNavVector3          vel
    # HtNavEuler            euler
    # HtNavQuaternion       quaternion
   
    tire_pva.pos.x = float(pos_wk[0])
    tire_pva.pos.y = float(pos_wk[1])
    tire_pva.pos.z = float(pos_wk[2])

    tire_pva.vel.x = float(v_etk_n[0])
    tire_pva.vel.y = float(v_etk_n[1])
    tire_pva.vel.z = float(v_etk_n[2])
    
    tire_pva.euler.roll = float(euler_wk[0])
    tire_pva.euler.pitch = float(euler_wk[1])
    tire_pva.euler.yaw = float(euler_wk[2])

    return tire_pva


def tire_dugoff_force_calc(alpha_t, sigma_t):
    C_alpha = config.C_alpha              
    C_sigma = config.C_sigma              
    mu = config.mu            
    F_z = config.F_z        
    R_0 = config.R_0
    vehicle_mass = config.vehicle_mass
 
    alpha = np.zeros((4,1))
    sigma = np.zeros((4,1))

    tire_out = HtNavTireOut()
    F_x = HtNavWheelVector()
    F_y = HtNavWheelVector()

    alpha[0] = alpha_t.w1
    alpha[1] = alpha_t.w2
    alpha[2] = alpha_t.w3
    alpha[3] = alpha_t.w4

    sigma[0] = sigma_t.w1
    sigma[1] = sigma_t.w2
    sigma[2] = sigma_t.w3
    sigma[3] = sigma_t.w4

    F_x_t = np.zeros((4,1))
    F_y_t = np.zeros((4,1))

    for i in range(4):
        lambda_temp = (mu * F_z * (1 + sigma[i])) / (2 * np.sqrt( np.power(C_sigma * sigma[i],2) + np.power(C_alpha * np.tan(alpha[i]),2) ) )
        if lambda_temp >= 1:
            f_lambda = 1
        else:
            f_lambda = (2 - lambda_temp)*lambda_temp
        F_x_t[i] = C_sigma * sigma[i] / (1 + sigma[i]) * f_lambda
        F_y_t[i] = C_alpha * np.tan(alpha[i]) / (1 + sigma[i]) * f_lambda
        
    # float64          effective_radius_est
    # float64          vehicle_mass_est
    # HtNavWheelVector wheel_side_slip_ang
    # HtNavWheelVector wheel_longitudinal_slip_ratio
    # HtNavWheelVector tire_lateral_forces
    # HtNavWheelVector tire_longitudinal_forces

    F_x.w1 = float(F_x_t[0])
    F_x.w2 = float(F_x_t[1])
    F_x.w3 = float(F_x_t[2])
    F_x.w4 = float(F_x_t[3])

    F_y.w1 = float(F_y_t[0])
    F_y.w2 = float(F_y_t[1])
    F_y.w3 = float(F_y_t[2])
    F_y.w4 = float(F_y_t[3])

    tire_out.effective_radius_est           = float(R_0)
    tire_out.vehicle_mass_est               = float(vehicle_mass)
    tire_out.wheel_side_slip_ang            = alpha_t
    tire_out.wheel_longitudinal_slip_ratio  = sigma_t
    tire_out.tire_lateral_forces            = F_y
    tire_out.tire_longitudinal_forces       = F_x

    return tire_out


def tire_sideslip_angle_calc(tire_debug, yaw_rate):
    DELTA_T = config.delta_t
    rh = config.vehicle_rear_half_m              
    fh = config.vehicle_front_half_m            
    wl = config.vehicle_width_m         

    # tire_debug = HtNavVehicleDebug()

    # float64       time
    # HtNavTireOut  wheel_variables
    # HtNavStrapOut imu_link_pva
    # HtNavStrapOut fl_wheel_pva
    # HtNavStrapOut fr_wheel_pva
    # HtNavStrapOut rl_wheel_pva
    # HtNavStrapOut rr_wheel_pva

    # tire_pva = HtNavStrapOut()
    # HtNavVector3          pos
    # HtNavVector3          vel
    # HtNavEuler            euler
    # HtNavQuaternion       quaternion