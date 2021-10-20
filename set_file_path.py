#!/usr/bin/python3

import time
import os
import sys
import platform

# Gets the current working directory
cd = os.getcwd()

# Checks if the current working directory is set to 'IXL-Bot' or has 'IXL-Bot' in the path
if "IXL-Bot" not in cd:
    # Exits the program if the current working directory is not set to 'IXL-Bot'
    print("Please move to the parent directory 'IXL-Bot'.")
    time.sleep(3)
    sys.exit()
else:
    # Clears the terminal
    if platform.system() == "Windows":
        os.system("cls")
    elif platform.system() == "Linux":
        os.system("clear")

# Checks if the user has the current working directory set to 'IXL-Bot'
while True:
    input1 = input("Is the current working directory set to 'IXL-Bot'? (y/n): ")
    print()

    # Processes input
    if input1.lower() == "y":
        # Breaks the loop
        break
    elif input1.lower() == "n":
        # Exits the program if the current working directory is not set to 'IXL-Bot'
        print()
        print("Please change the current working directory to 'IXL-Bot'")
        print()
        time.sleep(3)
        sys.exit()
    elif input1.lower() == "yes":
        # Breaks the loop
        break
    elif input1.lower() == "no":
        # Exits the program if the current working directory is not set to 'IXL-Bot'
        print()
        print("Please change the current working directory to 'IXL-Bot'")
        print()
        time.sleep(3)
        sys.exit()
    else:
        print("Please type 'y' or 'n'.")
        print()

while True:
    input2 = input("Would you like to manually set the file path? (y/n): ")

    # Processes input
    try:
        # Checks if the user wants to manually set the 'IXL-Bot' path or to have it automatically set.
        if input2.lower() == "y":
            manual_set = 1
            break
        elif input2.lower() == "n":
            manual_set = 0
            break
        elif input2.lower() == "yes":
            manual_set = 1
            break
        elif input2.lower() == "no":
            manual_set = 0
            break
        else:
            # Resets the loop if the user didn't type 'y' or 'n'
            print("Please type 'y' or 'n'.")
            print()
    except:
        # Resets the loop if there was an error
        print("Please type 'y' or 'n'.")

# 'IXL-Bot' path manual set
if manual_set == 1:
    # This runs if the user wanted to manually set the 'IXL-Bot' file path
    while True:
        # Gets input
        print()
        print("Enter the file path to 'IXL_Bot'.")
        manual_set_input = input("(Type here:) ")

        # Confirms input
        print()
        print()
        print()
        print(manual_set_input)
        print()
        print("Are you sure this is the correct file path?")
        confirm_input = input("(y/n): ")

        # Processes input
        try:
            if confirm_input.lower() == "y":
                # Breaks the loop
                break
            elif confirm_input.lower() == "yes":
                # Breaks the loop
                break
            elif confirm_input.lower() == "n":
                # Runs the loop again
                pass
            elif confirm_input.lower() == "no":
                # Runs the loop again
                pass
            else:
                # Runs the loop again
                print("Please type 'y' or 'n'.")
                print()
        except:
            # Runs the loop again if there was an error
            print("Please type 'y' or 'n'.")

    # Sets the file path to the user's input
    file_path = manual_set_input
else:
    # Sets the file path to the current working directory
    file_path = cd

# Prints the 'IXL-Bot' file path
print()
print("The file path to 'IXL-Bot' is '"+file_path+"'")

# Writes the file path to all the file path files
d = open(cd+r"/_data/data_file_path.txt", 'w')
e = open(cd+r"/_external_functions/ef_file_path.txt", 'w')
d.write(file_path)
e.write(file_path)
d.close()
e.close()

# Ends the script
time.sleep(3)
sys.exit()
