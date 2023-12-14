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

# Create a DriveBase object
robot = DriveBase(Motor(Port.B), Motor(Port.C), wheel_diameter=55.5, axle_track=104)

# Drive forward and display the ultrasonic sensor distance on the screen
while True:
    distance = ultrasonic_sensor.distance()

    # Display the distance on the EV3 screen
    ev3.screen.clear()
    ev3.screen.print("Distance: {} cm".format(distance))

    robot.drive(100, 0)  # Drive forward at a speed of 100 mm/s

    # Add a small delay to avoid rapid screen updates
    wait(200)

    # Break out of the loop if the touch sensor is pressed
    if touch_sensor.pressed():
        break

# Stop the robot when the program is terminated
robot.stop()
ev3.screen.clear()
ev3.speaker.beep()
