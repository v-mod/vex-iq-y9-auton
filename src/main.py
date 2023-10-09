# ---------------------------------------------------------------------------- #
#                                                                              #
# 	Module:       main.py                                                      #
# 	Author:       vivaa                                                        #
# 	Created:      07/10/2023, 23:16:55                                         #
# 	Description:  IQ2 project                                                  #
#                                                                              #
# ---------------------------------------------------------------------------- #

# Library imports
from vex import *

# Importing Device Modules
from GsColourSensor import GsColourSensor
from GsDistanceSensor import GsDistanceSensor
from GsSmartDrive import GsSmartDrive
from GsMotor import GsMotor
from GsBrain import GsBrain
from GsGyro import GsGyro
from GsController import GsController
from GsThreads import GsThreads

# Setting Ports
leftPort=Ports.PORT1
rightPort=Ports.PORT6
gyroPort=Ports.PORT3

# Setting drive constants
STOPPING_TYPE=HOLD
DRIVE_VEL=100
TURN_VEL=30
TRACK_WIDTH=200

# Creating Instances of devices
brain=GsBrain()
left=GsMotor(leftPort,2)
right=GsMotor(rightPort,2)
gyro=GsGyro(gyroPort)
controller=GsController()
drivetrain=GsSmartDrive(left,right,gyro,DRIVE_VEL,TURN_VEL,HOLD,TRACK_WIDTH)
driveManager=GsThreads(left,right,drivetrain,controller)

# Drive Control 
rc_auto_loop_thread = Thread(driveManager.rc_auto_loop)