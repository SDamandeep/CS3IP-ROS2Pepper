# CS3IP-ROS2Pepper
Use your Pepper Robot with ROS2 through Zeroc-ICE

The files present in this repository can be used to control Pepper with ROS2.\
The folder 'codeBridge' contains all the files needed to control Pepper but it requires some packahes to be present in the computer to function properly.

The folder 'pepperros2' contains a docker file which creates a contaioner where the code can be run without haviong to download and install any packages. However, before running the container download a zip file folder from the link below and save it in 'pepperros2/naoqiSDK' (save the file without unzipping it).

Link the file: https://community-static.aldebaran.com/resources/2.5.5/naoqi-sdk/naoqi-sdk-2.5.5.5-linux64.tar.gz

Before running the code deactivate the idle movements:
1. Connect to the robot
2. Open a new terminal
3. Type: ssh@nao <robot_ip_address>
4. Type yes and enter the password
5. Type: qicli call ALAutonomousLife.setState disabled
6. Type: qicli call ALMotion.wakeUp

After following the steps above the robot will stop the idle movements

## Tools used for developemnt

* Ubuntu 22.04
* ROS2 Humble Hawskbill
* Python3 & Python2.7
* Zeroc-ICE
* Visual Studio Code
* naoqi library
