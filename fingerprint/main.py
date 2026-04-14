# CONNECTIONS:
# R307 VCC -> Physical Pin 2 (5V)
# R307 GND -> Physical Pin 6 (GND)
# R307 TX  -> Physical Pin 10 (GPIO 15 - RXD)
# R307 RX  -> Physical Pin 8 (GPIO 14 - TXD)
#
# RASPI-CONFIG (CRITICAL):
# 1. sudo raspi-config
# 2. Interface Options -> Serial Port
# 3. Would you like a login shell...? NO
# 4. Would you like the serial port hardware...? YES
# 5. Finish and REBOOT
#
# INSTALLATION:
# pip install adafruit-circuitpython-fingerprint

import time
import serial
import adafruit_fingerprint

# Set up UART for R307
uart = serial.Serial("/dev/serial0", baudrate=57600, timeout=1)
finger = adafruit_fingerprint.Adafruit_Fingerprint(uart)

def get_fingerprint():
    print("Waiting for finger...")
    while finger.get_image() != adafruit_fingerprint.OK:
        pass
    
    print("Templating...")
    if finger.image_2_tz(1) != adafruit_fingerprint.OK:
        return False
        
    print("Searching...")
    if finger.finger_search() == adafruit_fingerprint.OK:
        print(f"Found ID #{finger.finger_id} with confidence {finger.confidence}")
        return True
    else:
        print("Finger not found")
        return False

# Basic Check
if finger.read_templates() != adafruit_fingerprint.OK:
    print("Failed to read templates from sensor")
else:
    print(f"Sensor contains {len(finger.templates)} templates")

try:
    while True:
        if get_fingerprint():
            time.sleep(2)
except KeyboardInterrupt:
    print("Exiting...")