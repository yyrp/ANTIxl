#!/bin/bash
echo "Installing libraries..."

# Installs pip3 if it hasn't already been installed
sudo apt install python3-pip

TK_ERROR=1
PYGUI_ERROR=1
CV2_ERROR=1
PYTESSERACT_ERROR=1

# Starts installing required libraries
sudo apt install python-tk || TK_ERROR=0
python3 -m pip install pyautogui || PYGUI_ERROR=0
python3 -m pip install opencv-python || CV2_ERROR=0
python3 -m pip install pytesseract || PYTESSERACT_ERROR=0

echo ""
echo "Done!"
echo ""
echo""

sudo apt update && sudo apt upgrade

echo ""
echo ""
echo ""

ALL_PACKAGES_INSTALLED=0
if [ $TK_ERROR == 0 ]
then
  echo "Sorry. Something went wrong. You will have to install the library 'tkinter' manually."
  ALL_PACKAGES_INSTALLED=1
fi
if [ $PYGUI_ERROR == 0 ]
then
  echo "Sorry. Something went wrong. You will have to install the library 'pyautogui' manually."
  ALL_PACKAGES_INSTALLED=1
fi
if [ $CV2_ERROR == 0 ]
then
  echo "Sorry. Something went wrong. You will have to install the library 'opencv-python' manually."
  ALL_PACKAGES_INSTALLED=1
fi
if [ $PYTESSERACT_ERROR == 0 ]
then
  echo "Sorry. Something went wrong. You will have to install the library 'pytesseract' manually."
  ALL_PACKAGES_INSTALLED=1
fi

if [ $ALL_PACKAGES_INSTALLED == 0 ]
then
  echo "All required libraries were sucessfully installed!"
  echo "0" > all_packages_installed.json
fi

exit
