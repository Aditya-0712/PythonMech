import numpy as np
import math as m
def pra_ndfi (x,y,xr):
    x = np.array(x,dtype=float)
    y = np.array(y,dtype=float)
    n = len(x)
    delta = np.zeros((n-1,n-1))
    for j in range (n-1):
        for i in range ((n-1)-j):
            if j == 0:
                delta [i,j] = y[i+1] - y[i]
        else:
            delta[i,j] = delta[i+1,j-1] - delta[i,j-1]
    h = x[1] - x[0]
    u = (xr - x[0])/h
    term = 0
    mult = 1
    for j in range (n-1):
        mult = mult * (u-j)
        term = term + delta[0,j] / m.factorial(j+1) * mult
    yr = y[0] + term
    print("Answer =",yr)