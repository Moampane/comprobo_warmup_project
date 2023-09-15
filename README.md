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

<p align="center">
<img src = "https://mermaid.ink/img/pako:eNp1kM1qwzAQhF9F7CkBx_VvilUoxM6lh7bQJJdiCGq8SQyRZCyZ1k387pVkTHupEGj0zezC7hUOskKgcGpZcybb9UMpSkGI6j5G8va6ifYvJqMs_mNs8YKycdboELKazUZKCkPn84nnE_9FhUGftdITQVFZ4R4rVmSxeLztFLbkSTSdvpHc4tzhE0qOuu33XJ3UnetzI4X1i_99Uw8ecGw5qysz8NXmS9Bn5FgCNbLCI-suuoRSDCbKOi03vTgA1W2HHnRNxTSua2bm50CP7KIMxarWsn0el-h26UHDxLuUfCo0X6BX-AKa-kGYheYGSZZEyyDxoAe6jP0kTtMoCw2K4vssHTz4dg0CPxtPEsRZakPDD4zGhZY?type=pnghttps://mermaid.live/edit#pako:eNp1kM1qwzAQhF9F7CkBx_VvilUoxM6lh7bQJJdiCGq8SQyRZCyZ1k387pVkTHupEGj0zezC7hUOskKgcGpZcybb9UMpSkGI6j5G8va6ifYvJqMs_mNs8YKycdboELKazUZKCkPn84nnE_9FhUGftdITQVFZ4R4rVmSxeLztFLbkSTSdvpHc4tzhE0qOuu33XJ3UnetzI4X1i_99Uw8ecGw5qysz8NXmS9Bn5FgCNbLCI-suuoRSDCbKOi03vTgA1W2HHnRNxTSua2bm50CP7KIMxarWsn0el-h26UHDxLuUfCo0X6BX-AKa-kGYheYGSZZEyyDxoAe6jP0kTtMoCw2K4vssHTz4dg0CPxtPEsRZakPDD4zGhZY" height = "200"/>
</p>  

<p align="left">
<img src = "https://github.com/Moampane/comprobo_warmup_project/blob/main/GIFs/Telep-min.gif" height ="400"/>
</p>

### Behavior 3: Driving in a Square
Problem: We aim to make the robot move in a 1m by 1m square path.

Approach: We used the Neato's odometry to have it keep track of its position in x and y relative to the starting point. Once it determined it had move 1m forward, it turned 90 degrees to the left, doing this 3 times to drive in a square.

Challenges: None for this stage (except an odd interaction with the odom getting strange values if running a different behaviour prior to Drive-Squre).

<p align="center">
<img src = "https://mermaid.ink/img/pako:eNp1UVtrwjAU_ivhPEWorvbiaAYDta-boD6NgkRzrAWbuDR1c-p_X9pQ1sEW8pB8N77kXGGnBAKDXPPTgazTp0xmkpCq3jpkuVgFm1erqRq4R6S6OONm9V5zja3A8YRMKV0IVaLRl8GgA2eUtgbiDD_EnNL1R1GZDkEpXIN-B1Vted45UkqXuFNaoCApN_yXsxcwJcPh803y86as8uqh63Qjs4adtWyODnSStsiNzBt-_j_f8_-RnmYSPChRl7wQ9mOvjToDc8ASM2D2KHDP66PJIJN3K-W1UauL3AEzukYP6pPgBtOC28eXwPb8WFkURWGUfnHDamfmwYnLN6XKzmivwK7wCSwe-eNkbLcfJVEw8SMPLsAm4SgK4zhIxhYKwsckvnvw1Qb4o8StyA-TuBHdvwH48qha?type=png)](https://mermaid.live/edit#pako:eNp1UVtrwjAU_ivhPEWorvbiaAYDta-boD6NgkRzrAWbuDR1c-p_X9pQ1sEW8pB8N77kXGGnBAKDXPPTgazTp0xmkpCq3jpkuVgFm1erqRq4R6S6OONm9V5zja3A8YRMKV0IVaLRl8GgA2eUtgbiDD_EnNL1R1GZDkEpXIN-B1Vted45UkqXuFNaoCApN_yXsxcwJcPh803y86as8uqh63Qjs4adtWyODnSStsiNzBt-_j_f8_-RnmYSPChRl7wQ9mOvjToDc8ASM2D2KHDP66PJIJN3K-W1UauL3AEzukYP6pPgBtOC28eXwPb8WFkURWGUfnHDamfmwYnLN6XKzmivwK7wCSwe-eNkbLcfJVEw8SMPLsAm4SgK4zhIxhYKwsckvnvw1Qb4o8StyA-TuBHdvwH48qha" height = "500"/>
</p>  

<p align="left">
<img src = "https://github.com/Moampane/comprobo_warmup_project/blob/main/GIFs/Drive-Square-min.gif" height ="400"/>
</p>

### Behavior 4: Wall Following
Problem: The objective is to make the robot follow a wall while maintaining a parallel alignment to the wall.

