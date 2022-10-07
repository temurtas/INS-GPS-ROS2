# We need install numpy in order to import it
from cmath import pi
import numpy as np
import math
import ht_strap_package.config as config

from ht_strap_package.strap_tf_operations import *
from ht_strap_package.strap_operations_cartesian import *
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
    w_ib_b = delta_ang / DELTA_T
    euler_rate = euler_rate_calc(euler, w_ib_b)
    # euler_rate = euler_rate_calc(euler, w_nb_b)

    yaw_rate = float(euler_rate[2])
    
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


def tire_sideslip_angle_calc(tire_debug):
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
    # alpha_t[0] = tire_debug.fl_wheel_pva.euler.yaw - math.atan2(tire_debug.fl_wheel_pva.vel.y + fh * yaw_rate, tire_debug.fl_wheel_pva.vel.x - wl/2 * yaw_rate)
    # alpha_t[1] = tire_debug.fr_wheel_pva.euler.yaw - math.atan2(tire_debug.fr_wheel_pva.vel.y + fh * yaw_rate, tire_debug.fr_wheel_pva.vel.x + wl/2 * yaw_rate)
    # alpha_t[2] = tire_debug.rl_wheel_pva.euler.yaw - math.atan2(tire_debug.rl_wheel_pva.vel.y + rh * yaw_rate, tire_debug.rl_wheel_pva.vel.x - wl/2 * yaw_rate)
    # alpha_t[3] = tire_debug.rr_wheel_pva.euler.yaw - math.atan2(tire_debug.rr_wheel_pva.vel.y + rh * yaw_rate, tire_debug.rr_wheel_pva.vel.x + wl/2 * yaw_rate)

    alpha_t[0] = tire_debug.fl_wheel_pva.euler.yaw - math.atan2(tire_debug.fl_wheel_pva.vel.y , tire_debug.fl_wheel_pva.vel.x)
    alpha_t[1] = tire_debug.fr_wheel_pva.euler.yaw - math.atan2(tire_debug.fr_wheel_pva.vel.y , tire_debug.fr_wheel_pva.vel.x)
    alpha_t[2] = tire_debug.rl_wheel_pva.euler.yaw - math.atan2(tire_debug.rl_wheel_pva.vel.y , tire_debug.rl_wheel_pva.vel.x)
    alpha_t[3] = tire_debug.rr_wheel_pva.euler.yaw - math.atan2(tire_debug.rr_wheel_pva.vel.y , tire_debug.rr_wheel_pva.vel.x)

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

    # The true slip is calculated as follows: Consider changing
    if (v_tk_x == 0.0):
        lin_vel = 1e-5
    else:
        lin_vel = math.fabs(v_tk_x)

    sigma_x = math.fabs(R_eff * w_tk) / lin_vel - 1.0 

    if (sigma_x > 1.0):
        sigma_x = 1.0
    elif (sigma_x < -1.0):
        sigma_x = -1.0

    # if ( math.fabs(v_tk_x) > math.fabs(R_eff*w_tk) ):   # During Braking
    #     sigma_x = (math.fabs(R_eff * w_tk) - math.fabs(v_tk_x)) / math.fabs(v_tk_x)
    # else:
    #     sigma_x = (math.fabs(R_eff * w_tk) - math.fabs(v_tk_x)) / math.fabs(R_eff * w_tk)

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

    C_tk_n = np.dot(c_bn, C_tk_b) # C_b_tk) C_tk_n = C_b_n * C_tk_b
    euler_wk =  cbn2euler(C_tk_n)
    
    # transport velocity solution from IMU to wheel
    w_ib_n = np.dot(c_bn , w_ib_b)

    r_btk_n = np.dot(c_bn , r_btk_b)
    temp_vel_tk = np.cross(w_ib_n, r_btk_n ,axis=0)  
    v_etk_n = v_eb_n + temp_vel_tk
    # temp_vel_tk = np.dot(c_nb, v_etk_n)
    # v_etk_tk =  np.dot(C_b_tk , temp_vel_tk)

    # transport position solution from IMU to wheel
    pos_wk[0] = pos[0] + r_btk_n[0]
    pos_wk[1] = pos[1] + r_btk_n[1]
    pos_wk[2] = pos[2] + r_btk_n[2] 

    tire_pva = HtNavStrapOut()
    # HtNavVector3          pos
    # HtNavVector3          vel
    # HtNavEuler            euler
    # HtNavQuaternion       quaternion

    # tire_pva.pos.x = float(pos[0])
    # tire_pva.pos.y = float(pos[1])
    # tire_pva.pos.z = float(pos[2])

    # tire_pva.vel.x = float(v_eb_n[0])
    # tire_pva.vel.y = float(v_eb_n[1])
    # tire_pva.vel.z = float(v_eb_n[2])
    
    # tire_pva.euler.roll = float(euler[0])
    # tire_pva.euler.pitch = float(euler[1])
    # tire_pva.euler.yaw = float(euler[2])

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


