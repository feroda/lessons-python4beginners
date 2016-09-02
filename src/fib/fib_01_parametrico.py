#!/usr/bin/python2

MAX = 50

# 1 1 2 3 5 8 13 21


def fib(x):
    if x == 1 or x == 2:
        return 1
    return fib(x-1) + fib(x-2)


def main():

    print("\n--- Il programma di fibonacci ---")
    while True:
        num = int(raw_input("\nQuanto vuoi calcolare fibonacci [max {}]? ".format(MAX)))
        if num <= MAX:
            break

    rv = fib(num)
    print("\n--- Il risultato di fib({}) e' {} ---\n".format(num, rv))

if __name__ == "__main__":
    main()
