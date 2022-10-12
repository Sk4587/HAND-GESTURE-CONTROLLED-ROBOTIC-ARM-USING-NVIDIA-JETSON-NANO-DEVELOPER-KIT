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

## Objectives
* To design and develop a real-time gesture based robotic arm control system under unconstrained environments
* To decrease the prediction time for object detection by training and analysing in different models to make the model run efficiently on low power edge devices.
* To integrate with IoT

## Motivation
*In teleoperation, the doctors position the surgical robots from a remote location by an efficient Human Machine Interaction system
Gesture-based implementation is associated with a number of fields in many applications, such as Human-Machine Interaction, Virtual Reality, Robot Control, Tele-surgery systems etc
*The gesture based control system build a richer bridge between the computers and humans. This method eliminates the keyboard and mouse inputs and to connect directly without any mechanical equipment.
*The key motivation is to show the power of AI for day-to-day activities which makes our life convenient

## Project Demo

## Block Diagram
![image](https://user-images.githubusercontent.com/46374770/195404754-0e11213b-6acb-437c-a8fc-de865d2175f8.png)

## Components Description and Working
### Niryo One 
![image](https://user-images.githubusercontent.com/46374770/195405644-41e4c42d-b376-4a95-99c7-177abfaab5dd.png) <br>
Niryo One is a robot arm created for robotic learning. 
With its three Dynamixel XL servomotors, NiryoSteppers and 6 axis, it allows to reproduce all the movements required for the most advanced uses.
There are many ways to program Niryo One (from high to low level):
* Program the robot with the learning mode
* Use a Xbox controller to move the robot axis directly
* Using the Python API to give commands to the robot using an easy-to-use programming interface. There is a modbus server running on the robot.
* Developing our own APIs to connect Niryo One to any industrial device.
* Can be made to communicate with other devices, such as Arduino and Raspberry Pi boards.
* Using ROS code and programming  using Python and C++. 

More information on Niryo One Can be found [here](https://niryo.com/product/niryo-one/)

#### Flowchart [Niryo One Learning Mode]
To obtain co-ordinates of the arm’s position :
![image](https://user-images.githubusercontent.com/46374770/195407027-102902e2-69e4-4e0f-8ed7-a7b06ae2adc8.png)

#### Flowchart [Niryo One Working Flow]

![image](https://user-images.githubusercontent.com/46374770/195407293-db4e0b59-19c2-4963-af3f-348b27e0afbc.png)

### MQTT 
![image](https://user-images.githubusercontent.com/46374770/195408734-ac452fde-06cc-4897-b141-18a9452df408.png)

MQTT is an open source, lightweight and publish- subscribe network that transports messages between devices
The MQTT broker is hosted on an Amazon Web Services (AWS) server <br>
The main advantages of MQTT broker are:
* Eliminates vulnerable and insecure client connections
* Can easily scale from a single device to thousands
* Manages and tracks all client connection states, including security credentials and certificates
* Reduced network strain without compromising the security (cellular or satellite network)

### Dataset (MITIHD-II)
![image](https://user-images.githubusercontent.com/46374770/195409359-629265e5-d817-4349-b918-f61cb12fce7d.png)
The dataset has about 10 classes and 970 samples per class.







 



