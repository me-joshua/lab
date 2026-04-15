# CONNECTIONS (Physical Pins):
# DHT11: VCC -> Pin 1 (3.3V), Data -> Pin 7 (GPIO 4), GND -> Pin 9 (GND)
# I2C LCD: VCC -> Pin 2 (5V), GND -> Pin 6 (GND), SDA -> Pin 3 (GPIO 2), SCL -> Pin 5 (GPIO 3)

# INSTALLATION:
# sudo pip3 install adafruit-circuitpython-dht RPLCD smbus2 --break-system-packages

import time
import board
import adafruit_dht
from RPLCD.i2c import CharLCD

# Initializing DHT11 on GPIO 4 and LCD on I2C address 0x27
dht_device = adafruit_dht.DHT11(board.D4)
lcd = CharLCD(i2c_expander='PCF8574', address=0x27, port=1, cols=16, rows=2)



try:
    print("Monitoring Temperature and Humidity...")
    while True:
        try:
            temp = dht_device.temperature
            hum = dht_device.humidity

            if temp is not None and hum is not None:
                lcd.clear()
                lcd.cursor_pos = (0, 0)
                lcd.write_string(f"Temp: {temp} C")
                lcd.cursor_pos = (1, 0)
                lcd.write_string(f"Humid: {hum}%")
                print(f"Temp: {temp}C | Humid: {hum}%")
            
        except RuntimeError as e:
            # DHT sensors often fail to read; continue to next attempt
            time.sleep(2.0)
            continue

        time.sleep(3.0)

except KeyboardInterrupt:
    lcd.clear()
    lcd.backlight_enabled = False
    dht_device.exit()