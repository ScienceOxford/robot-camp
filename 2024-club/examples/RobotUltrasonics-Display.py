# Imports go at the top
from microbit import *
import bot
import ultrasonic
bot.config()

while True:

    front = ultrasonic.distance(echo=pin1)
    if front < 0:
        bot.stop()
        display.show('F') # error message for front sensor
        sleep(20000) # pause for 20 seconds

    if front <= 10.0:
        bot.stop()

        left = ultrasonic.distance(echo=pin2)

        if left < 0:
            bot.stop()
            display.show('L') # error message for left sensor
            sleep(20000) # pause for 20 seconds
        
        print('Front =', front, '; Left =', left)
        if left <= 10.0:
            bot.drive(800, -800)
            sleep(200)

        else:
            bot.drive(-800, 800)
            sleep(200)

    else:
        print('Front =', front)
        bot.drive(800, 800)
        sleep(200)