
import json

def print_persons():
    print ("Name {name}, City {city}, Salary {salary}".format(**NAMES))
def main():

    choice = True
    PEOPLE = []

    while choice:
        NAMES = {}

        name = raw_input("Inserisci nome ")
        city = raw_input("Inseriscci citta ")
        # salary = raw_input("Inseriscci salario ")    # va dichiarato come int
        salary = int(raw_input("Inseriscci salario "))

        NAMES = {"name": name, "city": city, "salary": salary}

        PEOPLE.append(NAMES)

        print ("Name {name}, City {city}, Salary {salary}".format(**NAMES))

        choice = raw_input("vuoi inserire un altro nome (S/N)?").upper() in ["N", "NO"]

def save():
    # write content in a file
    file = open("people.txt", "w")
    json.dump(PEOPLE, file)
    file.close()

def main_and_save():
    PEOPLE = main()
    save(PEOPLE)

if __name__ == "__main__":
    main()
