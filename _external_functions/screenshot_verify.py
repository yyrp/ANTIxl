#!/usr/bin/python3
# This script prints a warning for the user that says that this program takes and saves screenshots temporarily
import json
import os
import sys
import time

# Main function
def screenshot_verify():
    # This gets the current working directory from file path files
    file_path = __file__[:-1]
    file_directory = os.path.dirname(__file__)
    with open(file_directory+r"/ef_file_path.json") as file:
        cd = json.load(file)

    # This gets info from run.json
    file = open(cd+r"/_data/run.json")
    info = json.load(file)
    file.close()

    if info == "1":
        # If the warning has been sent, it doesn't send it again
        pass
    else:
        # If the warning hasn't been sent, it prints it into the terminal
        print("WARNING: You are giving this program permission to acess your keyboard and take screenshots. Screenshots will later be deleted and are not saved.")
        # Tells the program the warning has been sent
        run_info = "1"
        with open(cd+r"/_data/run.json", 'w') as dump_file:
            json.dump(run_info, dump_file)
