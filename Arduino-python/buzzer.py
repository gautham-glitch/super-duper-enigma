from pyfirmata2 import Arduino
import time

board = Arduino(Arduino.AUTODETECT)
buzzer = board.get_pin('d:9:o')  # digital pin 9, output mode

# Define a rhythm pattern (durations in seconds)
tune_pattern = [0.1, 0.2, 0.1, 0.3, 0.1, 0.4, 0.1, 0.2]

for duration in tune_pattern:
    buzzer.write(1)  # buzzer ON
    time.sleep(duration)
    buzzer.write(0)  # buzzer OFF
    time.sleep(0.1)  # short pause between notes

board.exit()