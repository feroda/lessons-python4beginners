#!/usr/bin/python2

import sys

MAX = 50

# 1 1 2 3 5 8 13 21


def fib(x):
    if x == 0 or x == 1:
        return 1
    return fib(x-1) + fib(x-2)


def get_input():
    try:
        num = int(raw_input("\nQuanto vuoi calcolare fibonacci [max {}]? ".format(MAX)))
    except KeyboardInterrupt:
        print("\nSei voluto uscire")
        sys.exit(100)
    except Exception:
        pass
    else:
        return num


def main():

    print("\n--- Il programma di fibonacci ---")
    while True:
        num = get_input()
        if num and num <= MAX:
            break

    rv = fib(num)
    print("\n--- Il risultato di fib({}) e' {} ---\n".format(num, rv))

if __name__ == "__main__":
    main()
