import machine
import time

mq2 = machine.ADC(0)
def get_air_quality(value):
    if value <= 300:
        return "Excellent 🌟"
    elif value <= 500:
        return "Good 😊"
    elif value <= 700:
        return "Moderate 😐"
    elif value <= 850:
        return "Poor 😷"
    else:
        return "Hazardous ☠"

while True :
    gas = mq2.read()
    print(f"Gas concentration: {(gas/1023) * 100}% | Air quality :{get_air_quality(gas)}" , end = "\r")
    time.sleep(1)