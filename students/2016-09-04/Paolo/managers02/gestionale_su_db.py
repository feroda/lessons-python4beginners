# -*- coding: utf-8 -*-

import sys
from collections import defaultdict
import sqlite3
import os

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
    
    
class SqliteDatabase(object):
    def __init__(self, file_name):
        self.file_name = file_name
        
        self.conn = sqlite3.connect(file_name)
        self.conn.row_factory = sqlite3.Row

        cursor = self.conn.cursor()
        
        if not os.path.exists(file_name):
            cursor.execute("CREATE TABLE people (name VARCHAR(64), city VARCHAR(32), salary INTEGER);")
            
    def write(self, list):
        cursor = self.conn.cursor()
        
        for row in list:
            t = (row["name"], row["city"], row["salary"])
            cursor.execute('INSERT INTO people VALUES (?,?,?)', t)
            
    def read_all(self):
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM people")
        return cursor.fetchall()
        
    def commit(self):
        self.conn.commit()
        
    def close(self):
        self.conn.close()
    
def save_on_db(list_input, database_manager):
    database_manager.write(list_input)
    database_manager.commit()
    
    
def read_from_db(database_manager):
    result = database_manager.read_all()
    print("Cosa c'è nel database")
    print(result)
    
    
def main_and_save(input_args):
    main()
    
    database_manager = SqliteDatabase("mio_db.db")
    save_on_db(PEOPLE, database_manager)
    read_from_db(database_manager)
    
    database_manager.close()
    
if __name__ == "__main__":
    main_and_save(sys.argv)

    
    