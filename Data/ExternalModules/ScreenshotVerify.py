def screenshot_verify():
    import os

    cd = os.getcwd()
    f = open(cd+"/Data/PermissionVerification.txt", 'r')

    info = f.read()
    if info == "1":
        f.close()
        pass
    else:
        print("WARNING: You are giving this program permission to acess your keyboard and take screenshots. Screenshots will later be deleted and are not saved.")
        f.close()
        f = open(cd+"/Data/PermissionVerification.txt", 'w')
        f.write("1")
        f.close()
