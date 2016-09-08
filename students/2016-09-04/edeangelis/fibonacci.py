# -*- coding: utf-8 -*-

def succ_fib_from_string(x):
    s = "0 1 1 2 3 5 8"
    if x < 0:
        raise ValueError("Indice negativo non funziona")
    else:
        try:
           return int(s[x*2])
        except IndexError:
           raise NotImplementedError("non implementato")
        
 
def succ_fib_from_list(x):
    l = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597]
    if x < 0:
        raise ValueError
    else:
        try:
            return l[x]
        except IndexError:
           raise NotImplementedError("non implementato")
        
   
def succ_fib_algo(x):
    if x < 0:
        raise ValueError
    elif x <= 1:
        ris = x
    else:
        ris = succ_fib_algo(x - 1) + succ_fib_algo(x - 2)
        try:
            return ris
        except IndexError:
            raise NotImplementedError("non implementato")
            
               
def succ_fib_algo_luca_bolli(x):
    fib_serie = [0,1]
    
    for f in range (1, x):
        fib_serie.append(fib_serie[-1] + fib_serie[-1])
        
    return int(fib_serie[i])
        

succ_fib = succ_fib_from_string

if __name__ == "__main__":
    ris = succ_fib(3)
    print "il risultato e': {}".format(ris)