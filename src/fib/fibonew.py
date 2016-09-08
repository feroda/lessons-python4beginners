fib_d = {
    0 : 0,
    1 : 1,
}

def fib(x):
    """
    Calcola fibonacci con cache su dizionario

    Se trova il valore nel dizionario lo restituisce,
    altrimenti lo calcola, lo mette nel dizionario e lo
    restituisce
    """
    if x in fib_d:
        return fib_d[x]

    # fib_pre = fib(x-1)
    # fib_d[x-1] = fib_pre

    # fib_prepre = fib(x-2)
    # fib_d[x-2] = fib_prepre

    # modo elegante rispetto a quanto commentato
    fib_d[x-1], fib_d[x-2] = fib_pre, fib_prepre

    return fib_pre + fib_prepre
