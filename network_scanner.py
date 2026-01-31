
import network
import time

# Set your current position manually
x = 1  # Replace with actual x-coordinate
y = 1  # Replace with actual y-coordinate

# File name
filename = "wifi_log.csv"

# Overwrite the file (clears previous data)
with open(filename, "w") as f:
    f.write("")  # Just clears the file

# Initialize Wi-Fi in station mode
wlan = network.WLAN(network.STA_IF)
wlan.active(True)

# Scan for networks
print("Scanning for Wi-Fi networks...")
networks = wlan.scan()

# Save results to CSV
with open(filename, "a") as f:
    for net in networks:
        ssid = net[0].decode('utf-8')
        rssi = net[3]
        line = f"{x},{y},{ssid},{rssi}\n"
        f.write(line)

print(f"Scan complete. {len(networks)} networks saved to {filename}.")
