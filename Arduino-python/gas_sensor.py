import serial
import time

arduino = serial.Serial('COM3', 9600)  # Replace with your port
time.sleep(2)

while True:
    if arduino.in_waiting:
        value = arduino.readline().decode().strip()
        print(f"\r{value}")