# CONNECTIONS:
# S0  -> Physical Pin 15 (GPIO 22)
# S1  -> Physical Pin 16 (GPIO 23)
# S2  -> Physical Pin 18 (GPIO 24)
# S3  -> Physical Pin 22 (GPIO 25)
# OUT -> Physical Pin 13 (GPIO 27)
# LED -> Physical Pin 7  (GPIO 4)  <-- Controls the white lights
# VCC -> Physical Pin 2  (5V)
# GND -> Physical Pin 6  (GND)
#
# INSTALLATION:
# sudo apt-get install python3-rpi.gpio

import RPi.GPIO as GPIO
import time

# Pin Definitions
S0, S1, S2, S3 = 22, 23, 24, 25
OUT = 27
LED_PIN = 4

GPIO.setmode(GPIO.BCM)
GPIO.setup([S0, S1, S2, S3, LED_PIN], GPIO.OUT)
GPIO.setup(OUT, GPIO.IN, pull_up_down=GPIO.PUD_UP)

# Turn on the onboard white LEDs
GPIO.output(LED_PIN, GPIO.HIGH)

# Set Frequency scaling to 20% (Standard for Pi)
GPIO.output(S0, GPIO.HIGH)
GPIO.output(S1, GPIO.LOW)

def read_color(s2_val, s3_val):
    # Set photodiode filters
    GPIO.output(S2, s2_val)
    GPIO.output(S3, s3_val)
    time.sleep(0.1) # Stabilization
    
    # Measure frequency
    start = time.time()
    for _ in range(10):
        GPIO.wait_for_edge(OUT, GPIO.FALLING)
    duration = time.time() - start
    return 10 / duration 

try:
    print("Reading colors... Press Ctrl+C to stop.")
    while True:
        # Red Filter
        red = read_color(GPIO.LOW, GPIO.LOW)
        # Green Filter
        green = read_color(GPIO.HIGH, GPIO.HIGH)
        # Blue Filter
        blue = read_color(GPIO.LOW, GPIO.HIGH)
        
        print(f"R: {red:.0f} | G: {green:.0f} | B: {blue:.0f}")
        time.sleep(1)

except KeyboardInterrupt:
    # Turn off LEDs and clean up
    GPIO.output(LED_PIN, GPIO.LOW)
    GPIO.cleanup()