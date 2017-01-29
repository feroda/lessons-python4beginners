# -*- coding: utf-8 -*-

"""
modulo di esportazione in u file json
"""

import json
import codecs
from collections import OrderedDict

class Person(OrderedDict):
    def __init__(self, x, a) :
        OrderedDict.__init__(self, x)
        super(Person, self).__setitem__("conigli", a)  


def export():
    """
    utilizzo orderedDict per mantenere l'ordine di inserimento
    """
    p_rec = [
                OrderedDict([("name", "Gianni"), ("city", "Napoli"), ("salary", 3000), ("genfibo", 5)]),
                OrderedDict([("name", "Simone"), ("city", "Pesaro"), ("salary", 3300), ("genfibo", 7)]),
                OrderedDict([("name", "Gabriele"), ("city", "Faenza"), ("salary", 2900), ("genfibo", 12)]),
                OrderedDict([("name", "Fabio"), ("city", "Ascoli"), ("salary", 300), ("genfibo", 8)]),
                OrderedDict([("name", "Andrea"), ("city", "Ancona"), ("salary", 200), ("genfibo", 32)]),
                OrderedDict([("name", "Davide"), ("city", "Rimini"), ("salary", 2300), ("genfibo", 1)])
            ]

    
    p = []        

    for x in p_rec:
        
        if x["name"] == "Gianni":
            person = Person(x,[OrderedDict([("name", "coniglio1_Gianni"), ("age", 3)]),
            OrderedDict([("name", "coniglio2_Gianni"), ("age", 8)]),
            OrderedDict([("name", "coniglio3_Gianni"), ("age" , 4)])])
        elif x["name"] == "Simone":
            person = Person(x,[OrderedDict([("name", "coniglio1_Simone"), ("age" , 1)]),
            OrderedDict([("name", "coniglio2_Simone"), ("age" , 2)]),
            OrderedDict([("name", "coniglio3_Simone"), ("age" , 3)])])
        elif x["name"] == "Gabriele":
                person = Person(x,[OrderedDict([("name", "coniglio1_Gabriele"), ("age" , 1)])]) 
        elif x["name"] == "Fabio":
                person = Person(x,[OrderedDict([("name", "coniglio1_Fabio"), ("age" , 10)]),
                OrderedDict([("name", "coniglio2_Fabio"), ("age" , 6)])])
        elif x["name"] == "Andrea":
                person = Person(x,[OrderedDict([("name", "coniglio1_Andrea"), ("age" , 11)]),
                OrderedDict([("name", "coniglio2_Andrea"), ("age" , 1)])])
        elif x["name"] == "Davide":
                person = Person(x,[OrderedDict([("name", "coniglio1_Davide"), ("age" , 7)]),
                OrderedDict([("name", "coniglio2_Davide"), ("age" , 2)]),
                OrderedDict([("name", "coniglio3_Davide"), ("age" , 5)])])
    
        p.append(person)

    with codecs.open("C:/Persone.json", encoding="utf-8", mode="w+") as f:
        json.dump(p,f)

if __name__ == "__main__":
    export()
