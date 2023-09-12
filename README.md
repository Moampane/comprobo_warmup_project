# CompRobo WarmUp Project

## Project Overview
The goal of this project is to program the Neato robot to execute a set of behaviors using ROS 2 Humble. Through the implementation of these behaviors, we aim to gain practical experience with robotics programming, ROS, and debugging techniques.
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
Challenges: Terminating the teleop using Ctrl+C was proving difficult, but the skeleton code was helpful in getting it working.

![Teleop](https://github.com/Moampane/comprobo_warmup_project/blob/main/GIFs/Telep-min.gif)

### Behavior 3: Driving in a Square
Problem: We aim to make the robot move in a 1m by 1m square path.
Approach: We used the Neato's odometry to have it keep track of its position in x and y relative to the starting point. Once it determined it had move 1m forward, it turned 90 degrees to the left, doing this 3 times to drive in a square.
Challenges: None for this stage (except an odd interaction with the odom getting strange values if running a different behaviour prior to Drive-Squre).

![Driving in a Square](https://github.com/Moampane/comprobo_warmup_project/blob/main/GIFs/Drive-Square-min.gif)

### Behavior 4: Wall Following
Problem: The objective is to make the robot follow a wall while maintaining a parallel alignment to the wall.
Approach: We implemented a control strategy that checks the distance value from the laser scan at 45 and 135 degrees (relative to the Neato from the wall). It compares the difference to a pre-defined threshold, with turning adjustments made based on the proximity to the wall.
Challenges: Accurate wall detection, as the laser scan would often pick up unexpected 0.0 readings causing the Neato to go into a continuous left-right loop without any forward progress; we fixed this by havinhg it constantly moving forwards at a slower speed, turning to adjust itslef as required.

![Wall Follower](https://github.com/Moampane/comprobo_warmup_project/blob/main/GIFs/Wall-Follower-min.gif)

### Behavior 5: Finite State Controller
Problem: We need to create a finite state controller for managing different robot behaviors and transitions between states.
Approach: We'll define states, actions, and transitions for the controller. The states could include behaviors like teleoperation, square driving, and wall following. Transitions between states will depend on certain conditions, such as user input or sensor data.
Challenges: Designing a robust state machine, defining clear state transition criteria.

## Challenges Faced
During the project, we encountered various challenges such as:
Precise control of robot motion for tasks like driving in a square.
Handling user input effectively for teleoperation.
Accurate detection and control for wall following.

## Future Improvements
If we had more time, we would consider the following improvements:
Enhancing the user interface for teleoperation.
Fine-tuning control algorithms for smoother motion.

## Key Takeaways
From this project, we have learned valuable lessons for future robotic programming projects:
ROS and Robot Control: Gained proficiency in ROS and its usage for controlling robots.
Python Programming: Enhanced our Python programming skills in the context of robotics.
Debugging Techniques: Learned effective debugging strategies, especially using RViz.
Sensor Integration: Explored the integration of sensor data into robot control algorithms.
