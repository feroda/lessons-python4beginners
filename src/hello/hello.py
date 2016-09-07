# -*- coding: utf-8 -*-

def do_hello(who="pippo"):
	"""
	Funzione che saluta.
	
	:param str who: a chi saluto.
	"""
	print(u"Ciao {}".format(who))  # meglio format
	print(u"Ciao %s" % who)
	
#print("__name__ = {}".format(__name__))
if __name__ == "__main__":
	do_hello()
