import os
import sys

with open("requirements.txt","r") as f:
    modules = f.readlines()
    for module in modules:
        try:
            os.system("pip3 install "+module)
        else:
            raise Exception("module not found.")

os.system("sudo mv src /bin/")

with open("~/.bashrc","a") as f:
    t = "alias crux=/bin/src/main.py"
    f.write(t)

