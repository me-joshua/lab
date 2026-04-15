# CONNECTIONS (Physical Pins):
# PIR MOTION SENSOR:
# VCC -> Pin 2 (5V), OUT -> Pin 26 (GPIO 7), GND -> Pin 25 (GND)
#
# PROXIMITY SENSOR (IR):
# VCC -> Pin 4 (5V), OUT -> Pin 11 (GPIO 17), GND -> Pin 9 (GND)
#
# BUZZER (3-Pin Module):
# S (Signal) -> Pin 12 (GPIO 18), VCC -> Pin 2 (5V), GND -> Pin 14 (GND)
#
# LED:
# Anode (Long Leg) -> 220 or 330 Ohm Resistor -> Pin 13 (GPIO 27)
# Cathode (Short Leg) -> Pin 39 (GND)

# INSTALLATION:
# sudo apt-get update
# sudo apt-get install python3-gpiozero

from gpiozero import MotionSensor, DigitalInputDevice, Buzzer, LED
from signal import pause

# Initializing sensors and outputs
# PIR is usually active HIGH on motion
pir = MotionSensor(7) 
# IR Proximity is usually active LOW when an object is detected
proximity = DigitalInputDevice(17, pull_up=True)
buzzer = Buzzer(18)
led = LED(27)

def motion_detected():
    print("[!] MOTION: LED ON")
    led.on()

def motion_stopped():
    print("[.] MOTION: LED OFF")
    led.off()

def object_near():
    print("[!] PROXIMITY: BUZZER ON")
    buzzer.on()

def object_far():
    print("[.] PROXIMITY: BUZZER OFF")
    buzzer.off()

# Mapping PIR Events
pir.when_motion = motion_detected
pir.when_no_motion = motion_stopped

# Mapping Proximity Events (Using deactivated for "near" because it's Active Low)
proximity.when_deactivated = object_near
proximity.when_activated = object_far



try:
    print("Dual-Layer Security System Active...")
    print("PIR controls LED | Proximity controls Buzzer")
    pause()

except KeyboardInterrupt:
    print("\nShutting down system.")
    led.off()
    buzzer.off()