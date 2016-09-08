# -*- coding: utf-8 -*-


def dofib(counter):
    if counter < 0 :
        raise ValueError("Intero negativo non consentito")
    elif counter <= 1 :    
        return counter
    else :
        return dofib(counter - 1) + dofib(counter - 2)