# Importing modules
print("Importing modules...")

import time
import sys
import os

try:
    import pyautogui as pygui
except:
    print("You need to install the pyautogui module (pip install pyautogui).")
    sys.exit()

try:
    import tkinter as tk
except:
    print("You need to install the tkinter module (pip install tkinter).")
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

cd = os.path.realpath('IXL-Bot')
sys.path.insert(1, cd+'/Data/ExternalModules')

from ScreenshotVerify import screenshot_verify

sys.path.insert(1, cd)

print("Done!")

print()
print()
print()

# Prints keyboard and screenshot warning if it's the first time running.
screenshot_verify()
