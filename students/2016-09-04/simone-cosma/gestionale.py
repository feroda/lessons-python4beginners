import sys
import json
import xml
import csv
import io

def to_csv_string(dictionary):
    '''
    Converte un dictionary in string csv (con header)
    '''
    keys = dictionary[0].keys()
    with io.BytesIO() as f: 
        dict_writer = csv.DictWriter(f, keys)
        dict_writer.writeheader()
        dict_writer.writerows(dictionary)
        return f.getvalue()

FILE_HANDLER_GENERATOR = {
    'f' : {'ext': 'txt',    'func': str, 'parameters': {}},
    'j' : {'ext': 'json',   'func': json.dumps, 'parameters': {'indent':4}},
    'c' : {'ext': 'csv',    'func': to_csv_string, 'parameters': {}},
    'x' : {'ext': 'xml',    'func': xml, 'parameters': {}},
    }



def ask_info():
    name, city, salary = raw_input("Name?"), raw_input("City?"), raw_input("Salary?")
    return (name, city, int(salary))

def save_info(dictionary, name, city, salary):
    dictionary.append(dict(name=name, city=city, salary=salary))

def print_info(people):
    for info in people:
        print('Nome: {name} - City: {city} - Salary: {salary}'.format(**info))

def save_to_file(dictionary, file_type, filename):
    handler = FILE_HANDLER_GENERATOR[file_type]

    with open('{}.{}'.format(filename, handler['ext']), 'wb') as file:
        file.write(handler['func'](dictionary, **handler['parameters']))

def should_save(people, filename='PEOPLE'):
    file_format = raw_input('formato salvataggio? [[f]ile|[j]son|[x]ml|[c]sv|NO]').lower()

    if file_format in ('f', 'j', 'c'):
        save_to_file(people, file_format, filename)

def main():
    PEOPLE = []
    ask_please = True

    while ask_please:
        info = ask_info()
        save_info(PEOPLE, info[0],info[1],info[2])
        print_info(PEOPLE)

        ask_please = raw_input('Continuo? s/N').lower() == 's'

    return PEOPLE

def calculate_annual(people):
    for p in people:
       add_annual_field(person)

def add_annual_field(person):
    person['annual'] = person['salary'] * 13

def group_by_city(people):
    grouped = {}
    for p in people:
        if(not grouped.has_key(p['city'])):
            grouped[p['city']] = []
        grouped[p['city']].append(p)
    
    return grouped

if __name__ == "__main__":
    people = main() 
    calculate_annual(people)
    should_save(people)