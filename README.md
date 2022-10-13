# HAND-GESTURE-CONTROLLED-ROBOTIC-ARM-USING-NVIDIA-JETSON-NANO-DEVELOPER-KIT
<p>In teleoperation, the doctors position the surgical robots
from a remote location by an efficient Human Machine
Interaction system. The interaction between the human beings
and machines are carried out in more natural forms with the
development in the field of Artificial Intelligence. Hand
gestures are used to convey a non-verbal type of
information’s. Gesture-based implementation is associated
with a number of fields in many applications, such as HumanMachine Interaction, Virtual Reality, Robot Control, Telesurgery systems etc. The gesture based control system build a
richer bridge between the computers and humans. This
method eliminates the keyboard and mouse inputs and to
connect directly without any mechanical equipment. 
 
<p>In this project, a hand gesture recognition system using a
single stage deep convolutional neural network (CNN) to
control Niryo One, a robotic arm with 6 degrees of freedom (DOF) in a
remote location is proposed. The hand gestures are recognized
using a Single Shot Detector (SSD) Lite MobileNet-V2 based
CNN model. The MobileNet-V2 CNN model is used as a
feature extractor. The information of the recognized gesture is
transmitted using a Wi-Fi module and then to the 6 DOF
Robotic arm in the remote location. An MQTT broker hosted on AWS acts as a message queuing service.  The SSD Lite MobileNetV2 model predicts the input gestures at a faster rate when
compared with the SSD Inception-V2 model. 

## Methodology
<p> An overview of vision based robotic arm control using
hand gestures recognition is shown in fig.1. The hand gesture
recognition is performed using the single stage deep CNN.
SSD Lite MobileNet-V2 model and SSD Inception-V2
model are used in this framework for gesture recognition.
MobileNet-V2 and Inception-V2 CNN models are used as
feature extractor.
<p> These CNN models are trained and tested using a MITI
Hand Dataset–II (MITI HD-II). MITI HD-II is an improved
version of MITI HD dataset. It is a custom-created
dataset of hand posture obtained from different individuals
with differing skin tones, complex profiles, different hand
size, conditions of lighting, geometry, fast movements, and
different age classes. The dataset has about 10 classes and 970
samples per class. The sample frames of each class from MITI
HD-II are shown.<br>
![image](https://user-images.githubusercontent.com/46374770/195409359-629265e5-d817-4349-b918-f61cb12fce7d.png)

<p> The SSD is a CNN based object detector. It uses a single
forward pass network and a bounding box regression
technique to classify and localize the object. Over Faster RCNN, SSD offers significant speed gains. SSD is also used in
real-time for action recognition. SSD completes the process of
region proposal and classification in a single shot process.
SSD Lite  model is the lighter version of the conventional
SSD model. SSD Lite MobileNet-V2 is 20 times more
effective and 10 times lighter than YOLO-V2. It outperforms
YOLO-V2 architecture.
<p> MobileNet is a compact architecture that constructs a
lightweight deep convolutional neural network using deeply
separable convolutions. Depth-separable convolution filters
consist of filters for deep convolution and filters for point
convolution. On each input channel, the depthwise
convolution filter performs a single convolution, and the point
convolution filter combines linearly, the 1 to 1 convolutions
and the output of depthwise convolution. MobileNets
concentrate on latency optimization, but also generate small
networks. The depth-wise seperable convolution has separate
layers for filtering and combining which drastically
contributes in reducing the computation time and model size
compared to a standard convolution process. It offers a
computation reduction by a factor of 1/N + 1/Dk
2
, where N is
the number of output channels and Dk is kernel size. This is 8
to 9 times lesser compared to a standard convolution.

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







 



