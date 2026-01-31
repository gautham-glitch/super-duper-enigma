from machine import Pin, I2C
from machine_i2c_lcd import I2cLcd
import time, dht, network, uselect, sys, ubinascii

# --- CONFIGURATION & AUTO-DETECTION ---
i2c = I2C(scl=Pin(4), sda=Pin(5), freq=100000)

#--weather config--
last_measure = 0
measure_interval = 3000
mode = "idle"

def find_lcd():
    """Auto-detects LCD address to avoid ENODEV errors."""
    devices = i2c.scan()
    if not devices:
        print("No I2C devices found! Check D1/D2 wiring.")
        return None
    # Pick the first device found (usually 0x27 or 0x3F)
    return I2cLcd(i2c, devices[0], 2, 16)

def make_net(password, ssid):
    """Starts a WiFi Access Point (Hotspot) from the ESP8266."""
    ap = network.WLAN(network.AP_IF)
    ap.active(True)
    
    # WiFi standard requires passwords to be at least 8 characters
    if len(password) < 8:
        print("Password too short! Padding with zeros...")
        password = password + ("0" * (8 - len(password)))
        
    try:
        ap.config(essid=ssid, password=password)
        addr = ap.ifconfig()[0]
        print(f"Hotspot Active! SSID: {ssid} | IP: {addr}")
        update_lcd("AP: " + ssid, addr)
    except Exception as e:
        print("Failed to start Hotspot:", e)
        update_lcd("AP Failed", "Check Console")

lcd = find_lcd()
dht_sensor = dht.DHT11(Pin(14)) # Use D5 (GPIO14) for stability
buzzer = Pin(0, Pin.OUT)

poll_obj = uselect.poll()
poll_obj.register(sys.stdin, uselect.POLLIN)

# --- UTILITY FUNCTIONS ---
def update_lcd(line1, line2=""):
    """Safe wrapper for all LCD calls."""
    if not lcd: return
    try:
        lcd.clear()
        lcd.putstr(f"{line1}\n{line2}")
    except OSError:
        print("I2C Timeout: LCD failed to respond.")

def get_wifi():
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    update_lcd("Scanning...", "Please wait")
    
    # Map numerical auth modes to readable text
    # 0:open, 1:WEP, 2:WPA-PSK, 3:WPA2-PSK, 4:WPA/WPA2-PSK
    auth_modes = {0: "Open", 1: "WEP", 2: "WPA", 3: "WPA2", 4: "WPA/WPA2"}
    
    try:
        nets = sorted(wlan.scan(), key=lambda x: x[3], reverse=True)
    except:
        print("Scan failed")
        return

    print(f"\n{'SSID':<20}  {'Signal':<7}  {'Security':<10}  {'Channel':<15}  {'BSSID':<10}  {'is it hidden?':<10}")
    print("-" * 82)

    for n in nets:
        ssid = n[0].decode('utf-8', 'ignore')
        bssid = ubinascii.hexlify(n[1], ':').decode() # Convert MAC to human readable
        channel = n[2]
        rssi = n[3]
        auth = auth_modes.get(n[4], "Unknown")
        hidden = "Yes" if n[5] == 1 else "No"
        
        if not ssid or n[5] == 1:
            ssid = "<HIDDEN>"
            
        # Convert RSSI to 0-100% Quality
        quality = max(0, min(100, 2 * (rssi + 100)))
        
        print(f"{ssid:<20} | {quality:>5}% | {auth:<10} | Ch: {channel:<9} | {bssid:<10} | {hidden}")

    if nets:
        ssid = nets[0][0].decode('utf-8', 'ignore')
        display_ssid = ssid if len(ssid) <= 16 else ssid[:13] + "..."
        update_lcd("Best Net:", display_ssid)

def get_weather():
    try:
        # DHT11 needs at least 1-2 seconds between readings
        dht_sensor.measure()
        t, h = dht_sensor.temperature(), dht_sensor.humidity()
        update_lcd(f"Temp: {t}C", f"Hum: {h}%")
        if h >= 75: 
            buzzer.on(); time.sleep(0.2); buzzer.off()
    except OSError:
        update_lcd("Sensor Error", "Check D5 wiring")

# --- MAIN LOOP ---
print("Ready! Commands: [H/T] Weather, [W] WiFi, [O] Hotspot")
update_lcd("Waiting...")
while True:
    if mode == "weather":
        if time.ticks_diff(time.ticks_ms(), last_measure) > measure_interval:
            get_weather()
            last_measure = time.ticks_ms()
        
    if poll_obj.poll(0):
        char = sys.stdin.read(1).lower()
        if char in ['h', 't']:
            print("Entering Continuous Weather Mode...")
            mode = "weather"
            get_weather()
        elif char == 'w':
            print("in wifi mode, press 'h' to get back to weather mode")
            mode = "wifi"
            get_wifi()
        elif char == 'o':
            mode = "hotspot"
            while poll_obj.poll(0): sys.stdin.read(1)
            ssid = input("AP Name: ")
            pw = input("Password: ")
            make_net(pw, ssid)
            
    time.sleep(0.1)
