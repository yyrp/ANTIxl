#!/usr/bin/python3

import pyautogui as pygui
import os

# Main function
def take_screenshot():
    # Takes screenshot
    ss = pygui.screenshot()
    cd = os.getcwd()
    # Saves screenshot
    ss.save("Screenshot.png")
    # Moves screenshot to '_screenshot'
    os.replace("Screenshot.png", cd+"/_data/_screenshot/Screenshot.png")
    return 'Done!'
