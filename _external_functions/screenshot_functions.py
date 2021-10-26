#!/usr/bin/python3
import pyautogui as pygui
import os
import sys
import json

# Main function
def take_screenshot():
    # Takes screenshot
    ss = pygui.screenshot()

    # This gets the current working directory from file path files
    file_path = __file__
    file_directory = os.path.dirname(__file__)
    cd = json.load(file_directory+r"ef_file_path.json")

    # Saves screenshot
    ss.save("Screenshot.png")
    # Moves screenshot to '_screenshot'
    os.replace("Screenshot.png", cd+"/_data/_screenshot/Screenshot.png")
    return 'Done!'
