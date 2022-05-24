# We need install numpy in order to import it
import numpy as np
import math
import ht_strap_package.config as config
from ht_strap_package.strap_operations_cartesian import *
from ht_strap_package.strap_tf_operations import *
from ht_nav_variables.msg import HtNavStrapCarOut


def p0_matrix_construct():
    delta_t = config.delta_t
    pos_std = config.pos_std
    vel_std = config.vel_std
    att_std = config.att_std
    # bias_std = config.bias_std
    # drift_std = config.drift_std

    acc_bias_std    = config.acc_bias_std
    gyro_drift_std  = config.gyro_drift_std
    
    acc_bias    = acc_bias_std * 9.81 * 1e-3          # mg --> m/s^2
    gyro_drift  = gyro_drift_std / 57.295779 / 3600.0 # deg/hr --> rad/s

    p0 = np.zeros((15, 15))

    p0[0, 0] = pos_std * pos_std 
    p0[1, 1] = pos_std * pos_std 
    p0[2, 2] = pos_std * pos_std

    p0[3, 3] = vel_std * vel_std
    p0[4, 4] = vel_std * vel_std
    p0[5, 5] = vel_std * vel_std

    p0[6, 6] = att_std * att_std
    p0[7, 7] = att_std * att_std
    p0[8, 8] = att_std * att_std

    p0[9, 9]   = acc_bias * acc_bias
    p0[10, 10] = acc_bias * acc_bias
    p0[11, 11] = acc_bias * acc_bias

    p0[12, 12] = gyro_drift * gyro_drift
    p0[13, 13] = gyro_drift * gyro_drift
    p0[14, 14] = gyro_drift * gyro_drift

    # p0[9,  9]  = p0[9,  9]  + bias_stab_std * bias_stab_std
    # p0[10, 10] = p0[10, 10] + bias_stab_std * bias_stab_std
    # p0[11, 11] = p0[11, 11] + bias_stab_std * bias_stab_std

    # p0[12, 12] = p0[12, 12] + drift_stab_std * drift_stab_std
    # p0[13, 13] = p0[13, 13] + drift_stab_std * drift_stab_std
    # p0[14, 14] = p0[14, 14] + drift_stab_std * drift_stab_std

    return p0


def f_matrix_construct(pos, vel, quaternion, total_vel_inc):
    delta_t = config.delta_t
    mat_a = np.zeros((3, 3))
    mat_b = np.zeros((3, 3))
    mat_c = np.zeros((3, 3))

    c_bn = quaternion2cbn(quaternion)

    mat_a = -1 * np.dot(c_bn, total_vel_inc)

    l_b = pos[0]
    h_b = pos[2]
    rn, re = calc_rn_re(l_b)

    mat_b[0, 2] = -vel[0]/(rn+h_b)/(rn+h_b)
    mat_b[1, 0] = -vel[1]*math.tan(l_b)/((re+h_b)*math.cos(l_b))
    mat_b[1, 2] = -vel[1]/(re+h_b)/((re+h_b)*math.cos(l_b))

    mat_c[0, 0] = 1/(rn+h_b)
    mat_c[1, 1] = 1/((re+h_b)*math.cos(l_b))
    mat_c[2, 2] = -1

    f = np.zeros((15, 15))
    f[0:3, 0:3] = mat_b  # be careful here
    f[0:3, 3:6] = mat_c  # be careful here

    f[3:6, 6:9] = mat_a
    f[3:6, 9:12] = c_bn
    f[6:9, 12:15] = c_bn

    return f

def f_matrix_construct_pv(quaternion, total_vel_inc):
    delta_t = config.delta_t
    prop_t = config.delta_t * config.kalman_prop_const

    mat_a = np.zeros((3, 3))
    mat_b = np.zeros((3, 3))
    mat_c = np.zeros((3, 3))

    vec_a = np.zeros((3, 1))

    c_bn = quaternion2cbn(quaternion)

    vec_a = -1 * np.dot(c_bn, total_vel_inc)  / prop_t
    mat_a = skew_symmetric(vec_a)

    mat_c[0, 0] = 1
    mat_c[1, 1] = 1
    mat_c[2, 2] = 1

    f = np.zeros((15, 15))
    f[0:3, 3:6] = mat_c  # be careful here
    f[3:6, 6:9] = mat_a

    f[3:6, 9:12] = c_bn
    f[6:9, 12:15] = c_bn

    return f