Approach: We implemented a control strategy that checks the distance value from the laser scan at 45 and 135 degrees (relative to the Neato from the wall). It compares the difference to a pre-defined threshold, with turning adjustments made based on the proximity to the wall.

Challenges: Accurate wall detection, as the laser scan would often pick up unexpected 0.0 readings causing the Neato to go into a continuous left-right loop without any forward progress; we fixed this by havinhg it constantly moving forwards at a slower speed, turning to adjust itslef as required.

<p align="center">
<img src = "https://mermaid.ink/img/pako:eNqFkm9L6zAYxb9KeF5FqLNbW6UVBLfuvrp6YRMFKYzHNdZgm4wk1but--4mDcU_KJZCk3N-5wmnZA9rWTLIoFK4eSI3-XkhCkGIbh-8svi3nKyuLaOd_MG4w7pe_ZF1LV-Z6gkPEHJJ6V_UTJHlGsXR0SBPKXUZMmTenRmlN69cm0Fhovxy2OKW7wY6p_SW6xZrvkPDpSBXqJ7fx30TlvoBqyE-p3TB1lKVrCQ5GvyS6z9ucUmOjy86zYSWatXoSp_0pVynjkwdMe2JismGGbX1TN-jIzPnz372p_4MP-HlYxuP-UodyR2V_0Z9mubLcVH17Toyd9b8W8vmIICGqQZ5ae_A3qEFmCfWsAIyuyzZI7a1KaAQB4tia-RyK9aQGdWyANpNiYblHO2PbiB7xFpblZXcSHXl71V_vQLYoLiXshmCdgvZHv5DlozCcTq2bxin8eQ0jAPYQnYajeIoSSbp2EqT6CxNDgHs-gHhKPVPHEZpYqHo8AYW9OEp?type=png)](https://mermaid.live/edit#pako:eNqFkm9L6zAYxb9KeF5FqLNbW6UVBLfuvrp6YRMFKYzHNdZgm4wk1but--4mDcU_KJZCk3N-5wmnZA9rWTLIoFK4eSI3-XkhCkGIbh-8svi3nKyuLaOd_MG4w7pe_ZF1LV-Z6gkPEHJJ6V_UTJHlGsXR0SBPKXUZMmTenRmlN69cm0Fhovxy2OKW7wY6p_SW6xZrvkPDpSBXqJ7fx30TlvoBqyE-p3TB1lKVrCQ5GvyS6z9ucUmOjy86zYSWatXoSp_0pVynjkwdMe2JismGGbX1TN-jIzPnz372p_4MP-HlYxuP-UodyR2V_0Z9mubLcVH17Toyd9b8W8vmIICGqQZ5ae_A3qEFmCfWsAIyuyzZI7a1KaAQB4tia-RyK9aQGdWyANpNiYblHO2PbiB7xFpblZXcSHXl71V_vQLYoLiXshmCdgvZHv5DlozCcTq2bxin8eQ0jAPYQnYajeIoSSbp2EqT6CxNDgHs-gHhKPVPHEZpYqHo8AYW9OEp"/>
</p>

<p align="left">
<img src = "https://github.com/Moampane/comprobo_warmup_project/blob/main/GIFs/Wall-Follower-min.gif" height ="400"/>
</p>

### Behavior 6: Person Following

