import pyautogui as pygui
import os

def take_screenshot():
    ss = pygui.screenshot()
    return ss

def save_screenshot(ss):
    cd = os.getcwd()
    ss.save(cd+"/Data/Screenshots")
