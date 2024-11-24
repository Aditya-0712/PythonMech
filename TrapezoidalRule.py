import math as m
def pra_tr(fun,x0,xn,n):
    h = (xn - x0) / n
    y0 = fun(x0)
    yn = fun(xn)
    yr = 0
    for i in range (1,n):
        yr = yr + fun(x0 + i * h)
    A = 1/2 * h * (y0 + yn + 2 * yr)
    print("Area = ", A)