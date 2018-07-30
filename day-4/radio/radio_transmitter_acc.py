from microbit import *
import radio

# Please tag us if used!
# We'd love to see what you make:
# @ScienceOxford

radio.on()
radio.config(channel=12)

while True:
    if accelerometer.is_gesture("left"):
        radio.send("left")
        sleep(1)
    elif accelerometer.is_gesture("right"):
        radio.send("right")
        sleep(1)
    elif accelerometer.is_gesture("down"):
        radio.send("forward")
        sleep(1)
    elif accelerometer.is_gesture("up"):
        radio.send("backward")
        sleep(1)
    else:
        radio.send("stop")
        sleep(1)
