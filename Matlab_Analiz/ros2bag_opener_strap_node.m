%% -
clearvars;
close all;
clc;
%% -
folderpath_msg = 'D:\Ekstra\Thesis_work\INSGPS\INS-GPS-ROS2\Matlab\';
ros2genmsg(folderpath_msg)

%% -
% folderpath = 'F:\Ros2\bag_files\imu_data_only';
tic
folderpath = 'D:\Ekstra\Thesis_work\INSGPS\INS-GPS-ROS2\imu_strap_data_only';

bag = ros2bag(folderpath);

msgs = readMessages(bag);
toc
%% -
tic
j = 1;
j2 = 1;
j3 = 1;
k = 1;
j5 = 1;
for i=1:size(msgs,1)
    if ( string(msgs{i,1,1}.MessageType) == 'nav_msgs/Odometry' )
        time_sec = double(msgs{i,1,1}.header.stamp.sec);
        time_msec = double(msgs{i,1,1}.header.stamp.nanosec)*1e-6;
        odom.time(k,1) = time_sec*1e3 + time_msec;
        
        odom.pos(k,1) = msgs{i,1,1}.pose.pose.position.x;
        odom.pos(k,2) = msgs{i,1,1}.pose.pose.position.y;
        odom.pos(k,3) = msgs{i,1,1}.pose.pose.position.z;
        
        odom.quat(k,1) = msgs{i,1,1}.pose.pose.orientation.x;
        odom.quat(k,2) = msgs{i,1,1}.pose.pose.orientation.y;
        odom.quat(k,3) = msgs{i,1,1}.pose.pose.orientation.z;
        odom.quat(k,4) = msgs{i,1,1}.pose.pose.orientation.w;

        quat = quaternion(odom.quat(k,:));
        odom.euler(k,:) = euler(quat,'XYZ','frame');
        
        odom.lin_vel(k,1) = msgs{i,1,1}.twist.twist.linear.x;
        odom.lin_vel(k,2) = msgs{i,1,1}.twist.twist.linear.y;
        odom.lin_vel(k,3) = msgs{i,1,1}.twist.twist.linear.z;
        
        odom.ang_vel(k,1) = msgs{i,1,1}.twist.twist.angular.x;
        odom.ang_vel(k,2) = msgs{i,1,1}.twist.twist.angular.y;
        odom.ang_vel(k,3) = msgs{i,1,1}.twist.twist.angular.z;
        
        k = k+1;
    end
    
    if ( string(msgs{i,1,1}.MessageType) == 'sensor_msgs/Imu' )
        imu_data.lin_acc(j,1) = msgs{i,1,1}.linear_acceleration.x;
        imu_data.lin_acc(j,2) = msgs{i,1,1}.linear_acceleration.y;
        imu_data.lin_acc(j,3) = msgs{i,1,1}.linear_acceleration.z;
        
        imu_data.ang_rate(j,1) = msgs{i,1,1}.angular_velocity.x;
        imu_data.ang_rate(j,2) = msgs{i,1,1}.angular_velocity.y;
        imu_data.ang_rate(j,3) = msgs{i,1,1}.angular_velocity.z;
        
        j = j+1;
    end
    
    if ( string(msgs{i,1,1}.MessageType) == 'std_msgs/Float32' )
         distance(j5,1) = msgs{i,1,1}.data;
         j5 = j5 + 1;
    end
%     
%     if ( string(msgs{i,1,1}.MessageType) == 'geometry_msgs/Twist' )
%         cmd_vel(j2,1) = msgs{i,1,1}.linear.x;
%         cmd_vel(j2,2) = msgs{i,1,1}.linear.y;
%         cmd_vel(j2,3) = msgs{i,1,1}.linear.z;
%         
%         cmd_vel(j2,4) = msgs{i,1,1}.angular.x;
%         cmd_vel(j2,5) = msgs{i,1,1}.angular.y;
%         cmd_vel(j2,6) = msgs{i,1,1}.angular.z;
%         
%         j2 = j2+1;
%     end
%
%     if ( string(msgs{i,1,1}.MessageType) == 'geometry_msgs/Accel' )
%         cmd_acc(j3,1) = msgs{i,1,1}.linear.x;
%         cmd_acc(j3,2) = msgs{i,1,1}.linear.y;
%         cmd_acc(j3,3) = msgs{i,1,1}.linear.z;
%         
%         cmd_acc(j3,4) = msgs{i,1,1}.angular.x;
%         cmd_acc(j3,5) = msgs{i,1,1}.angular.y;
%         cmd_acc(j3,6) = msgs{i,1,1}.angular.z;
%         
%         j3 = j3+1;
%     end
    
end

toc
%% -
figure;
subplot(1, 2, 1);
plot(imu_data.lin_acc(:,1),'-or');
hold on; grid on;
plot(imu_data.lin_acc(:,2),'-og');
plot(imu_data.lin_acc(:,3),'-ob');
ylim([-2 12]);
legend('X','Y','Z'); title('Linear Acceleration 2-Hz');
xlabel('Time, seconds'); ylabel('Acceleration, m/s^2')

subplot(1, 2, 2);
plot(imu_data.ang_rate(:,1),'-or');
hold on; grid on;
plot(imu_data.ang_rate(:,2),'-og');
plot(imu_data.ang_rate(:,3),'-ob');
legend('X','Y','Z'); title('Angular Rate 2-Hz')
xlabel('Time, seconds'); ylabel('Angular Rate, rad/s')
%% -
figure;
subplot(1, 2, 1);
plot(odom.pos(:,1),odom.pos(:,2),'-or');
grid on;
title('Vehicle Position on X-Y Plane');
xlabel('x^b, meter'); ylabel('y^b, meter')

subplot(1, 2, 2);
plot(odom.time*1e-3,rad2deg(odom.euler(:,1)),'-or');
hold on; grid on;
plot(odom.time*1e-3,rad2deg(odom.euler(:,2)),'-og');
plot(odom.time*1e-3,rad2deg(odom.euler(:,3)),'-ob');
legend('Roll','Pitch','Yaw'); title('Vehicle Euler Angles')
xlabel('Time, seconds'); ylabel('Euler Ang, degree')