# -*- coding: utf-8 -*-
def do_hello(who="pippo"):
    print("Ciao {}".format(who)) #meglio format
    print("Ciao {}".format(who)) #meglio format
    print("Ciao %s" % who)
	
if __name__ == "__main__":
    do_hello()