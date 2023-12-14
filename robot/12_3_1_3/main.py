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

# Set the duration for counting (in seconds)
counting_duration = 5

# Variables to store count and time
press_count = 0

# Count how often the touch sensor has been pressed for the first 5 seconds
while True:
    if touch_sensor.pressed():
        press_count += 1
        wait(200)  # Wait for 200 milliseconds to avoid counting multiple presses quickly

    # Break out of the loop after 5 seconds
    if time.time() - start_time >= counting_duration:
        break

# Display the count on the EV3 screen
ev3.screen.print("Press Count: {}".format(press_count))

# Play a tone as many times as the touch sensor was pressed
for _ in range(press_count):
    ev3.speaker.play_file(SoundFile.CAT_PURR)
    wait(1000)  # Wait for 1 second between each tone

    