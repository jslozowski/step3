

from math import floor


def potega_dodatnia(a,b):
    c = a
    b = floor(b)
    if b == 0:
        return 1
    elif b<0:
        return ("b ma byc dodatnie")
    else:
        for i in range(1,b):
            a = a*c
        return (a)

def dodawanie_dwoch(a,b):
    return a+b
