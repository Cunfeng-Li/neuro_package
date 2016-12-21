cmake_minimum_required(VERSION 2.8.3)
project(neuro)


find_package(catkin REQUIRED COMPONENTS
  actionlib
  diagnostic_msgs
  drv_msgs
  dynamic_reconfigure
  geometry_msgs
  move_base_msgs
  nav_msgs
  #pi_trees_lib
  #pi_trees_ros
  rbx2_msgs
  roscpp
  rospy
  sensor_msgs
  smach
  smach_ros
  std_msgs
  tf2
  tf2_ros
  visualization_msgs
)


catkin_package(

)


include_directories(
  ${catkin_INCLUDE_DIRS}
)

#catkin_python_setup()