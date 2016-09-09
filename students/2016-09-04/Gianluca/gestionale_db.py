import sys
import json
import csv
import copy 
import sqlite3
import os


def get_pers_strin(p):
    return "Nome: {name}, Citta': {city}, Stipendio: {salary}".format(**p)

def fun_stipendio_annuo(d):
	salary_anno = d["salary"] * 13
	d['annual'] = salary_anno

def fun_chiedi(PEOPLE):
	name = raw_input("Quale e' il nome? ")
	city = raw_input("La citta'? ")
	salary = int(raw_input("Lo stipendio? ")) #Gestire se non
	person_d = {
		'name': name,
		'city': city,
		'salary': salary
		}
	fun_stipendio_annuo(person_d)
	PEOPLE.append(person_d)

def main(fname):
	PEOPLE = [] #list()
	if fname.endswith("db"):
		read_db(fname, PEOPLE)
	while True:
		fun_chiedi(PEOPLE)
		print("Hai inserito:\n")
		for p in PEOPLE:
			print(get_pers_strin(p))
		print("\n")
		if raw_input("Si desidera inserire altre persone (S/n)? ") in ("N","n"):
			break
	return PEOPLE

def save(lista_people, fname="data.txt"):
	if fname.endswith("json"):
		save_json(lista_people, fname)
	elif fname.endswith("xls"):
		save_xls(lista_people, fname)
	elif fname.endswith("db"):
		save_db(lista_people, fname)
	else:
		save_txt(lista_people, fname)

def save_txt(data, fname):
	with open(fname, "w") as f:
		for p in data:
			f.write(get_pers_strin(p) + "\n")

def get_conn(fname):
	conn = sqlite3.connect(fname)
	conn.row_factory = sqlite3.Row
	return conn

def create_db(fname):
	conn = get_conn(fname)
	c = conn.cursor()
	c.execute("CREATE TABLE people (name VARCHAR(64), city VARCHAR(32), salary INTEGER);")
	conn.commit()
	conn.close()
	
def save_db(data, fname):
	if not os.path.exists(fname):
		create_db(fname)

	conn = get_conn(fname)
	c = conn.cursor()
	for row in data:
		#t = list(row(k) for k in ("name","city","salary")) # => list compression
		t = (row["name"], row["city"], row["salary"])
		c.execute('INSERT INTO people VALUES (?,?,?)', t)
		conn.commit()
	conn.close()

def read_db(fname,PEOPLE):
	conn = get_conn(fname)
	c = conn.cursor()
	c.execute("SELECT name, city, salary FROM people")
	"""
	for row in c.fetchall():
		person_d = {
			'name': row['name'],
			'city': row["city"],
			'salary': row["salary"]
			}
		PEOPLE.append(person_d)
	"""
	while True:
		row = c.fetchone()
		if row == None:
			break
		person_d = {
			'name': row['name'],
			'city': row["city"],
			'salary': row["salary"]
			}
		PEOPLE.append(person_d)
	print("Sono presenti:\n")
	for p in PEOPLE:
		print(get_pers_strin(p))
	print("\n")

def save_json(data, fname):
	with open(fname, 'w') as f:
		json.dump(data, f)

def get_csv(data, fname):
	with open(fname, 'wb') as f:
		csv.writer(f, data)

def main_save(argv):
	if len(argv) > 1:
		fname = fname=argv[1]
	else:
		fname = "people.db"
	PEOPLE = main(fname)
	save(PEOPLE,fname)

if __name__ == "__main__":
	main_save(sys.argv)
  

