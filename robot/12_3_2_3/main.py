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
ultrasonic_sensor = UltrasonicSensor(Port.S4)

# Write your program here.
ev3.speaker.beep()

# Set the distances for different warning tones
warning_distance_high = 50  # Adjust as needed
warning_distance_medium = 30  # Adjust as needed

# Create a DriveBase object
robot = DriveBase(Motor(Port.B), Motor(Port.C), wheel_diameter=55.5, axle_track=104)

# Drive forward and play different tones based on distance
while True:
    distance = ultrasonic_sensor.distance()

    if distance > warning_distance_high:
        ev3.speaker.tone(500, 200)  # Play a high-frequency tone
    elif distance > warning_distance_medium:
        ev3.speaker.tone(300, 200)  # Play a medium-frequency tone
    else:
        ev3.speaker.tone(100, 200)  # Play a low-frequency tone

    robot.drive(100, 0)  # Drive forward at a speed of 100 mm/s

    # Add a small delay to avoid rapid tone playing
    wait(200)

    # Break out of the loop if the touch sensor is pressed
    if touch_sensor.pressed():
        break

# Stop the robot when the program is terminated
robot.stop()
ev3.speaker.beep()