#!/usr/bin/python2
# -*- coding: utf-8 -*-               # <-- specifica dell'encoding del file se != ASCII

# This is hello_who_2.py

def hello(who):
    """                               # <-- `docstring` della funzione. Attributo `__doc__`
    Say hello to someone.

       :param str who: The person to say Hello  # <-- [notazione parametri python in sphinx](http://www.sphinx-doc.org/en/stable/domains.html#python-signatures)
   """                               # <-- chiusura della docstring su linea dedicata (PEP 257)
   print("Hello {}!".format(who)

if __name__ == "__main__":
    hello("mamma")
