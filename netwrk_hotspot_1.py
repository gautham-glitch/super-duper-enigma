import network

ap = network.WLAN(network.AP_IF)
ap.active(True)
ap.config(essid='ESP32_Hotspot', password='24446666668888888')

print('Access Point created')
print('IP address:', ap.ifconfig()[0])