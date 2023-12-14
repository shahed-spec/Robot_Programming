#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile




# Create your objects here.
ev3 = EV3Brick()
UltraSensor=UltrasonicSensor(Port.S4)


# Write your program here.
ev3.speaker.beep()

# Set the distance to stop in centimeters
stop_distance_cm = 20

# Create a DriveBase object
robot = DriveBase(Motor(Port.B), Motor(Port.C), wheel_diameter=55.5, axle_track=104)

# Drive forward until the robot is 20cm away from an obstacle
while UltraSensor.distance() > stop_distance_cm:
    robot.drive(100, 0)  # Drive forward at a speed of 100 mm/s

# Stop the robot when the desired distance is reached
robot.stop()

# Beep to indicate that the robot has stopped
ev3.speaker.beep()