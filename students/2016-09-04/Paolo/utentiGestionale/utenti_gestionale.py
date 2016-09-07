# -*- coding: utf-8 -*-

import csv  
import json
import xml.etree.cElementTree as ET

def print_on_screen(list_input):
    for i,p in enumerate(list_input):
        print("Utente {}".format(i))
        
        print("     Name: {}".format(p["name"]))
        print("     City: {}".format(p["city"]))
        print("     Salary: {}".format(p["salary"]))
        
        
def write_on_csv(list_input):
    with open("people.csv", "wb") as csvfile:
        spamwriter = csv.writer(csvfile, delimiter=' ', quotechar='|', quoting=csv.QUOTE_MINIMAL)
        spamwriter.writerow(list_input)
        

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
    
    PEOPLE = []
    number_of_people = int(raw_input("Per quanti utenti vuoi inserire le anagrafiche?"))
    
    for count in range(number_of_people):
        anagraphic_people_dict = {} 
        name, city, salary = raw_input("Inserisci name, city, salary:").split()
        
        anagraphic_people_dict["name"] = name
        anagraphic_people_dict["city"] = city
        anagraphic_people_dict["salary"] = int(salary)
        PEOPLE.append(anagraphic_people_dict)
        
    print_on_screen(PEOPLE)      
    write_on_csv(PEOPLE)
    write_on_json(PEOPLE)
    write_on_xml(PEOPLE)
    


if __name__ == "__main__":
    main()
    
    