[![](https://mermaid.ink/img/pako:eNqNU11vmzAU_SvWfXIl2oV80I5Jk5LQ9GXZpqXaw4SEPHxLrYEd2aZdEvLfZ0BWgqYue4Nzz7nn-IAPkCuOEEOh2faZPCYfUplKQkz9s0e-fdmMs8-OY1r4bPAVtVEyW6myVK-oO05PIWRO6SdmUJNNzuTVlYcXlPYq4lWn2ZLSx1dhrEdQ8j7JeZYXsR_4JJS22EXNd2FqVoo9s0JJL76ndICTNRrDCjT_XIe50lzIYpBj5XL4wWU18ixhlnnxgxcjJy0-WHC2Z06urz82BqVROqtMYd51HbcVN2TRMhYdo0BVodW7ntOV2pDlaf5yfuietGb6F-qG3J9Yb_h0jOXbPl2O5L98LrDmWrPdIJL27XHXUmbVVuQNWbXz1V-RfaNtoQ15SCUEUKGumODuZz-0ohTsM1aYQuweOT6xurQppPLoqKy2arOTOcRW1xhAvXWemAjmvmMF8RMrjUORC6v0ur9A3T0KYMvkD6UqL3SvEB_gN8RhdPN-NrudzSbRJIpGUTgNYAfxdHxzG44n49HddDS5C0fTYwD7bkF4_AMArS58?type=png)](https://mermaid.live/edit#pako:eNqNU11vmzAU_SvWfXIl2oV80I5Jk5LQ9GXZpqXaw4SEPHxLrYEd2aZdEvLfZ0BWgqYue4Nzz7nn-IAPkCuOEEOh2faZPCYfUplKQkz9s0e-fdmMs8-OY1r4bPAVtVEyW6myVK-oO05PIWRO6SdmUJNNzuTVlYcXlPYq4lWn2ZLSx1dhrEdQ8j7JeZYXsR_4JJS22EXNd2FqVoo9s0JJL76ndICTNRrDCjT_XIe50lzIYpBj5XL4wWU18ixhlnnxgxcjJy0-WHC2Z06urz82BqVROqtMYd51HbcVN2TRMhYdo0BVodW7ntOV2pDlaf5yfuietGb6F-qG3J9Yb_h0jOXbPl2O5L98LrDmWrPdIJL27XHXUmbVVuQNWbXz1V-RfaNtoQ15SCUEUKGumODuZz-0ohTsM1aYQuweOT6xurQppPLoqKy2arOTOcRW1xhAvXWemAjmvmMF8RMrjUORC6v0ur9A3T0KYMvkD6UqL3SvEB_gN8RhdPN-NrudzSbRJIpGUTgNYAfxdHxzG44n49HddDS5C0fTYwD7bkF4_AMArS58)

### Behavior 7: Finite State Controller
Problem: We need to create a finite state controller for managing different robot behaviors and transitions between states.

Approach: We'll define states, actions, and transitions for the controller. The states include behaviors Wall Following and Person Following behaviors. Transitions between states will depend on certain conditions, such as user input or sensor data.

Challenges: 

<p align="center">
<img src = "https://mermaid.ink/img/pako:eNq1VFtv2jAU_iuWn1yJMu6QTJrEJeltbFOpNmmKFHnklFpLbGQ77YDw3-c4jYANSB-2PKDwne9yzrHiDZ6LCLCLF5Iun9DD5H3AA46QSn8UyP3nWSv8ZDgqh_cK32gch76IY_EC0jIKAkJDQj5SBRLN5pRfXJTwiJBcg0rNrjIm5OGFKV0iwKOii724LyCV4McDJ8cDPUIK1ZFI_w2RPuNMQzjT1PyOBdfS2PwRfUVIQUOWhna0c873z2x9YHNNSI5Var4yldKYralmgpfiG0IOcDQFpegC1Fk7mAsZMb446OPW9FEWqtUQhROqaSm-K8UQoRw_MNjzGaLLyw-ZAq6EDBO1UO_s6eWHl6FRzhhZxgJEAlquCo49rgyNd_Xn_aEL0pTKnyAzdLNjncixjPHpHNvH9ZtyKlhDKenqoCVZbi8yWwq1WLJ5hm7zuv9Xy-VG84Vm6K7Y4OTcZF7O8E5P5u_qVZN5lRv0T-d4_2WD3r_Z4FVBs5-2lpQrZkNfnUbVFDMdruEEZEJZZO7PTS4JsH6CBALsmtcIHmka6wAHfGuoNNVituJz7GqZQg2nS9M7TBg1X1SC3UcaK4NCxLSQ0-JOtldzDS8p_y5EUgrNX-xu8C_stuptp9XpdAdOx-m1Gr1uv4ZXBu479U6v6TT6TsPpNpr9bQ2vrUGj7rw-rfag03Tag-1vwvH98Q?type=png)](https://mermaid.live/edit#pako:eNq1VFtv2jAU_iuWn1yJMu6QTJrEJeltbFOpNmmKFHnklFpLbGQ77YDw3-c4jYANSB-2PKDwne9yzrHiDZ6LCLCLF5Iun9DD5H3AA46QSn8UyP3nWSv8ZDgqh_cK32gch76IY_EC0jIKAkJDQj5SBRLN5pRfXJTwiJBcg0rNrjIm5OGFKV0iwKOii724LyCV4McDJ8cDPUIK1ZFI_w2RPuNMQzjT1PyOBdfS2PwRfUVIQUOWhna0c873z2x9YHNNSI5Var4yldKYralmgpfiG0IOcDQFpegC1Fk7mAsZMb446OPW9FEWqtUQhROqaSm-K8UQoRw_MNjzGaLLyw-ZAq6EDBO1UO_s6eWHl6FRzhhZxgJEAlquCo49rgyNd_Xn_aEL0pTKnyAzdLNjncixjPHpHNvH9ZtyKlhDKenqoCVZbi8yWwq1WLJ5hm7zuv9Xy-VG84Vm6K7Y4OTcZF7O8E5P5u_qVZN5lRv0T-d4_2WD3r_Z4FVBs5-2lpQrZkNfnUbVFDMdruEEZEJZZO7PTS4JsH6CBALsmtcIHmka6wAHfGuoNNVituJz7GqZQg2nS9M7TBg1X1SC3UcaK4NCxLSQ0-JOtldzDS8p_y5EUgrNX-xu8C_stuptp9XpdAdOx-m1Gr1uv4ZXBu479U6v6TT6TsPpNpr9bQ2vrUGj7rw-rfag03Tag-1vwvH98Q"/>
</p>

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
