#!/usr/bin/python3

import time
import os
import sys
from platform import platform

cd = os.getcwd()

if "IXL-Bot" not in cd:
    print("Please move to the parent directory 'IXL-Bot'.")
    time.sleep(3)
    sys.exit()
else:
    if platform == "Windows":
        os.system("cls")
    elif platform == "Linux":
        os.system("clear")

while True:
    input1 = input("Is the current working directory set to 'IXL-Bot'? (y/n): ")
    print()

    if input1.lower() == "y":
        break
    elif input1.lower() == "n":
        print()
        print("Please change the current working directory to 'IXL-Bot'")
        print()
        time.sleep(3)
        sys.exit()
    elif input1.lower() == "yes":
        break
    elif input1.lower() == "no":
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

    try:
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
            print("Please type 'y' or 'n'.")
            print()
    except:
        print("Please type 'y' or 'n'.")

if manual_set == 1:
    while True:
        print()
        print("Enter the file path to 'IXL_Bot'.")
        manual_set_input = input("(Type here:) ")

        print()
        print()
        print()
        print(manual_set_input)
        print()
        print("Are you sure this is the correct file path?")
        confirm_input = input("(y/n): ")
        try:
            if confirm_input.lower() == "y":
                break
            elif confirm_input.lower() == "yes":
                break
            elif confirm_input.lower() == "n":
                pass
            elif confirm_input.lower() == "no":
                pass
            else:
                print("Please type 'y' or 'n'.")
                print()
        except:
            print("Please type 'y' or 'n'.")

    file_path = manual_set_input
else:
    file_path = cd

print()
print("The file path to 'IXL-Bot' is '"+file_path+"'")

# Writes the file path to all the file path files
d = open(cd+r"/_data/data_file_path.txt", 'w')
e = open(cd+r"/_external_functions/ef_file_path.txt", 'w')
d.write(cd)
e.write(cd)
d.close()
e.close()


time.sleep(3)
sys.exit()
