import numpy as np

# define global variables
#delta_t = 0.01

from pathlib import Path

#base_path = Path("/home/temur/INS-GPS-ws/INS-GPS-Matlab/veriler/veri2/input/")           #Ubuntu Path  # veri2_Senaryo2 # veri1_to_Dogukan # veri2/input
#base_path = Path("/home/temur/INS-GPS-ws/INS-GPS-Matlab/veriler/veri2_Senaryo2/")           #Ubuntu Path  # veri2_Senaryo2 # veri1_to_Dogukan # veri2/input


base_path = Path("/home/temur/INS-GPS-ROS2/veri_gazebo/veri_deneme/")           #Ubuntu Path  # veri2_Senaryo2 # veri1_to_Dogukan # veri2/input
# veri_3_joint_vel_50Hz
# veri_4_joint_vel_25Hz
# veri_5_joint_vel_100Hz

imu_pub_freq = 99.75808 # 100.0
kalman_prop_const = 5
gps_pub_freq = 5.0

delta_t = 1/imu_pub_freq


buffer_size = 30

# INS/GPS variances
pos_std = 5                         # m
h_std = 7                           # m
vel_std = 0.25                      # m/s
att_std = np.deg2rad(1.0)           # deg->rad
bias_std = 9.81 * 1e-3              # mg
drift_std = np.deg2rad(1) / 3600    # deg/hr

tau_i = 1 / 5
tau_bad = 1 / 5

sigma_ra = 9.81 * 1e-3              # mg
sigma_rg = np.deg2rad(1) / 3600     # deg / hr
sigma_bad = 9.81 * 2e-3             # mg
sigma_bgd = np.deg2rad(5) / 3600    # deg / hr

# IMU Modelling Specs
acc_bias_std    = 1.0   # mg 
gyro_drift_std  = 1.0   # deg/hr
acc_sf_std      = 0.0   # ppm
gyro_sf_std     = 0.0   # ppm
acc_rw_std      = 0.065 # ft/s/rt-hr
gyro_rw_std     = 0.125 # deg/rt-hr 

PI_NUMBER = 3.14159265358979
DEG2RAD = 0.0174532925199433
RAD2DEG = 57.2957795130823

# vehicle_rear_half_m   = 1.144 # 1.41 - 0.266  # m      
# vehicle_front_half_m  = 1.716 # 1.45 + 0.266  # m    
vehicle_rear_half_m   = 0.00 # 1.41 - 0.266  # m      
vehicle_front_half_m  = 2.86 # 1.45 + 0.266  # m    

vehicle_width_m       = 1.572 # m
R_0                   = 0.31265 # 0.3   # m
vehicle_mass          = 1326.0 # kg 

F_z = vehicle_mass/4 * 9.81
mu = 0.7; # Dry Asphalt %http://hyperphysics.phy-astr.gsu.edu/
C_sigma = 1.98e5
C_alpha = 1.56e5


