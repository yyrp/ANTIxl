@echo off
echo Installing libraries...

SET TK_ERROR=1
SET PYGUI_ERROR=1
SET CV2_ERROR=1
SET PYTESSERACT_ERROR=1

python3 -m pip install pyautogui || SET PYGUI_ERROR=0
python3 -m pip install opencv-python || SET CV2_ERROR=0
python3 -m pip install pytesseract || SET PYTESSERACT_ERROR=0

echo.
echo Done!
echo.
echo.

SET ALL_PACKAGES_INSTALLED=0
if %TK_ERROR%==0 (
  echo Sorry. Something went wrong. You will have to install the library 'tkinter' manually.
  SET ALL_PACKAGES_INSTALLED=1
)

if %PYGUI_ERROR%==0 (
  echo Sorry. Something went wrong. You will have to install the library 'pyautogui' manually.
  SET ALL_PACKAGES_INSTALLED=1
)

if %CV2_ERROR%==0 (
  echo Sorry. Something went wrong. You will have to install the library 'opencv-python' manually.
  SET ALL_PACKAGES_INSTALLED=1
)

if %PYTESSERACT_ERROR%==0 (
  echo Sorry. Something went wrong. You will have to install the library 'pytesseract' manually.
  SET ALL_PACKAGES_INSTALLED=1
)


if %ALL_PACKAGES_INSTALLED%==0 (
  echo All required libraries were sucessfully installed!
  echo 1 > all_packages_installed.json
)

echo.
PAUSE
echo.
exit
