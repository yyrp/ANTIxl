#!/usr/bin/python3

# This script sees if color shows up in the terminal
import os

# Main function
def color_verify():
    f = open("ef_file_path.txt", 'r')
    cd = f.read()
    f.close()

    # Checks to see if the script has been run before
    f = open(cd+r"/_data/run.txt", 'r')
    info = f.read()
    f.close()

    if info == "1":
        # Moves along with the script if it has been run before
        pass
    # This runs if the script hasn't been run before
    else:
        # Gets input
        print("Is the following text green?")
        print("\u001b[32mThis should be green.\u001b[0m")
        main_input = input("y/n: ")

        while True:
            # Processes input
            try:
                if main_input.lower() == "y":
                    print("\u001b[45;1mColor support enabled!\u001b[0m")
                    food = 1
                    break
                elif main_input.lower() == "n":
                    print("Color support not enabled.")
                    food = 0
                    break
                elif main_input.lower() == "yes":
                    print("\u001b[45;1mColor support enabled!\u001b[0m")
                    food = 1
                    break
                elif main_input.lower() == "no":
                    print("Color support not enabled.")
                    food = 0
                    break
                else:
                    # Restarts the loop if the user didn't answer 'y' or 'n'
                    print("Please type 'y' or 'n'.")
                    print()
            except:
                # Restarts the loop if there was an error
                print("Please type 'y' or 'n'.")

        # Tells the program if color shows up in the terminal
        f = open(cd+r"/_data/color_verification.txt")
        if food == 1:
            f.write("1")
        else:
            f.write("0")
        f.close()
