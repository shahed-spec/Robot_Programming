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
left_motor = Motor(Port.B)
right_motor = Motor(Port.C)
robot = DriveBase(left_motor, right_motor, wheel_diameter=55.5, axle_track=104)


# Write your program here.
ev3.speaker.beep()

# Drive forward quickly for 1 meter
robot.straight(1000)  # 1000 mm = 1 meter

# Stop for 2 seconds and play a tone
robot.stop()
ev3.speaker.beep(500, 1000)  # Frequency: 500 Hz, Duration: 1000 ms

# Reverse slowly to the starting position
robot.straight(-1000)  # Negative value for reverse

# Beep to signal completion
ev3.speaker.beep()

# Stop the motors
robot.stop()