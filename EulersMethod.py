import math as m
def pra_em(fun,x0,y0,xn,n):
    h = (xn - x0) / n
    for i in range (1,n+1):
        ynew = y0 + h *fun(x0,y0)
        x0 = x0 + h
        y0 = ynew
    print("xn = ", xn," ; yn = ",ynew)