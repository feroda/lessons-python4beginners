#!/usr/bin/python2

import sys
import time

MAX = 1050

# 1 1 2 3 5 8 13 21

rv_fib = {
    0: 1,
    1: 1
}


def fib(x):
    if x in rv_fib:
        return rv_fib[x]
    rv_fib[x-1], rv_fib[x-2] = fib(x-1), fib(x-2)
    return rv_fib[x-1] + rv_fib[x-2]


def get_input():
    try:
        num = int(sys.argv[1])
        # num = int(raw_input("\nQuanto vuoi calcolare fibonacci [max {}]? ".format(MAX)))
    except Exception:
        pass
    else:
        return num


def do():
    print("\n--- Il programma di fibonacci ---")
    while True:
        num = get_input()
        if num and num <= MAX:
            break

    rv = fib(num)
    print("\n--- Il risultato di fib({}) e' {} ---\n".format(num, rv))

    choice = 'y' # raw_input("Ti mostro il procedimento? [Y/n] ")
    if choice.upper() != "N":
        for step in range(num+1):
            if step == 0 or step == 1:
                print("fib({}) = {}".format(step, fib(step)))
            else:
                print("fib({}) = fib({}) + fib({}) = {} + {} = {}".format(step, step-2, step-1, fib(step-2), fib(step-1), fib(step)))
            # time.sleep(0.3)


def main():

    try:
        while True:
            print("\n## Per uscire premi CTRL+C su Unix")
            do()
            break
    except KeyboardInterrupt:
        print("\nSei voluto uscire")
        sys.exit(100)

if __name__ == "__main__":
    main()
