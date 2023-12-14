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


# Write your program here.
ev3.speaker.beep()

while True:
    pressed_buttons = ev3.buttons.pressed()

    if pressed_buttons:
        for button in pressed_buttons:
            if button == Button.UP:
                ev3.speaker.tone(440, 500)  # Play a tone for the UP button
            elif button == Button.DOWN:
                ev3.speaker.tone(523, 500)  # Play a tone for the DOWN button
            elif button == Button.LEFT:
                ev3.speaker.tone(587, 500)  # Play a tone for the LEFT button
            elif button == Button.RIGHT:
                ev3.speaker.tone(659, 500)  # Play a tone for the RIGHT button
            elif button == Button.CENTER:
                ev3.speaker.tone(698, 500)  # Play a tone for the CENTER button
            elif button == Button.BACK:
                ev3.speaker.tone(784, 500)  # Play a tone for the BACK button

    # Check for multiple button presses
    if len(pressed_buttons) > 1:
        ev3.screen.print("Multiple Buttons Pressed")

    # Wait for a short duration to avoid rapid tone playing
    wait(500)

    # Clear the screen after a delay
    ev3.screen.clear()