import math as m
def ombbsm(fun,x1,x2,acc,maxitr):
    while fun(x1)*fun(x2) > 0:
        print("WRONG INTIAL GUESS")
        x1 = float(input("Enter the New Value of x1: "))
        x2 = float(input("Enter the New Value of x2: "))
    for itr in range(maxitr):
        x0 = (x1+x2)/2
        if fun(x0)*fun(x1) < 0:
            x1 =x1
            x2 =x0
        elif fun(x0)*fun(x1) > 0:
            x1 = x0
            x2 =x2
    print("The root of given function =",x0)

