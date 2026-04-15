# CONNECTIONS (Physical Pins):
# RC522: SDA->24, SCK->23, MOSI->19, MISO->21, RST->22, VCC->1 (3.3V), GND->6
# BUZZER: S (Signal)->12 (GPIO 18), VCC->2 (5V), GND->14

# INSTALLATION:
# sudo pip3 install mfrc522 gpiozero --break-system-packages

import time
import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522
from gpiozero import Buzzer

# Initialize RFID and Buzzer
reader = SimpleMFRC522()
buzzer = Buzzer(18)

def boost_antenna_gain():
    # Troubleshooting: Set Antenna Gain to Maximum (48dB) 
    # Helps recognize the blue keychain/chip more easily.
    # Register 0x26 is RFCfgReg. Bits 4-6 set to 111 (0x07) for max power.
    print("[SYSTEM] Boosting antenna gain for easy recognition...")
    reader.reader.MFRC522_Write(0x26, 0x07 << 4)

def success_beep():
    # Short beep for successful read
    buzzer.on()
    time.sleep(0.2)
    buzzer.off()

def run_security_gate():
    boost_antenna_gain()
    print("[READY] Scan your tag to unlock...")
    
    try:
        while True:
            # reader.read() blocks until a tag is present
            tag_id, tag_text = reader.read()
            
            if tag_id:
                print(f"\n[!] ACCESS GRANTED")
                print(f"[*] ID: {tag_id}")
                success_beep()
                
                # Small delay to avoid multiple reads of the same tag
                time.sleep(2)
                print("\n[READY] Waiting for next scan...")

    except KeyboardInterrupt:
        print("\n[SHUTDOWN] Exiting...")
    finally:
        GPIO.cleanup()

if __name__ == "__main__":
    run_security_gate()