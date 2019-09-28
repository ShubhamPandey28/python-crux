import numpy as np
from math import sqrt

def solvequadratic(a,b,c):
    d = b**2 - 4*a*c
    return (-b+sqrt(d))/2*a

