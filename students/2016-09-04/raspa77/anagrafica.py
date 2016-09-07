# -*- coding: utf-8 -*-

def inserimento():

    var_next = "N"
    PEOPLE = []
    
    while var_next != "y":
        person = {}
        var_nome = raw_input("Nome Studente ")
        var_city = raw_input("City Studente ")
        var_sala = raw_input("Stipendio Studente ")
        
        person['name'] = var_nome
        person['city'] = var_city
        person['salary'] = var_sala
        
        PEOPLE.append(person)
        
        stampa(PEOPLE)
        
        var_next = raw_input("Interrompere l'immisione? y/n ")
        
def stampa(l):

    print
    for s in l:
        print("lo studente {name} di {city} guadagna {salary}".format(**s))
    print

    
if __name__ == "__main__":
    inserimento()