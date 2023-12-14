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
left_motor=Motor(Port.B)
right_motor=Motor(Port.C)

# Initialize the DriveBase using the motors
robot = DriveBase(left_motor, right_motor, wheel_diameter=55.5, axle_track=104)


# Write your program here.
ev3.speaker.beep()



# Drive in a square
for _ in range(4):
    # Drive forward
    robot.drive_time(100, 0, 2000)  # Adjust the time (milliseconds) and speed as needed

    # Turn 90 degrees to the right
    robot.drive_time(0, 90, 1000)  # Adjust the angle (degrees) and speed as needed

# Beep to signal completion
ev3.speaker.beep()

# Stop the motors
robot.stop()