def q_matrix_construct(pos, vel, quaternion, total_vel_inc):
    delta_t = config.delta_t
    kalman_prop_const = config.kalman_prop_const
    prop_t = delta_t*kalman_prop_const

    q   = np.zeros((15, 15))
    f   = np.zeros((15, 15))
    theta    = np.zeros((15, 15))
    theta_tr = np.zeros((15, 15))
    q_c = np.zeros((6, 6))
    g   = np.zeros((15, 6))
    g_tr= np.zeros((6, 15))

    q_c = q_c_matrix_construct()
    g = g_matrix_construct(quaternion)
    f = f_matrix_construct(pos, vel, quaternion, total_vel_inc)

    f_sqr = np.zeros((15, 15))
    f_sqr = np.dot(f, f)
    theta = np.eye(15) + delta_t * f + delta_t * 0.5 * f_sqr
    theta_tr = np.transpose(theta)
    g_tr = np.transpose(g)

    temp_1 = np.zeros((15, 6))
    temp_2 = np.zeros((15, 6))
    temp_3 = np.zeros((15, 15))
    temp_4 = np.zeros((15, 15))

    temp_1 = np.dot(theta, g)
    temp_2 = np.dot(temp_1, q_c)
    temp_3 = np.dot(temp_2, g_tr)
    temp_4 = np.dot(temp_3, theta_tr)

    q = temp_4 * prop_t

    return q

def q_matrix_construct_pv(quaternion, total_vel_inc, total_ang_inc):
    delta_t = config.delta_t
    kalman_prop_const = config.kalman_prop_const
    prop_t = delta_t*kalman_prop_const

    q   = np.zeros((15, 15))
    f   = np.zeros((15, 15))
    theta    = np.zeros((15, 15))
    theta_tr = np.zeros((15, 15))
    q_c = np.zeros((12, 12))
    g   = np.zeros((15, 12))
    g_tr= np.zeros((12, 15))

    q_c = q_c_matrix_construct_12(total_vel_inc, total_ang_inc)
    g = g_matrix_construct_12(quaternion)
    f = f_matrix_construct_pv(quaternion, total_vel_inc)

    f_sqr = np.zeros((15, 15))
    f_sqr = np.dot(f, f)
    theta = np.eye(15) + delta_t * f + delta_t * delta_t * 0.5 * f_sqr
    theta_tr = np.transpose(theta)
    g_tr = np.transpose(g)

    temp_1 = np.zeros((15, 6))
    temp_2 = np.zeros((15, 6))
    temp_3 = np.zeros((15, 15))
    temp_4 = np.zeros((15, 15))

    temp_1 = np.dot(theta, g)
    temp_2 = np.dot(temp_1, q_c)
    temp_3 = np.dot(temp_2, g_tr)
    temp_4 = np.dot(temp_3, theta_tr)

    q = temp_4 * prop_t

    return q


