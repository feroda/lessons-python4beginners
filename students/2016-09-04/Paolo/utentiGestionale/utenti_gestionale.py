# -*- coding: utf-8 -*-

import csv  

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
        
    print(PEOPLE)
    
    with open("people.csv", "wb") as csvfile:
        spamwriter = csv.writer(csvfile, delimiter=' ', quotechar='|', quoting=csv.QUOTE_MINIMAL)
        spamwriter.writerow(PEOPLE)


if __name__ == "__main__":
    main()
    
    