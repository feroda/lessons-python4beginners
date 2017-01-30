# -*- coding: utf-8 -*-

"""
modulo di esportazione in u file json
"""

import json
import codecs
from collections import OrderedDict

class Person(OrderedDict):

    def __init__(self, x, a) :
        # WAS: OrderedDict.__init__(self, x) ... in questo modo funziona
        # ma se devi invocare il costruttore della classe base quando hai un'unica classe da cui derivi, devi fare
        super(Person, self).__init__(x)
        # WAS: super(Person, self).__setitem__("conigli", a)
        # in questo modo funziona, ma non occorre che lo richiami con la super dato che non vai in ciclo infinito
        # puoi direttamente settare la chiave
        self["conigli"] = a

        # NOTA: il tuo costruttore rompe la compatibilità con il dizionario
        # per questo ti scrivo sotto una classe che userò nel resto del codice
        # per essere totalmente compatibile con un OrderedDict


class Person(OrderedDict):  # tieni presente che questa seconda classe verrà usata dall'interprete

    def __init__(self, *args, **kw):  # parametri variabili perché non mi voglio curare di come viene inizializzato l'oggetto
        super(OrderedDict, self).__init__(*args, **kw)
        # Verifico che non sia stata usata la chiave riservata "conigli"

        if "conigli" in self:  # self ora è un dizionario e questo è un modo analogo per dire "conigli" in self.keys()
            raise KeyError("la chiave 'conigli' è riservata")

        # Poi inizializzo la chiave "conigli" ad una lista vuota
        self["conigli"] = []

    def set_conigli(self, lista_di_conigli):
        # questo metodo fa uso della __setitem__
        self["conigli"] = lista_di_conigli

        # NOTA: in questa classe derivata per la precisione dovrei proteggere la chiave riservata anche nella __setitem__,
        # e usare il metodo nella superclasse ogni volta mi serve, ma non è scopo di questo esercizio
        # fare un'applicazione che vada in produzione.

    def add_coniglio(self, name, age):
        """
        Questo metodo aggiunge un coniglio alla lista di conigli.

        Personalmente non credo che ci importi che name e age siano attributi
        ordinati, quindi userò un dizionario tradizionale e non un OrderedDict
        """
        self["conigli"].append(dict(name=name, age=age))



def create():
    """
    creazione dei dati in una lista di oggetti Person (derivati da dizionari ordinati)

    :return: la lista creata
    """

    # NOTA: separo la creazione dall'esportazione
    p = [
        # WAS: OrderedDict([("name", "Gianni"), ("city", "Napoli"), ("salary", 3000), ("genfibo", 5)]),
        # Inizializzo direttamente Person
        Person([("name", "Gianni"), ("city", "Napoli"), ("salary", 3000), ("genfibo", 5)]),
        Person([("name", "Simone"), ("city", "Pesaro"), ("salary", 3300), ("genfibo", 7)]),
        Person([("name", "Gabriele"), ("city", "Faenza"), ("salary", 2900), ("genfibo", 12)]),
        Person([("name", "Fabio"), ("city", "Ascoli"), ("salary", 300), ("genfibo", 8)]),
        Person([("name", "Andrea"), ("city", "Ancona"), ("salary", 200), ("genfibo", 32)]),
        Person([("name", "Davide"), ("city", "Rimini"), ("salary", 2300), ("genfibo", 1)])
    ]

    for x in p:

        if x["name"] == "Gianni":
            # Esempio 1: uso il metodo aggiunto nel modo in cui lo hai fatto tu
            x.set_conigli([
                OrderedDict([("name", "coniglio1_Gianni"), ("age", 3)]),
                OrderedDict([("name", "coniglio2_Gianni"), ("age", 8)]),
                OrderedDict([("name", "coniglio3_Gianni"), ("age" , 4)])
            ])
        elif x["name"] == "Simone":
            # Esempio 2: uso il metodo add_coniglio
            x.add_coniglio(name="coniglio1_Simone", age=1)
            x.add_coniglio(name="coniglio2_Simone", age=2)
            x.add_coniglio(name="coniglio3_Simone", age=3)

        elif x["name"] == "Gabriele":
            # NOTA: questi di seguito non ti funzioneranno più, ma te li lascio
            # anche per farti vedere come puoi indentare liberamete all'interno delle parentesi
            # e per farti notare la differenza di pulizia del codice.
            # Ricorda: l'eleganza conta in Python, ti mette sulla strada giusta!
            # DA RIADATTARE: person = Person(x,[OrderedDict([("name", "coniglio1_Gabriele"), ("age" , 1)])])
            pass
        elif x["name"] == "Fabio":
            pass
            # DA RIADATTARE:     person = Person(x,[
            # DA RIADATTARE:         OrderedDict([("name", "coniglio1_Fabio"), ("age" , 10)]),
            # DA RIADATTARE:         OrderedDict([("name", "coniglio2_Fabio"), ("age" , 6)])
            # DA RIADATTARE:     ])
        elif x["name"] == "Andrea":
            pass
            # DA RIADATTARE:     person = Person(x,[OrderedDict([("name", "coniglio1_Andrea"), ("age" , 11)]),
            # DA RIADATTARE:         OrderedDict([("name", "coniglio2_Andrea"), ("age" , 1)])])

        elif x["name"] == "Davide":
            pass
            # DA RIADATTARE:     person = Person(x,[
            # DA RIADATTARE:         OrderedDict([("name", "coniglio1_Davide"), ("age" , 7)]),
            # DA RIADATTARE:         OrderedDict([("name", "coniglio2_Davide"), ("age" , 2)]),
            # DA RIADATTARE:         OrderedDict([("name", "coniglio3_Davide"), ("age" , 5)])
            # DA RIADATTARE:     ])

        # WAS: p.append(person)
        # Hai risparmiato una variabile e non devi fare l'append

    return p


def export(p):
    """
    utilizzo orderedDict per mantenere l'ordine di inserimento
    """


    # OK ricorda solo che C:/ ti funzionerà solo su sistemi Windows
    # dovresti usare os.path.join("/Persone.json")
    # ora non lo posso provare, ma se puoi provalo e fammi sapere se su Windows ti funziona
    with codecs.open("Persone.json", encoding="utf-8", mode="w+") as f:
        json.dump(p,f)


if __name__ == "__main__":

    # separata la creazione dall'export
    people = create()
    export(people)
