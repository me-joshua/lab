# CONNECTIONS (16x2 LCD - 4-bit Mode):
# LCD Pin 1 (VSS)  -> Physical Pin 6 (GND)
# LCD Pin 2 (VDD)  -> Physical Pin 2 (5V)
# LCD Pin 3 (V0)   -> Potentiometer Center Pin (Contrast)
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

def run_diagnostic():
    print("Starting LCD Diagnostic...")
    
    try:
        # Initialize LCD
        lcd = CharLCD(
            pin_rs=26, pin_e=19, 
            pins_data=[13, 6, 5, 11],
            numbering_mode=GPIO.BCM,
            cols=16, rows=2
        )

        # Step 1: Clear and Basic Write
        print("Step 1: Testing Text Display...")
        lcd.clear()
        lcd.write_string("LCD Diagnostic")
        lcd.cursor_pos = (1, 0)
        lcd.write_string("Line 2: OK")
        time.sleep(3)

        # Step 2: Test Cursor and Blinking
        print("Step 2: Testing Cursor...")
        lcd.clear()
        lcd.write_string("Testing Cursor")
        lcd.cursor_mode = 'blink'
        time.sleep(3)
        lcd.cursor_mode = 'hide'

        # Step 3: Test Scrolling
        print("Step 3: Testing Scrolling...")
        lcd.clear()
        long_text = "This is a long string to test scrolling functionality..."
        for i in range(len(long_text) - 16 + 1):
            lcd.cursor_pos = (0, 0)
            lcd.write_string(long_text[i:i+16])
            time.sleep(0.2)

        lcd.clear()
        lcd.write_string("Test Complete!")
        print("Diagnostic finished. If screen is blank, adjust the Potentiometer (Contrast).")

    except Exception as e:
        print(f"HARDWARE ERROR: {e}")
        print("Check: 1. Wiring 2. GPIO Numbers 3. Pin seating")
    finally:
        GPIO.cleanup()

if __name__ == "__main__":
    run_diagnostic()