# CONNECTIONS (Digital Output Mode):
# MQ3 VCC -> Physical Pin 2 (5V)
# MQ3 GND -> Physical Pin 6 (GND)
# MQ3 DO  -> Physical Pin 11 (GPIO 17)
#
# NOTE: 
# 1. Raspberry Pi lacks Analog pins. This code uses the Digital Out (DO) pin.
# 2. Adjust the blue potentiometer on the sensor to set the detection threshold.
# 3. Sensor needs ~60s to "warm up" (the internal heater) before readings stabilize.
#
# INSTALLATION:
# pip install gpiozero

from gpiozero import DigitalInputDevice
from time import sleep

# Initialize MQ3 on GPIO 17
# Most MQ3 modules are 'Active Low' (output 0 when alcohol is detected)
sensor = DigitalInputDevice(17)

try:
    print("Sensor Warming Up...")
    while True:
        # Check if sensor is triggered (LOW state)
        if sensor.value == 0:
            print("ALERT: Alcohol Detected!")
        else:
            print("Status: Clear")
        
        sleep(0.5)

except KeyboardInterrupt:
    print("Exiting...")