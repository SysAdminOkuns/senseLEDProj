from sense_hat import SenseHat
from random import randint
from time import sleep

sense = SenseHat()

sense.clear(255, 255, 255)
sense.low_light = True
sleep(2)
sense.low_light = False

"""
for i in reversed(range(0,10)):
    sense.show_letter(str(i))
    sleep(1)
"""
# sense.show_message("Hello World")
"""
while True:
  x= randint(0, 7)
  y= randint(0, 7)
  r= randint(0, 255)
  g= randint(0, 255)
  b= randint(0, 255)
  sense.set_pixel(x, y, r, g, b)
  sleep(0.0001)

sense.clear()
"""