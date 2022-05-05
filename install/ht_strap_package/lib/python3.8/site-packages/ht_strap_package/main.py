from pathlib import Path
import numpy as np
from strap_operations import *
from kalman_operations import *
from strapdown import *
from strap_tf_operations import *


#base_path = Path("D:/Drive/Thesis_work/INSGPS/INS-GPS-Matlab/veriler/veri1_to_Dogukan/")
#base_path = Path("D:/Drive/Thesis_work/INSGPS/INS-GPS-Matlab/veriler/veri2/input/")        #Windows Path
base_path = Path("/home/temur/INS-GPS-ws/INS-GPS-Matlab/veriler/veri2/input/")           #Ubuntu Path
imu_data_path = base_path / "aob_veri.txt"
initial_data_path = base_path / "ilk_deger.txt"
kks_data_path = base_path / "kks_veri.txt"
kks_data_txt = open(kks_data_path, 'r')

out_data_path = base_path / "python_out.txt"
out_data_txt = open(out_data_path, 'w')

initial_pos = np.zeros((3, 1))
initial_vel = np.zeros((3, 1))
initial_euler = np.zeros((3, 1))

old_pos = np.zeros((3, 1))
old_vel = np.zeros((3, 1))
old_euler = np.zeros((3, 1))
old_quaternion = np.zeros((4, 1))
ang_rate = np.zeros((3, 1))
vel_diff = np.zeros((3, 1))
new_pos = np.zeros((3, 1))
new_vel = np.zeros((3, 1))
new_quaternion = np.zeros((4, 1))
new_euler = np.zeros((3, 1))

iteration = 0

with open(initial_data_path) as initial_data_txt: # open the file for reading
    for line_x in initial_data_txt: # iterate over each line
        p1, p2, p3, v1, v2, v3, e1, e2, e3 = line_x.split() # split it by whitespace
        initial_pos[0] = float(p1) # convert bs from string to float
        initial_pos[1] = float(p2) # convert bs from string to float
        initial_pos[2] = float(p3) # convert bs from string to float

        initial_vel[0] = float(v1) # convert bs from string to float
        initial_vel[1] = float(v2) # convert bs from string to float
        initial_vel[2] = float(v3) # convert bs from string to float

        initial_euler[0] = float(e1) # convert bs from string to float
        initial_euler[1] = float(e2) # convert bs from string to float
        initial_euler[2] = float(e3) # convert bs from string to float

        initial_quaternion_temp = euler2quaternion(initial_euler)
        initial_quaternion = quaternion_normalize(initial_quaternion_temp)

with open(imu_data_path) as imu_data_txt: # open the file for reading
    for line in imu_data_txt: # iterate over each line
        w1, w2, w3, a1, a2, a3 = line.split() # split it by whitespace
        ang_rate[0] = float(w1) # convert bs from string to float
        ang_rate[1] = float(w2) # convert bs from string to float
        ang_rate[2] = float(w3) # convert bs from string to float

        vel_diff[0] = float(a1) # convert bs from string to float
        vel_diff[1] = float(a2) # convert bs from string to float
        vel_diff[2] = float(a3) # convert bs from string to float

        if iteration == 0:
            old_pos = initial_pos
            old_vel = initial_vel
            old_euler = initial_euler
            old_quaternion_temp = euler2quaternion(old_euler)
            old_quaternion = quaternion_normalize(old_quaternion_temp)

            p = p0_matrix_construct()
            bias = np.zeros((3, 1))
            drift = np.zeros((3, 1))
            x_k = np.zeros((15, 1))

        ang_rate = ang_rate - drift
        vel_diff = vel_diff - bias
        new_pos, new_vel, new_quaternion = strapdown(old_pos, old_vel, old_quaternion, ang_rate, vel_diff)
        new_euler = quaternion2euler(new_quaternion)
        old_pos = new_pos
        old_vel = new_vel
        old_quaternion = new_quaternion

        if np.mod(iteration, 1) == 0:
            f = f_matrix_construct(new_pos, new_vel, new_quaternion)
            q = q_matrix_construct()
            p = p_update(p, f, q)

        if np.mod(iteration, 1) == 0:
            gnss_pos = np.zeros((3, 1))  # f.readline()
            temp = kks_data_txt.readline()
            x1, x2, x3, y1, y2, y3 = temp.split()  # split it by whitespace
            gnss_pos[0] = float(x1)  # convert bs from string to float
            gnss_pos[1] = float(x2)  # convert bs from string to float
            gnss_pos[2] = float(x3)  # convert bs from string to float

            p, x_k = kalman_update(p, x_k, gnss_pos, new_pos)
            new_pos, new_vel, new_quaternion = kalman_duzeltme(new_pos, new_vel, new_quaternion, x_k)

            bias = x_k[9:12]
            drift = x_k[12:15]
            new_euler = quaternion2euler(new_quaternion)
            old_pos = new_pos
            old_vel = new_vel
            old_quaternion = new_quaternion

            x_k = np.zeros((15, 1))

        iteration = iteration + 1
        print(new_pos[0], new_pos[1], new_pos[2], new_vel[0], new_vel[1], new_vel[2], new_euler[0], new_euler[1], new_euler[2], sep='\t', file=out_data_txt)

print("finito")
