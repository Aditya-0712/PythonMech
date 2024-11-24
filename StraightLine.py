import numpy as np
def pra_slcf(x,y):
    x = x.astype(float)
    y = y.astype(float)
    a = np.array([[len(x),sum(x)],[sum(x),sum(x*x)]])
    d = np.array([[sum(y)],[sum(x*y)]])
    b= np.linalg.solve(a,d)
    print("Output")
    print("y = %.4f + (%.4f) * x" %(b[0],b[1]))