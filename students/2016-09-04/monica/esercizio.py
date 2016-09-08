

def main():
    """
    # 1.finche utente non smette.
    # 2.l'utente inserisce il nome 
         usa raw_input per chiedere le info all'utente 
    # 3.l'utente inserisce la città
    # 4.l'utente inserisce lo stipendio
    # 5.inserisci il dizionario con chiavi 
         'name','city','salary'
          nella lista PEOPLE = []
    PEOPLE.append(person_d)          
    
    # 6.STAMPA A VIDEO PEOPLE nel modo che ti piace
    # 7.ri-inizia da Step 1
    # FINE 
    
    #----BONUS-----
    #STEP 8.QUANDO L'UTENTE SMETTE --> SCRIVI I DATI IN UN FILE
    #     SE VUOI STEP 8.1 IN FOMRATO JSON
    #     SE VUOI STEP 8.2 IN FORMATO CSV
    #     SE VUOI STEP  8.3 IN FORMATO XML
    # STEP 9. FALLO ANCHE SE L 'UTENTE PREME CTRL+C O CTRL+Z
    
  """  

PEOPLE =[]

def main():
    scelta = True 
    while scelta:
    
        nome = raw_input("Nome? ")
        citta = raw_input("Citta? ")
        salario = raw_input("Salario? ")
 #       try:
        salario = int(salario)
 #       except ValueError:
 #           raise ValueError("salario non valido")
        d = { "name": nome , "city": citta , "salary": salario }
        PEOPLE.append(d)
    
        scelta = raw_input("Continui o no? ")
        if scelta.lower() in ('n','no'):
            scelta = False
    
        for x in PEOPLE:
            print(x)
        #    print("Nome: {name}".format(name=x["name"])
            print("Nome: {name}".format(**x))

            
if __name__ == "__main__":
    main1()            
#c = raw_input("\nInserisci [NOME/1 / CITTA/2 / SALARIO/3 ] ? ")
 
PEOPLE =[]
#person_d={} oppure person_d = dict (name="luca")
def get_person_str(p) :
    return "nome: "nome:{name}, city: {city}, stipendio: {salary}".format(**p)
def main1():
    scelta = True 
    while scelta:
    
        nome = raw_input("Nome? ")
        city = raw_input("City? ")
        salary = int(raw_input("Salary? "))
        person_d = {
        "name":name,
        "city":city,
        "salary":salary,
        }
        
        PEOPLE.append({
            'name':name,
            'city':city,
            'salary':salary
            })
            print("hai inserito")
            for p in PEOPLE:
            print("nome:{name}, city: {city}, stipendio: {salary}".formt(**p))
            print (get_person_str(p))
            
            want_continue = raw_input("vuoi continuare [y/n]").upper() not in  ["N" ,"NO"]
            want_continue = raw_input("vuoi continuare [y/n]").upper() != "N"
            a = raw_input("vuoi continuare [Y/n]?").upper()
            want_continue = a not in ["N","NO"]
            #OPPURE WANT_CONTINUE = A != "N"
            
            # a = raw_input("vuoi continuare [Y/n]?").upper()
            # if a in ["N","NO"]:
            #     break
            
            if scelta.upper()[0] == "N":
                scelta = False
 #       try:
        salario = int(salario)
 #       except ValueError:
 #           raise ValueError("salario non valido")
        d = { "name": nome , "city": citta , "salary": salario }
        PEOPLE.append(d)
    
        scelta = raw_input("Continui o no? ")
        if scelta.lower() in ('n','no'):
            scelta = False
    
        for x in PEOPLE:
            print(x)
        #    print("Nome: {name}".format(name=x["name"])
            print("Nome: {name}".format(**x))    
            
def main_and_save():
                main()
                save()
def get_person_str(p) :
    return "nome: "nome:{name}, city: {city}, stipendio: {salary}".format(**p)
    
    
import csv
def save_csv(list_of_dicts , f):
    writer = csv.writer(f, delimiter=',')
    writer.writerow(['NAME','CITY', 'SALARY'])
    for p in list_of_dicts:
        writer.writerow([]) 
        
    
import json        
def get_json(data):
    return json.dumps(data, indent=2)
    
def save(list_of_dicts, fname="data.txt"):
    """
    SAVE DATA IN MANY FORMATS DEPENDING ON THE FILENAME EXTENSIONS.
    """
    if fname.endswith(".json"):
        export_data = get_json(list_of_dicts)
    else:
        export_data = ""
        for p in list_of_dicts:
            export_data += get_person_str(p) + "\n"
    # open : https://docs.......
    with open(fname, "w") as f:
        f.write(export_data)


    
    with open (fname, "w") as f:
    for p in list_of_dicts
    f.write(get_person_str(p) + "\n")


def main_and_save(argv):
    PEOPLE = main ()
        print("lista parametri: {}" .format(argv))
        if len(argv) > 1:
            save(PEOPLE, fname=argv[1])
        else:
            save(PEOPLE)
    
if __name__=="__main__:
        main_and_save(sys.argv)
        
import json        
def get_json(data):
    return json.dumps(data)
       


# OOP

class Greeter(object):


    def__init__(self, name):
        self.name = name 
        
    def hello(self):    
        print ("Hello {}".format(self.name})
    def hello(self):
        print ("Hello {0.name}" .format(self)
        
        
luca = greeter("luca")
luca.hello()
simone = greeter("simone")
simone.hello () 