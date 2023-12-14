#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile


# This program requires LEGO EV3 MicroPython v2.0 or higher.
# Click "Open user guide" on the EV3 extension tab for more information.


# Create your objects here.
ev3 = EV3Brick()
CSensor = ColorSensor(Port.S3)

# Write your program here.
ev3.speaker.beep()

# Create a DriveBase object
robot = DriveBase(Motor(Port.B), Motor(Port.C), wheel_diameter=55.5, axle_track=104)

# Drive forward until the robot reaches a red line
while CSensor.color() != Color.RED:
    robot.drive(100, 0)  # Drive forward at a speed of 100 mm/s

# Stop the robot when it reaches the red line
robot.stop()

# Beep to indicate that the robot has stopped
ev3.speaker.beep()