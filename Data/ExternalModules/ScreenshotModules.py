import pyautogui as pygui
import os

def take_screenshot():
    ss = pygui.screenshot()
    return ss

def save_screenshot(ss):
    cd = os.path.realpath('IXL-Bot')
    ss.save(cd+"/Data/Screenshots")
