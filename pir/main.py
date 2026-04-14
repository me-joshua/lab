# CONNECTIONS:
# PIR VCC -> Physical Pin 2 (5V)
# PIR GND -> Physical Pin 6 (GND)
# PIR OUT -> Physical Pin 11 (GPIO 17)
#
# INSTALLATION:
# pip install gpiozero
#
# ADJUSTMENTS:
# - Time Potentiometer: Turn fully counter-clockwise (for shortest delay).
# - Sensitivity Potentiometer: Adjust for range (up to 7 meters).
# - Jumper: Set to 'H' (Repeatable Trigger) for continuous detection.

from gpiozero import MotionSensor
from signal import pause

# Initialize PIR on GPIO 17
pir = MotionSensor(17)

def motion_detected():
    print("Motion Detected!")

def motion_stopped():
    print("Motion Stopped")

# Assign events
pir.when_motion = motion_detected
pir.when_no_motion = motion_stopped

try:
    print("PIR Sensor Warming Up...")
    pause() # Keeps the script running to listen for events
except KeyboardInterrupt:
    print("Exiting...")