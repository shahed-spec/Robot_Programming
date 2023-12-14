#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile

from umqtt.robust import MQTTClient
import time

#MQTT setup
MQTT_ClientID = 'RobotA'
MQTT_Broker = '172.20.10.3'
MQTT_Topic_Hallo = 'python/course'
MQTT_Topic_Sensor = "python/message"
client = MQTTClient(MQTT_ClientID, MQTT_Broker)
client.connect()
client.publish(MQTT_Topic_Sensor, "initial_message")

# Create objects for Robot A
ev3 = EV3Brick()
left_motor = Motor(Port.B)
right_motor = Motor(Port.C)
ultrasonic_sensor = UltrasonicSensor(Port.S4)
color_sensor = ColorSensor(Port.S1)

# Callback for listening to topics
def listen(topic, msg):
    if topic == MQTT_Topic_Hallo.encode():
        message = str(msg.decode())
        ev3.screen.print(message)

        if message == "FORWARD":
            ev3.speaker.beep(300)
            # Move the robot forward
            left_motor.run(200)
            right_motor.run(200)
        elif message == "BACKWARD":
            ev3.speaker.beep(400)
            # Move the robot backward
            left_motor.run(-200)
            right_motor.run(-200)
        elif message == "RIGHT":
            ev3.speaker.beep(500)
            # Turn the robot right
            left_motor.run(50)
            right_motor.run(-50)
        elif message == "LEFT":
            ev3.speaker.beep(600)
            # Turn the robot left
            left_motor.run(-50)
            right_motor.run(50)
        else: 
            ev3.speaker.beep(700)
            # Stop the robot
            left_motor.stop()
            right_motor.stop()


# Subscribe to the topic
client.set_callback(listen)
client.subscribe(MQTT_Topic_Hallo)


while True:
    ultrasonic_distance = ultrasonic_sensor.distance()
    color_value = color_sensor.color()
    
    message = "DISTANCE: {} cm \n {}".format(
        ultrasonic_distance, color_value
    )
    
    client.publish(MQTT_Topic_Sensor, message)
    
    client.check_msg()
    time.sleep(0.5)
