# -*- coding: utf-8 -*-


def fib_from_string(index):
    s = "0 1 1 2 3 5 8"
    if(index < 0):
        raise ValueError ("indice negativo ({} ) non funziona".format(index))
    try:
        return int(s[index*2])
    except IndexError:
            raise NotImplementedError("Non sono stato capace da 7 in su")

l = [0, 1, 1, 2, 3, 5, 8,13,21,34,55,89,144,233,377,610,987,1597]
def fib_from_list(index):
    if(index < 0):
        raise ValueError ("indice negativo ({} ) non funziona".format(index))
    print("index is {} ".format(index) )
    return l[index]

def fib_algo(index):
    if index < 0 :
        raise ValueError ("indice negativo ({} ) non funziona".format(index))
    elif index <= 1 :    #i == 0 or i == 1
        return index
    else :
        return fib_algo(index - 1) + fib_algo(index - 2)

def fib_algo_lb(i):
    fib_serie = [0,1]
    for f in range(1,i):  #f non è una variabile utilizzata e quindi in python una varibile non usata si può scrivere con _
        fib_serie.append(fib_serie[-1]+fib_serie[-2] )
    return int(fib_serie[i])

def fib_algo_lb_performante(i):
    fib_serie = [0,1]
    for _ in xrange(1,i):  
        fib_serie.append(fib_serie[-1]+fib_serie[-2] )
    return int(fib_serie[i])
	
def fib_algo_so(i):
    numero_corrente = 0
    indice_corrente = 0
    base = 1
    while indice_corrente < 1:
        old_base = numero_corrente
        numero_corrente += base
        base = old_base
        indice_corrente += 1
    return numero_corrente

def fib_algo_so_migliorato(i):
    numero_corrente ,indice_corrente, base = 0, 0, 1
    while indice_corrente < 1:
        old_base = numero_corrente
        numero_corrente += base
        base = old_base
        indice_corrente += 1
    return numero_corrente
   
#dofib = fib_from_string
dofib = fib_from_list
#dofib = fib_algo
if __name__ == "__main__":
    dofib(3)