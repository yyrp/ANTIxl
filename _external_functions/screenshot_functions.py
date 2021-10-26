#!/usr/bin/python3

import pyautogui as pygui
import os
import sys

# Main function
def take_screenshot():
    # Takes screenshot
    ss = pygui.screenshot()

    # This gets the current working directory from file path files
    file_path = __file__
    cd = os.path.dirname(__file__)
    f = open(cd+r"/ef_file_path.txt", 'r')
    cd = f.read()
    f.close()

    # Saves screenshot
    ss.save("Screenshot.png")
    # Moves screenshot to '_screenshot'
    os.replace("Screenshot.png", cd+"/_data/_screenshot/Screenshot.png")
    return 'Done!'
