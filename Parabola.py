import numpy as np
def pra_plcf(x,y):
    x = x.astype(float)
    y = y.astype(float)
    a = np.array([[len(x),sum(x),sum(x*x)],
    [sum(x),sum(x*x),sum(x*x*x)],
    [sum(x*x),sum(x*x*x),sum(x*x*x*x)]])
    d = np.array([[sum(y)],
    [sum(x*y)],
    [sum(x*x*y)]])
    b = np.linalg.solve(a,d)
    print("y = %.4f + (%.4f) * x + (%.4f) * x ^ 2"%(b[0],b[1],b[2]))