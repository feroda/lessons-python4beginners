# -*- coding: utf-8 -*-
"""
Questo modulo offre strumenti per calcolare
la funzione di Fibonacci

fib(0) --> 0
fib(1) --> 1
fib(2) --> 1
fib(3) --> 2
fib(n) --> fib(n-1) + fib(n-2)
"""
import sys
import types
import collections

d = {
    "inizializza": "fibonacci",
    0: 0,
    1: 1,
}

d = collections.OrderedDict([
    ("inizializza", "fibonacci"), (0,0), (1,1)
])


def calc_fibo(n):
    """
    Calcola la funzione di Fibonacci, appoggiandosi ad una cache

    :param n: un intero positivo di input
    :return: il valore (intero) di Fibonacci per n
    """

    if n in d:
        rv = d[n]
    elif n < 0:
        raise ValueError("Fibo not supported for negative numbers ({})".format(n))
    # elif type(n) != types.IntType:
    elif not isinstance(n, types.IntType):
        raise TypeError("\CORSO: type {} is not valid".format(type(n)))
    else:
        rv = calc_fibo(n - 1) + calc_fibo(n - 2)
        d[n] = rv
        d["stringa{}".format(n)] = "pippo"

    return rv

def main(argv):

    if len(argv) < 2:
        print("Usage {} <num>".format(argv[0]))
        sys.exit(1)

    n = int(argv[1])
    rv = calc_fibo(n)
    print("LA SEQUENZA DI FIBONACCI PER {}: ".format(n))

    for k, v in d.iteritems():
        print("fibo({}) = {}".format(k, v))

    for k, v in sorted(d.items()):
        print("fibo({}) = {}".format(k, v))

if __name__ == "__main__":
    main(sys.argv)    
