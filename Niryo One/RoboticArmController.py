##### Niryo One Robotic Arm Controller and MQTT SUBSCRIBER ######
#
# Author: Sreekar C
# Mail: sreekar.cango@gmail.com
# Description:
# This program connects to the MQTT server under topic 'gesture' and controlls the robotic arm
# based on the command received

from AWSIoTPythonSDK.MQTTLib import AWSIoTMQTTClient
import logging
from AWSIoTPythonSDK.MQTTLib import AWSIoTMQTTClient
import logging
import time
import json
from niryo_one_python_api.niryo_one_api import *
import rospy


#from robotics import *
rospy.init_node('niryo_one_example_python_api')

host = '<AWS IOT server url>'
rootCAPath = '<Path to rootCA>'
certificatePath = '<Path to certificate>'
privateKeyPath = '<Path to private key>'
port = 8883
clientId = 'Niryoone'
topic = 'gesture'


positions={'init':[-0.08355988707486255, 0.12708096598731644, -0.31266326885726986, 0.01689478715930511, -1.2886114933324535, -0.5263913024014898],
           'action1':[-0.8530881494387129, -0.9788541320658724, 0.19148755221880642, 0.14283774598321594, -0.6957580530150196, -0.47071529926287065],
           'action1_1':[0.020080282940470845, 0.05810765359271347, -0.04637589155299218, -0.08447393579652554, -0.0153588974175501, -0.31887165433936404],
           'action1_2':[-0.0012955021251916674, 0.0656663727592453, -0.20694618273647047, -0.08908160502179058, -0.01843067690106012, 1.3767157139731272],
           'tup_pick_1':[-0.529860369203392, -0.2338478742145786, -0.8641873124874779, 0.3977954431145476, -0.26724481506537173, -1.2400564335419713],
           'tup_pick_2':[-0.3692181056796252, -0.5073790240534493, -0.6771877497737998, -0.307177948351002, -0.3839724354387525, -0.4808382089244378],
           'tup_pick_3':[-0.4061399162475877, -0.5092687038450823, -0.8442406924646856, -0.34711108163663223, 0.02764601535159018, -0.31887165433936404],
           'tup_drop_1':[0.23772463997267096, -0.9812162318054136, 0.15209297767379157, 0.11979939985689078, -0.5790304326416388, -0.2935643801854462],
           'tup_drop_3':[0.2344858846596918, -0.7724066148299717, 0.10821041362364843, -0.00307177948351002, -0.7218681786248548, -0.16702800941585733],
           'tup_drop_2':[0.2422588974108418, -0.8527180059743724, 0.06432784957350528, 0.12901473830742086, -0.5805663223833938, -0.273318560862312],
           'drop':[0.6645925902233254, -0.3807704780140411, -0.2428500987774967, -0.14283774598321594, -0.6972939427567745, 0.409977841293468],
           'pick1':[-0.6924458859149462, -0.7818550137881365, -0.2887273248299191, -0.032253684576855214, -0.32714451499381714, -0.27838001569309556],
           'pick2':[1.0642549958449548, -0.5536761789484568, -0.8193074174361952, -0.04300491276914028, -0.2165604535874564, -0.2682571060315284],
           'pick3':[1.8124074731431428, -0.6713087459776085, -0.3984337349552769, -0.03839724354387525, -0.22423990229623147, -0.2885029253546627],
           'end':[-0.12955021251916674, -0.01086565880188951, -1.3628528130572863, -0.01843067690106012, 0.03378957431861022, -0.010122909661567111],
             'j1':[-0.049876831819879196, -0.1110186877584363, -1.0975627667541483, 0.1827708792688462, 0.01228711793404008, -0.5061454830783555],
             'j2':[-1.5403520268528925, -0.5475347196256497, -0.819806082936765, -0.1244070690821558, -0.09829694347232064, -0.5365142120630568],
             'j3':[1.3453789570115466, -0.6892607039981216, -0.4562789330213747, 0.12594295882391082, -0.11211995114811574, -0.5618214862169747],
             'j4':[-1.0137304129624798, -0.8234279692040616, -0.22739146825983264, 0.0614355896702004, -0.11672762037338076, -0.5770058507093254],
             'j5':[-1.210646735991613, -0.5376139007195766, -0.4901881870601217, 0.2580294766148417, -0.05222025121967034, -0.5213298475707062],
             }



#j=n.get_joints()
print "--- Start"

n = NiryoOne()

n.calibrate_auto()
print "Calibration finished !"

n.activate_learning_mode(False)

n.change_tool(TOOL_GRIPPER_2_ID)

n.move_joints(positions['init'])

state = 1

def Action1():
    n.move_joints(positions['init'])
    n.open_gripper(TOOL_GRIPPER_2_ID,500)
    time.sleep(1)
    n.move_joints(positions['j1'])
    n.close_gripper(TOOL_GRIPPER_2_ID,500)
    n.move_joints(positions['init'])
    time.sleep(1)
    n.move_joints(positions['j2'])
    n.open_gripper(TOOL_GRIPPER_2_ID,500)



def Action2():
    n.move_joints(positions['init'])
    n.open_gripper(TOOL_GRIPPER_2_ID,500)
    time.sleep(1)
    n.move_joints(positions['j1'])
    n.close_gripper(TOOL_GRIPPER_2_ID,500)
    n.move_joints(positions['init'])
    time.sleep(1)
    n.move_joints(positions['j3'])
    n.open_gripper(TOOL_GRIPPER_2_ID,500)

