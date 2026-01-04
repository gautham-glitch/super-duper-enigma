from pyfirmata2 import Arduino
import time

board = Arduino(Arduino.AUTODETECT)


led_pin = board.get_pin('d:8:o')

while True:
    led_pin.write(0) 
    time.sleep(1)
    led_pin.write(1)
    time.sleep(1)