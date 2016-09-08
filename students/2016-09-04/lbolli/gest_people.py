import json

PEOPLE = []

def main():
    # file di testo
    t = open('gest_people.txt', 'w')
    # file json
    j = open('gest_people.json', 'w')
    # file csv
    #c = open('gest_people.csv', 'w')
    # file xml
    #x = open('gest_people.xml', 'w')
    while True:
        el_dict = {}
        el_list = input("Inserire Name, City, Salary: ").split() 

        if 'exit' in el_list:
            break
        el_dict = {'name': el_list[0], 'city': el_list[1], 'salary': int(el_list[2])}
 
        #_name = input("Inserire Name :")
        #if (_name == "exit"):
        #    break
        #el_dict['name'] = _name
        #_city = input("Inserire City :")
        #if (_city == "exit"):
        #    break
        #el_dict['city'] = _city
        #_salary = input("Inserire Salary :")
        #if (_salary == "exit"):
        #    break
        #el_dict['salary'] = int(_salary)

        PEOPLE.append(el_dict)
        # PEOPLE.append({'name': el_list[0], 'city': el_list[1], 'salary': int(el_list[2])})

    print("")
    print("######### gest_people #########")
    for i, f in enumerate(PEOPLE):
        _str = "[{}] Name: {name}, City: {city}, Salary: {salary}".format(i+1, **f)
        print(_str)
        # stampa su file di testo
        f.write(_str + "\n")
        # stampa su file json
        j.write(json.dumps(f, indent=2))
        # stampa su file csv

    # Se definisco main_and_save devo far ritornare PEOPLE da questa funzione main()

# def save(list_of_dicts, fname="data.json"):
    # with consente di incapsulare tutte le istruzioni fra open e close di un file
    #
    # with open(fname) as f:
    #   f.write()

# def main_and_save():
    # PEOPLE = main()
    # save(PEOPLE)

if __name__ == "__main__" :
	main()
    # Posso mettere il salvataggio su file in questo punto in modo che venga eseguito solo
    # quando si lancia come script, mentre non viene fatto se lo si lancia come modulo
    #
    # Oppure posso definire un'altra funzione che viene eseguita come script
    # main_and_save()
