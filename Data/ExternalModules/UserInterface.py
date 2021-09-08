import tkinter as tk
import pyautogui as pygui

def main_menu():
    def test():
        pygui.alert("You pressed a button.")
    window = tk.Tk()

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
        activeforeground = "grey",
        font=("Arial", 50),
        width = "35",
        height = "5",
        command = test,
    )

    start_button.pack()
    main_frame.pack(padx=50, pady=50)
    background_frame.pack()

    window.mainloop()
