# This represents a vector in free space. 
# It is only meant to represent a direction. Therefore, it does not
# make sense to apply a translation to it (e.g., when applying a 
# generic rigid transformation to a Vector3, tf2 will only apply the
# rotation). If you want your data to be translatable too, use the
# geometry_msgs/Point message instead.

float64       time
HtNavTireOut  wheel_variables
HtNavStrapOut imu_link_pva
HtNavStrapOut fl_wheel_pva
HtNavStrapOut fr_wheel_pva
HtNavStrapOut rl_wheel_pva
HtNavStrapOut rr_wheel_pva
