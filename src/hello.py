# -*- coding: utf-8 -*-

def do_hello(who):
    #il carattere "u" prima di una stringa definisce una stringa unicode
    print (u"ciao {}" .format(who))  # equivale a print (u"Ciao %s" % who)
			
if __name__ == "__main__":
    #questa stringa viene stampata solo se viene eseguito e non se viene
    #importato:
    #doppio underscore -> metodo privato
    do_hello(u"Elena")
