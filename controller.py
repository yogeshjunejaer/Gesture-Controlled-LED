import inspect
# Patch inspect.getargspec for compatibility with Python 3.11+
if not hasattr(inspect, "getargspec"):
    inspect.getargspec = inspect.getfullargspec

import pyfirmata

comport = 'COM24'
board = pyfirmata.Arduino(comport)

led_1 = board.get_pin('d:12:o')
led_2 = board.get_pin('d:10:o')
led_3 = board.get_pin('d:11:o')
led_4 = board.get_pin('d:12:o')
led_5 = board.get_pin('d:13:o')

def led(fingerUp):
    if fingerUp == [0, 0, 0, 0, 0]:
        led_1.write(0)
        led_2.write(0)
        led_3.write(0)
        led_4.write(0)
        led_5.write(0)
    elif fingerUp == [0, 1, 0, 0, 0]:
        led_1.write(1)
        led_2.write(0)
        led_3.write(0)
        led_4.write(0)
        led_5.write(0)
    elif fingerUp == [0, 1, 1, 0, 0]:
        led_1.write(1)
        led_2.write(1)
        led_3.write(0)
        led_4.write(0)
        led_5.write(0)
    elif fingerUp == [0, 1, 1, 1, 0]:
        led_1.write(1)
        led_2.write(1)
        led_3.write(1)
        led_4.write(0)
        led_5.write(0)
    elif fingerUp == [0, 1, 1, 1, 1]:
        led_1.write(1)
        led_2.write(1)
        led_3.write(1)
        led_4.write(1)
        led_5.write(0)
    elif fingerUp == [1, 1, 1, 1, 1]:
        led_1.write(1)
        led_2.write(1)
        led_3.write(1)
        led_4.write(1)
        led_5.write(1)
