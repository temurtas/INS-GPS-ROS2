# We need install numpy in order to import it
import numpy as np
import math
import ht_strap_package.config as config
from ht_strap_package.strap_tf_operations import *


# ########### POSITION UPDATE ###########

def car_pos_update(vel, old_car_pos):
    new_car_pos = np.zeros((3, 1))
    delta_t = config.delta_t

    old_x = old_car_pos[0]
    old_y = old_car_pos[1]
    old_z = old_car_pos[2]

    # Update height using (5.56)
    new_x = old_x + delta_t * vel[1] 
    new_y = old_y + delta_t * vel[0] 
    new_z = old_z + delta_t * vel[2] # Down position, not height 

    new_car_pos[0] = new_x
    new_car_pos[1] = new_y
    new_car_pos[2] = new_z

    return new_car_pos

def pos_update(vel, old_pos):
    new_pos = np.zeros((3, 1))
    delta_t = config.delta_t

    old_l_b = old_pos[0]
    old_lambda_b = old_pos[1]
    old_h_b = old_pos[2]

    rn, re = calc_rn_re(old_l_b)

    # Update height using (5.56)
    h_b = old_h_b - delta_t * vel[2]
    # Update latitude using (5.56)
    l_b = old_l_b + delta_t * vel[0] / (rn + h_b)
    # Update longitude using (5.56)
    lambda_b = old_lambda_b + delta_t * vel[1] / ((re + h_b) * math.cos(l_b))

    new_pos[0] = l_b
    new_pos[1] = lambda_b
    new_pos[2] = h_b

    return new_pos

def calc_rn_re(lb):
    # Parameters
    r0 = 6378137        # WGS84 Equatorial radius in meters
    e = 0.0818191908425  # WGS84 eccentricity

    # Calculate meridian radius of curvature using (2.105)
    temp = 1 - (e * math.sin(lb))**2
    rn = r0 * (1 - e**2) / temp**1.5

    # Calculate transverse radius of curvature using (2.105)
    re = r0 / math.sqrt(temp)

    return rn, re

# ########### VELOCITY UPDATE ###########

def vel_update(old_vel, f_ib_b, old_pos, old_quaternion):
    # Transform specific force to 
    delta_t = config.delta_t
    c_b_n = quaternion2cbn(old_quaternion)
    vel_diff = np.dot(c_b_n, f_ib_b)
    g = g_calc(old_pos)

    new_vel = old_vel + vel_diff + g * delta_t
    return new_vel

def g_calc(pos):
    g = np.zeros((3, 1))
    # Parameters
    r0 = 6378137           # WGS84 Equatorial radius in meters
    rp = 6356752.31425     # WGS84 Polar radius in meters
    e = 0.0818191908425     # WGS84 eccentricity
    f = 1 / 298.257223563   # WGS84 flattening
    mu = 3.986004418E14     # WGS84 Earth gravitational constant (m^3 s^-2)
    # omega_ie = 7.292115E-5  # Earth rotation rate (rad/s)
    omega_ie = 0

    lb = pos[0]
    hb = pos[2]

    # Calculate surface gravity using the Somigliana model, (2.134)
    sinl = math.sin(lb)
    sinsql = sinl**2
    g_0 = 9.7803253359 * (1 + 0.001931853 * sinsql) / math.sqrt(1 - e**2 * sinsql)

    # Calculate north gravity using (2.140)
    g[0] = -8.08E-9 * hb * math.sin(2 * lb)

    # East gravity is zero
    g[1] = 0

    # Calculate down gravity using (2.139)
    temp = (1 + f * (1 - 2 * sinsql) + (omega_ie**2 * r0**2 * rp / mu))
    temp2 = (3 * hb**2 / r0**2)
    temp_g = 1 - (2 / r0) * temp * hb + temp2
    g[2] = g_0 * temp_g


    g[2] = 0.0
    g[2] = 0.0
    g[2] = 9.80
    return g

# ########### ATTITUDE UPDATE ###########

def quaternion_update(quaternion_old, ang_diff, old_pos, old_vel):
    ang_diff_temp = np.reshape(ang_diff, (3, 1))
    quaternion_1 = np.zeros((4, 1))

    # delta_t = config.delta_t

    att_inc_norm = math.sqrt ( ang_diff_temp[0]*ang_diff_temp[0] + ang_diff_temp[1]*ang_diff_temp[1] + ang_diff_temp[2]*ang_diff_temp[2])

    quaternion_1[0] = math.cos(att_inc_norm * 0.5)
    if (att_inc_norm < 1e-8):
        temp_1 = 0.5
    else:
        temp_1 = (math.sin(att_inc_norm * 0.5)) / (att_inc_norm)
    
    quaternion_1[1] = temp_1 * ang_diff_temp[0]
    quaternion_1[2] = temp_1 * ang_diff_temp[1]
    quaternion_1[3] = temp_1 * ang_diff_temp[2]

    quaternion_new_temp = quaternion_product(quaternion_old, quaternion_1)
    quaternion_new = quaternion_normalize(quaternion_new_temp)

    return quaternion_new

def skew_symmetric(in_vector):
    # Skew_symmetric - Calculates skew-symmetric matrix
    out_matrix = np.zeros((3, 3))
    out_matrix[0, 1] = - in_vector[2]
    out_matrix[0, 2] = + in_vector[1]
    out_matrix[1, 0] = + in_vector[2]
    out_matrix[1, 2] = - in_vector[0]
    out_matrix[2, 0] = - in_vector[1]
    out_matrix[2, 1] = + in_vector[0]

    return out_matrix

def quaternion_product(p_in, q_in):
    q_out_p = np.zeros((4, 1))
    p0 = p_in[0]
    p1 = p_in[1]
    p2 = p_in[2]
    p3 = p_in[3]
    q0 = q_in[0]
    q1 = q_in[1]
    q2 = q_in[2]
    q3 = q_in[3]

    q_out_p[0] = p0 * q0 - p1 * q1 - p2 * q2 - p3 * q3
    q_out_p[1] = p0 * q1 + p1 * q0 + p2 * q3 - p3 * q2
    q_out_p[2] = p0 * q2 - p1 * q3 + p2 * q0 + p3 * q1
    q_out_p[3] = p0 * q3 + p1 * q2 - p2 * q1 + p3 * q0

    return q_out_p

def quaternion_normalize(q_in):
    q_out_n = np.zeros((4, 1))
    norm_q = math.sqrt(q_in[0]**2 + q_in[1]**2 + q_in[2]**2 + q_in[3]**2 )

    q_out_n[0] = q_in[0] / norm_q
    q_out_n[1] = q_in[1] / norm_q
    q_out_n[2] = q_in[2] / norm_q
    q_out_n[3] = q_in[3] / norm_q

    return q_out_n



