# -*- coding: utf-8 -*-

import csv  
import json
import xml.etree.cElementTree as ET

PEOPLE = []

def print_on_screen(list_input):
    for i,p in enumerate(list_input):
        print("Utente {}".format(i))
        
        print("     Name: {}".format(p["name"]))
        print("     City: {}".format(p["city"]))
        print("     Salary: {}".format(p["salary"]))
        
        
def write_on_csv(list_input):
    with open("people.csv", "wb") as csvfile:
        
        fieldnames = ['name', 'city', 'salary']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames, delimiter = ";")

        writer.writeheader()
        
        for p in list_input:
            writer.writerow(p)

def write_on_json(list_input):
    with open("people.json", "wb") as jsonfile:
        json.dump(list_input, jsonfile)
        
  
def write_on_xml(list_input):
    root = ET.Element("root")
    doc = ET.SubElement(root, "doc")
    utenti_child = ET.SubElement(doc, "Utenti")
    
    for i,p in enumerate(list_input):
        ET.SubElement(utenti_child, "utente " + str(i), name="name").text = p["name"]
        ET.SubElement(utenti_child, "utente " + str(i), name="city").text = p["city"]
        ET.SubElement(utenti_child, "utente " + str(i), name="salary").text = str(p["salary"])
        
    tree = ET.ElementTree(root)
    tree.write("people.xml")

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

def save(list_of_dict):
    write_on_csv(list_of_dict)
    write_on_json(list_of_dict)
    write_on_xml(list_of_dict)
    

def main_and_save():
    main()
    save(PEOPLE)
    
    
if __name__ == "__main__":
 
    try:
        main_and_save()
    except KeyboardInterrupt:
        print("Non puoi uscire")
        #response = raw_input("Sei sicuro di voler uscire? (s/n)")
        #if response == s:
         #   sys.exit()
    
    