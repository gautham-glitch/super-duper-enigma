from pymata4 import pymata4
import tkinter as tk
from collections import deque

# Arduino setup
board = pymata4.Pymata4()

SERVO_PIN = 9
POT_PIN = 0

# Set pin modes
board.set_pin_mode_servo(SERVO_PIN)
board.set_pin_mode_analog_input(POT_PIN)

# Buffer for smoothing
buffer_size = 10
readings = deque(maxlen=buffer_size)

# Tkinter GUI setup
root = tk.Tk()
root.title("Servo Control Panel")
root.geometry("350x250")

# Variables
angle_var = tk.IntVar()
checkbox_var = tk.BooleanVar()
slider_var = tk.IntVar()

# GUI Elements
angle_label = tk.Label(root, textvariable=angle_var, font=("Arial", 24))
angle_label.pack(pady=10)

def reset_servo():
    board.servo_write(SERVO_PIN, 0)
    angle_var.set(0)

reset_button = tk.Button(root, text="Reset to 0°", command=reset_servo)
reset_button.pack(pady=10)

checkbox = tk.Checkbutton(root, text="Use Potentiometer", variable=checkbox_var)
checkbox.pack()

slider = tk.Scale(root, from_=0, to=180, orient=tk.HORIZONTAL, variable=slider_var,
                  label="Manual Servo Control", length=250)
slider.pack(pady=10)

# Callback for potentiometer
def update_servo():
    if checkbox_var.get():
        value = board.analog_read(POT_PIN)[0]  # Read value
        readings.append(value)
        avg = sum(readings) / len(readings)
        angle = int(avg * 180)
        board.servo_write(SERVO_PIN, angle)
        angle_var.set(angle)
    root.after(100, update_servo)

# Manual control loop
def manual_control_loop():
    if not checkbox_var.get():
        angle = slider_var.get()
        board.servo_write(SERVO_PIN, angle)
        angle_var.set(angle)
    root.after(100, manual_control_loop)

# Start loops
update_servo()
manual_control_loop()

# Run GUI
root.mainloop()

# Cleanup on exit
board.shutdown()