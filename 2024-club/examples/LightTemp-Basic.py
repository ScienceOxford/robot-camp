# Imports go at the top
from microbit import *


# Code in a 'while True:' loop repeats forever
while True:
    light = display.read_light_level()
    if light <= 10.0:
        display.scroll('dark')

        temp = temperature()
        if temp <= 10.0:
            display.scroll('cold')

        else:
            display.scroll('warm')

    else:
        display.scroll('bright')