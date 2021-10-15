#!/usr/bin/python3

import os
import sys

cd = os.getcwd()

if "IXL-Bot" not in cd:
    print("Please move to the parent directory 'IXL-Bot'.")
    sys.exit()
else:
    pass

while True:
    input1 = input("Is the current working directory set to 'IXL-Bot'? (y/n): ")
    print()

    if input1.lower() == "y":
        break
    elif input1.lower() == "n":
        print()
        print("Please change the current working directory to 'IXL-Bot'")
        print()
        sys.exit()
    elif input1.lower() == "yes":
        break
    elif input1.lower() == "no":
        print()
        print("Please change the current working directory to 'IXL-Bot'")
        print()
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
        print("Enter the file path to 'IXL_Bot'.")
        manual_set_input = input("(Type here:) ")

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

print("The file path to 'IXL-Bot' is '"+file_path+"'")
