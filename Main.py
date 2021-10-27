#!/usr/bin/python3

# Importing modules
print("Importing modules...")

import sys
import os
import platform
import json

# These variables are used to see what libraries are or aren't installed
cv2_error = False
pygui_error = False
pytesseract_error = False

# This gets the current working directory from file path files
def get_cd():
    file_path = __file__
    cd = os.path.dirname(__file__)
    # Prints the 'IXL-Bot' file path
    print()
    print("NOTE: The file path to 'IXL-Bot' is '"+cd+"'")
    print()

    # Writes the file path to all the file path files
    with open(cd+r"/_data/data_file_path.json", 'w') as dump_file:
        json.dump(cd, dump_file)
    with open(cd+r"/_external_functions/ef_file_path.json", 'w') as dump_file:
        json.dump(cd, dump_file)
    with open(cd+r"/path.json", 'w') as dump_file:
        json.dump(cd, dump_file)

    return cd

cd = get_cd()

# This is the function checks what libraries need to be installed
def library_install_check():
    libraries_that_need_installed = []

    # This prints what libraries need to be installed
    if pygui_error == True:
        libraries_that_need_installed.append("  - pyautogui (pip install pyautogui)")
    if pytesseract_error == True:
        libraries_that_need_installed.append("  - pytesseract (pip install pytesseract)")
    if cv2_error == True:
        libraries_that_need_installed.append("  - cv2 (pip install opencv-python)")

    print()
    print(" ERROR: You need to install the following libraries:")
    print("\n".join(libraries_that_need_installed))
    print()
    print()

    sys.exit()

# This sees what libraries are or aren't installed
try:
    import pyautogui as pygui
except:
    pygui_error = True
# ------------------------This will probably be removed later-------------------
try:
    import cv2
except:
    cv2_error = True

try:
    import pytesseract
except:
    pytesseract_error = True

# ------------------------------------------------------------------------------

# This checks the platform of the host to send the right command to clear the termianl
if platform.system() == "Windows":
    os.system('cls')
elif platform.system() == "Linux":
    os.system('clear')

# This checks if the required libraries are installed
if pygui_error == True:
    library_install_check()
elif cv2_error == True:
    library_install_check()
elif pytesseract_error == True:
    library_install_check()

# This imports functions from external scripts
sys.path.insert(1, cd+'/_external_functions')

from screenshot_verify import screenshot_verify

from screenshot_functions import take_screenshot

from main_ui import main_menu

sys.path.insert(1, cd)

# This is a function that is used to take a screenshot. It is currently not in use.
def take_screenshot_func():
    dir = cd+"/_data/_screenshot"
    for f in os.listdir(dir):
        os.remove(os.path.join(dir, f))

    take_screenshot()
    return "Done!"

# Prints keyboard and screenshot warning if it's the first time running.
screenshot_verify()

# This is where the actual script starts
pygui.alert("Welcome.")

# Displays the main menu
main_menu()

# -------ANYTHING BEYOND THIS POINT IS UNFINISHED AND IS GOING TO CHANGE--------

# This is the main loop.
while True:
    main_input = pygui.confirm("Please select an option.", buttons=["Scan", "Quit"])

    if main_input == "Quit":
        sys.exit()
    elif main_input == "Scan":
        take_screenshot_func()
    else:
        pygui.alert("Please enter a valid action.")
