#!/bin/bash

# Installs pip3 if it hasn't already been installed
sudo apt install python3-pip

# Starts installing required libraries
sudo apt install python-tk || echo "Sorry. Something went wrong. You will have to install the library 'tkinter' manually."
python3 -m pip install pyautogui || echo "Sorry. Something went wrong. You will have to install the library 'pyautogui' manually."
python3 -m pip install opencv-python || echo "Sorry. Something went wrong. You will have to install the library 'opencv-python' manually."
python3 -m pip install pytesseract || echo "Sorry. Something went wrong. You will have to install the library 'pytesseract' manually."
echo "Done!"
quit
