from microbit import *

def pinCheckLeft(A1A=pin13, A1B=pin12):
    '''
    This function is used to test the orientation of the left motor.
    By default, A1A on the motor driver is connected to pin13 of the microbit,
    and A1B on the motor driver is connected to pin12 of the microbit.
    '''
    on = 800
    off = 0
    # Check if A1A turns left motor forward
    display.show("F")
    A1A.write_analog(on)
    A1B.write_analog(off)
    sleep(2000)
    # Check if A1B turns left motor backward
    display.show("B")
    A1A.write_analog(off)
    A1B.write_analog(on)
    sleep(2000)
    # Turn motor off
    display.show(Image.NO)
    A1B.write_analog(off)

def pinCheckRight(B1A=pin15, B1B=pin14):
    '''
    This function is used to test the orientation of the right motor.
    By default, B1A on the motor driver is connected to pin15 of the microbit,
    and B1B on the motor driver is connected to pin14 of the microbit.
    '''
    on = 800
    off = 0
    # Check if B1A turns right motor forward
    display.show("F")
    B1A.write_analog(on)
    B1B.write_analog(off)
    sleep(2000)
    # Check if B1B turns right motor backward
    display.show("B")
    B1A.write_analog(off)
    B1B.write_analog(on)
    sleep(2000)
    # Turn motor off
    display.show(Image.NO)
    B1B.write_analog(off)
