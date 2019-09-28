from Parser import Parser
from finder import finder 
import numpy as np
import sys
import argparse

funcname = sys.argv[1]
args = sys.argv[2:]

if(funcname == "getsize"):
    imgPath = args[2]
    parser = Parser()
    parser.fit(imgPath)
    parser.getpenumbra()
    parser.getumbra()

elif(funcname == "find"):
    obj = args[2]
    objt = finder()
    obj.fit(obj)
    obj.liveplot()
    
else:
    raise Exception("Function not available.")

