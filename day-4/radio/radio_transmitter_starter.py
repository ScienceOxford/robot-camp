from microbit import *
import radio

# Please tag us if used!
# We'd love to see what you make:
# @ScienceOxford

radio.on()
radio.config(channel=142) # Change this to a number between 0 & 83

while True:
    if accelerometer.is_gesture("down"):
        radio.send("forward")
        sleep(1)
    else:
        radio.send("stop")
        sleep(1)
