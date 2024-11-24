import numpy as np
a = np.array([[4,1,2],[1,3,1],[1,2,5]])
d = np.array([[16],[10],[12]])
a = np.array(a,dtype=float)
d = np.array(d,dtype=float)
n = len(d)
x = np.zeros(n)
maxitr = 10
for itr in range (maxitr):
    for i in range(0,n,1):
        temp = 0
    for j in range(0,n,1):
        if i!=j:
            temp = temp + a[i,j]*x[j]
    x[i] = (d[i] - temp)/a[i,i]
print(x)