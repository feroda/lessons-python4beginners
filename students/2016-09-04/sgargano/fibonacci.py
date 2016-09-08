#!/usr/bin/python2

MAX = 50

# 1 1 2 3 5 8 13 21


def fib(x):
    if x == 0 or x == 1:
        return 1
    return fib(x-1) + fib(x-2)


def main():

    num = 11
    print("\n--- Il programma di fibonacci ({})---".format(num))
    rv = fib(num)
    print("\n--- Il risultato di fib({}) e' {} ---\n".format(num, rv))

if __name__ == "__main__":
    main()