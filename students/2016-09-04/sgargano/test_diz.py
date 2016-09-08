people=[]

    


def main():
    prosegui=True
    while prosegui: 
        name = raw_input("Inserisci il nome ")
        city = raw_input("Inserisci la city ")
        salary = raw_input("Inserisci il salario ")
        person_d= {"name": name, "city": city, "salary": salary}
        people.append(person_d)
        continue_inserimento= raw_input("Vuoi continuare? [Y/N]")
        if  continue_inserimento!= "N":
            prosegui = True
        else :
            prosegui = False
    print("La lista inserita è {}".format(people))
    stampa_lista()
            
def stampa_lista():
    for x in people:
        print ("PERSONA (name), (city), (salary)".format(**x) )          
            
if __name__== "__main__":
    main()
