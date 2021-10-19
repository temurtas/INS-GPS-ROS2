import numpy as np

# define global variables
delta_t = 0.01
from pathlib import Path

base_path = Path("/home/temurtas/INS-GPS-ws/INS-GPS-Matlab/veriler/veri2/input/")           #Ubuntu Path  # veri2_Senaryo2 # veri1_to_Dogukan # veri2/input

buffer_size = 10

# INS/GPS variances
pos_std = 5                         # m
h_std = 7                           # m
vel_std = 0.25                      # m/s
att_std = np.deg2rad(1)             # deg
bias_std = 9.81 * 1e-3              # mg
drift_std = np.deg2rad(1) / 3600    # deg/hr

tau_i = 1 / 5
tau_bad = 1 / 5

sigma_ra = 9.81 * 1e-3              # mg
sigma_rg = np.deg2rad(1) / 3600     # deg / hr
sigma_bad = 9.81 * 2e-3             # mg
sigma_bgd = np.deg2rad(5) / 3600    # deg / hr

