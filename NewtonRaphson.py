import math as m
def ombnrm(fun,dfun,ddfun,x1,acc,maxitr):
    while abs(fun(x1)*ddfun(x1)/(dfun(x1))**2) > 1:
        print("WRONG INITIAL GUESS")
        x1 = float(input("Enter the New Value of x1:"))
    for itr in range (maxitr):
        x0 = x1 - fun(x1)/dfun(x1)
        if abs(x1-x0) < acc:
            break
            x1 = x0
    print("The root is: ", x0)