# -*- coding: utf-8 -*-
import sys
import json
import csv

def get_json(data):
    return json.dumps(data, indent = 2) #esporta un dato in formato json

def main_amd_save(argv):
    PEOPLE = main()
    #print ("Lista parametri: {}".format(argv))
    
    if len(argv) > 1:
        save(PEOPLE, argv[1])
    else:
        save(PEOPLE)
        
    add_annual(PEOPLE)
    
    
def main():
    """
    Richiede all'utente di inserire nome, citta' e salario
    finchè l'utente non decide di smettere;
    salva su una lista ciascun input
    """
    choice = "s"
    PEOPLE =[]
    while choice == "s" or choice == "S":
        choice = raw_input("\n\nVuoi inserire un altra persona (S/n)? ")
        if not(choice == "n" or choice == "N"):
            nome = raw_input("Scrivi il nome: ")
            city = raw_input("Scrivi la citta': ")
            salario = int(raw_input("Scrivi lo stipendio: "))
            dati_persona = {
                            "name":nome,
                            "city":city,
                            "salary":salario
                            }
            PEOPLE.append(dati_persona)
            for p in PEOPLE:
                print get_person_str(p)
    return PEOPLE

def add_annual(PEOPLE):
    for diz_pers in PEOPLE:
        diz_pers["annual"] = diz_pers["salary"]*13
        print (get_person_str(diz_pers))

    
def save(PEOPLE, fname = "persone.txt"):
    """
    scrive su file il contenuto della lista di persone
    il formato del file può essere .json, .csv, .txt
    """
    with open(fname, "wb") as f:
        if fname.endswith(".json"):
            f.write(get_json(PEOPLE)+"\n")
#       elif fname.endswith(".csv")
#           writer = csv.writer(f, delimiter=";")
#           writer.writerow()
        else:
            for p in PEOPLE:
                f.write(get_person_str(p)+"\n")
    
    print ("\n\nscritto file: {}".format(fname))
        
def get_person_str(x):
    return "nome = {name}, citta' = {city}, salario = {salary}" .format(**x)
    
if __name__ == "__main__":
    main_amd_save(sys.argv)
        