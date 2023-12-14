#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile
import time



# This program requires LEGO EV3 MicroPython v2.0 or higher.
# Click "Open user guide" on the EV3 extension tab for more information.


# Create your objects here.
ev3 = EV3Brick()
left_motor = Motor(Port.B)
right_motor = Motor(Port.C)
robot = DriveBase(left_motor, right_motor, wheel_diameter=55.5, axle_track=104)
touch_sensor = TouchSensor(Port.S1)

# Write your program here.
ev3.speaker.beep()

# Set the initial speed, acceleration, and time interval
initial_speed = 100  # Start with a speed of 100 mm/s
acceleration = 100   # Acceleration rate (adjust as needed)
time_interval = 1    # Accelerate every 1 second

# Drive forward with gradual acceleration

while True:
    if touch_sensor.pressed():
     for _ in range(5):  # Drive for 5 seconds (adjust as needed)
        robot.drive_time(initial_speed, 0, 1000)  # Drive for 1 second (adjust as needed)
        initial_speed += acceleration  # Increase the speed
        time.sleep(time_interval)  # Wait for the specified time interval

# Beep to signal completion
ev3.speaker.beep()
