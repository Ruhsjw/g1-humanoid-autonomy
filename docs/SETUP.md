# Setup and execution

## Offline inspection

Python 3.8 or newer is sufficient for the standard-library audit tool:

```sh
python tools/audit_dataset.py /path/to/yolo_dataset
python -m unittest discover -s tests
```

## Soccer simulation

Use a compatible Linux ROS 1/Gazebo environment with the G1 12-DoF simulation already building and walking. This release does not install that environment. Python modules require rospy, geometry_msgs, sensor_msgs, tf, cv_bridge, NumPy, SciPy, OpenCV and Ultralytics compatible with that environment. The supplied deployment snapshot corresponds to `robocup_g1_ws(1)`, whose MoveCmd fields are float32 and whose callback accepts direct commands.

1. Copy `ros/soccer_robot` into the external catkin workspace's `src/` directory. Object and ObjectArray messages are included in this package. Ensure float32 MoveCmd exists in `unitree_legged_msgs`; see `reference/messages`. Rebuild messages and workspace with your ROS environment sourced.
2. Provide your authorized detector weights at `soccer_robot/models/yolo11.pt`. Policy weights and simulation assets remain in the external workspace. Enable both D435 instances and verify the four RGB/depth topics listed in the architecture document.
3. Mark the Python scripts executable and build/source the workspace. The runtime must use Python 3 with matching ROS bindings.
4. Start Gazebo and the compatible walking controller, then run `roslaunch soccer_robot vision.launch`.
5. When position estimates and the MoveCmd receiver are verified, run `roslaunch soccer_robot soccer_behavior.launch` in simulation.
6. For optional fusion, use `roslaunch soccer_robot vision_ekf.launch` instead of the vision-only launch, then `roslaunch soccer_robot soccer_behavior.launch use_ekf:=true`.

The new launch files replace an obsolete upstream launch that referenced a missing object_tracker.py. They have been XML-checked, but the full ROS/Gazebo stack has not been executed during release packaging. The scripts open OpenCV visualization windows and need a display.

## Detector training

Run from `perception/` after supplying a licensed/authorized `yolo_dataset` with train/images, train/labels, val/images and val/labels. Install an environment matching your Ultralytics/GPU setup. `python train.py` writes a local dataset YAML and trains from yolo11n.pt. The script requests up to 1050 epochs; this is a configuration, not a training result. `python predict.py` expects the resulting best.pt and local prediction inputs. Training may download upstream weights and consumes GPU time.

## Speech prototype

The historical environment snapshot is `voice/environment.reference.yml`; it is a reference, not a portable lockfile. The modules require the Volcengine Ark SDK, websockets, PyAudio and audio-system dependencies. Service endpoints, account permissions and model availability must match your provider account.

Set ARK_API_KEY, SPEECH_APP_ID, SPEECH_APP_TOKEN and ARK_MODEL in your process environment. `voice/.env.example` lists the names; .env files are not loaded automatically. Do not commit values. From `voice/`, run `python demo.py` to start microphone input and external ASR/LLM/TTS requests. Provider usage may incur account charges.

The prompt's room coordinates are illustrative. Responses such as `--Nav(x,y)` are spoken text; no ROS movement command is published. Do not connect unvalidated generated text directly to a robot. For future integration use a destination allowlist, structured parsing, frame checks and an explicit execution interface.
