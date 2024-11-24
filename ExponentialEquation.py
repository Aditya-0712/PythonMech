import numpy as np
def pra_cfee(x,y):
    y = np.array(y,dtype=float)
    x = np.array(x,dtype=float)
    Y = np.log(y)
    A = np.array([[len(x),sum(x)],[sum(x),sum(x*x)]])
    C = np.array([[sum(Y)],[sum(x*Y)]])
    B = np.linalg.solve(A,C)
    a0 = B[0]
    a1 = B[1]
    a = np.exp(a0)
    b = a1
    print("y = %4f * e ^ (%4f * x)"%(a,b))