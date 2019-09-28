from Parser import Parser
from finder import finder 
import numpy as np
import sys
import argparse
from matplotlib.pyplot as plt
from astropy.visualization import astropy_mpl_style
plt.style.use(astropy_mpl_style)

funcname = sys.argv[1]
args = sys.argv[2:]

if(funcname == "getsize"):
    imgPath = args[2]
    parser = Parser()
    parser.fit(imgPath)
    parser.getpenumbra()
    parser.getumbra()
    print("radius of umbra: ",parser.ru)
    print("radius of penumbra: ",parser.rp)


elif(funcname == "find"):
    obj = args[2]
    objt = finder()
    obj.fit(obj)
    obj.liveplot()
    
else:
    raise Exception("Function not available.")

