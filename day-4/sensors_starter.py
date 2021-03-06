from microbit import *

# Please tag us if used!
# We'd love to see what you make:
# @ScienceOxford

# Line-following robot code for microbit with L9110s motor driver
# Thanks to MultiWingSpan, whose code for the Bit:Bot was a great starting point
# http://www.multiwingspan.co.uk/micro.php?page=botline

LF = pin14
LB = pin13
RF = pin12
RB = pin15


# 1023 turns the motors off; 0 turns them on at full speed
def stop():
    LF.write_analog(1023)
    LB.write_analog(1023)
    RF.write_analog(1023)
    RB.write_analog(1023)


# The L9110s motor driver uses an input of 0 (low) to turn the motor on at full speed, and an input of 1023 (high) to turn it off
# The below function flips this so that when calling drive(), a high number runs the motors faster
def drive(left_motor, right_motor):
    # Below controls the left wheel: forward, backward, stop at given speed
    if left_motor > 0 and left_motor <= 1023:
        LF.write_analog(abs(left_motor-1023))  # go forwards at speed given
        LB.write_analog(1023)         # don't go backwards
    elif left_motor < 0 and left_motor >= -1023:
        LF.write_analog(1023)         # don't go forwards
        LB.write_analog(abs(left_motor+1023))  # go backwards at speed given
    else:
        LF.write_analog(1023)         # stop the left wheel
        LB.write_analog(1023)
    # Below controls the right wheel: forward, backward, stop at given speed
    if right_motor > 0 and right_motor <= 1023:
        RF.write_analog(abs(right_motor-1023))  # go forwards at speed given
        RB.write_analog(1023)         # don't go backwards
    elif right_motor < 0 and right_motor >= -1023:
        RF.write_analog(1023)         # don't go forwards
        RB.write_analog(abs(right_motor+1023))  # go backwards at speed given
    else:
        RF.write_analog(1023)         # stop the right wheel
        RB.write_analog(1023)

# WRITE YOUR CODE BELOW HERE
