from microbit import *

servo = pin0

while True:
    if button_a.was_pressed():
        servo.write_analog(35)
        sleep(1000)
        servo.write_analog(85)
        sleep(1000)
