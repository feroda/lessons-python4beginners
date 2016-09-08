
# returning the index from the fibonacci's sequence
def fib_from_string(n):
    s = "0112358"
    # verificare la natura del campo (intero o stringa)
    if n < 0:
       raise ValueError("indice negativo ({}) non ammesso".format(n))
    elif n > 6:
        raise ValueError("indice ({})non presente".format(n))
    else:
        return int(s[n])

def fib_from_list(n):
    l = [0,1,1,2,3,8,13,21,34,55,89,144,233,377,610,987,1597]
    if n < 0:
        raise ValueError("indice negativo ({}) non ammesso".format(n))
    elif n > 17:
        raise ValueError("indice ({})non presente".format(n))
    else:
        return l[n]

def fib_algo(n):
    lista = [0,1,1]
    for i in range (2, n):
        lista.append(lista[-1] + lista[-2])
    return lista[n]

fib = fib_algo()

