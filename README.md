# CompRobo WarmUp Project

## Project Overview
The goal of this project is to program the Neato robot to execute a set of behaviors using ROS 2 Humble. Through the implementation of these behaviors, we aim to gain practical experience with robotics programming, ROS, and debugging techniques. The behaviors include:

Simple visualizations using rviz
Teleoperation (Teleop)
Driving the robot in a square path
Wall following behavior
Finite state controller

## Code Structure
Our code is organized within a ROS package called warmup_project. The package structure includes the following directories and files:
warmup_project/
├── bags/
│   ├── drive_square_demo.bag
│   ├── finite_state_controller_demo.bag
│   ├── obstacle_avoider_demo.bag
│   ├── person_follower_demo.bag
│   ├── test_drive.bag
│   └── wall_follower_demo.bag
├── resource/
│   ├── warmup_project
├── test/
│   ├── test_copyright.py
│   ├── test_flake8.py
│   └── test_pep257.py
├── CMakeLists.txt
├── package.xml
├── setup.py
└── warmup_project/
    ├── __init__.py
    ├── teleop.py
    ├── drive_square.py
    ├── finite_state_controller.py
    ├── obstacle_avoider.py
    ├── person_follower.py
    ├── wall_follower.py
    └── README.md

This structure organizes our code, configuration files, and resources neatly within a ROS package.

## Behavior Descriptions
### Behavior 1: Simple Visualizations using RViz
Problem: The goal is to visualize data from the simulated Neato robot using RViz.
Approach: We connect to the Neato and configure RViz as follows:
Set the fixed_frame to odom.
Visualize the Neato's laser scan (topic /scan).
Visualize the Neato's position using the Robot Model visualization (topic robot_description).
Challenges: None at this stage.

### Behavior 2: Teleoperation (Teleop)
Problem: We need to teleoperate the robot using custom Python code.
Approach: We wrote a ROS node that listens to keyboard input and publishes commands to control the robot's motion. This includes commands to move forward, backward, turn left, turn right, and stop.
Challenges: Handling keyboard input and converting it into meaningful robot commands. After solving this, terminating the teleop using Ctrl+C was proving difficult, but the skeleton code was helpful in getting it working.

### Behavior 3: Driving in a Square
Problem: We aim to make the robot move in a 1m by 1m square path.
Approach: We can achieve this using either timed movements (e.g., turn at a fixed speed for a specific duration) or by utilizing the robot's odometry to control its path accurately.
Challenges: Precision control to ensure the robot follows the desired square path.

### Behavior 4: Wall Following
Problem: The objective is to make the robot follow a wall while maintaining a parallel alignment to the wall.
Approach: We'll implement a control strategy that enables the robot to move forward while adjusting its direction to remain parallel to the nearest wall.
Challenges: Accurate wall detection, maintaining a consistent distance from the wall.

### Behavior 5: Finite State Controller
Problem: We need to create a finite state controller for managing different robot behaviors and transitions between states.
Approach: We'll define states, actions, and transitions for the controller. The states could include behaviors like teleoperation, square driving, and wall following. Transitions between states will depend on certain conditions, such as user input or sensor data.
Challenges: Designing a robust state machine, defining clear state transition criteria.

## Challenges Faced
During the project, we encountered various challenges such as:
Precise control of robot motion for tasks like driving in a square.
Handling user input effectively for teleoperation.
Accurate detection and control for wall following.
Designing a robust finite state controller with clear state transitions.

## Future Improvements
If we had more time, we would consider the following improvements:
Enhancing the user interface for teleoperation.
Fine-tuning control algorithms for smoother motion.
Implementing obstacle avoidance strategies.
Integrating computer vision for advanced behaviors like person following.

## Key Takeaways
From this project, we have learned valuable lessons for future robotic programming projects:
ROS and Robot Control: Gained proficiency in ROS and its usage for controlling robots.
Python Programming: Enhanced our Python programming skills in the context of robotics.
Debugging Techniques: Learned effective debugging strategies, especially using RViz.
Sensor Integration: Explored the integration of sensor data into robot control algorithms.
Behavior Design: Designed and implemented reactive control strategies and finite state controllers for different robot behaviors.
