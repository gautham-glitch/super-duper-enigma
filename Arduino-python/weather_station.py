from pymata4 import pymata4
import time
import datetime

# Setup
board = pymata4.Pymata4()
DHT_PIN = 2  # Change to the digital pin your sensor is connected to

# Set pin mode for DHT sensor
board.set_pin_mode_dht(DHT_PIN, sensor_type=11, differential=0)  # 11 = DHT11, use 22 for DHT22

try:
    while True:
        # Read DHT sensor
        data = board.dht_read(DHT_PIN)
        temp = data[0]
        humi = data[1]
        now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        print(f"\r🌡️ Temp: {temp:.1f} °C | 💧 Humidity: {humi:.1f} % | Time: {now}", end="")
        time.sleep(0.5)

except KeyboardInterrupt:
    print("\nShutting down...")
    board.shutdown()


"""wiring :
VCC - 5v
gnd - gnd
data - d2"""