# -*- coding: utf-8 -*-

def succ_fib_from_string(x):
    s = "0 1 1 2 3 5 8"
    if x < 0:
        raise ValueError
    else:
        try:
           i = x * 2
        except TypeError:
           raise
        
        return int(s[i])
 
def succ_fib_from_list(x):
    l = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597]
    if x < 0:
        raise ValueError
    else:
        try:
           l[x]
        except TypeError:
           raise
        
        return l[x]
   
def succ_fib_algo(x):
    if x < 0:
        raise ValueError
    elif x <= 1:
        ris = x
    else:
        try:
            ris = succ_fib_algo(x - 1) + succ_fib_algo(x - 2)
        except TypeError:
           raise
        
    return ris

succ_fib = succ_fib_algo

if __name__ == "__main__":
    ris = succ_fib(3)
    print "il risultato e': {}".format(ris)