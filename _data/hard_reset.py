#!/usr/bin/python3

import os
import sys
import time
import json
import platform

while True:
    print("Are you sure you want to factory-reset the program?")
    input1 = input("(y/n): ")
    # Processes input
    if input1.lower() == "y":
        # Breaks the loop
        break
    elif input1.lower() == "n":
        sys.exit()
    elif input1.lower() == "yes":
        # Breaks the loop
        break
    elif input1.lower() == "no":
        sys.exit()
    else:
        print("Please type 'y' or 'n'.")
        print()

if platform.system() == "Linux":
    os.system('clear')
elif platform.system() == "Windows":
    os.system('cls')
else:
    print("Apparently, the operating system you are using is not supported. Please use Windows or Linux.")
    sys.exit()

# This gets the current working directory from file path files
file_path = __file__[:-1]
file_directory = os.path.dirname(__file__)
file = open(file_directory+r"/data_file_path.json")
cd = json.load(file)
file.close()

reset_data = 0

print("File path is ''"+cd+"'.")
time.sleep(0.5)

print("Reseting files...")

print("Reseting 'data_file_path.json'")
with open(cd+r"/_data/data_file_path.json", 'w') as dump_file:
    json.dump(reset_data, dump_file)
time.sleep(0.1)

print("Reseting 'ef_file_path.json'")
with open(cd+r"/_external_functions/ef_file_path.json", 'w') as dump_file:
    json.dump(reset_data, dump_file)
time.sleep(0.1)

print("Reseting 'path.json'")
with open(cd+r"/path.json", 'w') as dump_file:
    json.dump(reset_data, dump_file)
time.sleep(0.1)

print("Reseting 'run.json'")
with open(cd+r"/_data/run.json", 'w') as dump_file:
    json.dump(reset_data, dump_file)
time.sleep(0.1)

print("Done!")
time.sleep(3)

sys.exit()
