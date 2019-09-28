import numpy as np
from math import sqrt

def solvequadratic(a,b,c):
    d = b**2 - 4*a*c
    return (-b+sqrt(d))/2*a # only the positve one is neccessary for after processes

# rs/ro = A which is calcualted by below
# source radius : rs
# object radius : ro

def getsizes(x,d,ru,rp):
    b = 4 -(2*d*x)/rp**2 + (2*d*x)/ru**2 + 2*(x**2)/(rp**2) + 2*(x**2)/(ru**2)
    a = x**2/(rp**2) - (x**2/ru**2)
    c = (d**2)*(1/rp**2 - 1/ru**2)  - 2*d*x(1/rp**2 + 1/ru**2)   + x**2/rp**2 - x**2/ru**2
    A = solvequadratic(a,b,c)

    ro = d/sqrt((A-1)**2 + d**2/ru**2 + ((A-1)**2)*(x**2)/ru**2 -2*d*x*(A-1)/ru**2)
    rs = ro*A

    return rs, ro



