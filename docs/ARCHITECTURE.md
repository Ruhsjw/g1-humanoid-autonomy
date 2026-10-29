# Technical walkthrough

## Perception and localization

`robot_localizer.py` subscribes to `/camera/color/image_raw`, `/camera/depth/image_raw`, `/horizontal_camera/color/image_raw` and `/horizontal_camera/depth/image_raw`. Its entry point selects depth mode for both cameras and a 0.6 detection threshold. Depth is interpreted as uint16 millimeters. In its forward-X camera convention: X=d, Y=-(u-cx)d/fx, Z=-(v-cy)d/fy. Intrinsics are hardcoded (fx=fy=347.9975, cx=320, cy=240) and must match the camera configuration.

Goalposts use the box bottom midpoint; other classes use box centers. Extrinsics transform points into the robot frame. Horizontal-camera landmarks are associated with the known field layout using image ordering and class-specific rules. Least squares minimizes map-point minus transformed observed-point residuals over x, y, yaw. A single-landmark fallback fixes yaw to zero and is ambiguous. RGB and depth callbacks do not explicitly synchronize acquisition times.

The estimated robot pose maps the inclined-camera ball and horizontal-camera goalpost observations into the field frame. Two posts yield a midpoint; a single post is used directly as the target and can bias the goal location.

## Behavior

INIT → ROTATE_FOR_DETECTION → WAIT_FOR_DETECTION → NAVIGATE_TO_BALL → ADJUST_ORIENTATION → KICK_BALL → DONE.

For ball b and goal g, d=(g-b)/||g-b|| and approach point p=b-0.6d. Position tolerance is 0.15 m and orientation tolerance is 0.15 rad. The final action is walking contact, not a separate learned kick. Robot pose updates continuously but ball/goal callbacks latch their first measurements. The 0.1 m completion threshold measures robot-to-goal distance rather than ball scoring.

## Locomotion interface

The matching float-command adapter clips each incoming channel to [-1,1], applies lx=vx+0.120, ly=vy+0.025, rx=vyaw-0.034, then supplies [ly,-lx,-rx] to the policy. A fully zero input explicitly clears the command. Other supplied workspace versions use integer/incremental commands and must not be mixed with this behavior.

The 47 observations comprise gyro 3, projected gravity 3, velocity condition 3, joint position 12, joint velocity 12, previous action 12 and phase 2. Targets are q_default+0.25*action. PD tracking handles execution. Nominal rates are 50 Hz policy and 500 Hz main loop, not measured real-time guarantees.

## Optional fusion

State: [x,y,z,qx,qy,qz,qw]. The reference uses Gazebo relative pose increments, F=I for covariance prediction, additive visual correction and quaternion normalization. Q diagonal is [0.005,0.005,0.01,0.001,0.001,0.001,0.001]; R is [0.4,0.4,0.1,0.01,0.01,0.01,0.01]. Pose2D observations are stamped on receipt; stored-state replay does not establish accurate sensor-delay compensation.

## Navigation and interaction extensions

The navigation reference uses FAST-LIO mapping, NDT for initial scan registration, then FastGICP tracking. Point-cloud projection supplies a 2D map for A* and DWA-style local trajectory sampling. The retained navigation archive has exercise placeholders; Jie completed the exercises but no longer has the final filled version. Accordingly these files are not shipped as runnable navigation code.

Speech: microphone → ASR → conversation history and LLM → TTS. Playback disables recording and clears queued audio; recognized text is also compared with the previous TTS response. The prompt maps room names to navigation-intent strings. The supplied code does not execute them in ROS. Live provider integration and timing need separate validation.
