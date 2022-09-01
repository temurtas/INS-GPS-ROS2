# This represents a vector in free space. 
# It is only meant to represent a direction. Therefore, it does not
# make sense to apply a translation to it (e.g., when applying a 
# generic rigid transformation to a Vector3, tf2 will only apply the
# rotation). If you want your data to be translatable too, use the
# geometry_msgs/Point message instead.

float64           time
HtNavContactState fl_wheel_contact_states
HtNavContactState fr_wheel_contact_states
HtNavContactState rl_wheel_contact_states
HtNavContactState rr_wheel_contact_states