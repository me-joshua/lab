# CONNECTIONS:
# VCC   -> Physical Pin 2 (5V)
# TRIG  -> Physical Pin 11 (GPIO 17)
# ECHO  -> Physical Pin 13 (GPIO 27) **REQUIRED: Use Voltage Divider**
# GND   -> Physical Pin 6  (GND)
#
# VOLTAGE DIVIDER (ECHO PROTECTION):
# Echo Pin -> 1k ohm resistor -> Physical Pin 13
# Physical Pin 13 -> 2k ohm resistor -> GND
#
# INSTALLATION:
# pip install gpiozero

from gpiozero import DistanceSensor
from time import sleep

# Initialize sensor
# Note: distance_sensor uses decimal meters by default (0.0 to 1.0)
sensor = DistanceSensor(echo=27, trigger=17, max_distance=2)

try:
    while True:
        # Convert meters to cm
        distance_cm = sensor.distance * 100
        print(f"Distance: {distance_cm:.2f} cm")
        sleep(0.5)

except KeyboardInterrupt:
    print("Measurement stopped by user")