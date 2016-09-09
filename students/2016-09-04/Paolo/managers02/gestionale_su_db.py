# -*- coding: utf-8 -*-

import sys
from collections import defaultdict
import sqlite3
import os
import sqlitedatabase as sqlmanager

PEOPLE = []

def print_on_screen(list_input):
    for i,p in enumerate(list_input):
        print("Utente {}".format(i))
        
        print("     Name: {}".format(p["name"]))
        print("     City: {}".format(p["city"]))
        print("     Salary: {}".format(p["salary"]))
        

def main():
    
    number_of_people = int(raw_input("Per quanti utenti vuoi inserire le anagrafiche?"))
    
    for count in range(number_of_people):
        anagraphic_people_dict = {}
        name, city, salary = raw_input("Inserisci name, city, salary:").split()
        
        anagraphic_people_dict["name"] = name
        anagraphic_people_dict["city"] = city
        anagraphic_people_dict["salary"] = int(salary)
        PEOPLE.append(anagraphic_people_dict)
        
    print_on_screen(PEOPLE)
    
    
def save_on_db(list_input, database_manager):
    database_manager.write(list_input)
    database_manager.commit()
    
    
def read_from_db(database_manager):
    result = database_manager.read_all()
    print("Cosa c'è nel database")
    print(result)
    
    
def main_and_save(input_args):
    main()
    
    database_manager = sqlmanager.SqliteDatabase("mio_db.db")
    save_on_db(PEOPLE, database_manager)
    read_from_db(database_manager)
    
    database_manager.close()
    
if __name__ == "__main__":
    main_and_save(sys.argv)

    
    