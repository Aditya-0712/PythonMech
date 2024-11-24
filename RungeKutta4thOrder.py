import math as m
def pra_rk4(fun,x0,y0,xn,n):
    h = (xn - x0) / n
    for i in range (1,n+1):
        k1 = h * fun(x0,y0)
        k2 = h * fun(x0+h/2,y0+k1/2)
        k3 = h * fun(x0+h/2,y0+k2/2)
        k4 = h * fun(x0+h,y0+k3)
        ynew = y0 + 1/6 * (k1+2*k2+2*k3+k4)
        x0 = x0 + h
        y0 = ynew
    print("xn = ", xn," ; yn = ", ynew)