import math as m
def pra_s38(fun,x0,xn,n):
    h = (xn - x0) / n
    y0 = fun(x0)
    yn = fun(xn)
    ym3 = 0
    yr = 0
    for i in range (3,n-2,3):
        ym3 = ym3 + fun(x0 + i * h)
    for j in range (1,n,1):
        yr = yr + fun(x0 + j * h)
    yr = yr - ym3
    A = 3/8 * h * (y0 + yn + 3 * yr + 2 * ym3)
    print("Area = ", A)