# CONNECTIONS:
# DHT11 VCC  -> Physical Pin 1 (3.3V)
# DHT11 DATA -> Physical Pin 7 (GPIO 4)
# DHT11 GND  -> Physical Pin 9 (GND)
# (Add 10k resistor between VCC & DATA if using a bare 4-pin sensor)
#
# INSTALLATION:
# pip install adafruit-circuitpython-dht
# sudo apt install libgpiod2

import time
import board
import adafruit_dht

# Initialize DHT11 on GPIO 4
dht_device = adafruit_dht.DHT11(board.D4)

try:
    while True:
        try:
            temp = dht_device.temperature
            hum = dht_device.humidity
            if temp is not None and hum is not None:
                print(f"Temp: {temp:.1f}C | Humidity: {hum}%")
        
        except RuntimeError:
            # DHT sensors are timing-sensitive; ignore occasional read errors
            pass
            
        time.sleep(2.0)

except KeyboardInterrupt:
    dht_device.exit()