# -*- coding: utf-8 -*-

import sys
import json

def inserimento():

    var_next = True

    while var_next:
        PEOPLE = []
        person = {}
        var_nome = raw_input("Nome Studente ")
        var_city = raw_input("City Studente ")
        var_sala = int(raw_input("Stipendio Studente "))
        
        person['name'] = var_nome
        person['city'] = var_city
        person['salary'] = var_sala
        
        PEOPLE.append(person)
        
        stampa_persona(PEOPLE)
        
        var_next = raw_input("Continuare l'immisione? Y/n ").upper not in ["N" , "NO"]

    return PEOPLE

    
def get_person_str(p):
    return "lo studente {name} di {city} guadagna {salary}".format(**p)
    
def get_json(data):
    return json.dumps(data, indent=2)


def stampa_persona(l):

    print
    for p in l:
        print(get_person_str(p))
    print

    
def save(list_of_dict, fname="data.txt"):
    with open(fname, "w") as f:
        for p in list_of_dict:
            if fname.endswith("json"):
                f.write(get_json(p))
            else:
                f.write(get_person_str(p))
                
                
def inserimento_save(argv):
    PEOPLE = inserimento()
    print("lista parametri: {}".format(argv))
    if len(argv) > 1:
        save(PEOPLE, fname=argv[1])
    else:
        save(PEOPLE)

    
if __name__ == "__main__":
    inserimento_save(sys.argv)
