# Imports go at the top
from microbit import *
import bot
import ultrasonic
bot.config()

while True:

    front = ultrasonic.distance(echo=pin1)
    if front <= 10.0:
        bot.stop()

        left = ultrasonic.distance(echo=pin2)
        if left <= 10.0:
            bot.drive(500, -500)
            sleep(200)

        else:
            bot.drive(-500, 500)
            sleep(200)

    else:
        bot.drive(500, 500)
        sleep(200)