def q_c_matrix_construct_12(total_vel_inc, total_ang_inc):
    delta_t = config.delta_t
    kalman_prop_const = config.kalman_prop_const
    prop_t = delta_t*kalman_prop_const
    
    q_c    = np.zeros((12, 12))
    M_acc  = np.zeros((3, 3))
    M_gyro = np.zeros((3, 3))

    acc_bias_stab_std   = config.acc_bias_std
    gyro_drift_stab_std = config.gyro_drift_std

    acc_bias_stab_tc    = config.acc_bias_std
    gyro_drift_stab_tc  = config.gyro_drift_std
    
    acc_sf_std      = config.acc_sf_std
    gyro_sf_std     = config.gyro_sf_std
    acc_mis_std     = config.acc_mis_std
    gyro_mis_std    = config.gyro_mis_std
  
    acc_rw_std      = config.acc_rw_std
    gyro_rw_std     = config.gyro_rw_std

    acc_bias_stab   = acc_bias_stab_std * 9.81 * 1e-3          # mg --> m/s^2
    gyro_drift_stab = gyro_drift_stab_std / 57.295779 / 3600.0 # deg/hr --> rad/s

    acc_sf      = acc_sf_std * 1e-6                   # ppm -> unitless     # Assumed to be zero for now
    gyro_sf     = gyro_sf_std * 1e-6                  # ppm -> unitless     # Assumed to be zero for now

    acc_rw      = acc_rw_std  * 0.3048 / 60.0 * math.sqrt(delta_t) # ft/s/rt-hr --> m/s^2  
    gyro_rw     = gyro_rw_std / 57.295779 / 3600.0 / 60.0 * math.sqrt(delta_t) # deg/rt-hr --> rad/s

    M_acc[0,0] = acc_sf * acc_sf
    M_acc[1,1] = acc_sf * acc_sf
    M_acc[2,2] = acc_sf * acc_sf
    
    M_acc[0,1] = acc_mis_std * acc_mis_std
    M_acc[0,2] = acc_mis_std * acc_mis_std
    M_acc[1,0] = acc_mis_std * acc_mis_std
    M_acc[1,2] = acc_mis_std * acc_mis_std
    M_acc[2,0] = acc_mis_std * acc_mis_std
    M_acc[2,1] = acc_mis_std * acc_mis_std

    temp_vel_vec = np.dot(M_acc, total_vel_inc)
    temp_vel_vecl_tr  = np.transpose(temp_vel_vec)
    temp_vel_matrix = np.dot(temp_vel_vec, temp_vel_vecl_tr) / prop_t # m/s^2
    
    M_gyro[0,0] = gyro_sf * gyro_sf
    M_gyro[1,1] = gyro_sf * gyro_sf
    M_gyro[2,2] = gyro_sf * gyro_sf

    M_gyro[0,1] = gyro_mis_std * gyro_mis_std
    M_gyro[0,2] = gyro_mis_std * gyro_mis_std
    M_gyro[1,0] = gyro_mis_std * gyro_mis_std
    M_gyro[1,2] = gyro_mis_std * gyro_mis_std
    M_gyro[2,0] = gyro_mis_std * gyro_mis_std
    M_gyro[2,1] = gyro_mis_std * gyro_mis_std

    temp_ang_vec = np.dot(M_gyro, total_ang_inc)
    temp_ang_vec_tr  = np.transpose(temp_ang_vec)
    temp_ang_matrix = np.dot(temp_ang_vec, temp_ang_vec_tr) / prop_t # m/s^2

    q_c[0:3, 0:3] = temp_vel_matrix
    q_c[3:6, 3:6] = temp_ang_matrix

    q_c[0,0] = q_c[0,0] + (acc_rw*acc_rw) * delta_t  # m^2/s^3
    q_c[1,1] = q_c[1,1] + (acc_rw*acc_rw) * delta_t  # m^2/s^3
    q_c[2,2] = q_c[2,2] + (acc_rw*acc_rw) * delta_t  # m^2/s^3

    q_c[3,3] = q_c[3,3] + (gyro_rw*gyro_rw) * delta_t # rad^2/s
    q_c[4,4] = q_c[4,4] + (gyro_rw*gyro_rw) * delta_t # rad^2/s
    q_c[5,5] = q_c[5,5] + (gyro_rw*gyro_rw) * delta_t # rad^2/s

    temp_bias_instab  = acc_bias_stab * acc_bias_stab * (1 - math.exp(-2 * delta_t / acc_bias_stab_tc))
    temp_drift_instab = gyro_drift_stab * gyro_drift_stab * (1 - math.exp(-2 * delta_t / gyro_drift_stab_tc))

    q_c[6:9,  6:9]    = np.eye(3) * temp_bias_instab
    q_c[9:12, 9:12]   = np.eye(3) * temp_drift_instab

    return q_c

