# CONNECTIONS:
# LED: Physical Pin 11 (GPIO 17)
# Buzzer S (Signal): Physical Pin 13 (GPIO 27)
# Buzzer + (VCC): Physical Pin 1 (3.3V)
# Buzzer - (GND): Physical Pin 9 (GND)
#
# INSTALLATION:
# pip install gpiozero

from gpiozero import LED, Buzzer
from time import sleep

# Initialize components
led = LED(17)
buzzer = Buzzer(27)

try:
    while True:
        # State 1: LED ON, Buzzer OFF
        led.on()
        buzzer.off()
        print("LED: ON  | Buzzer: OFF")
        sleep(0.5)
        
        # State 2: LED OFF, Buzzer ON
        led.off()
        buzzer.on()
        print("LED: OFF | Buzzer: ON")
        sleep(0.5)

except KeyboardInterrupt:
    # Safety reset on exit
    led.off()
    buzzer.off()