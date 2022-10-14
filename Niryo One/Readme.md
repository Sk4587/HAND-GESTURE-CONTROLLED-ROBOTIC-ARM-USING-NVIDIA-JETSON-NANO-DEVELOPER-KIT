# Using Code

These steps must be implemented in the Raspberry-Pi controller of NiryoOne

## 1. Setup the Raspberry Pi image
* Make sure the raspberry-pi controller of Niryo One is running on the 'Niryo One Raspberry Pi image'. Else follow the steps [here](https://niryo.com/docs/niryo-one/update-your-robot/update-raspberry-pi-image/).<br>

Note: Niryo One Raspberry Pi image has the ros package api pre installed that is required for the application. Mostly the pi should be pre loaded with this image, in which case this step can be ignored.

## 2. Clone the repository
Download the Niryo One folder and copy it to the raspberry pi controller of the Niryo One.
## 3. Setup AWS MQTT Broker
* Make sure you have an AWS account. If not create it [here](https://portal.aws.amazon.com/billing/signup?nc2=h_ct&src=header_signup&redirect_url=https%3A%2F%2Faws.amazon.com%2Fregistration-confirmation#/start/email)
* Follow the steps given in this [link](https://us-west-2.console.aws.amazon.com/iot/home?region=us-west-2#/connectdevice) to setup the 
 AWSIoTPythonSDK and to get the host url, rootCA and private keys.
* Copy the url and the file paths and replace it in RoboticController.py
## 4. Run the python Script
* Make sure that the raspberry-pi controller is connected to the internet.
* Run the python script using
```sh
python RoboticController.py
```
