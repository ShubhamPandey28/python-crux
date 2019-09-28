import os
import sys

with open("requirements.txt","r") as f:
    modules = f.readlines()
    for module in modules:
        try:
            os.system("pip3 install "+module)
        except:
            c = input("pip3 is not installed. Would you like to install it?(Y/n): ")
            if(c.lower() == "y"):
                os.system("sudo apt-get install python3-pip")
            else:
                raise Exception("Unable to install "+module)

os.system("sudo mv src /bin/")

with open("~/.bashrc","a") as f:
    t = "alias crux=/bin/src/main.py"
    f.write(t)

