from Parser import Parser
import numpy as np
import sys
import argparse
from utils

funcname = sys.argv[1]
args = sys.argv[2:]

if(funcname == "getsize"):
    imgPath = args[2]
    parser = Parser()
    parser.fit(imagePath)
    parser.getpenumbra()
    parser.getumbra()

elif(funcname == "find"):
    obj = args[2]

    
else:
    raise Exception("Function not available.")

