import sys
import json
import csv

def get_pers_strin(p):
    return "Nome: {name}, Citta': {city}, Stipendio: {salary}".format(**p)

def fun_chiedi(PEOPLE):
	name = raw_input("Quale e' il nome? ")
	city = raw_input("La citta'? ")
	salary = int(raw_input("Lo stipendio? ")) #Gestire se non
	PEOPLE.append({
		'name': name,
		'city': city,
		'salary': salary
		})

def main():
	PEOPLE = [] #list()
	while True:
		fun_chiedi(PEOPLE)
		print("Hai inserito:\n")
		for p in PEOPLE:
			print(get_pers_strin(p))
		print("\n")
		if raw_input("Si desidera inserire altre persone (S/n)? ") in ("N","n"):
			break
		# if raw_input("Si desidera inserire altre persone (S/n)? ").upper  == "N":
		# if raw_input("Si desidera inserire altre persone (S/N)? ").upper not in ["N", "NO"]:
			
	"""
	Ritorna valore boolean
	booContinue = raw_input("Si desidera inserire altre persone (S/N)? ").upper.startswith not in ["N", "NO"]
	La stringa vuota viene considerata FALSE se l'utente inserisce nessun dato viene preso "S"
	#continua = raw_input("Si desidera inserire altre persone (S/N)? ") OR "S"
	"""
	return PEOPLE

def save(lista_people, fname="data.txt"):
	if fname.endswith == "json":
		save_json(lista_people, fname)
	elif fname.endswith == "xls":
		save_xls(lista_people, fname)
	else
		save_txt(lista_people, fname)

def save_txt(data, fname):
	with open(fname, "w") as f:
		for p in lista_people:
			f.write(get_pers_strin(p) + "\n")

def save_json(data, fname):
	with open(fname, 'w') as f:
		json.dump(data, f)

def get_csv(data, fname):
	with open(fname, 'wb') as f:
		csv.writer(f, data)

def main_save(argv):
	PEOPLE = main()
	# print("Lista parametri: {}".format(argv))
	if len(argv) > 1:
		save(PEOPLE,fname=argv[1])
	else:
		save(PEOPLE)
	
if __name__ == "__main__":
	main_save(sys.argv)
  

