from Parser import Parser
from finder import finder
from solver import * 
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
    dist_OP = args[3] # distance between object and observing plane of shadow image
    dist_SO = args[4] # distance between source and object
    
    parser = Parser()
    parser.fit(imgPath)
    parser.getpenumbra()
    parser.getumbra()
    print("radius of umbra: ",parser.ru)
    print("radius of penumbra: ",parser.rp)

    rs, ro = getsizes(dist_OP,dist_SO,parser.ru,parser.rp)

    print("radius of Light Source: "+str(round(rs,2))
    print("radius of Object: "+str(round(ro,2))



elif(funcname == "find"):
    obj = args[2]
    objt = finder()
    obj.fit(obj)
    obj.liveplot()
    
else:
    raise Exception("Function not available.")