def q_c_matrix_construct():
    delta_t = config.delta_t
    q_c = np.zeros((6, 6))

    acc_bias_std    = config.acc_bias_std
    gyro_drift_std  = config.gyro_drift_std
    # acc_sf_std      = config.acc_sf_std
    # gyro_sf_std     = config.gyro_sf_std
    acc_rw_std      = config.acc_rw_std
    gyro_rw_std     = config.gyro_rw_std

    acc_bias    = acc_bias_std * 9.81 * 1e-3          # mg --> m/s^2
    gyro_drift  = gyro_drift_std / 57.295779 / 3600.0 # deg/hr --> rad/s
    # acc_sf      = acc_sf_std * 1e-6                   # ppm -> unitless     # Assumed to be zero for now
    # gyro_sf     = gyro_sf_std * 1e-6                  # ppm -> unitless     # Assumed to be zero for now

    acc_rw      = acc_rw_std  * 0.3048 / 60.0 * math.sqrt(delta_t) # ft/s/rt-hr --> m/s^2  
    gyro_rw     = gyro_rw_std / 57.295779 / 3600.0 / 60.0 * math.sqrt(delta_t) # deg/rt-hr --> rad/s

    q_c[0,0] = (acc_bias*acc_bias + acc_rw*acc_rw) * delta_t * delta_t  # (m/s)^2
    q_c[1,1] = (acc_bias*acc_bias + acc_rw*acc_rw) * delta_t * delta_t  # (m/s)^2
    q_c[2,2] = (acc_bias*acc_bias + acc_rw*acc_rw) * delta_t * delta_t  # (m/s)^2

    q_c[3,3] = (gyro_drift*gyro_drift + gyro_rw*gyro_rw) * delta_t * delta_t  # (rad)^2
    q_c[4,4] = (gyro_drift*gyro_drift + gyro_rw*gyro_rw) * delta_t * delta_t  # (rad)^2
    q_c[5,5] = (gyro_drift*gyro_drift + gyro_rw*gyro_rw) * delta_t * delta_t  # (rad)^2

    return q_c

def g_matrix_construct(quaternion):
    delta_t = config.delta_t
    c_bn = np.zeros((3, 3))

    c_bn = quaternion2cbn(quaternion)

    g = np.zeros((15, 6))
    g[3:6, 0:3] = c_bn  # be careful here
    g[6:9, 3:6] = c_bn  # be careful here

    g[9:12,  0:3] = np.eye(3)  # be careful here
    g[12:15, 3:6] = np.eye(3)  # be careful here


    return g

def g_matrix_construct_12(quaternion):
    delta_t = config.delta_t
    c_bn = np.zeros((3, 3))

    c_bn = quaternion2cbn(quaternion)

    g = np.zeros((15, 12))
    g[3:6, 0:3] = c_bn  # be careful here
    g[6:9, 3:6] = c_bn  # be careful here

    g[9:12,  6:9]  = np.eye(3)  # be careful here
    g[12:15, 9:12] = np.eye(3)  # be careful here

    return g

def p_update(p_minus, f, q):
    delta_t = config.delta_t * config.kalman_prop_const 

    f_sqr = np.zeros((15, 15))
    f_sqr = np.dot(f, f)
    theta = np.eye(15) + delta_t * f + delta_t * 0.5 * f_sqr 
    temp_a = np.dot(theta, p_minus)
    theta_tr = np.transpose(theta)
    p_plus = np.dot(temp_a, theta_tr) + q

    for i in range(15):
        if (p_plus[i, i] <= 0.0):
            p_plus[i, i] = 1e-20
    
    return p_plus


def h_matrix_construct():
    h = np.zeros((3, 15))
    h[0:3, 0:3] = -1 * np.eye(3)
    return h

def h_matrix_construct_pv():
    h = np.zeros((6, 15))
    h[0:3, 0:3] = -1 * np.eye(3)
    h[3:6, 3:6] = -1 * np.eye(3)
    return h

def r_matrix_construct(pos):
    pos_std = config.pos_std
    h_std = config.h_std
    l_b = pos[0]
    h_b = pos[2]
    rn, re = calc_rn_re(l_b)

    r = np.zeros((3, 3))
    temp_1 = pos_std/(rn+h_b)
    temp_2 = pos_std/((re+h_b)*math.cos(l_b))
    r[0, 0] = temp_1*temp_1
    r[1, 1] = temp_2*temp_2
    r[2, 2] = pos_std*pos_std
    return r

