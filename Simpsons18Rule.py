import math as m
def pra_s13(fun,x0,xn,n):
    h = (xn - x0) / n
    y0 = fun(x0)
    yn = fun(xn)
    yodd = 0
    yeven = 0
    for i in range (1,n,2):
        yodd = yodd + fun(x0 + i * h)
    for j in range (2,n-1,2):
        yeven = yeven + fun(x0 + j * h)
        A = 1/3 * h * (y0 + yn + 4 * yodd + 2 * yeven)
    print("Area = ", A)