
"""
⚠️ Educational Use Only ⚠️

This script simulates techniques used by malicious infostealers for learning and cybersecurity training purposes.
It does NOT perform real data exfiltration and avoids collecting sensitive information.
Run only in isolated environments for awareness and defense training.

Author: CiND2R1 (Youssef Hossam)
"""

import os
import json
import base64
import sqlite3
import shutil
import subprocess
import re
import zipfile
import ctypes
from PIL import ImageGrab

# Optional: simulate hidden console (commented for safety)
# ctypes.windll.user32.ShowWindow(ctypes.windll.kernel32.GetConsoleWindow(), 0)

OUTPUT_DIR = "output"
ZIP_NAME = "collected_simulation.zip"

def add_to_startup():
    # Simulated persistence (no actual file copying)
    print("[SIMULATION] Would copy file to startup folder for persistence.")

def get_master_key():
    # Simulated Chrome master key retrieval
    print("[SIMULATION] Would extract Chrome master key.")
    return b"fake-master-key"

def decrypt_password(buff, key):
    # Simulated decryption of a password
    print("[SIMULATION] Decrypting a password...")
    return "simulated_password"

def steal_chrome_passwords():
    print("[SIMULATION] Simulating Chrome password extraction...")
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    sample_data = [
        "Site: https://example.com\nUser: user@example.com\nPass: simulated_password\n" + "-"*40
    ]
    with open(f"{OUTPUT_DIR}/chrome_passwords.txt", "w", encoding="utf-8") as f:
        f.write("\n".join(sample_data))

def steal_wifi_passwords():
    print("[SIMULATION] Simulating Wi-Fi profile reading...")
    sample_wifi = ["Home_Network: simulated_wifi_password", "Cafe_Wifi: simulated1234"]
    with open(f"{OUTPUT_DIR}/wifi_passwords.txt", "w", encoding="utf-8") as f:
        f.write("\n".join(sample_wifi))

def steal_clipboard():
    print("[SIMULATION] Simulating clipboard access...")
    simulated_data = "Copied text (simulation)"
    with open(f"{OUTPUT_DIR}/clipboard.txt", "w", encoding="utf-8") as f:
        f.write(simulated_data)

def take_screenshot():
    print("[SIMULATION] Taking a screenshot (safe mode)...")
    img = ImageGrab.grab()
    img.save(f"{OUTPUT_DIR}/screenshot.png")

def compress_data():
    print("[SIMULATION] Compressing collected simulation data...")
    with zipfile.ZipFile(ZIP_NAME, 'w') as zipf:
        for root, _, files in os.walk(OUTPUT_DIR):
            for file in files:
                zipf.write(os.path.join(root, file), arcname=file)

def send_to_discord():
    print("[SIMULATION] Would send the zip to a remote server (disabled for safety).")

def main():
    add_to_startup()
    steal_chrome_passwords()
    steal_wifi_passwords()
    steal_clipboard()
    take_screenshot()
    compress_data()
    send_to_discord()
    print("[SIMULATION COMPLETE] All steps executed in safe mode.")

if __name__ == "__main__":
    main()