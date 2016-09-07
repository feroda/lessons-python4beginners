# -*- coding: utf-8 -*-

fib_d = {
    0:0,
    1:1
}

def fib(x):

    """
    Calcola fibonacci con cache sul dizionario.
    
    Se trova il valore nel dizionario lo restituisce,
    altrimenti lo calcola, lo mette nel dizionario e lo restituisce.
    """
    if x in fib_d:
        return fib_d[x]
        
    fib_pre = fib(x-1)
    fib_d[x-1] = fib_pre
    
    fib_prepre = fib(x-2)
    fib_d[x-2] = fib_prepre
    
    return fib_pre + fib_prepre
    

if __name__ == "__main__":
    choice = raw_input("Per quale input vuoi sapere il corrispondente fibonacci?")
    print(fib(int(choice)))
    
    