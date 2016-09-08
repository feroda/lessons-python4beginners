# -*- coding: utf-8 -*-

# funzione che saluta
def do_hello(who="pippo"):
    """
    funzione che saluta
    :param str who: a chi saluto
    """
    print("Hello {}".format(who))  # meglio format, la seconda istruzione antica
    print("Hello %s" %who)
    tot = 1 + 2
    print(tot)
	
if __name__ == "__main__":
    do_hello()