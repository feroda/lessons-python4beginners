#!/usr/bin/python2

x = 0
MAX = 3
GREET = 'Hello'


def hello(who):
    print("[{}] {} {}!".format(x, GREET, who))


def main():

    global x
    print("\n--- Il programma dei saluti ---")
    while x < MAX:
        who = raw_input("\nChi vuoi salutare oggi? ")
        hello(who)
        x += 1

    print("\n--- Complimenti, hai salutato {} persone ---\n".format(MAX))

if __name__ == "__main__":
    main()
