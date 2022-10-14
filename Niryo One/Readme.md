# Using Code

These steps must be implemented in the Raspberry-Pi controller of NiryoOne
## 1. Clone the repository
Download the Niryo One folder and copy it to the raspberry pi controller of the Niryo One.
## 2. Setup AWS MQTT Broker
* Make sure you have an AWS account. If not create it [here](https://portal.aws.amazon.com/billing/signup?nc2=h_ct&src=header_signup&redirect_url=https%3A%2F%2Faws.amazon.com%2Fregistration-confirmation#/start/email)
* Follow the steps given in this [link](https://us-west-2.console.aws.amazon.com/iot/home?region=us-west-2#/connectdevice) to setup the 
 AWSIoTPythonSDK and to get the host url, rootCA and private keys.
* Copy the url and the file paths and replace it in RoboticController.py
## 3. Run the python Script
* Make sure that the raspberry-pi controller is connected to the internet.
* Run the python script using
```sh
python RoboticController.py
```
