# Importing modules
print("Importing modules...")

import time
import sys
import os

try:
    import tkinter as tk
except:
    print("You need to install the tkinter module (sudo apt-get install python3-tk python3-dev).")
    sys.exit()

try:
    import pyautogui as pygui
except:
    print("You need to install the pyautogui module (pip install pyautogui).")
    sys.exit()

try:
    import cv2
except:
    print("You need to install the cv2 module (pip install opencv-python).")
    sys.exit()

try:
    import pytesseract
except:
    print("You need to install the pytesseract module (pip install pytesseract).")
    sys.exit()

cd = os.getcwd()
sys.path.insert(1, cd+'/Data/ExternalModules')

from ScreenshotVerify import screenshot_verify

from ScreenshotModules import take_screenshot

from ScreenshotModules import save_screenshot

sys.path.insert(1, cd)

print("Done!")

print()
print()
print()

def scan_func():
    dir = cd+"/Data/Screenshot"
    for f in os.listdir(dir):
        os.remove(os.path.join(dir, f))

    ss = take_screenshot()
    save_screenshot(ss)

    return "Done!"

# Prints keyboard and screenshot warning if it's the first time running.
screenshot_verify()

# This is where the actual script starts
pygui.alert("Welcome.")
while True:
    main_input = pygui.confirm("...", buttons=["Scan", "Quit"])

    if main_input == "Quit":
        sys.exit()
    elif main_input == "Scan":
        scan_func()
    else:
        pygui.alert("Please enter a valid action.")
