# -*- coding: utf-8 -*-
"""
Questo e' un gestionale delle persone che hanno conigli.
"""
import codecs

import export_manager as emanager
from people_manager import Person

def export_repr_all(people, fname="export.txt"):
    with codecs.open(fname, encoding="utf-8", mode="w+") as f:
        f.write(repr(people))

def export_repr_line_by_line(people, fname="export.txt"):

    all_reprs = [ repr(x) for x in people ]
    with codecs.open(fname, encoding="utf-8", mode="w+") as f:
        f.writelines(all_reprs)

def export_custom_line_by_line(people, fname="export.txt",
                               fmt=u"n:{name}, c:{city}, s:{salary}, g:{genfibo}\n"):

    all_reprs = [fmt.format(**x) for x in people]
    with codecs.open(fname, encoding="utf-8", mode="w+") as f:
        f.writelines(all_reprs)


def ask_for_person():
    p = Person()
    for attr in ['name', 'city', 'salary', 'genfibo']:
        ain = u"Inserisci {}: ".format(attr)
        value = raw_input(ain.encode("utf-8"))
        if value == "STOP":
            return
        else:
            p[attr] = value
    return p


def main():
    """
    # Step 1. Finché l'utente non scrive STOP
    # Step 2. L'utente inserisce il nome
    #         Usa raw_input("Inserisci ...") per chiedere le info all'utente
    # Step 3. L'utente inserisce la città
    # Step 4. L'utente inserisce lo stipendio
    # Step 5. Inserisci il dizionario con chiavi 
    #   'name', 'city', 'salary', 'genfibo'
    #   nella lista PEOPLE = []
    # Step 6. Stampa a video PEOPLE nel modo che ti piace
    # Step 7. Riinizia da Step 1
    # FINE
    """
    PEOPLE = []
    while True:
        person = ask_for_person()
        if person:
            PEOPLE.append(person)
            print("INSERITI:")
            for i, p in enumerate(PEOPLE):
                print("{}. {name} da {city}: genfibo {genfibo}".format(i, **p))
        else:
            break

    exporter_name = raw_input("In che formato li vuoi esportare? ")

    factory = emanager.ExporterFactory()

    try:    
        exporter = factory.get_instance(exporter_name)
    except KeyError:
        print("Formati di export supportati: {}".format(factory.supported))
    else:
        exporter.do_export(PEOPLE)


if __name__ == "__main__":
    main()    
