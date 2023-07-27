from microbit import *

def config(leftForward=pin13, leftBackward=pin12, rightForward=pin15, rightBackward=pin14):
    '''
    This function assigns which micro:bit pin controls which motor direction.
    You must call this function at the start of your program.
    '''
    global FL, BL, FR, BR
    FL = leftForward
    BL = leftBackward
    FR = rightForward
    BR = rightBackward

def drive(leftVelocity, rightVelocity):
    '''
    This function controls the robot's left and right motors, within the range -1023 to 1023.
    '''
    L = leftVelocity
    R = rightVelocity
    # Below controls the left wheel: forward, backward, stop at given speed
    if L > 0 and L <= 1023:
        FL.write_analog(abs(L))  # go forwards at speed given
        BL.write_analog(0)         # don't go backwards
    elif L < 0 and L >= -1023:
        FL.write_analog(0)         # don't go forwards
        BL.write_analog(abs(L))  # go backwards at speed given
    else:
        FL.write_analog(0)         # stop the left wheel
        BL.write_analog(0)
    # Below controls the right wheel: forward, backward, stop at given speed
    if R > 0 and R <= 1023:
        FR.write_analog(abs(R))  # go forwards at speed given
        BR.write_analog(0)         # don't go backwards
    elif R < 0 and R >= -1023:
        FR.write_analog(0)         # don't go forwards
        BR.write_analog(abs(R))  # go backwards at speed given
    else:
        FR.write_analog(0)         # stop the right wheel
        BR.write_analog(0)

def stop():
    '''
    This function turns off the motors.
    '''
    drive(0, 0)
