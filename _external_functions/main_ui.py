#!/usr/bin/python3
from PIL import Image, ImageTk
import PIL.Image
import sys
import os
import json

# Checks for libraries that might not be installed
try:
    try:
        import tkinter as tk
        from tkinter import *
    except:
        import Tkinter as tk
        from Tkinter import *
except:
    print("You need to install the tkinter module (sudo apt-get install python3-tk python3-dev).")
    sys.exit()

try:
    import pyautogui as pygui
except:
    print("You need to install the pyautogui module (pip install pyautogui).")
    sys.exit()

# Main menu
def main_menu():
    # This gets the current working directory from file path files
    file_path = __file__[:-1]
    file_directory = os.path.dirname(__file__)
    file = open(file_directory+r"/ef_file_path.json")
    cd = json.load(file)
    file.close()


    # Functions that run when you click a button
    def quit_func():
        sys.exit()

    def info_func():
        pygui.alert("Made by me.\nOS: Windows 10, Linux\n(Sadly, it can't run on Chromebook.)")

    def on_closing():
        sys.exit()

    window = tk.Tk()
    window.title("Main Menu | IXL-Bot")

    # Creates a photoimage object of the image in the path
    # image1 = open(cd+r"/_external_functions/_other/update_info_001.png", "rb")
    # image2 = image1.resize((500, 375),Image.ANTIALIAS)
    # side_image_var = PhotoImage(file=cd+r"/_external_functions/_other/update_info_001.png")

    # Read the Image
    image = Image.open("Image File Path")

    # Resize the image using resize() method
    resize_image = image.resize((width, height))

    img = ImageTk.PhotoImage(resize_image)

    # Main elements
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
        command = window.destroy,
    )

    resize_image = side_image_var.resize((500, 375))

    side_logo = tk.Label(
        background_frame,
        resize_image = side_image_var,
    )

    info_button = tk.Button(
        background_frame_1,
        text = "Info",
        foreground = "white",
        background = "#F1C40F",
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

    # Packs all the elements
    start_button.pack()
    main_frame.pack(padx=0, pady=0)
    info_button.pack(side=tk.LEFT)
    quit_button.pack(side=tk.RIGHT)
    side_logo.pack(side=tk.RIGHT)
    background_frame_1.pack(side=tk.LEFT)
    background_frame.pack()

    window.protocol("WM_DELETE_WINDOW", on_closing)

    window.mainloop()

# Main window
def main_window():
    while True:
        window = tk.Tk()

        title_label = tk.Label(
            text = "Select Lesson",
            font = ("Arial", 75)
        )

        title_label.pack()
