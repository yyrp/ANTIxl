#!/usr/bin/python3

# Importing modules
print("Importing modules...")

import sys
import os
import platform

# These variables are used to see what libraries are or aren't installed
cv2_error = False
pygui_error = False
pytesseract_error = False

# This is the function checks what libraries need to be installed
def library_install_check():
    libraries_that_need_installed = []

    if platform.system() == "Windows":
        # This adds color to the text if the os is Windows becuase I can't get it to work on Linux
        if cv2_error == True:
            libraries_that_need_installed.append("  - \u001b[32mcv2\u001b[37m (pip install opencv-python)")
        if pygui_error == True:
            libraries_that_need_installed.append("  - \u001b[32mpyautogui\u001b[37m (pip install pyautogui)")
        if pytesseract_error == True:
            libraries_that_need_installed.append("  - \u001b[32mpytesseract\u001b[37m (pip install pytesseract)")

        print()
        print(" \u001b[31mERROR:\u001b[37m You need to install the following libraries:")
        print(libraries_that_need_installed)
        print()
        print()
    else:
        # This is for any other operating system besides Windows
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
library_install_check()

# This gets the current working directory from file path files
f = open(os.path.join(sys.path[0], "my_file.txt"), "r")
cd = f.read()
f.close()

# This imports functions from external scripts
sys.path.insert(1, cd+'/_external_functions')

from ScreenshotVerify import screenshot_verify

from ScreenshotModules import take_screenshot

from MainMenu import main_menu

sys.path.insert(1, cd)

print("Done!")

print()
print()
print()

# This is a function that is later used to take a screenshot
def take_screenshot_func():
    dir = cd+"/_data/_screenshot"
    for f in os.listdir(dir):
        os.remove(os.path.join(dir, f))

    take_screenshot()
    return "Done!"

# Prints keyboard and screenshot warning if it's the first time running.
screenshot_verify()

#-------ANYTHING BEYOND THIS POINT IS UNFINISHED AND IS SUBJECT TO CHANGE-------

# This is where the actual script starts
pygui.alert("Welcome.")

# Displays the main menu
main_menu()

# This is the main loop.
while True:
    main_input = pygui.confirm("...", buttons=["Scan", "Quit"])

    if main_input == "Quit":
        sys.exit()
    elif main_input == "Scan":
        take_screenshot_func()
    else:
        pygui.alert("Please enter a valid action.")
