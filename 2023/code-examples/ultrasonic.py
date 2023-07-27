from microbit import *
from machine import time_pulse_us
# https://firialabs.com/blogs/lab-notes/ultrasonic-distance-sensor-with-python-and-the-micro-bit

def config(trigPin=pin0, echoPin=pin1):
    global trig, echo
    trig = trigPin
    echo = echoPin
    trig.write_digital(0)
    echo.read_digital()

def distance():
    # output a pulse
    trig.write_digital(1)
    trig.write_digital(0)
    # measure input echo & convert to seconds
    micros = time_pulse_us(echo, 1)
    t_echo = micros / 1000000
    # calculate distance in cm
    dist_cm = (t_echo / 2) * 34300
    dist_cm = "{:.2f}".format(dist_cm)
    return dist_cm
