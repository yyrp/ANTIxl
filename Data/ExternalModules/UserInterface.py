#!/usr/bin/python3

from PIL import Image, ImageTk
import tkinter as tk
from tkinter import *
import pyautogui as pygui
import sys
import os

def main_menu():
    cd = os.getcwd()
    window = tk.Tk()

    # side_image_1 = PIL.Image.open(cd+r"/Data/ExternalModules/Other/Side_Logo.png")
    # side_image_var = ImageTk.PhotoImage(side_image_1)
    side_image_var = ImageTk.PhotoImage(Image.open(cd+r"/Data/ExternalModules/Other/Side_Logo.png"))
    while True:
        window = tk.Tk()

        def quit_func():
            sys.exit()

        def info_func():
            pygui.alert("Made by Lucas Maritato\nOS: Windows 10, Linux\n(Sadly, it can't run on Chromebook.)")

        background_frame = tk.LabelFrame(
            background = "white",
        )

        background_frame_1 = tk.LabelFrame(
            background = "white",
        )

        main_frame = tk.LabelFrame(
            background_frame_1,
            background = "white",
        )

        start_button = tk.Button(
            main_frame,
            text = "Start",
            foreground = "white",
            background = "#00FF06",
            activebackground = "green",
            activeforeground = "white",
            font=("Arial", 50),
            width = "12",
            height = "2",
            command = "break",
        )

        side_logo = tk.Label(
            background_frame,
            image = side_image_var,
        )

        info_button = tk.Button(
            background_frame_1,
            text = "Info",
            foreground = "white",
            background = "yellow",
            activebackground = "grey",
            activeforeground = "white",
            font=("Arial", 25),
            width = "11",
            height = "1",
            command = info_func,
        )

        quit_button = tk.Button(
            background_frame_1,
            text = "Exit",
            foreground = "white",
            background = "red",
            activebackground = "grey",
            activeforeground = "white",
            font=("Arial", 25),
            width = "11",
            height = "1",
            command = quit_func,
        )

        start_button.pack()
        main_frame.pack(padx=0, pady=0)
        info_button.pack(side=tk.LEFT)
        quit_button.pack(side=tk.RIGHT)
        side_logo.pack(side=tk.RIGHT)
        background_frame_1.pack(side=tk.LEFT)
        background_frame.pack()

        window.mainloop()
