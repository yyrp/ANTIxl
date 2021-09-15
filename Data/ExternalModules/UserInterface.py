#!/usr/bin/python3

import tkinter as tk
import pyautogui as pygui
import sys
import os

def main_menu():
    cd = os.getcwd()

    def test():
        print("Button pressed.")
        pygui.alert("You pressed a button.")

    window = tk.Tk()
    while True:
        window = tk.Tk()

        def quit_func():
            sys.exit()

        def info_func():
            pygui.alert("Made by Lucas Maritato\nOS: Windows 10, Linux\n(Sadly, it can't run on Chromebook.)")

        background_frame = tk.LabelFrame(
            background = "white",
        )

        main_frame = tk.LabelFrame(
            background_frame,
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
            command = quit_func,
        )

        info_button = tk.Button(
            background_frame,
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
            background_frame,
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
        background_frame.pack()

        window.mainloop()
