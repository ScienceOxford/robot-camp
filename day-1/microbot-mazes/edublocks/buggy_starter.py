from microbit import *
on=511
off=1023
def stop(time):
  display.clear()
  pin14.write_analog(off)
  pin13.write_analog(off)
  pin12.write_analog(off)
  pin15.write_analog(off)
  sleep(time)
def forward(time):
  display.show(Image.ARROW_N)
  pin14.write_analog(on)
  pin13.write_analog(off)
  pin12.write_analog(on)
  pin15.write_analog(off)
  sleep(time)
def backward(time):
  display.show(Image.ARROW_S)
  pin14.write_analog(off)
  pin13.write_analog(on)
  pin12.write_analog(off)
  pin15.write_analog(on)
  sleep(time)
def left_turn(time):
  display.show(Image.ARROW_W)
  pin14.write_analog(off)
  pin13.write_analog(on)
  pin12.write_analog(on)
  pin15.write_analog(off)
  sleep(time)
def right_turn(time):
  display.show(Image.ARROW_E)
  pin14.write_analog(on)
  pin13.write_analog(off)
  pin12.write_analog(off)
  pin15.write_analog(on)
  sleep(time)
stop(1)
