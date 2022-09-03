source ~/INS-GPS-ROS2/bash_pre_sim_build.sh $1
		
for i in `seq 1 $3`;
	do 
		timeout $2m bash ~/INS-GPS-ROS2/bash_gazebo_sim_run.sh
		killall -9 gzserver gzclient
   		mkdir ~/ThesissDataArchieve/$1/data_$i
		rm -r ~/ThesissDataArchieve/$1/data_$i
		cp -R ~/INS-GPS-ROS2/veri_gazebo/veri_deneme/. ~/ThesissDataArchieve/$1/data_$i
	done

