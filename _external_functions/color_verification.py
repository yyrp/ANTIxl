def color_verify():
    import os
    cd = os.getcwd()

    print("Is the following text green?")
    print("\u001b[32mThis should be green.\u001b[0m")
    main_input = input("y/n: ")

    while True:
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
                print("Please type 'y' or 'n'.")
                print()
        except:
            print("Please type 'y' or 'n'.")

    f = open(cd+r"/_data/color_verification.txt")
    if food == 1:
        f.write("1")
    else:
        f.write("0")
    f.close()
