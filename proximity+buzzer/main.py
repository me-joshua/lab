# CONNECTIONS (Physical Pins):
# PROXIMITY SENSOR (IR): 
# VCC -> Pin 2 (5V) or Pin 1 (3.3V) 
# GND -> Pin 14 (GND)
# OUT -> Pin 11 (GPIO 17)

# BUZZER (3-Pin Module with 'S'):
# S (Signal) -> Pin 12 (GPIO 18)
# V (VCC)    -> Pin 4 (5V)
# - (GND)    -> Pin 6 (GND)

# RESISTORS: 
# Modules usually have onboard resistors. No external resistors needed. 
# If signal is too weak, a 1k Ohm resistor between S and GPIO 18 is optional.

# INSTALLATION:
# sudo apt-get install python3-gpiozero

from gpiozero import DigitalInputDevice, Buzzer
from signal import pause
import time

# Initialize Proximity (IR) on GPIO 17 and Buzzer on GPIO 18
# Proximity sensors are often "Active Low" (0 when detecting something)
proximity = DigitalInputDevice(17, pull_up=True)
buzzer = Buzzer(18)

def object_detected():
    print("Object Detected! Alarm ON")
    buzzer.on()

def object_cleared():
    print("Clear. Alarm OFF")
    buzzer.off()

# Link actions to sensor states
proximity.when_activated = object_cleared    # Sensor output is HIGH (Idle)
proximity.when_deactivated = object_detected # Sensor output is LOW (Detecting)

try:
    print("Security System Active. Press Ctrl+C to exit.")
    pause() # Keeps the script running to listen for events

except KeyboardInterrupt:
    print("\nSystem Deactivated.")
    buzzer.off()