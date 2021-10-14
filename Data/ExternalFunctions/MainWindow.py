#!/usr/bin/python3

import tkinter as tk
from tkinter import *
import pyautogui as pygui
import sys
import os

def main_window():
    while True:
        window = tk.Tk()

        title_label = tk.Label(
            text = "Select Lesson",
            font = ("Arial", 75)
        )

        title_label.pack()
