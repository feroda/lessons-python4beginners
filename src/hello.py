# -*- coding: utf-8 -*-

def compose_hello(who, force=False):
    try:
	    message = "Hello " + who + "!"
    except TypeError:
	    print ("[WARNING]: il parametro 'who' dovrebbe essere una stringa")
			
if __name__ == "__main__":
    #questa stringa viene stampata solo se viene eseguito e non se viene
    #importato:
    #doppio underscore -> metodo privato
    do_hello()
