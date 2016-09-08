
import sys


def main():

    PEOPLE = []
    while True:

        name = raw_input("Nome? ")
        city = raw_input("City? ")
        salary = int(raw_input("Salary? "))
        person_d = {
            "name": name,
            "city": city,
            "salary": salary,
        }

        PEOPLE.append(person_d)

        print("Hai inserito")
        for p in PEOPLE:
            print(get_person_str(p))
            
        
        while True:
            a = raw_input("Vuoi continuare [Y/n]? ").upper() 
            if a in ["Y", "N"]:
                break

        if a == "N":
            break

    return PEOPLE


def get_person_str(p):
    return "Nome: {name}, City: {city}, Stipendio: {salary}".format(**p)

import json
def get_json(data):
    return json.dumps(data, indent=2 )
    


# def save(list_of_dicts, fname="data.txt"):
#     """
#     Save data in many formats depending on the filename extension.
#     """
# 
#     if fname.endswith(".json"):
#         export_data = get_json(list_of_dicts)
#     else:
#         export_data = ""
#         for p in list_of_dicts:
#             export_data += get_person_str(p) + "\n"
# 
#     # open: https://docs.python.org/2.7/library/functions.html?highlight=open#open
#     with open(fname, "w") as f:
#         f.write(export_data)


import csv
def save_csv(list_of_dicts, f):

    writer = csv.writer(f, delimiter=',')
    writer.writerow(['NAME', 'CITY', 'SALARY'])

    for p in list_of_dicts:
        writer.writerow([ p["name"], p["city"], p["salary"] ])


def save(list_of_dicts, fname="data.txt"):
    """
    Save data in many formats depending on the filename extension.
    """

    # open: https://docs.python.org/2.7/library/functions.html?highlight=open#open
    with open(fname, "wb") as f:

        if fname.endswith(".json"):
            json.dump(list_of_dicts, f)

        elif fname.endswith(".csv"):
            save_csv(list_of_dicts, f)
        else:
            export_data = ""
            for p in list_of_dicts:
                export_data += get_person_str(p) + "\n"

            f.write(export_data)

def main_and_save(argv):

    PEOPLE = main()

    if len(argv) > 1:
        save(PEOPLE, fname=argv[1])
    else:
        save(PEOPLE)


if __name__ == "__main__":
    main_and_save(sys.argv)

