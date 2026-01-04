import time
from pymata4 import pymata4

# Setup board
board = pymata4.Pymata4()
LIGHT_PIN = 8  # Digital pin connected to DO of light sensor

# Set pin mode for digital input
board.set_pin_mode_digital_input(LIGHT_PIN)

try:
    while True:
        value = board.digital_read(LIGHT_PIN)[0]
        if value is not None:
            state = "Bright" if value else "Dark"
            print(f"Digital light sensor state: {state}")
        else:
            print("Waiting for sensor value...")
        time.sleep(0.5)

except KeyboardInterrupt:
    print("\nShutting down...")
    