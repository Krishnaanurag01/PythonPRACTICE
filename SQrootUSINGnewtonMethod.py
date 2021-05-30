def SQ_root(num,tol):
    assume=num
    count=0
    while True:
        count+=1
        s_root=0.5*(assume+(num/assume))
        z=abs(s_root-assume)
        if(z<tol):
            break
        assume=s_root
    return s_root

print(SQ_root(int(input()),0.000001))