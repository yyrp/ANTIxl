#!/usr/bin/python3

# Importing modules
print("Importing modules...")

import sys
import os
import platform

# These variables are used to see what libraries are or aren't installed
pygui_error = False
cv2_error = True
pytesseract_error = False

# This is the function checks what libraries need to be installed
def library_install_check():
    libraries_that_need_installed = []

    if platform.system() == "Windows":
        # This adds color to the text if the os is Windows becuase I can't get it to work on Linux
        if pygui_error == True:
            libraries_that_need_installed.append("  - \u001b[32mpyautogui\u001b[37m (pip install pyautogui)")
        if cv2_error == True:
            libraries_that_need_installed.append("  - \u001b[32mcv2\u001b[37m (pip install opencv-python)")
            print("food")
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
    pygui_error = True

# ------------------------------------------------------------------------------
if platform.system() == "Windows":
    os.system('cls')
elif platform.system() == "Linux":
    os.system('clear')

library_install_check()

cd = os.getcwd()
sys.path.insert(1, cd+'/Data/ExternalModules')

from ScreenshotVerify import screenshot_verify

from ScreenshotModules import take_screenshot

from MainMenu import main_menu

sys.path.insert(1, cd)

print("Done!")

print()
print()
print()

def take_screenshot_func():
    dir = cd+"/Data/Screenshot"
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

# This is the main loop. It will later be removed.
while True:
    main_input = pygui.confirm("...", buttons=["Scan", "Quit"])

    if main_input == "Quit":
        sys.exit()
    elif main_input == "Scan":
        take_screenshot_func()
    else:
        pygui.alert("Please enter a valid action.")
