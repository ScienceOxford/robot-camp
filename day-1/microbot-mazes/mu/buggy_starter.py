from microbit import *

# Please tag us if used!
# We'd love to see what you make:
# @ScienceOxford

'''
This tells us which of the micro:bit's pins is connected to which input on the motor driver (follow the coloured wires!).
e.g. FL means that it controls the pin that turns on the left-hand motor in the forward direction.
'''
FL = pin14
BL = pin13
FR = pin12
BR = pin15

'''
If the pin is set to HIGH (1023), the motor is turned off. The lower the number, the faster the motor goes.
Currently the motors are set to turn on at half speed (511), as this makes it easier to control.
'''
on = 511
off = 1023

'''
The following functions define the combination of pins to control direction.
'''
def stop(time):
    display.clear()
    FL.write_analog(off)
    BL.write_analog(off)
    FR.write_analog(off)
    BR.write_analog(off)
    sleep(time)

def forward(time):
    display.show(Image.ARROW_N)
    FL.write_analog(on)
    BL.write_analog(off)
    FR.write_analog(on)
    BR.write_analog(off)
    sleep(time)

def backward(time):
    display.show(Image.ARROW_S)
    FL.write_analog(off)
    BL.write_analog(on)
    FR.write_analog(off)
    BR.write_analog(on)
    sleep(time)

def left_turn(time):
    display.show(Image.ARROW_W)
    FL.write_analog(off)
    BL.write_analog(on)
    FR.write_analog(on)
    BR.write_analog(off)
    sleep(time)

def right_turn(time):
    display.show(Image.ARROW_E)
    FL.write_analog(on)
    BL.write_analog(off)
    FR.write_analog(off)
    BR.write_analog(on)
    sleep(time)

stop(1)

# WRITE YOUR CODE BELOW HERE!
