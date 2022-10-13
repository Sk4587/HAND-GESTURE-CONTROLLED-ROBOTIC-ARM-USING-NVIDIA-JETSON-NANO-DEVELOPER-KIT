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
hand gestures recognition is shown below. The hand gesture
recognition is performed using the single stage deep CNN.
SSD Lite MobileNet-V2 model and SSD Inception-V2
model are used in this framework for gesture recognition.
MobileNet-V2 and Inception-V2 CNN models are used as
feature extractor.
 
 ![image](https://user-images.githubusercontent.com/46374770/195404754-0e11213b-6acb-437c-a8fc-de865d2175f8.png)
 
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
 
<p>Numerous CNN models are tested in object detection
problems. Some of them are Region-based convolutional
neural network (R-CNN), You Only Look Once (YOLO), and
Single Shot Detector (SSD). In this project SSD Lite
MobileNet-V2 model and SSD Inception-V2 model are used
for Hand Gesture Recognition. The performances of the above
specified models are evaluated and compared with each other.
 
<p> Inception-V2 is faster and computationally efficient than
other similar architectures like VGG Net and Alex Net. The
reduction of dimensionality is carried out effectively in the
convolutions of the Inception-V2 model by integrating a smart
factorization process. Inception-V2 consists of three layers.
The first layer consists of three convolutional layers
with dimensionality reduction filter bank. The second layer
consists of five layers with deeper filter banks and last layer
consists of two wider filter banks. It is then connected to fully
connected layers. Out of these two CNN models, SSD Lite
MobileNet-V2 model is highly preferred for remotely
operated robots because of its light weight. This improves the
speed of Hand Gesture Recognition.
 
<p> The robotic arm has six degrees of freedom with a gripper. The robotic arm moves
to fixed positions based on the gestures recognized by the SSD
model.  The robot is interfaced with a Raspberry Pi attached with it. The SSD model for Hand
gesture recognition is implemented on the Jetson Nano. A USB camera attached to the Jetson Nano is used to
get the input data.
 
 ![image](https://user-images.githubusercontent.com/46374770/195408734-ac452fde-06cc-4897-b141-18a9452df408.png)
 
<p> Finally, to integrate with IOT, the Hand Gesture
recognition is implemented on Jetson Nano and the
corresponding signals are sent to the Raspberry Pi, which in turn
controls the robotic arm movement. Both the Pi and Jetson Nano are
connected to different networks. The Jetson Nano is
remotely communicated with Raspberry Pi using Message
Queuing Telemetry Transport (MQTT) protocol as
shown above. MQTT is an open source, lightweight and
publish- subscribe network that transports messages between
devices. The MQTT broker is hosted on an Amazon Web
Services (AWS) server.  The given tables represents the algorithm
used in Jetson Nano and Raspberry Pi controllers
respectively. 

![image](https://user-images.githubusercontent.com/46374770/195624747-a33992e3-d26f-4c87-bf10-c3ecc4300f3e.png)

 
The overall training objective loss function of SSD [7],
[11] is calculated based on the weighted sum of the confidence
loss Lcnf and the localisation loss Llcl. It is given by

![image](https://user-images.githubusercontent.com/46374770/195622540-3c5c544c-a3bb-4106-8888-f5f39b599331.png)
 
where ρ is the weight term and by cross‐validation it is set to
1, K is the number of matched boxes. The loss is said to be 0
if the number of matched boxes default to zero. The term  is
the priors, it is 1 when it matches the ground truth box and 0
otherwise. The term n is the number of classes, p is the
predicted bounding box parameters and t is the ground truth
bounding box parameter.
 
## Experimental Setup

### A. Training
The SSD and SSD Lite models are trained utilizing the
fine-tuned pretrained weights from COCO dataset. MITIHand Gesture dataset is used for training and testing process.
The train model is optimized using the gradient decent
optimization technique (ADAM optimization [12]). The
models are trained for 50000 steps with batchsize-8 and
learning rate of 0.0002. The models are trained using the
hardware and software setup as described below. Deep
Learning toolbox with Python libraries and TensorFlow
framework is used. An Intel ® Core TM i7-4790 CPU @ 3.60
GHz, 64-bit processor, 20 GB RAM, Windows 10 PRO
operating system and GPU (NVIDIA GeForce GTX TITAN
X (PASCAL)) is used to train the architecture. CUDA /
CuDNN is used for providing parallel computations in a GPU.
The python modules such as Numpy, Matplotlib, Cython,
Pandas and Open-CV packages are used in the experimental
analysis. 
 
### B. Evaluation and Prediction
The trained models are tested using the test samples and
their performances are evaluated by the parameters such as
Average Precision, Average Recall, F1 score and Prediction
time for various intersection over union (IoU) values. IoU
determines the accuracy of hand action detection. IoU is unity
when the predicted bounding box exactly overlaps the ground‐
truth bounding box. The prediction is considered to be true as
long as the IoU is 0.5 and for the larger value of IoU's, the
prediction is accurate. 
 
### C. Implementation
The robotic arm positioning is implemented by a 
Raspberry Pi (Model 3B) controller (Quad Core 1.2GHz
Broadcom BCM2837 64bit CPU, 1GB RAM and 40-pin
extended GPIO pins) and a Jetson Nano controller(NVIDIA Maxwell architecture with 128 NVIDIA CUDA® cores,4 GB 64-bit LPDDR4 Memory,Quad-core ARM Cortex-A57 MPCore processor) using python framework. The hand
gesture recognition is implemented on Jetson Nano with
USB camera. The Raspberry Pi is used to control the robotic
arm in remote location. The MQTT broker is
hosted on the IOT server of Amazon Web Services (AWS).
The Python SDK AWS IoT Python SDK is used to access the
AWS server in end devices. 

### D. Niryo One
The flowchart to on how to get the robotic arm positions and the work flow of the Niryo One operation is as shown below
![image](https://user-images.githubusercontent.com/46374770/195628619-88d0e409-38d8-43f0-9dbd-f60fb3198375.png)
![image](https://user-images.githubusercontent.com/46374770/195628893-737464a2-1f2e-4506-a146-f852b3595c3e.png)

## Results and Discussion

<p>The SSD Lite Mobilenet-V2 and SSD Inception-V2 based
hand gesture recognition models are evaluated. The
performance of the models are assessed by Average Precision
(AP), Average Recall (AR) and F1-Score. The prediction time
of the model is calculated during the detection process on a
Raspberry Pi processor. Average Precision of different models
is calculated for various values of IoU threshold.
The term APall is the overall average precision, APsmall is
the average precision for the size of the object in an image
lesser than 32 × 32 pixels, APmedium is the average precision for
the object size lesser than 96 × 96 pixels and greater than
32 × 32 pixels and APlarge is for the object size greater than
96 × 96 pixels.
 
<p>Similarly, ARsmall average recall for the object is lesser
than 32 × 32 pixels, ARmedium and ARlarge are the average recall
for the object size smaller than 96 × 96 pixels and greater than
32 × 32 pixels, greater than 96 × 96 pixels, respectively. AR1,
AR10 and AR100 are the average recall values determined for
various number of detections such as 1, 10 and 100.
Both the models are trained for 50,000 epochs with batch
size as 8. SSD Lite Mobilenet-V2 and SSD Inception-V2
models are trained with a learning rate of 0.0002. The models
are compared on the basis of Average Precision, Average
Recall and F1 Score. It may be noted that SSD Inception-V2
performs better on terms of accuracy while SSD Lite
MobileNet-V2 has lower prediction time.
 
<p>Table 3 shows the Average Precision of Single Stage
Deep CNN models using MITIHD-II datasets for the various
IoU ranges of 0.5, 0.75 and 0.5:0.95. The performance metrics
obtained for SSD Inception-V2 is described as AP0.50 is 0.993,
AP0.75 is 0.991 and AP0.5:0.95 is 0.884. The metrics of SSD Lite
MobileNet-V2 is given as AP0.50 is 0.987, AP0.75 is 0.968 and
AP0.5:0.95 is 0.804 respectively. The comparison of these two
models shows that the SSD Inception-V2 has higher Average
precision values when compared to the SSD Lite MobileNetV2 model.
The Average Recall of Single Stage Deep CNN models
using MITIHD-II datasets for the IoU range of 0.5:0.95 is
illustrated in table 4. The Average Recall of SSD InceptionV2 model is 0.911 for AR1 and 0.914 for both AR10 and AR100.
For SSD Lite MobileNet-V2 model AR1 is 0.839 and 0.842
for both AR10 and AR100.
 
<p>Table 5 demonstrates the comparison of the Performance
metrics of Single Stage Deep CNN models using MITIHD-II
dataset for the IoU range of 0.5. The AP0.5, AR0.5, and F1-
Score0.5 are calculated as 99.27%, 95.58% and 97.39% for
SSD Inception-V2 Model and 98.74%, 94.11% and 96.37%
for SSD Lite MobileNet-V2 Model. Though the Precision,
Recall and F1-score are higher for SSD Inception-V2 model,
the prediction time of SSD Lite MobileNet-V2 Model is low
(0.67s). This makes a significant contribution in the speed of
communication between human and robot.
 
![image](https://user-images.githubusercontent.com/46374770/195639353-547c27e8-c2d9-4795-b29d-1f883651df5a.png)
 
<p>The overall loss curve is plotted with number of training steps in x axis and loss in y axis. The graph is shown in fig.4.  The loss is higher at the start and slowly decreases towards the end. It may be noted from the graph that after 50,000 steps SSD Lite MobileNet-V2 has higher loss than SSD Inception-V2 CNN model. 

 ![image](https://user-images.githubusercontent.com/46374770/195639562-a57d7887-e095-49fc-b89e-0832f1986bb1.png)
 
 ## Conclusion
<p> The remote location robotic arm control is performed using the single stage deep CNN hand gesture recognition model. The SSD lite MobileNet-V2 and SSD Inception V2 models are trained and tested using MITI HD-II dataset. SSD Lite model is preferred to run the hand gesture recognition applications on low power devices such as a Jetson Nano due to its light weight and speedy recognition. Jetson Nano is used for hand gesture recognition and to transmit the information to cloud.  Raspberry Pi controller receives the information from the cloud and control the operations of Robotic arm.  Both the Raspberry Pi’s are remotely communicated using MQTT Protocol and the MQTT broker is hosted on an AWS server.  For IoU threshold of 0.5, the Average precision, Average recall and F1 score of SSD Inception-V2 model is calculated as 99.27%, 95.58%, and 97.39% and the corresponding values for SSD MobileNet-V2 model is 98.74%, 94.11% and 96.37% respectively. The prediction time for SSD Inception-V2 Model using Jetson Nano controller is 0.21s whereas SSD Lite MobileNet-V2 model consumes 0.14s.  The MobileNet model runs faster at the cost of lower precision. Hence to run on low power edge devices, the SSD Lite Mobilenet-V2 model is preferred. Further reduction in prediction time will improve the speed of communication between humans and robots. This prototype can be extended into a Tele-surgery system which is considered as our future work.






 



