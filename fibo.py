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

def calc_fibo(n):
    if n == 0: 
        return 0
    elif n == 1:
        return 1

    return calc_fibo(n - 1) + calc_fibo(n-2)

if __name__ == "__main__":
    
    if len(sys.argv) < 2:
        print("Usage {} <num>".format(sys.argv[0]))
        sys.exit(1)

    n = int(sys.argv[1])
    rv = calc_fibo(n)
    print("fibo({0}) = {1}".format(n, rv))