def Action3():
    n.move_joints(positions['init'])
    n.open_gripper(TOOL_GRIPPER_2_ID,500)
    time.sleep(1)
    n.move_joints(positions['j4'])
    n.close_gripper(TOOL_GRIPPER_2_ID,500)
    n.move_joints(positions['init'])
    time.sleep(1)
    n.move_joints(positions['j1'])
    n.open_gripper(TOOL_GRIPPER_2_ID,500)


def Action4():
    n.move_joints(positions['init'])
    n.open_gripper(TOOL_GRIPPER_2_ID,500)
    time.sleep(1)
    n.move_joints(positions['pick1'])
    n.close_gripper(TOOL_GRIPPER_2_ID,500)
    n.move_joints(positions['init'])
    time.sleep(1)
    n.move_joints(positions['drop'])
    n.open_gripper(TOOL_GRIPPER_2_ID,500)
def Action5():
    n.move_joints(positions['init'])
    n.open_gripper(TOOL_GRIPPER_2_ID,500)
    time.sleep(1)
    n.move_joints(positions['pick2'])
    n.close_gripper(TOOL_GRIPPER_2_ID,500)
    n.move_joints(positions['init'])
    time.sleep(1)
    n.move_joints(positions['drop'])
    n.open_gripper(TOOL_GRIPPER_2_ID,500)
def Action6():
    n.move_joints(positions['init'])
    n.open_gripper(TOOL_GRIPPER_2_ID,500)
    time.sleep(1)
    n.move_joints(positions['pick3'])
    n.close_gripper(TOOL_GRIPPER_2_ID,500)
    n.move_joints(positions['init'])
    time.sleep(1)
    n.move_joints(positions['drop'])
    n.open_gripper(TOOL_GRIPPER_2_ID,500)

def Action7():
    n.move_joints(positions['init'])
    n.open_gripper(TOOL_GRIPPER_2_ID,500)
    time.sleep(1)
    n.move_joints(positions['action1'])
    n.close_gripper(TOOL_GRIPPER_2_ID,500)
    n.move_joints(positions['init'])
    time.sleep(1)
    n.move_joints(positions['action1_1'])
    n.open_gripper(TOOL_GRIPPER_2_ID,500)

def Action8():
    n.move_joints(positions['init'])
    n.open_gripper(TOOL_GRIPPER_2_ID,500)
    time.sleep(1)
    n.move_joints(positions['tup_pick_1'])
    n.close_gripper(TOOL_GRIPPER_2_ID,500)
    n.move_joints(positions['init'])
    time.sleep(1)
    n.move_joints(positions['action1_1'])
    n.open_gripper(TOOL_GRIPPER_2_ID,500)
    n.move_joints(positions['init'])
    time.sleep(1)
    n.move_joints(positions['tup_pick_2'])
    n.close_gripper(TOOL_GRIPPER_2_ID,500)
    n.move_joints(positions['init'])
    time.sleep(1)
    n.move_joints(positions['action1_1'])
    n.open_gripper(TOOL_GRIPPER_2_ID,500)
    n.move_joints(positions['init'])
    time.sleep(1)
    n.move_joints(positions['tup_pick_3'])
    n.close_gripper(TOOL_GRIPPER_2_ID,500)
    n.move_joints(positions['init'])
    time.sleep(1)
    n.move_joints(positions['action1_1'])
    n.open_gripper(TOOL_GRIPPER_2_ID,500)




def customCallback(client, userdata, message):
    print("Received a new message: ")
    m=json.loads(message.payload.decode('utf-8')) 
    print(m['message'])
    gesture=m['message']
    #print(message.payload)
    print("from topic: ")
    print(message.topic)
    print("--------------\n\n")
    
    if gesture == "one" :
       Action1()
       # return 1
    if gesture == "two" :
       Action2()
	   #return 1
    if gesture == "three" :
       Action3()
       #return 1
    if gesture == "four" :
       Action4()
       #return 1
    if gesture == "five" :
       Action5()
       #return 1
    if gesture == "love":
       Action6()
       #return 1
    if gesture == "ok":
       Action7()
       #return 1
    if gesture == "tup":
       Action8()
       #return 1
    if gesture == "straight":
       #return 0
       n.move_joints(positions['init'])
       time.sleep(1)
       n.move_joints(positions['end'])
       global state
       state = 0
    if gesture == "fold":
       n.move_joints(positions['init'])    
       #return 1 


print("Connecting.........")

# Init AWSIoTMQTTClient
myAWSIoTMQTTClient = AWSIoTMQTTClient(clientId)
myAWSIoTMQTTClient.configureEndpoint(host, port)
myAWSIoTMQTTClient.configureCredentials(rootCAPath, privateKeyPath, certificatePath)

# AWSIoTMQTTClient connection configuration
myAWSIoTMQTTClient.configureAutoReconnectBackoffTime(1, 32, 20)
myAWSIoTMQTTClient.configureOfflinePublishQueueing(-1)  # Infinite offline Publish queueing
myAWSIoTMQTTClient.configureDrainingFrequency(2)  # Draining: 2 Hz
myAWSIoTMQTTClient.configureConnectDisconnectTimeout(10)  # 10 sec
myAWSIoTMQTTClient.configureMQTTOperationTimeout(5)  # 5 sec

# Connect and subscribe to AWS IoT
myAWSIoTMQTTClient.connect()

myAWSIoTMQTTClient.subscribe(topic, 1, customCallback)
time.sleep(2)
print("LISTENING>>>>>>>")

while(True) :
    if state == 0 :
        break

