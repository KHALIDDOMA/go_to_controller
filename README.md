# go_to_controller

A ROS package to control a turtle in the turtlesim simulator, moving it to a specified goal position using custom control parameters.

## Features
- Moves the turtle to a goal position (`x_goal`, `y_goal`) in turtlesim.
- Allows user to set control parameters `beta` and `phi` at runtime.
- Uses ROS parameters and topics for communication.

## Installation
1. Clone this repository into your catkin workspace's `src` directory:
   ```bash
   cd ~/catkin_ws/src
   git clone <this-repo-url>
   ```
2. Build the workspace:
   ```bash
   cd ~/catkin_ws
   catkin_make
   ```
3. Source your workspace:
   ```bash
   source devel/setup.bash
   ```

## Usage
1. Launch the controller and turtlesim using the provided launch file:
   ```bash
   roslaunch my_robot_controller go_to_controller.launch
   ```
2. When prompted in the terminal, enter values for `beta` and `phi` (control gains).
3. The turtle will move to the goal position specified in `config/params.yaml`.

## Configuration
- Edit `config/params.yaml` to set the desired goal position and default control parameters:
  ```yaml
  x_goal: 1
  y_goal: 1
  beta: 0
  phi: 0
  ```
- You can also set these parameters at runtime using `rosparam` or by editing the YAML file before launching.

## Dependencies
- ROS (tested with ROS Noetic)
- `turtlesim`
- `rospy`
- `geometry_msgs`
