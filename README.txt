# neuro_package
task planning for NEU household service robot
## 1. Software Prerequisites
### 1.1 ROS
We run this package in **indigo**, other versions of ROS may not be supported.
### 1.2 Install the required additional ROS packages
$sudo apt-get install ros-indigo-arbotix ros-indigo-dynamixelmotor ros-indigo-rosbridge-suite ros-indigo-mjpeg-server rosindigo-rgbd-launch  ros-indigo-openni-camera ros-indigo-moveitfull ros-indigo-turtlebot-* ros-indigo-kobuki-* ros-indigo-moveit-python python-pygraph python-pygraphviz python-easygui mini-httpd ros-indigo-laser-pipeline ros-indigo-ar-track-alvar ros-indigo-laser-filters ros-indigo-hokuyo-node ros-indigodepthimage-to-laserscan ros-indigo-moveit-ikfast ros-indigo-gazebo-ros ros-indigo-gazebo-ros-pkgs ros-indigogazebo-msgs ros-indigo-gazebo-plugins ros-indigo-gazebo-roscontrol ros-indigo-cmake-modules ros-indigo-kobuki-gazebo-plugins ros-indigo-kobuki-gazebo ros-indigo-smach ros-indigo-smach-ros ros-indigo-grasping-msgs ros-indigo-executive-smach ros-indigosmach-viewer ros-indigo-robot-pose-publisher ros-indigo-tf2-webrepublisher graphviz-dev libgraphviz-dev gv python-scipy
### 1.3 Install the rbx1 code
$ cd ~/catkin_ws/src
$ git clone https://github.com/pirobot/rbx1.git
$ cd rbx1
$ git checkout indigo-devel
$ cd ~/catkin_ws
$ catkin_make
$ source ~/catkin_ws/devel/setup.bash
### 1.4 Install the rbx2 code
$ cd ~/catkin_ws/src
$ git clone https://github.com/pirobot/rbx2.git
$ cd rbx2
$ git checkout indigo-devel
$ cd ~/catkin_ws
$ catkin_make
## 2. Installation
1. Clone this repository into catkin_ws/src:
`git clone https://github.com/NEU-TEAM/neuro_package.git`
3. Then run `catkin_make` to make all the packages.

## 3. Usage
1. Run `roscore` first.
2. Run launch file: `roslaunch neubro neuro_smach.launch` to launch the whole task planning system. 

## 5. Trouble Shooting
1.In the installation process, may be wrong, due to not properly installed the relevant package, you can follow the prompts to install the corresponding function package.
#change 1