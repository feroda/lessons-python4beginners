import sys
import json
import csv

def get_person_str(p):
    return  "Nome: {name}, City: {city}, Salary:{salary}".format(**p) 


def get_csv(data):
    return csv.
    
def get_json(data):
    return json.dumps(data, indent=2)

def main():
    PEOPLE=[]
    want_continue = True
    while True:
        name = raw_input("Nome?")
        city = raw_input("City?")
        salary = int(raw_input("Salary?"))
        
        PEOPLE.append({
            'name': name,'city':city,'salary':salary })
        print ("Hai inserito")
        for p in PEOPLE:
            get_person_str(p)
            print("Nome:{name}, City: {city}, Stipendio: {salary}".format(**p))
 
        a = raw_input("Vuoi continuare [y/n] ").upper()
        if a in ["N","NO"]:
            break
    return PEOPLE
    
def main_and_save(argv):
    PEOPLE = main()
    print("Lista parametri : {}".format(argv))
    if len(argv)>1 and argv[1].endswith(".json"):
        saveJson(PEOPLE, fname=argv[1]) 
    elif len(argv)>1:
        save(PEOPLE, fname=argv[1]) 
    else:
        save(PEOPLE)


def save_csv (list_of_dicts, f):
    
    writer = csv.writer(f, delimiter=',')
    writer.writerow(['NAME','CITY','SALARY']  )     
    
    for p in list_of_dicts:
        writer.writerow([p["name"],p["city"],p["salary"]])
        
def save(list_of_dicts, fname="data.txt"):
    
    """
    Save data in many formats depending on the filename extensions
    """
    
    with open(fname, "w") as f:
        for p in list_of_dicts:
            f.write(get_person_str(p) + "\n")
    
def saveJson(list_of_dicts, fname="data.txt"):
    with open(fname, "w") as f:
        for p in list_of_dicts:
            f.write(get_json(p))
          
if __name__== "__main__":
    main_and_save(sys.argv)
