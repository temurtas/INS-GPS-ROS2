# We need install numpy in order to import it
import numpy as np
import math
import ht_strap_package.config as config
from ht_strap_package.strap_operations import *
from ht_nav_variables.msg import HtNavStrapOut


def p0_matrix_construct():
    delta_t = config.delta_t
    pos_std = config.pos_std
    vel_std = config.vel_std
    att_std = config.att_std
    bias_std = config.bias_std
    drift_std = config.drift_std

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

    p0[9, 9] = bias_std * bias_std
    p0[10, 10] = bias_std * bias_std
    p0[11, 11] = bias_std * bias_std

    p0[12, 12] = drift_std * drift_std
    p0[13, 13] = drift_std * drift_std
    p0[14, 14] = drift_std * drift_std

    return p0


def f_matrix_construct(pos, vel, quaternion):
    delta_t = config.delta_t

    w_ie_n = earth_rate_calc(pos)
    omega_ie_n = skew_symmetric(w_ie_n)

    w_en_n = craft_rate_calc(vel, pos)
    omega_en_n = skew_symmetric(w_en_n)

    mat_a = omega_ie_n - 2 * omega_en_n
    mat_b = omega_ie_n + omega_en_n
    c_bn = quaternion2cbn(quaternion)

    mat_c = np.zeros((3, 3))
    l_b = pos[0]
    h_b = pos[2]
    rn, re = calc_rn_re(l_b)

    mat_c[0, 0] = 1/(rn+h_b)
    mat_c[1, 1] = 1/((re+h_b)*math.cos(l_b))
    mat_c[2, 2] = -1

    f = np.zeros((15, 15))
    f[0:3, 3:6] = mat_c  # be careful here

    f[3:6, 3:6] = mat_a
    f[3:6, 9:12] = c_bn

    f[6:9, 6:9] = mat_b
    f[6:9, 12:15] = c_bn

    return f


def q_matrix_construct():
    delta_t = config.delta_t
    q = np.zeros((15, 15))

    tau_i = config.tau_i
    tau_bad = config.tau_bad

    sigma_ra = config.sigma_ra
    sigma_rg = config.sigma_rg

    sigma_bad = config.sigma_bad
    sigma_bgd = config.sigma_bgd

    temp_eye = np.eye(3)

    q[3: 6, 3: 6] = temp_eye * sigma_ra * sigma_ra * tau_i
    q[6: 9, 6: 9] = temp_eye * sigma_rg * sigma_rg * tau_i

    q[9: 12, 9: 12] = temp_eye * sigma_bad * sigma_bad / tau_bad
    q[12: 15, 12: 15] = temp_eye * sigma_bgd * sigma_bgd / tau_bad

    return q


def p_update(p_minus, f, q):
    delta_t = config.delta_t * config.kalman_prop_const 

    theta = np.eye(15) + delta_t * f
    temp_a = np.dot(theta, p_minus)
    theta_tr = np.transpose(theta)
    p_plus = np.dot(temp_a, theta_tr) + q
    return p_plus


def h_matrix_construct():
    h = np.zeros((3, 15))
    h[0:3, 0:3] = -1 * np.eye(3)
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
    r[0, 0] = temp_1**2
    r[1, 1] = temp_2**2
    r[2, 2] = h_std**2
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
    p_next = p_prev - np.dot(temp_d, p_prev)

    return p_next, x_next


def kalman_duzeltme(old_strap, delta_x):

    new_pos_ip = np.zeros((3,1))
    new_pos_ip[0] = old_strap.pos.x
    new_pos_ip[1] = old_strap.pos.y
    new_pos_ip[2] = old_strap.pos.z

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

    delta_euler = delta_x[6:9]
    ss_delta_euler = skew_symmetric(delta_euler)
    mat_a = np.eye(3) - ss_delta_euler
    c_bn = quaternion2cbn(new_quaternion_ip)

    mat_b = np.dot(mat_a, c_bn)
    new_quaternion_temp = cbn2quaternion(mat_b)
    new_quaternion = quaternion_normalize(new_quaternion_temp)

    new_euler = quaternion2euler(new_quaternion)

    new_strap = HtNavStrapOut()
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
