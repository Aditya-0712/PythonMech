import numpy as np
def pra_li(x,y,xr):
    x = x.astype(float)
    y = y.astype(float)
    n = len(x)
    yr = 0
    for i in range(n):
        L = 1
        for j in range(n):
            if i !=j:
                L = L*(xr-x[j])/(x[i]-x[j])
        yr = yr + y[i] * L
    print("y at x = %.4f is equal to %.4f"%(xr,yr))