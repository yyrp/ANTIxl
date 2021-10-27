#!/usr/bin/python3
import pyautogui as pygui
import os
import sys
import json

# Main function
def take_screenshot():
    # This gets the current working directory from file path files
    file_path = __file__[:-1]
    file_directory = os.path.dirname(__file__)
    file = open(file_directory+r"/ef_file_path.json")
    cd = json.load(file)
    
    # Takes screenshot
    ss = pygui.screenshot()

    # Saves screenshot
    ss.save("Screenshot.png")
    # Moves screenshot to '_screenshot'
    os.replace("Screenshot.png", cd+"/_data/_screenshot/Screenshot.png")
    return 'Done!'
