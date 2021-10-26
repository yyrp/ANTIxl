#!/usr/bin/python3
# This script prints a warning for the user that says that this program takes and saves screenshots temporarily
import json
import os
import sys

# Main function
def screenshot_verify():
    # This gets the current working directory from file path files
    file_path = __file__
    file_directory = os.path.dirname(__file__)
    cd = json.load(file_directory+"/ef_file_path.json")

    # Sees if the warning has been sent before
    f = open(cd+"/_data/run.txt", 'r')
    info = f.read()

    # If the warning has been sent, it doesn't send it again
    if info == "1":
        # Closes the file
        f.close()
        pass
    # If it hasn't been sent, it prints it into the terminal
    else:
        print("WARNING: You are giving this program permission to acess your keyboard and take screenshots. Screenshots will later be deleted and are not saved.")
        # Closes the file
        f.close()
        # Tells the program the warning has been sent
        f = open(cd+"/_data/PermissionVerification.txt", 'w')
        f.write("1")
        f.close()
