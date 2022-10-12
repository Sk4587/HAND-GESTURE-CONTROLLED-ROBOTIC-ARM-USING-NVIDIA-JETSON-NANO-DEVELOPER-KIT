# HAND-GESTURE-CONTROLLED-ROBOTIC-ARM-USING-NVIDIA-JETSON-NANO-DEVELOPER-KIT
In tele operation mechanism, the surgical robots are controlled using hand gestures
from remote location. The remote location robotic arm control using hand gesture
recognition is a challenging computer vision problem. The hand action recognition
under complex environment (cluttered background, lighting variation, scale variation
etc.) is a difficult and time consuming process. In this project, a light weight
Convolutional Neural Network (CNN) model Single Shot Detector (SSD) Lite
MobileNet-V2 is used for real-time hand gesture recognition. SSD Lite versions
tend to run hand gesture recognition applications on low-power computing devices
like Jetson Nano due to its light weight and timely recognition. The model is deployed
using a Camera, Jetson Nano and a Raspberry Pi Controller. For the hand gesture
recognition and data transfer to the cloud server, the Jetson Nano is used. An MQTT broker is hosted on AWS server that enables remote communication between the robot and Jetson Nano using publisher-subscriber model. The
Raspberry Pi Controller receives the cloud information and controls the Robotic arm
operations. The model is trained using the MITI Hand dataset-II (MITI HD-II) with the learning rate of
0.0002 using Adam optimizer and has obtained an Average precision of 98.74%. The prediction time for
SSD Lite MobileNet-V2 model using Raspberry Pi controller takes only 0.14s. The model is then demonstrated using highly
accurate robotic arm Niryo one.