def r_matrix_construct_pv():
    pos_std = config.gps_pos_std
    h_std = config.gps_h_std
    vel_std = config.gps_vel_std

    r = np.zeros((6, 6))

    r[0, 0] = pos_std*pos_std
    r[1, 1] = pos_std*pos_std
    r[2, 2] = pos_std*pos_std

    r[3, 3] = vel_std*vel_std
    r[4, 4] = vel_std*vel_std
    r[5, 5] = vel_std*vel_std

    return r


def kalman_update(p_prev, x_prev, gnss_pos, pos):

    h = h_matrix_construct()
    r = r_matrix_construct(pos)

    h_tr = np.transpose(h)
    temp_a = np.dot(p_prev, h_tr)
    temp_b = np.dot(h, temp_a) + r
    temp_c = np.linalg.inv(temp_b)

    k = np.dot(temp_a, temp_c)
    z = gnss_pos - pos

    x_next = x_prev + np.dot(k, z)

    temp_d = np.dot(k, h)
    p_temp = p_prev - np.dot(temp_d, p_prev)

    for i in range(15):
        if (p_temp[i, i] <= 0.0):
            p_temp[i, i] = 1e-20

    p_next = np.add(p_temp , p_prev) * 0.5

    return p_next, x_next

def kalman_update_pv(p_prev, x_prev, y):

    h = h_matrix_construct_pv()
    r = r_matrix_construct_pv()

    h_tr = np.transpose(h)
    temp_a = np.dot(p_prev, h_tr)
    temp_b = np.dot(h, temp_a) + r
    temp_c = np.linalg.inv(temp_b)

    k = np.dot(temp_a, temp_c)

    x_next = x_prev + np.dot(k, y)

    temp_d = np.dot(k, h)
    p_temp = p_prev - np.dot(temp_d, p_prev)

    for i in range(15):
        if (p_temp[i, i] <= 0.0):
            p_temp[i, i] = 1e-20

    p_next = np.add(p_temp , p_prev) * 0.5

    return p_next, x_next

def kalman_duzeltme(old_strap, delta_x):

    new_pos_ip = np.zeros((3,1))
    new_pos_ip[0] = old_strap.pos.x
    new_pos_ip[1] = old_strap.pos.y
    new_pos_ip[2] = old_strap.pos.z

    new_car_pos_ip = np.zeros((3,1))
    new_car_pos_ip[0] = old_strap.car_pos.x
    new_car_pos_ip[1] = old_strap.car_pos.y
    new_car_pos_ip[2] = old_strap.car_pos.z

    new_vel_ip = np.zeros((3,1))
    new_vel_ip[0] = old_strap.vel.x
    new_vel_ip[1] = old_strap.vel.y
    new_vel_ip[2] = old_strap.vel.z

    new_quaternion_ip = np.zeros((4,1))
    new_quaternion_ip[0] = old_strap.quaternion.x
    new_quaternion_ip[1] = old_strap.quaternion.y
    new_quaternion_ip[2] = old_strap.quaternion.z
    new_quaternion_ip[3] = old_strap.quaternion.w

    l_b = new_pos_ip[0]
    h_b = new_pos_ip[2]
    rn, re = calc_rn_re(l_b)

    delta_x_car = np.zeros((3,1))
    delta_x_car[0] = delta_x[0] * (rn + h_b)
    delta_x_car[1] = delta_x[1] * (re + h_b) * math.cos(l_b)
    delta_x_car[2] = delta_x[2] 

    new_car_pos = new_car_pos_ip - delta_x_car[0:3]
    new_pos = new_pos_ip - delta_x[0:3]
    new_vel = new_vel_ip - delta_x[3:6]

    delta_euler = delta_x[6:9]
    ss_delta_euler = skew_symmetric(delta_euler)
    mat_a = np.eye(3) - ss_delta_euler
    c_bn = quaternion2cbn(new_quaternion_ip)

    mat_b = np.dot(mat_a, c_bn)
    new_quaternion_temp = cbn2quaternion(mat_b)
    new_quaternion = quaternion_normalize(new_quaternion_temp)

    new_euler = quaternion2euler(new_quaternion)

    new_strap = HtNavStrapCarOut()
    new_strap.pos.x = float(new_pos[0])
    new_strap.pos.y = float(new_pos[1])
    new_strap.pos.z = float(new_pos[2])

    new_strap.car_pos.x = float(new_car_pos[0])
    new_strap.car_pos.y = float(new_car_pos[1])
    new_strap.car_pos.z = float(new_car_pos[2])

    new_strap.vel.x = float(new_vel[0])
    new_strap.vel.y = float(new_vel[1])
    new_strap.vel.z = float(new_vel[2])

    new_strap.quaternion.x = float(new_quaternion[0])
    new_strap.quaternion.y = float(new_quaternion[1])
    new_strap.quaternion.z = float(new_quaternion[2])
    new_strap.quaternion.w = float(new_quaternion[3])

    new_strap.euler.roll = float(new_euler[0])
    new_strap.euler.pitch = float(new_euler[1])
    new_strap.euler.yaw = float(new_euler[2])

    return new_strap

