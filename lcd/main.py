# CONNECTIONS (16x2 LCD):
# LCD Pin 1 (VSS)  -> Physical Pin 6 (GND)
# LCD Pin 2 (VDD)  -> Physical Pin 2 (5V)
# LCD Pin 3 (V0)   -> Potentiometer Center (Contrast)
# LCD Pin 4 (RS)   -> Physical Pin 37 (GPIO 26)
# LCD Pin 5 (RW)   -> Physical Pin 34 (GND)
# LCD Pin 6 (E)    -> Physical Pin 35 (GPIO 19)
# LCD Pin 11 (D4)  -> Physical Pin 33 (GPIO 13)
# LCD Pin 12 (D5)  -> Physical Pin 31 (GPIO 6)
# LCD Pin 13 (D6)  -> Physical Pin 29 (GPIO 5)
# LCD Pin 14 (D7)  -> Physical Pin 23 (GPIO 11)
# LCD Pin 15 (A)   -> Physical Pin 4 (5V)
# LCD Pin 16 (K)   -> Physical Pin 39 (GND)
#
# INSTALLATION:
# pip install RPLCD

import RPi.GPIO as GPIO
from RPLCD.gpio import CharLCD
import time

# Initialize LCD (16x2)
lcd = CharLCD(
    pin_rs=26, pin_e=19, 
    pins_data=[13, 6, 5, 11],
    numbering_mode=GPIO.BCM,
    cols=16, rows=2
)

try:
    lcd.clear()
    lcd.write_string("Hello Joshua!")
    
    while True:
        lcd.cursor_pos = (1, 0) # Move to second row
        lcd.write_string(time.strftime("%H:%M:%S"))
        time.sleep(1)

except KeyboardInterrupt:
    lcd.clear()
    GPIO.cleanup()