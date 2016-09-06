# -*- coding: utf-8 -*-

def do_hello():
    print (u"ciao Elena!") #il carattere "u" prima di una stringa definisce
                           #una stringa unicode
    tot = 1 + 1
    print (tot)
	
if __name__ == "__main__":
    #questa stringa viene stampata solo se viene eseguito e non se viene
    #importato:
    #doppio underscore -> metodo privato
    do_hello()
