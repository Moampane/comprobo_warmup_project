# CompRobo WarmUp Project

## Project Overview
The goal of this project is to program the Neato robot to execute a set of behaviors using ROS 2 Humble. Through the implementation of these behaviors, we aim to gain practical experience with robotics programming, ROS2, and debugging techniques. 6 Behaviours were implemented on the Neato in this endeavour:
1. [Teleoperation](#behavior-1-teleoperation)
2. [Driving in a Square](#behavior-2-driving-in-a-square)
3. [Wall Following](#behavior-3-wall-following)
4. [Person Following](#behavior-4-person-following)
5. [Obstacle Avoidance](#behavior-5-obstacle-avoidance)
6. [Finite-State Controller](#behavior-6-finite-state-controller)

## Behavior Descriptions
### Behavior 1: Teleoperation
<p align="center">
  <table style="border-collapse: collapse;">
    <tr>
      <td align="center" style="border: none;">
        <a href="https://mermaid.live/edit#pako:eNpFkWFP4kAQhv_KZr6ASSWFugV7ickJiMhpjPDpWnNZ2cFubHeb7VYPCf_d7YCyn56ZeWfyzs4O1kYiJPBqRZWz1eRXphn7nS6dsO655evuXCunRKE-kXUcFmiqDnvwXWdtedwdWxQO2WPzUqg6R8s2xrLOupT_3rHokGiSHkUrVaKlsdP0qdHsjzEVhTe7GTq2wO2-jWbpOMf1WxtT9TY9TmerD1U7do91LV6RavP00Sr9k6speZcu88ZJ86GZ0e2YFyOsnGuH1jbVYbFFOtXSEy3Mzs-v2DXtSzg-4YQ2IJySc8Ibck04I8uEtyeck7lT20F7R-4IF7TZtwAC8F9TCiX9MXZtKQOXY4kZJB4lbkRTuAwyvfdS0Tiz3Oo1JM42GEBTSf-9EyX8GUtINqKofRalcsbeHw5Mdw6gEvqvMeV3ow8h2cF_SPpRvzcY8Wh0weNwyHkcBbD16bAXDiIehXzAh_GQx5f7AD5pQr8XHh6_jMOLOBrtvwDherDF?type=png">
          <img src="https://mermaid.ink/img/pako:eNpFkWFP4kAQhv_KZr6ASSWFugV7ickJiMhpjPDpWnNZ2cFubHeb7VYPCf_d7YCyn56ZeWfyzs4O1kYiJPBqRZWz1eRXphn7nS6dsO655evuXCunRKE-kXUcFmiqDnvwXWdtedwdWxQO2WPzUqg6R8s2xrLOupT_3rHokGiSHkUrVaKlsdP0qdHsjzEVhTe7GTq2wO2-jWbpOMf1WxtT9TY9TmerD1U7do91LV6RavP00Sr9k6speZcu88ZJ86GZ0e2YFyOsnGuH1jbVYbFFOtXSEy3Mzs-v2DXtSzg-4YQ2IJySc8Ibck04I8uEtyeck7lT20F7R-4IF7TZtwAC8F9TCiX9MXZtKQOXY4kZJB4lbkRTuAwyvfdS0Tiz3Oo1JM42GEBTSf-9EyX8GUtINqKofRalcsbeHw5Mdw6gEvqvMeV3ow8h2cF_SPpRvzcY8Wh0weNwyHkcBbD16bAXDiIehXzAh_GQx5f7AD5pQr8XHh6_jMOLOBrtvwDherDF?type=png" />
        </a>
      </td>
      <td align="center" style="border: none;">
        <a href="https://github.com/Moampane/comprobo_warmup_project/blob/main/GIFs/Telep-min.gif">
          <img src="https://github.com/Moampane/comprobo_warmup_project/blob/main/GIFs/Telep-min.gif" height="400" />
        </a>
      </td>
    </tr>
  </table>
</p>



Teleoperation, often referred to as "teleop," is a crucial aspect of controlling mobile robots remotely via network connectivity. The implementation of teleop enables manual control of a mobile robot by commanding its velocity through the ROS2 network. This approach allows operators to remotely steer the robot, making it a valuable tool for various applications, such as robot testing, exploration, or monitoring. 

We wrote a ROS node that listens to keyboard input and publishes commands to control the robot's motion. This includes commands to move forward (mapped to W), backward (mapped to S), turn left (mapped to A), turn right (mapped to D), and stop (mapped to Ctrl+C). 

Implementing a robust and responsive teleoperation system presented its challenges. Notably, designing a non-blocking protocol for capturing keypresses from the operating system required a dedicated approach. The use of the 'select' function to determine the readiness of the input stream proved unreliable, often ignoring user inputs. To overcome this issue, a separate loop dedicated to reading input was introduced. This loop operates in parallel with other teleoperation logic, ensuring that keypresses are consistently detected and processed, ultimately enhancing the reliability and responsiveness of the teleop system.

### Behavior 2: Driving in a Square
<p align="center">
  <table style="border-collapse: collapse;">
    <tr>
      <td align="center" style="border: none;">
        <a href="https://mermaid.live/edit#pako:eNpdkm1v2jAQx7-KdW_opLQiHdCQF5NaoDy0nbrRvtiSCRl8gCXHZo5NRxHfvc6lKNLe_X33u0ffEVZGIKSwsXy3ZS_DXDN2m80dt-5Ppe8uplo6yZV8R9YSVu5xUf713GKLfQ-hXypocDGwyB2yZ79UstyiZWtjWWtViMUeVYug4Rma-2W5snJ5powwRY2Msk_kRRZoqf59tuVaKFxUFDp7IOs4e90JKmjK0J3RLEDsVm8Ukn-SWa8XypgdPafZGDVayvwmS8eesCz5pmZn2cBoZ41iP83S1FM_VLY9Wsd--BBldVXCGfaLv5H_MRtpERRti11efmN3tCySg0YOGzmiHZC8p8FIjmmaJsOI5IRmIDml_knOqNuGrTM8UL9NskkDzP7v7BEiCIstuBThy4-VIwe3xQJzSIMUuOZeuRxyfQoo987MD3oFqbMeI_C086Hk4VgKSNdclcGKQjpjn-ozomuKYMf1b2OKc2B4QnqEf5D2rvpxcnOdJEm_3et9bccRHCDt966u20mnG8ft7k2n0z1F8E7h8ekDFczMDg?type=png">
          <img src="https://mermaid.ink/img/pako:eNpdkm1v2jAQx7-KdW_opLQiHdCQF5NaoDy0nbrRvtiSCRl8gCXHZo5NRxHfvc6lKNLe_X33u0ffEVZGIKSwsXy3ZS_DXDN2m80dt-5Ppe8uplo6yZV8R9YSVu5xUf713GKLfQ-hXypocDGwyB2yZ79UstyiZWtjWWtViMUeVYug4Rma-2W5snJ5powwRY2Msk_kRRZoqf59tuVaKFxUFDp7IOs4e90JKmjK0J3RLEDsVm8Ukn-SWa8XypgdPafZGDVayvwmS8eesCz5pmZn2cBoZ41iP83S1FM_VLY9Wsd--BBldVXCGfaLv5H_MRtpERRti11efmN3tCySg0YOGzmiHZC8p8FIjmmaJsOI5IRmIDml_knOqNuGrTM8UL9NskkDzP7v7BEiCIstuBThy4-VIwe3xQJzSIMUuOZeuRxyfQoo987MD3oFqbMeI_C086Hk4VgKSNdclcGKQjpjn-ozomuKYMf1b2OKc2B4QnqEf5D2rvpxcnOdJEm_3et9bccRHCDt966u20mnG8ft7k2n0z1F8E7h8ekDFczMDg?type=png" />
        </a>
      </td>
      <td align="center" style="border: none;">
        <a href="https://github.com/Moampane/comprobo_warmup_project/blob/main/GIFs/Drive-Square-min.gif">
          <img src="https://github.com/Moampane/comprobo_warmup_project/blob/main/GIFs/Drive-Square-min.gif" height="400" />
        </a>
      </td>
    </tr>
  </table>
</p>

The task of guiding a robot to traverse a square path represents a fundamental navigation challenge. This behavior requires the robot to follow a predefined trajectory while adjusting its orientation and linear movement at specific corners of the square. To address this challenge, the implementation adopts a closed-loop control strategy, relying on feedback from odometry data to maintain accurate position and orientation tracking. The 'DriveSquareNode' node is the core of this implementation, orchestrating the robot's movements.

One of the primary challenges is ensuring that the robot accurately follows the square's path while considering its position and orientation. In this regard, the implementation leans on the 'odom' topic, which provides odometry data crucial for tracking the robot's state. Despite the accumulation of error over time in wheel encoders, this approach proves suitable for the relatively simple square trajectory.

One noteworthy aspect of the code is the determination of when the robot should adjust its linear and angular velocities. The logic in the 'run_loop' function carefully considers the robot's position within the square, using conditional statements to decide whether it should move forward, turn, or stop. These decisions are essential to ensure that the robot accurately follows the square's path and completes the traversal successfully.

While the code implementation is relatively straightforward, it still presents challenges in achieving smooth square traversal. For instance, the abrupt correction of yaw errors during corner turns may lead to slight distortions in the square's shape. To enhance the robustness of the behavior, further refinement could involve incorporating a PID controller and fine-tuning its parameters. Such adjustments would help mitigate discontinuous yaw error corrections, resulting in a more precise square path.

### Behavior 3: Wall Following
<div align="center">
  <table style="border-collapse: collapse; display: inline-block;">
    <tr>
      <td align="center" style="border: none;">
        <a href="https://mermaid.live/edit#pako:eNpdkW9v2jAQxr-KdW_opLSCBAhk0qSW8K-i0zTQXiyZqltygCXHRo4zShHffc61E1P96ue7587P-c5QmJIggZ3Fw15s0s-5FuI-Wzu07lfLDzdLLZ1EJV9JdI6o1PPWKGWOZDviqy_-1KomNxNL6Eh8a34rWe_Jiq2xolNU5fMfUh0Wpdm7aCMrstx9mn1vtFgZc-Dr7LxAXSoSK6zJrgvUIkWHlzY3zyaoika1De71zoMVP0iZQroTFy_-E6ykpo_5ZfZuTmyOsnbiieoad8S5x2yqS088vbi9_SIeeHjGyRVTnoNxyv4ZZ-ydcc5WGRdsinHJ71_L5lecfWz2mGsIwH9QhbL0mzm3qRzcnirKIfFY0hYb5XLI9cVLsXFmfdIFJM42FEBzKP0XpBL9TitItqhqH6VSOmOf3rbNSw_ggPqnMdW_Qn-F5AwvkITx4C7ujsNx2IviMO72BgGcIGmDo2gYjsZR2B8P494lgFdu0Lvrvp0oGg36_WEYXf4CHfi2Gg?type=png">
          <img src="https://mermaid.ink/img/pako:eNpdkW9v2jAQxr-KdW_opLSCBAhk0qSW8K-i0zTQXiyZqltygCXHRo4zShHffc61E1P96ue7587P-c5QmJIggZ3Fw15s0s-5FuI-Wzu07lfLDzdLLZ1EJV9JdI6o1PPWKGWOZDviqy_-1KomNxNL6Eh8a34rWe_Jiq2xolNU5fMfUh0Wpdm7aCMrstx9mn1vtFgZc-Dr7LxAXSoSK6zJrgvUIkWHlzY3zyaoika1De71zoMVP0iZQroTFy_-E6ykpo_5ZfZuTmyOsnbiieoad8S5x2yqS088vbi9_SIeeHjGyRVTnoNxyv4ZZ-ydcc5WGRdsinHJ71_L5lecfWz2mGsIwH9QhbL0mzm3qRzcnirKIfFY0hYb5XLI9cVLsXFmfdIFJM42FEBzKP0XpBL9TitItqhqH6VSOmOf3rbNSw_ggPqnMdW_Qn-F5AwvkITx4C7ujsNx2IviMO72BgGcIGmDo2gYjsZR2B8P494lgFdu0Lvrvp0oGg36_WEYXf4CHfi2Gg?type=png" />
        </a>
      </td>
      <td align="center" style="border: none;">
        <a href="https://github.com/Moampane/comprobo_warmup_project/blob/main/GIFs/Wall-Follower-min.gif">
          <img src="https://github.com/Moampane/comprobo_warmup_project/blob/main/GIFs/Wall-Follower-min.gif" height="400" />
        </a>
      </td>
    </tr>
  </table>
</div>

The Wall Following behavior is a fundamental capability for mobile robots operating in indoor environments, as it allows them to navigate and follow along walls while maintaining a safe distance. In this implementation, we aim to create a robust Wall Follower using ROS2 and a LaserScan sensor. To begin with, the Wall Follower node is initialized as a ROS2 node, and a publisher is created to send Twist messages to control the robot's velocity. Additionally, a subscription to the 'scan' topic is established to receive LaserScan data, which is crucial for detecting obstacles and calculating the distance from the walls. 

One of the key challenges in Wall Following is handling the LaserScan data effectively. In the handle_scan callback function, the code extracts relevant scan data from specific angles (45 degrees and 135 degrees) to determine the distances from the front right and front left of the robot, respectively. This information is then used to make decisions about adjusting the robot's orientation. The core of the Wall Following behavior lies in the run_loop function. It calculates the angular velocity based on the difference in distances from the right and left sides of the robot, effectively determining if the robot needs to turn to maintain a specific distance from the wall. This angular adjustment ensures that the robot follows the wall closely without colliding with it. In addition to the angular velocity control, linear velocity is set to maintain a constant forward motion while wall following. This ensures that the robot continues to navigate along the wall in a stable manner. 

One noteworthy aspect of this implementation is its simplicity and efficiency. It efficiently computes the angular velocity based on the difference in distances from the LaserScan data, allowing the robot to smoothly follow walls.

### Behavior 4: Person Following
<div align="center">
  <table style="border-collapse: collapse; display: inline-block;">
    <tr>
      <td align="center" style="border: none;">
        <a href="https://mermaid.live/edit#pako:eNpdkm9v2jAQxr-K5Td0Eq2AtoAyaRIltNACrQbaizlTZeKDeHPsyH9KKeK7z1zKkPYm-vnuOTv33O1pbgTQhG4srwqyTL9mmpABW3hu_a8j311MtPSSK_kBpFGBdUa_ro1SZgu2Qeax_MtRN7wYWuAeyEtYKekKsGRtLGnkpXh9A9VAUXoSLcLK5VauTiqXc11LRuxTspQlWPyFezbmWiggU-7ALqKUpNxzzD2wIVd5UHhpYawH50kqnec6B1SM2fegydSYCo8TNiwg_0MmWsA7Rh7ZQPwOsWygN_EiS36AMrn0O8w-nbJTqeH_5JR9dkuW2_gmmYFzfFO_O2MvVup_MYfBOVsUwQuz1cRo8gS7leFWTLQHa0NVO_7MRlpEwkmQy8tv5A4HgTg8Y3rGEZqLeI-OIT6gQYhjdAJxgi4gPmL7iE_YK-IUO0OcYSPnG-qyOXaC-Jxp2qRxUCWXIq7R_pjKqC-ghIwmEQWseVA-o5k-RCkP3ix2OqeJtwGaNFQiji6VPC5gSZM1Vy5GQUhv7KxeTdzQJq24_mlMeSqMR5rs6TtNOtfXV73bTq_VbvVb7W6r36Q7mtxetXudm363V3-7N4cm_cD69uEveJjriA?type=png">
          <img src="https://mermaid.ink/img/pako:eNpdkm9v2jAQxr-K5Td0Eq2AtoAyaRIltNACrQbaizlTZeKDeHPsyH9KKeK7z1zKkPYm-vnuOTv33O1pbgTQhG4srwqyTL9mmpABW3hu_a8j311MtPSSK_kBpFGBdUa_ro1SZgu2Qeax_MtRN7wYWuAeyEtYKekKsGRtLGnkpXh9A9VAUXoSLcLK5VauTiqXc11LRuxTspQlWPyFezbmWiggU-7ALqKUpNxzzD2wIVd5UHhpYawH50kqnec6B1SM2fegydSYCo8TNiwg_0MmWsA7Rh7ZQPwOsWygN_EiS36AMrn0O8w-nbJTqeH_5JR9dkuW2_gmmYFzfFO_O2MvVup_MYfBOVsUwQuz1cRo8gS7leFWTLQHa0NVO_7MRlpEwkmQy8tv5A4HgTg8Y3rGEZqLeI-OIT6gQYhjdAJxgi4gPmL7iE_YK-IUO0OcYSPnG-qyOXaC-Jxp2qRxUCWXIq7R_pjKqC-ghIwmEQWseVA-o5k-RCkP3ix2OqeJtwGaNFQiji6VPC5gSZM1Vy5GQUhv7KxeTdzQJq24_mlMeSqMR5rs6TtNOtfXV73bTq_VbvVb7W6r36Q7mtxetXudm363V3-7N4cm_cD69uEveJjriA?type=png" />
        </a>
      </td>
      <td align="center" style="border: none;">
        <a href="https://github.com/Moampane/comprobo_warmup_project/blob/main/GIFs/Person-Follower-min.gif">
          <img src="https://github.com/Moampane/comprobo_warmup_project/blob/main/GIFs/Person-Follower-min.gif" height="400" />
        </a>
      </td>
    </tr>
  </table>
</div>

The primary objective is to enable the robot to autonomously track and follow a human operator while maintaining a specified following distance. The code initializes a ROS2 node named 'person_follower,' which serves as the core controller for the behavior. Within this node, it sets up a publisher to control the robot's velocity by publishing to the 'cmd_vel' topic. Additionally, the node subscribes to laser scan data on the 'scan' topic, which is essential for human detection and tracking. Upon receiving laser scan data, the code processes it within the 'handle_scan' function. The primary purpose here is to identify the closest object within the specified detection range (greater than 0.15 meters). The distance to this detected object is recorded as 'shortest_dist' and is crucial for subsequent tracking decisions. The core tracking logic is encapsulated within the 'run_loop' function. It focuses on two critical aspects:
1. Angular Velocity Control: To align the robot with the detected human, the code calculates the angular velocity. It assesses whether the human is closer to one side of the robot and adjusts the angular velocity accordingly, ensuring that the robot follows the human's direction effectively.
2. Linear Velocity Control: A constant forward linear velocity of '0.1' is maintained to ensure the robot follows the human's movements smoothly.

The robot continually processes laser scan data to adapt to changes in the human's position and motion. If the laser scan data suggests that the human is either too close or too far from the robot, it adjusts its movement to maintain the desired following distance, thus ensuring the safety of the interaction. One notable aspect of the implementation is its modular design. Each feature is structured independently, allowing for unit testing of individual components. This modular approach significantly enhances the debugging process and contributes to overall robustness during development.

### Behavior 5: Obstacle Avoidance
<div align="center">
  <table style="border-collapse: collapse; display: inline-block;">
    <tr>
      <td align="center" style="border: none;">
        <a href="https://mermaid.live/edit#pako:eNptkl1v2jAUhv-K5Rs2Ka2aQQvNpEmU8FmYpoF6sWSqDs4BLDk2cpxuFPHf5xyGjKbdPfZ53_Olc-TCFMgTvrWw37FV-jnXjPWzpQPrfjb89GGqpZOg5DuylllXDoTCV3gzskDbYl-9_2MjHGQDi-CQrWSJlrzp5WtZryth5d5Jo9nGWDaHCu1SgCbd8KL7Vq-VrHZoSdQSZfH6hqpFolF21cgLWAlrhRWFxscJ6EJhSMtScHBqYpNsAErUitooQXmPY6n0Y2iB5J4ev9ea9ZuBmj82N1spyDu78vb11oNlL6iMkO5A1ucrwVxq_Dc-z_5OxFa_fEm2wKqC7bnsIhvqwhMtnN3cfGFPtG_CQcA04DDgiPZLOKYVEE5oYsIpjUY4C_hMXRPOqcFQYhZ-F6Ha2bYIecchA-EoCGb_EfCI-2soQRb-yI5NKOduhyXmPPFY4AZq5XKe65OXQu3M8qAFT5ytMeL1vvCrTSX48yx5sgFV-V8spDN2cT5cut-I70H_MKa8GP2TJ0f-mydxu3v76b7X6XZ7vXYn7tw9RPzAk85tL467j-347jG-77Xjh1PE3ylBfPoDp_fw6w?type=png">
          <img src="https://mermaid.ink/img/pako:eNptkl1v2jAUhv-K5Rs2Ka2aQQvNpEmU8FmYpoF6sWSqDs4BLDk2cpxuFPHf5xyGjKbdPfZ53_Olc-TCFMgTvrWw37FV-jnXjPWzpQPrfjb89GGqpZOg5DuylllXDoTCV3gzskDbYl-9_2MjHGQDi-CQrWSJlrzp5WtZryth5d5Jo9nGWDaHCu1SgCbd8KL7Vq-VrHZoSdQSZfH6hqpFolF21cgLWAlrhRWFxscJ6EJhSMtScHBqYpNsAErUitooQXmPY6n0Y2iB5J4ev9ea9ZuBmj82N1spyDu78vb11oNlL6iMkO5A1ucrwVxq_Dc-z_5OxFa_fEm2wKqC7bnsIhvqwhMtnN3cfGFPtG_CQcA04DDgiPZLOKYVEE5oYsIpjUY4C_hMXRPOqcFQYhZ-F6Ha2bYIecchA-EoCGb_EfCI-2soQRb-yI5NKOduhyXmPPFY4AZq5XKe65OXQu3M8qAFT5ytMeL1vvCrTSX48yx5sgFV-V8spDN2cT5cut-I70H_MKa8GP2TJ0f-mydxu3v76b7X6XZ7vXYn7tw9RPzAk85tL467j-347jG-77Xjh1PE3ylBfPoDp_fw6w?type=png" />
        </a>
      </td>
      <td align="center" style="border: none;">
        <a href="https://github.com/Moampane/comprobo_warmup_project/blob/main/GIFs/Obstacle-Avoidance-min.gif">
          <img src="https://github.com/Moampane/comprobo_warmup_project/blob/main/GIFs/Obstacle-Avoidance-min.gif" height="400" />
        </a>
      </td>
    </tr>
  </table>
</div>

Obstacle avoidance is a fundamental component of mobile robot control systems, ensuring safe and efficient navigation. In this implementation, a modified potential field approach is employed to guide the robot's movements. The algorithm generates repulsive forces directed away from detected obstacles, with the strength of these forces inversely proportional to the distance between the robot and the obstacle. By incorporating these repulsive forces into the control system, the robot can intelligently avoid collisions with its surroundings. The implemented obstacle avoidance algorithm consists of the following key components:
1. Laser Scan Data: The robot receives laser scan data, which provides information about the distances to objects in its vicinity. These distance measurements are essential for identifying obstacles.
2. Repulsive Forces: Repulsive forces are calculated based on the detected obstacle distances. The algorithm considers both inner and outer regions around the robot to ensure comprehensive obstacle detection.
3. Turn Input: To determine the robot's angular velocity, the algorithm computes a turn input based on the repulsive forces. This input helps steer the robot away from obstacles.
4. Linear Velocity: The linear velocity is adjusted based on the closest detected obstacle's distance. If the closest obstacle is far away, the robot can move at a higher linear speed.

The initial implementation faced challenges when dealing with wide front-facing obstacles. The sum of repulsive forces sometimes led to undesirable behavior, such as erratic collisions or oscillatory movements. To address this issue, a tangential component was introduced into the potential field, originating from the center of the obstacle cluster. This addition provides an extra guiding force, encouraging the robot to navigate around obstacles effectively.

### Behavior 6: Finite State Controller
<p align="center">
<img src = "https://mermaid.ink/img/pako:eNp1lG1v2jAQx7_KyW_YJFoBLQVlW6fy0JbyUEpokRYm5CamsZbYkeNAW8R3n3MhM6q6N9Evzv_u_r5zvCO-DBhxyIuiSQjz3relALjyXE2V_p1z58tAcM1pxN8ZVNbcvLBVqql5-lJoJaOIqQpMTJqvub7rdRUzX2GaPUc8DZmCtVRQ8eNgtWFRBZP2SpGbPae-4onmUqBuRFOmXJ8K1PVL3ZzHTOHStXfkZ0GjCK6NBbnl4gWmVNGYaaZSlN78t0onixOU3Hou03DICG6-LdASKluTeLXGxGZ3KB0cF-7KTOiDo7vdLRVBxKx36FFN9_m3oTeIk4jFTOiPZjsspBsuixwj79Cuj6qujGOTvdjQuKyU-4f-xmTFKhPP3XLth2hdPpvp-BFbhVxXii1h8P3uYBq-Q_Mnxk29GduYbjEYy7w3qHv4p7v8AU0wBcEGNmpF5MybybJZVxvJA7g_lMUc7nGOMmZeuuxQ_88nXT7y-miMpWYwx21-8tww04HcCjxsuLbw-iIwhIcWTk4uoYNnFrFrsWexb_HG4q3FAR5QxDscL-LQ4gjPFuIYp4I4wUEg3mO7EacWH7C5iDOLLrYLcW7xEftl8dHaGVoPQ-th9KmdqS08s9WO8j4hLmwJxEXRKBEsBakS8-PFlAfmjtjlH5dEh-Y8L4ljMGBrmkV6SZZib6Q009J9Ez5xtMpYlWRJYCba49TcLjFx1jRKzSoLuJZqXNw7eP1USULFLynjMtC8EmdHXonTODs7bTUbrVq91q7VL2rtKnkjTvO03mqcty9axfPifF8l7xhf3_8FdHF-dg?type=png)](https://mermaid.live/edit#pako:eNp1lG1v2jAQx7_KyW_YJFoBLQVlW6fy0JbyUEpokRYm5CamsZbYkeNAW8R3n3MhM6q6N9Evzv_u_r5zvCO-DBhxyIuiSQjz3relALjyXE2V_p1z58tAcM1pxN8ZVNbcvLBVqql5-lJoJaOIqQpMTJqvub7rdRUzX2GaPUc8DZmCtVRQ8eNgtWFRBZP2SpGbPae-4onmUqBuRFOmXJ8K1PVL3ZzHTOHStXfkZ0GjCK6NBbnl4gWmVNGYaaZSlN78t0onixOU3Hou03DICG6-LdASKluTeLXGxGZ3KB0cF-7KTOiDo7vdLRVBxKx36FFN9_m3oTeIk4jFTOiPZjsspBsuixwj79Cuj6qujGOTvdjQuKyU-4f-xmTFKhPP3XLth2hdPpvp-BFbhVxXii1h8P3uYBq-Q_Mnxk29GduYbjEYy7w3qHv4p7v8AU0wBcEGNmpF5MybybJZVxvJA7g_lMUc7nGOMmZeuuxQ_88nXT7y-miMpWYwx21-8tww04HcCjxsuLbw-iIwhIcWTk4uoYNnFrFrsWexb_HG4q3FAR5QxDscL-LQ4gjPFuIYp4I4wUEg3mO7EacWH7C5iDOLLrYLcW7xEftl8dHaGVoPQ-th9KmdqS08s9WO8j4hLmwJxEXRKBEsBakS8-PFlAfmjtjlH5dEh-Y8L4ljMGBrmkV6SZZib6Q009J9Ez5xtMpYlWRJYCba49TcLjFx1jRKzSoLuJZqXNw7eP1USULFLynjMtC8EmdHXonTODs7bTUbrVq91q7VL2rtKnkjTvO03mqcty9axfPifF8l7xhf3_8FdHF-dg"/>
</p>

The Finite State Controller, implemented as the 'finite_state_controller' ROS2 node, combines two distinct behaviors, Wall Following and Bump Reaction, to provide adaptive navigation for the robot. The Wall Following behavior, integrated into this controller, is based on laser scan data. The node subscribes to the 'scan' topic, which provides distance measurements to obstacles around the robot. The algorithm calculates the difference in distances between the left and right sides, adjusting the angular velocity to follow a nearby wall smoothly. The code also employs a timer to execute this behavior periodically. 

Challenges in implementing Wall Following include fine-tuning the parameters to ensure the robot stays close to the wall without oscillating excessively. The 'difference' parameter determines when to adjust the angular velocity, striking a balance between stability and responsiveness. Additionally, efficient handling of laser scan data to minimize computational load is crucial for real-time performance. The second behavior, Bump Reaction, responds to collision events. The robot's bump sensors trigger a state change to 'obstacle_hit' when it collides with an object. During this state, the robot reverses for a short duration and then rotates to avoid the obstacle. After a predefined number of iterations, the controller switches back to Wall Following. 

The Finite State Controller effectively orchestrates these behaviors by switching between them based on the robot's state. When an obstacle is encountered, the controller seamlessly transitions from Wall Following to Bump Reaction, ensuring the robot responds appropriately to different environmental conditions. 

One noteworthy aspect is the need for careful synchronization between the two behaviors to prevent conflicts. The code ensures a smooth transition by setting the robot's velocity commands as needed for each behavior. Moreover, it incorporates a counter to manage the duration of the Bump Reaction, ensuring that the robot eventually returns to Wall Following mode.
