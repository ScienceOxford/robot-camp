'''
For more information and links to other examples:
https://scienceoxford.github.io/shine-on/2023.html
'''

from microbit import *
from random import randint, choice
import neopixel

'''
edit the arguments of the below line to specify:
- which pin your string of neopixels is connected to
- how many pixels are in your string of neopixels
'''
lights = neopixel.NeoPixel(pin0, 10)

red = (100, 0, 0)
green = (0, 100, 0)
blue = (0, 0, 100)

colours = [red, green, blue]

while True:
    for i in range(0, len(lights)):  
      lights[i] = choice(colours)
      lights.show()
      sleep(1000)
