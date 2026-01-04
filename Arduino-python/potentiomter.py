from pymata4 import pymata4
import tkinter as tk
import time
import threading

# Setup Arduino
board = pymata4.Pymata4()

POT_PIN = 0     # Analog pin A0
LED_PIN = 9     # PWM pin D9

# Set pin modes
board.set_pin_mode_analog_input(POT_PIN)
board.set_pin_mode_pwm_output(LED_PIN)

# GUI Setup
root = tk.Tk()
root.title("LED Brightness Controller")

# Manual slider
slider = tk.Scale(root, from_=0, to=100, orient=tk.HORIZONTAL, label="Manual Brightness")
slider.pack()

# Potentiometer value label
pot_label = tk.Label(root, text="Potentiometer: 0")
pot_label.pack()

# Checkbox to toggle control mode
use_pot = tk.BooleanVar(value=True)
toggle = tk.Checkbutton(root, text="Use Potentiometer", variable=use_pot)
toggle.pack()

def update():
    while True:
        if use_pot.get():
            pot_value = board.analog_read(POT_PIN)[0]
            if pot_value is not None:
                brightness = int(pot_value * 255)
                board.pwm_write(LED_PIN, brightness)
                pot_label.config(text=f"Potentiometer: {int(pot_value * 100)}")
        else:
            val = slider.get()
            board.pwm_write(LED_PIN, int(val * 2.55))
            pot_label.config(text=f"Manual: {val}")
        time.sleep(0.05)

# Start background thread
threading.Thread(target=update, daemon=True).start()

# Run GUI
root.mainloop()

# Cleanup on exit