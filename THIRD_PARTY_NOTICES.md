# Provenance and redistribution scope

The supplied project was developed through Shenlan robotics training exercises and integrates Unitree, ROS/Gazebo, Ultralytics, SciPy, Isaac Gym/rsl_rl, MuJoCo and Volcengine ecosystem components. Original comments and package maintainer metadata are retained; they are provenance, not claims of additional Git contributors.

- `ros/soccer_robot`: selected scripts from the user-supplied soccer_robot archive, also present in robocup_g1_ws(1). Original package metadata lists Shenlan and a TODO license.
- `voice`: user-supplied shenlan_ai speech examples. Packaging replaces credential literals with environment configuration and removes the original credential-bearing configuration/README. Provider protocol code remains reference code.
- `perception`: user-supplied train_yolo11 entry points using Ultralytics; no datasets or model checkpoints redistributed.
- `reference`: selected interface excerpts from the user-supplied G1 workspace. These are not a complete simulator or vendor library distribution.
- Documentation, launch wrappers and the offline audit tool were prepared for this project release.

No blanket open-source license is asserted for the mixed reference code: explicit redistribution licenses were not supplied for all course files. Existing upstream rights and terms remain applicable. This public portfolio is not a grant to reuse third-party material under a new license. Dependency source trees, binaries, original PDFs and course data are excluded.
