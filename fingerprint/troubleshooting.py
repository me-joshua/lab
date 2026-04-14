# CONNECTIONS:
# R307 VCC -> Physical Pin 2 (5V)
# R307 GND -> Physical Pin 6 (GND)
# R307 TX  -> Physical Pin 10 (GPIO 15 - RXD)
# R307 RX  -> Physical Pin 8 (GPIO 14 - TXD)
# Note: R307 TX goes to Pi RX; R307 RX goes to Pi TX.
#
# RASPI-CONFIG:
# 1. sudo raspi-config
# 2. Interface Options -> Serial Port
# 3. Login shell over serial? -> NO
# 4. Serial port hardware enabled? -> YES
# 5. REBOOT
#
# INSTALLATION:
# pip install adafruit-circuitpython-fingerprint pyserial

import time
import serial
import adafruit_fingerprint

# Troubleshooting Logic: Testing common UART ports and baud rates
def test_connection():
    # Use /dev/serial0 (primary UART) or /dev/ttyS0 / /dev/ttyAMA0
    port = "/dev/serial0"
    # Default R307 baud is usually 57600. Some use 9600.
    baud_rates = [57600, 9600]

    for baud in baud_rates:
        print(f"Testing {port} at {baud} baud...")
        try:
            uart = serial.Serial(port, baudrate=baud, timeout=1)
            finger = adafruit_fingerprint.Adafruit_Fingerprint(uart)
            
            if finger.read_templates() == adafruit_fingerprint.OK:
                print(f"SUCCESS: Sensor found at {baud} baud!")
                print(f"Templates stored: {len(finger.templates)}")
                print(f"Library version: {finger.library_version}")
                return finger
            else:
                print("Sensor not responsive at this baud rate.")
        except Exception as e:
            print(f"Error opening port: {e}")
            print("CHECK: Is 'Serial Port' enabled and 'Serial Console' disabled in raspi-config?")
    return None

# Main Troubleshooting Execution
finger = test_connection()

if finger:
    print("\n--- Diagnostic Check ---")
    # Verify sensor hardware status
    if finger.get_image() == adafruit_fingerprint.NOFINGER:
        print("Hardware Status: OK (Waiting for finger...)")
    else:
        print("Hardware Status: Unknown - verify wiring.")
else:
    print("\n--- FAILURE ---")
    print("1. Swap TX and RX wires (Physical Pin 8 and 10).")
    print("2. Check VCC is on 5V (Physical Pin 2).")
    print("3. Ensure user is in 'dialout' group: sudo usermod -a -G dialout $USER")