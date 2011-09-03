"""
Math operations functions
"""
import math

def addFrac(frac1, frac2):
    """
    Add fraction 1 and fraction 2
    """
#TODO: Support for multiple fractions
# x/r + z/w = a+b/c
    e=str(frac1)
    y=str(frac2)
    x=e[0 : frac1.index('/')]
    w=y[(y.index('/')+1) : len(y)]
    z=y[0 : frac2.index('/')]
    r=e[(e.index('/')+1) : len(e)]
    a=int(x) * int(w)
    b=int(z) * int(r)
    c=int(r) * int(w)
    if (a+b)%c==0:
        result=(a+b)/c
    else:
        result=str(a+b)+'/'+str(c)
    return result
