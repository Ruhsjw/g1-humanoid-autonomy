# Evaluation and known limits

Release checks cover Python syntax, launch XML, credential handling and the offline audit tests. They do not establish end-to-end ROS execution, hardware operation or current cloud-provider compatibility.

The supplied detector dataset contains 100 training and 18 validation images. SHA-256 comparison found 12 validation images identical to training images. Data and weights are intentionally not republished. Split future evaluation by independent capture sequence or scene, remove duplicate images and report per-class metrics.

Compare three separately labeled conditions: Gazebo-ground-truth behavior baseline, raw visual localization, and visual plus simulated-motion fusion. Record initial robot/ball poses, goal definition, time limit, trial count, ball crossing, falls and completion time. The fusion branch's Gazebo input must be disclosed.

Priorities: continuous ball updates; stale-measurement handling; robust landmark association; synchronized RGB-D; independent odometry; behavior recovery; a goal-line scoring test; and a validated voice-to-navigation bridge. These are future work, not completed features.
