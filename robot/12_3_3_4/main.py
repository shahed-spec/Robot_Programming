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
left_sensor = ColorSensor(Port.S1)
right_sensor = ColorSensor(Port.S4)


# Write your program here.
ev3.speaker.beep()

# Create a DriveBase object
robot = DriveBase(Motor(Port.B), Motor(Port.C), wheel_diameter=55.5, axle_track=104)

# Set the target color for stopping and slowing down
stop_color = Color.RED
slow_down_color = Color.BLUE

# Set the speed for normal and reduced speed
normal_speed = 100
reduced_speed = 50

# Follow the line until the touch sensor is pressed
while not touch_sensor.pressed():
    left_intensity = left_sensor.reflection()
    right_intensity = right_sensor.reflection()

    # Calculate the difference in intensities
    intensity_difference = left_intensity - right_intensity

    # Adjust the motor speeds based on the intensity difference
    left_speed = normal_speed - intensity_difference
    right_speed = normal_speed + intensity_difference

    # Set motor speeds
    robot.drive(left_speed, right_speed)

    # Check for red color and stop
    if left_sensor.color() == stop_color or right_sensor.color() == stop_color:
        robot.stop()
        break

    # Check for blue color and reduce speed
    elif left_sensor.color() == slow_down_color or right_sensor.color() == slow_down_color:
        robot.drive(reduced_speed, reduced_speed)

# Stop the robot when the program is terminated
robot.stop()
ev3.speaker.beep()
