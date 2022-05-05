# We need install numpy in order to import it
import numpy as np
import math
import ht_strap_package.config as config


def cbn2quaternion(c_bn):
    quaternion = np.zeros((4, 1))
    quaternion[0] = 0.5 * math.sqrt(1 + c_bn[0, 0] + c_bn[1, 1] + c_bn[2, 2])
    quaternion[1] = (c_bn[2, 1] - c_bn[1, 2]) / (4 * quaternion[0])
    quaternion[2] = (c_bn[0, 2] - c_bn[2, 0]) / (4 * quaternion[0])
    quaternion[3] = (c_bn[1, 0] - c_bn[0, 1]) / (4 * quaternion[0])
    return quaternion


def quaternion2cbn(quaternion_in):
    quaternion = np.reshape(quaternion_in, (4, 1))
    c_nb = np.zeros((3, 3))
    q0 = quaternion[0]
    q0s = q0**2
    q1 = quaternion[1]
    q1s = q1**2
    q2 = quaternion[2]
    q2s = q2**2
    q3 = quaternion[3]
    q3s = q3**2

    c_nb[0, 0] = q0s + q1s - q2s - q3s
    c_nb[0, 1] = 2*(q1*q2+q3*q0)
    c_nb[0, 2] = 2*(q1*q3-q2*q0)
    c_nb[1, 0] = 2*(q1*q2-q3*q0)
    c_nb[1, 1] = q0s - q1s + q2s - q3s
    c_nb[1, 2] = 2*(q2*q3+q1*q0)
    c_nb[2, 0] = 2*(q1*q3+q2*q0)
    c_nb[2, 1] = 2*(q2*q3-q1*q0)
    c_nb[2, 2] = q0s - q1s - q2s + q3s

    c_bn = c_nb.transpose()
    return c_bn

def cbn2euler(cbn):
    euler_out = np.zeros((3,1))

    euler_out[0] = math.atan2(cbn[2,1], cbn[2,2])
    euler_out[1] = - math.asin(cbn[2,0])
    euler_out[2] = math.atan2(cbn[1,0], cbn[0,0])

    return euler_out

def euler2cbn(euler_in):
    c_nb = np.zeros((3, 3))

    c_nb[0,0] = math.cos(euler_in[1]) * math.cos(euler_in[2])
    c_nb[0,1] = math.cos(euler_in[1]) * math.sin(euler_in[2])
    c_nb[0,2] = -math.sin(euler_in[1])
    c_nb[1,0] = -math.cos(euler_in[0]) * math.sin(euler_in[2]) + math.sin(euler_in[0]) * math.sin(euler_in[1]) * math.cos(euler_in[2])
    c_nb[1,1] = math.cos(euler_in[0]) * math.cos(euler_in[2]) + math.sin(euler_in[0]) * math.sin(euler_in[1]) * math.sin(euler_in[2])
    c_nb[1,2] = math.sin(euler_in[0]) * math.cos(euler_in[1])
    c_nb[2,0] = math.sin(euler_in[0]) * math.sin(euler_in[2]) + math.cos(euler_in[0]) * math.sin(euler_in[1]) * math.cos(euler_in[2])
    c_nb[2,1] = -math.sin (euler_in[0]) * math.cos(euler_in[2]) + math.cos(euler_in[0]) * math.sin(euler_in[1]) * math.sin(euler_in[2])
    c_nb[2,2] = math.cos(euler_in[0]) * math.cos(euler_in[1])

    c_bn = c_nb.transpose()
    return c_bn


def euler2quaternion(euler_in):
    quaternion_out = np.zeros((4, 1))
    c1_2 = math.cos(euler_in[0] / 2)
    c2_2 = math.cos(euler_in[1] / 2)
    c3_2 = math.cos(euler_in[2] / 2)

    s1_2 = math.sin(euler_in[0] / 2)
    s2_2 = math.sin(euler_in[1] / 2)
    s3_2 = math.sin(euler_in[2] / 2)

    quaternion_out[0] = c1_2 * c2_2 * c3_2 + s1_2 * s2_2 * s3_2
    quaternion_out[1] = s1_2 * c2_2 * c3_2 - c1_2 * s2_2 * s3_2
    quaternion_out[2] = c1_2 * s2_2 * c3_2 + s1_2 * c2_2 * s3_2
    quaternion_out[3] = c1_2 * c2_2 * s3_2 - s1_2 * s2_2 * c3_2

    return quaternion_out

def quaternion2euler(quaternion_in):
    euler_out = np.zeros((3, 1))
    q0 = quaternion_in[0]
    q0s = q0**2
    q1 = quaternion_in[1]
    q1s = q1**2
    q2 = quaternion_in[2]
    q2s = q2**2
    q3 = quaternion_in[3]
    q3s = q3**2

    euler_out[0] = math.atan2(2 * (q0 * q1 + q2 * q3) , (1 - 2 * q1s - 2 * q2s))
    euler_out[1] = math.asin(2 * (q0 * q2 - q1 * q3))
    euler_out[2] = math.atan2(2 * (q0 * q3 + q1 * q2) , (1 - 2 * q2s - 2 * q3s))

    return euler_out

def euler_rate_calc(euler, w_nb_b):
    euler_rate = np.zeros((3,1))
    temp_matrix = np.zeros((3, 3))
    
    temp_matrix[0, 0] = 1
    temp_matrix[0, 1] = math.sin(euler[0]) * math.tan(euler[1])
    temp_matrix[0, 2] = math.cos(euler[0]) * math.tan(euler[1])
    temp_matrix[1, 1] = math.cos(euler[0])
    temp_matrix[1, 2] = - math.sin(euler[0])
    temp_matrix[2, 1] = math.sin(euler[0]) / math.cos(euler[1])
    temp_matrix[2, 2] = math.cos(euler[0]) / math.cos(euler[1])

    euler_rate = np.dot(temp_matrix, w_nb_b)

    return euler_rate

