# CONNECTIONS:
# Physical Pin 11 (GPIO 17) -> 220 ohm Resistor -> LED Anode (+)
# Physical Pin 6 (GND) -> LED Cathode (-)
#
# INSTALLATION:
# pip install gpiozero

from gpiozero import LED
from time import sleep

# Initialize LED on GPIO 17
led = LED(17)

try:
    while True:
        led.on()
        print("LED ON")
        sleep(1)
        led.off()
        print("LED OFF")
        sleep(1)
except KeyboardInterrupt:
    # Clean exit on Ctrl+C
    led.off()