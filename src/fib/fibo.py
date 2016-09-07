def fib_from_string(i):
    s = "0112358"
    if i < 0:
        raise ValueError(
            "indice negativo ({}) non funziona".format(i))
        
    try:
        return int(s[i])
    except IndexError:
        raise NotImplementedError(
            "Non sono stato capace da 7 in su")


def fib_from_string_simple(i):
    s = "0 1 1 2 3 5 8"
    if i < 0:
        raise ValueError(
            "indice negativo ({}) non funziona".format(i))
    return int(s[i*2])


def fib_from_list(i):
    if i < 0:
        raise ValueError(
            "indice negativo ({}) non funziona".format(i))
        
    return l[i]

fib = fib_from_string_simple