def kalman_duzeltme_pv(old_strap, delta_x):

    new_pos_ip = np.zeros((3,1))
    new_pos_ip[0] = old_strap.pos.x
    new_pos_ip[1] = old_strap.pos.y
    new_pos_ip[2] = old_strap.pos.z

    new_car_pos_ip = np.zeros((3,1))
    new_car_pos_ip[0] = old_strap.car_pos.x
    new_car_pos_ip[1] = old_strap.car_pos.y
    new_car_pos_ip[2] = old_strap.car_pos.z

    new_vel_ip = np.zeros((3,1))
    new_vel_ip[0] = old_strap.vel.x
    new_vel_ip[1] = old_strap.vel.y
    new_vel_ip[2] = old_strap.vel.z

    new_quaternion_ip = np.zeros((4,1))
    new_quaternion_ip[0] = old_strap.quaternion.x
    new_quaternion_ip[1] = old_strap.quaternion.y
    new_quaternion_ip[2] = old_strap.quaternion.z
    new_quaternion_ip[3] = old_strap.quaternion.w


    new_pos = new_pos_ip - delta_x[0:3]
    new_vel = new_vel_ip - delta_x[3:6]

    dq0 = 0.5 * (delta_x[6]  * new_quaternion_ip[1] + delta_x[7] * new_quaternion_ip[2] + delta_x[8] * new_quaternion_ip[3])
    dq1 = 0.5 * (-delta_x[6] * new_quaternion_ip[0] - delta_x[7] * new_quaternion_ip[3] + delta_x[8] * new_quaternion_ip[2])
    dq2 = 0.5 * (delta_x[6]  * new_quaternion_ip[3] - delta_x[7] * new_quaternion_ip[0] - delta_x[8] * new_quaternion_ip[1])
    dq3 = 0.5 * (-delta_x[6] * new_quaternion_ip[2] + delta_x[7] * new_quaternion_ip[1] - delta_x[8] * new_quaternion_ip[0])

    new_quaternion_temp = np.zeros((4,1))
    new_quaternion_temp[0] = new_quaternion_ip[0] + dq0
    new_quaternion_temp[1] = new_quaternion_ip[1] + dq1
    new_quaternion_temp[2] = new_quaternion_ip[2] + dq2
    new_quaternion_temp[3] = new_quaternion_ip[3] + dq3


    new_quaternion = quaternion_normalize(new_quaternion_temp)

    new_euler = quaternion2euler(new_quaternion)

    new_strap = HtNavStrapCarOut()
    new_strap.pos.x = float(new_pos[0])
    new_strap.pos.y = float(new_pos[1])
    new_strap.pos.z = float(new_pos[2])

    new_strap.vel.x = float(new_vel[0])
    new_strap.vel.y = float(new_vel[1])
    new_strap.vel.z = float(new_vel[2])

    new_strap.quaternion.x = float(new_quaternion[0])
    new_strap.quaternion.y = float(new_quaternion[1])
    new_strap.quaternion.z = float(new_quaternion[2])
    new_strap.quaternion.w = float(new_quaternion[3])

    new_strap.euler.roll = float(new_euler[0])
    new_strap.euler.pitch = float(new_euler[1])
    new_strap.euler.yaw = float(new_euler[2])

    return new_strap
