from microbit import *

while True:
    infrared_sensor = pin0.read_analog()
    print('IR sensor = ', infrared_sensor)
  
    if infrared_sensor <= 100:
        display.show(Image.YES)
    else:
        display.show(Image.NO)
