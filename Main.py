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

from cd+"/Data/ExternalModules/ScreenshotVerify.py" import screenshot_verify

print("Done!")

screenshot_verify()

cd = os.getcwd()
