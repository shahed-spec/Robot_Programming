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
touch_sensor = TouchSensor(Port.S1)


# Write your program here.
ev3.speaker.beep()

while True:
    if touch_sensor.pressed():
        # Play a tone when the touch sensor is pressed
        ev3.speaker.play_file(SoundFile.CAT_PURR)  # Play the cat purr sound

    # Add a small delay to avoid rapid tone playing
    wait(100)

