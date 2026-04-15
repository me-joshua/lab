# ------------------------------------------------------------------------------
# 1. INSTALLATION COMMANDS (Run these on your Pi after pulling from Git)
# ------------------------------------------------------------------------------
# sudo apt-get update
# sudo apt-get install python3-dev python3-pip -y
# sudo pip3 install spidev mfrc522 --break-system-packages

# RC522 PIN    | RPi PIN (PHYSICAL) | RPi GPIO NAME
# -------------|--------------------|------------------
# SDA (SS)     | Pin 24             | GPIO 8
# SCK          | Pin 23             | GPIO 11
# MOSI         | Pin 19             | GPIO 10
# MISO         | Pin 21             | GPIO 9
# IRQ          | -- NOT CONNECTED --| --
# GND          | Pin 6              | Ground
# RST          | Pin 22             | GPIO 25
# 3.3V         | Pin 1              | 3.3V (!!! DO NOT USE 5V !!!)
# ------------------------------------------------------------------------------

import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522
import time

# Initialize the MFRC522 reader
reader = SimpleMFRC522()

def enable_high_sensitivity():
    """
    TROUBLESHOOTING: 'High Power' Antenna Configuration.
    Modifies Register 0x26 (RFCfgReg) to set RxGain to 48dB (Maximum).
    This significantly improves the range and recognition of small tags 
    like the blue keychains and chips.
    """
    print(">>> Optimizing antenna gain for maximum sensitivity (48dB)...")
    # 0x07 << 4 sets the RxGain bits (6, 5, 4) to 111 (max gain)
    reader.reader.MFRC522_Write(0x26, 0x07 << 4)

def start_scan():
    enable_high_sensitivity()
    print(">>> System Live. Place your keychain/chip near the sensor.")
    print(">>> Press Ctrl+C to terminate.")
    
    try:
        while True:
            # reader.read() blocks until a tag is detected
            tag_id, tag_text = reader.read()
            
            print("\n" + "="*30)
            print(f"[*] TAG DETECTED")
            print(f"[*] ID:   {tag_id}")
            
            # Display text data if the tag isn't empty
            clean_text = tag_text.strip()
            if clean_text:
                print(f"[*] DATA: {clean_text}")
            else:
                print(f"[*] DATA: [Memory Empty]")
            print("="*30)
            
            # Prevents spamming the console for the same tag hold
            time.sleep(2)
            
    except KeyboardInterrupt:
        print("\n[!] Stopping scanner...")
    finally:
        # Crucial to prevent short circuits and clear GPIO states
        GPIO.cleanup()
        print("[!] GPIO Cleaned up. System offline.")

if __name__ == "__main__":
    start_scan()