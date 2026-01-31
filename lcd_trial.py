from machine import Pin, I2C
from machine_i2c_lcd import I2cLcd
import time

# Set up I2C (D1 = SCL, D2 = SDA on NodeMCU)
i2c = I2C(scl=Pin(5), sda=Pin(4), freq=400000)

# LCD address and dimensions
lcd = I2cLcd(i2c, 0x27, 2, 16)  # 2 rows, 16 columns

for i in range(1,6):
    lcd.clear()
    lcd.move_to(0,0)
    lcd.putstr(str(i))
    time.sleep(1)