def tire_dugoff_force_calc(F_z_total, alpha_t, sigma_t):
    C_alpha = config.C_alpha              
    C_sigma = config.C_sigma              
    mu = config.mu           
    F_z_front = config.F_z_front        
    F_z_rear = config.F_z_rear        
    R_0 = config.R_0
    vehicle_mass = config.vehicle_mass
 
    alpha = np.zeros((4,1))
    sigma = np.zeros((4,1))
    F_z    = np.zeros((4,1))

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

    F_z[0] = F_z_total.w1
    F_z[1] = F_z_total.w2
    F_z[2] = F_z_total.w3
    F_z[3] = F_z_total.w4

    F_x_t = np.zeros((4,1))
    F_y_t = np.zeros((4,1))

    for i in range(4):
        # if (i < 2):
        #     F_z = F_z_front
        # else:
        #     F_z = F_z_rear

        lambda_temp = (mu * F_z[i] * (1 + sigma[i])) / (2 * np.sqrt( np.power(C_sigma * sigma[i],2) + np.power(C_alpha * np.tan(alpha[i]),2) ) )
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
    tire_out.tire_longitudinal_forces       = F_x
    tire_out.tire_lateral_forces            = F_y
    tire_out.tire_normal_forces             = F_z_total

    return tire_out

def tire_pacejka_force_calc(F_z_total, alpha_t, sigma_t):
    C_alpha = config.C_alpha              
    C_sigma = config.C_sigma              
    mu = config.mu           
    F_z_front = config.F_z_front        
    F_z_rear = config.F_z_rear        
    R_0 = config.R_0
    vehicle_mass = config.vehicle_mass
 
    alpha = np.zeros((4,1))
    sigma = np.zeros((4,1))
    F_z    = np.zeros((4,1))

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

    F_z[0] = F_z_total.w1
    F_z[1] = F_z_total.w2
    F_z[2] = F_z_total.w3
    F_z[3] = F_z_total.w4

    F_x_t = np.zeros((4,1))
    F_y_t = np.zeros((4,1))

    for i in range(4):
        # if (i < 2):
        #     F_z = F_z_front
        # else:
        #     F_z = F_z_rear

        D_x0 = mu * F_z[i] 
        D_y0 = mu * F_z[i]

        # C_F_alpha = 4.15 * F_z[i]     # c_1 * c_2 * sin(2*atan(F_z/c_2/F_z0)) * F_z0;
        # C_F_alpha = 8.0 * F_z[i]      # c_1 * c_2 * sin(2*atan(F_z/c_2/F_z0)) * F_z0;
        # C_F_alpha = 8.0 * F_z[i]      # Thessis edition  # c_1 * c_2 * sin(2*atan(F_z/c_2/F_0)) * F_z0;
        # C_F_sigma = 8.0 * F_z[i]        # Thessis edition # c_8 * F_z; 
        C_F_alpha = 6.0 * F_z[i]        # c_1 * c_2 * sin(2*atan(F_z/c_2/F_0)) * F_z0;
        C_F_sigma = 8.0 * F_z[i]        # Thessis edition # c_8 * F_z; 
        # C_F_gamma = F_z;              # c_5 * F_z;

        # C_F_alpha_0 = C_F_alpha;
        # C_F_sigma_0 = C_F_sigma;
        
        C_x = 1.44
        # C_x = 0.8
        C_y = 1
  
        B_x0 = C_F_sigma / C_x / D_x0
        B_y0 = C_F_alpha / C_y / D_y0

        E_x0 = -1
        E_y0 = -1

        E_x = E_x0
        E_y = E_y0

        # Combined Slips
        # alpha = alpha_k + C_F_gamma / C_F_alpha * gamma_k;
        # sigma_cx = sigma_k / (1 + sigma_k);
        # sigma_cy = tan(alpha) / (1 + sigma_k);
        # sigma = sqrt(sigma_cx^2 + sigma_cy^2);

        F_x0 = D_x0 * math.sin(C_x * math.atan(B_x0 * sigma[i] - E_x * (B_x0 * sigma[i] - math.atan(B_x0 * sigma[i])) ) )
        F_y0 = D_y0 * math.sin(C_y * math.atan(B_y0 * alpha[i] - E_y * (B_y0 * alpha[i] - math.atan(B_y0 * alpha[i])) ) )
        # F_x0 = D_x0 * math.sin(C_x * math.atan(B_x0 * sigma[i] - E_x0 * sigma[i] - E_x * (B_x0 * sigma[i] - math.atan(B_x0 * sigma[i])) ) )
        # F_y0 = D_y0 * math.sin(C_y * math.atan(B_y0 * alpha[i] - E_y0 * alpha[i] - E_y * (B_y0 * alpha[i] - math.atan(B_y0 * alpha[i])) ) )

        F_x_t[i] = F_x0
        F_y_t[i] = F_y0
        
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
    tire_out.tire_longitudinal_forces       = F_x
    tire_out.tire_lateral_forces            = F_y
    tire_out.tire_normal_forces             = F_z_total

    return tire_out

