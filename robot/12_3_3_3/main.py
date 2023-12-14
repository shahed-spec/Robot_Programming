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

# Mapping colors to notes (adjust as needed)
color_notes = {
    Color.RED: 'C',
    Color.GREEN: 'D',
    Color.BLUE: 'E',
    Color.YELLOW: 'F',
}

# Create a DriveBase object
robot = DriveBase(Motor(Port.B), Motor(Port.C), wheel_diameter=55.5, axle_track=104)

# Drive forward and play different notes based on the color detected
while True:
    detected_color = CSensor.color()

    # Check if the detected color has a corresponding note
    if detected_color in color_notes:
        note = color_notes[detected_color]
        ev3.speaker.beep(note)  # Play the note

    # Drive forward at a speed of 100 mm/s
    robot.drive(100, 0)

    # Add a small delay to avoid rapid note playing
    wait(500)

    # Break out of the loop if the touch sensor is pressed
    if touch_sensor.pressed():
        break

# Stop the robot when the program is terminated
robot.stop()
ev3.speaker.beep()