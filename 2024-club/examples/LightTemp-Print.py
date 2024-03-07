# Imports go at the top
from microbit import *


# Code in a 'while True:' loop repeats forever
while True:
    light = display.read_light_level()
    if light <= 10.0:
        display.scroll('dark')

        temp = temperature()
        print('Light level =', light, '; Temperature =', temp)
        if temp <= 10.0:
            display.scroll('cold')

        else:
            display.scroll('warm')

    else:
        print('Light level =', light)
        display.scroll('bright')