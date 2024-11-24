import math as m
def pra_rk2(fun,x0,y0,xn,n):
    h = (xn - x0) / n
    for i in range (1,n+1):
        k1 = h * fun(x0,y0)
        k2 = h * fun(x0+h,y0+k1)
        ynew = y0 + 1/2 * (k1+k2)
        x0 = x0 + h
        y0 = ynew
    print("xn = ", xn," ; yn = ", ynew)