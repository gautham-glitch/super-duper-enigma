import machine
import dht
import time



dht = dht.DHT11(machine.Pin(12))

while True :
    try:
        dht.measure()
        temp = dht.temperature()
        hum = dht.humidity()
        print(f"temperature: {temp}°C | Humidity: {hum}% ", end = "\r")
        
    except OSError as e:
        print(e)
    time.sleep_us(5)
        