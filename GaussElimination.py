import numpy as np
def ombgem(a,d):
    a = np.array(a, dtype = float)
    d = np.array(d, dtype = float)
    n = len(d)
    for i in range (0, n, 1):
        for k in range (i+1, n, 1):
            f = a[k,i] / a[i,i]
            for j in range (0, n):
                a[k,j] = a[k,j] - f * a[i,j]
                d[k] = d[k] - f * d[i]
    print(a)
    print(d)
    x = np.zeros(n)
    print(x)
    for i in range (n-1, -1, -1):
        temp = 0
        for j in range (i+1, n, 1):
            temp = temp + a[i,j] * x[j]
        x[i] = (d[i] - temp) / a[i,i]
    print("Answer = ", x)