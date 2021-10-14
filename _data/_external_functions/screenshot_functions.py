#!/usr/bin/python3

import pyautogui as pygui
import os

def take_screenshot():
    ss = pygui.screenshot()
    cd = os.getcwd()
    ss.save("Screenshot.png")
    os.replace("Screenshot.png", cd+"/_data/_screenshot/Screenshot.png")
    return
