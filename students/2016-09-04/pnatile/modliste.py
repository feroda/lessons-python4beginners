# -*- coding: utf-8 -*-
import collections

def mod_list():
	l2 = [0, 1, 1, 2, 3, 5, 8,13,21,34]
	print("l2 : {} ".format(l2))
	l3 = [x*2 for i,x in enumerate(l2) if not i %2 ]
	print("l3 : {} ".format(l3))
	"""
	dizionari
	d2_ord = collections.OrderedDict ([('a', 1), ('b',2), ('l', 10)] )
	d2 = {"a":1, "b":2, "l":10}
	d2["a"]
	d2.get("a") --> se non trova elemento restituisce none
	d2.get("a",300) --> gli do valore di default se non trovo elemento
	se voglio verificare se esiste una chiave
	if "c" in d2:
		print("OK")
	la lista delle chiavi possiamo averla con
	d2.keys()
	per i valori abbiamo
	d2.values()
	nei diizonari è utile iterazione chiave, valore
	a questo scopo possiamo usare
	d2.items()
	for k, v in d2.items():
		print("Lettera {} in posizione {} ".format(k,v))
	se si sovrascrive una chiave non si hanno errori
	d2.has_key("c") --> metodo non piu usato perche da python 7 è sostituito da costrutto if "c" in d2
	10 in d2.values() --> meno performante, meglio andare per chiave
	"""

	
if __name__ == "__main__":
    mod_list()

