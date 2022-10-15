# Using Code

These steps are for the implementation in Jetson Nano

## 1.Getting started with Jetson Nano
* Complete the setup of the Jetson Nano developer kit by following the steps in this [guide](https://developer.nvidia.com/embedded/learn/get-started-jetson-nano-devkit#intro)

## 2. Clone the repository
Download the Jetson Nano folder and copy it to the jetson nano controller of the Niryo One.

## 3. Setup AWS MQTT Broker
* Make sure you have an AWS account. If not create it [here](https://portal.aws.amazon.com/billing/signup?nc2=h_ct&src=header_signup&redirect_url=https%3A%2F%2Faws.amazon.com%2Fregistration-confirmation#/start/email)
* Follow the steps given in this [link](https://us-west-2.console.aws.amazon.com/iot/home?region=us-west-2#/connectdevice) to setup the 
 AWSIoTPythonSDK and to get the host url, rootCA and private keys.
* Copy the url and the file paths and replace it in GesturePredictor.py

## 4. Depedencies
Install the required python dependencies using
```sh
pip install tflite-runtime
sudo apt-get install python3-opencv 
```
## 5. Trained Model
* Copy your trained tflite model to Jetson Nano or download my trained model from [here](https://drive.google.com/file/d/1zniRK4ny0hmmfFe31xw299gPFT9sKxCS/view?usp=sharing)
* Copy the path location of the trained model and replace it in GesturePredictor.py

## 6. Run the python Script
* Make sure that the jetson nano controller is connected to the internet.
* Run the python script using
```sh
python GesturePredictor.py
```
