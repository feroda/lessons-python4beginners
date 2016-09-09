def main():

    PEOPLE = insert_people()

    sum_salary_all(PEOPLE)

    list_people_by_city(PEOPLE)

def insert_people():
    PEOPLE = []

    while True:
        NAMES = {}

        NAMES["name"] = name = raw_input("Inserisci nome ")
        NAMES["city"] = city = raw_input("Inseriscci citta ")
        NAMES["salary"] = salary = int(raw_input("Inseriscci salario "))

        PEOPLE.append(NAMES)

        # print ("Name {name}, City {city}, Salary {salary} Annual {annual}".format(**NAMES))

        while True:
            a = raw_input("Vuoi continuare [Y/n]? ").upper()
            if a in ["Y", "N"]:
                break

        if a == "N":
            break

    return PEOPLE

def sum_salary_all(list_people):
    for p in list_people:
        sum_salary_single(p)

def sum_salary_single(list_people):
    list_people['annual'] = list_people['salary'] * 13

def list_people_by_city(list_people):
    list_city = list_people.sort()

if __name__ == '__main__':
    main()
