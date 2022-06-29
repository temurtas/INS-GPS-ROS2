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

imu_pub_freq = 100.0 #99.75808 # 100.0
kalman_prop_const = 5
gps_pub_freq = 5.0

delta_t = 1/imu_pub_freq

buffer_size = 30

# INS/GPS variances
pos_std = 25        # m
h_std   = 35        # m
vel_std = 2.0       # m/s
att_std = 100e-3    # rad

gps_pos_std = 4     # m
gps_h_std   = 5     # m
gps_vel_std = 0.2   # m/s

# bias_std = 9.81 * 1e-3              # mg
# drift_std = np.deg2rad(1) / 3600    # deg/hr

# tau_i = 1 / 5
# tau_bad = 1 / 5

# sigma_ra = 9.81 * 1e-3              # mg
# sigma_rg = np.deg2rad(1) / 3600     # deg / hr
# sigma_bad = 9.81 * 2e-3             # mg
# sigma_bgd = np.deg2rad(5) / 3600    # deg / hr

# IMU Modelling Specs
acc_bias_std    = 5.0   #1.0  # mg 
gyro_drift_std  = 10.0  #1.0   # deg/hr

acc_bias_stab_std   = 0.5    # mg 
gyro_drift_stab_std = 1.0    # deg/hr
acc_bias_stab_tc    = 1500   # sec
gyro_drift_stab_tc  = 1500   # sec

acc_sf_std   = 0.0  # ppm
gyro_sf_std  = 0.0  # ppm
acc_mis_std  = 0.0  # rad
gyro_mis_std = 0.0  # rad

acc_rw_std  = 0.06  # 0.065; % ft/s/rt-hr
gyro_rw_std = 0.125 # 0.125; % deg/rt-hr 

PI_NUMBER   = 3.14159265358979
DEG2RAD     = 0.0174532925199433
RAD2DEG     = 57.2957795130823

# GPS Modelling Specs
updateRateHZ = gps_pub_freq # 5.0
posDriftFreq = 500.0
posBiasStd   = 0.25 
posDriftStd  = 1.5 
velErrStd    = 0.10 

# Vehicle Model
vehicle_cg_2_rear_half_m   = 1.144 # 1.41 - 0.266  # m      
vehicle_cg_2_front_half_m  = 1.716 # 1.45 + 0.266  # m    
vehicle_rear_half_m   = 0.00 # 1.41 - 0.266  # m      
vehicle_front_half_m  = 2.86 # 1.45 + 0.266  # m    

vehicle_width_m       = 1.572 # m
R_0                   = 0.31265 # 0.3   # m
vehicle_mass          = 1326.0 # kg 

F_z_front = (vehicle_mass/2 + 1 + 22)/2 * 9.81
F_z_rear  = (vehicle_mass/2 + 30 + 22)/2 * 9.81

mu = 0.7; # Dry Asphalt %http://hyperphysics.phy-astr.gsu.edu/
C_sigma = 1.78e5;        # 1.98e5
C_alpha = 3.56e5; # 89e3 # 1.56e5


