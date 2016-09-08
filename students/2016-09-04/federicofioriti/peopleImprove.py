import sys
import json

def get_persons_str(NAMES):
    return ("Name {name}, City {city}, Salary {salary}".format(**NAMES))

def main():

    PEOPLE = []

    while True:
        NAMES = {}

        name = raw_input("Inserisci nome ")
        city = raw_input("Inseriscci citta ")
        # salary = raw_input("Inseriscci salario ")    # va dichiarato come int
        salary = int(raw_input("Inseriscci salario "))

        NAMES = {"name": name, "city": city, "salary": salary}

        PEOPLE.append(NAMES)

        print ("Name {name}, City {city}, Salary {salary}".format(**NAMES))

        while True:
            a = raw_input("Vuoi continuare [Y/n]? ").upper()
            if a in ["Y", "N"]:
                break

        if a == "N":
            break

        return PEOPLE

# write content in a file
def save(list_of_dicts, fname="data.txt"):
    """
    Save data in many formats depending on the filename extension
    :param list_of_dicts: list of names saved in input phase
    :param fname: file name to save content
    :return:
    """
    if fname.endswith(".json"):
        export_data = get_json(list_of_dicts)
    else:
        export_data = ""
        for p in list_of_dicts:
            export_data += get_persons_str(p) + "\n"

    with open(fname) as f:
        f.write(export_data)

def get_json(data):
    return json.dumps(data)

def main_and_save(argv):
    PEOPLE = main()
    print ("lista parametri -> ".format(argv))
    if len(argv) > 1:
        save(PEOPLE, argv)
    else:
        save(PEOPLE)

if __name__ == "__main__":
    # main()
    main_and_save(sys.argv)
