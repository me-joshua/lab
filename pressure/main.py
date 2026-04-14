# CONNECTIONS:
# VCC -> Physical Pin 1 (3.3V)
# GND -> Physical Pin 6 (GND)
# SDA -> Physical Pin 3 (GPIO 2)
# SCL -> Physical Pin 5 (GPIO 3)
#
# RASPI-CONFIG:
# 1. sudo raspi-config
# 2. Interface Options -> I2C -> Enable -> YES
# 3. Finish and REBOOT
#
# INSTALLATION:
# pip install adafruit-circuitpython-bmp280
# If the sensor isn't detected, run sudo i2cdetect -y 1 in the terminal. If the table is empty, check your SDA/SCL wiring or ensure I2C is enabled in raspi-config.
import time
import board
import adafruit_bmp280

# Create I2C bus interface
i2c = board.I2C()

# Initialize sensor (Address is usually 0x76 or 0x77)
try:
    bmp280 = adafruit_bmp280.Adafruit_BMP280_I2C(i2c, address=0x76)
except ValueError:
    bmp280 = adafruit_bmp280.Adafruit_BMP280_I2C(i2c, address=0x77)

# Change this to your local sea level pressure for accurate altitude
bmp280.sea_level_pressure = 1013.25

try:
    while True:
        print(f"\nTemperature: {bmp280.temperature:.2f} C")
        print(f"Pressure: {bmp280.pressure:.2f} hPa")
        print(f"Altitude: {bmp280.altitude:.2f} meters")
        time.sleep(2)

except KeyboardInterrupt:
    print("Program Stopped")