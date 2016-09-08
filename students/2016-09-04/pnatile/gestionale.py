import sys
import json
import csv

def get_person_str(p):
	return 	"Nome: {name}, city: {city}, stipendio: {salary}".format(**p)

def main():
	PEOPLE = []
	"""
	invece di fare così
	want_continue = True
	while want_continue:
	e testare sempre want_continue
	
	posso fare 
	while True:
	e all'interno del ciclo
	if not want_continue
		break
	"""
	#want_continue = True
	#while want_continue:
	while True:
		name = raw_input("Name ? ")
		city = raw_input("City ? ")
		salary = raw_input("Salary ? ")
		
		PEOPLE.append({
			'name':name,
			'city':city,
			'salary':salary
		})
	
		for p in PEOPLE:
			get_person_str( p)
		#want_continue = raw_input("Vuoi continuare [y/n] ?").upper() or "N"  #se l'utente non inserisce nulla si prende il default "N"
		a = raw_input("Vuoi continuare [Y/N] ?").upper() 
		#want_continue = a not in ["N", "NO"]
		if a in ["N", "NO"]:
			break
		# oppure want_continue = a !="N"
		#if want_continue not in ["N", "NO"]
		#if choice.upper().startWith("N")
		# if choice and choice.upper()[0] == "N"
	return PEOPLE

	
def get_json(data):
	"""
	json.dump metodo che ha in input già il file
	json.dumps ha in input una list
	json.load carica file
	json.loads carica stringa
	"""
	return json.dumps(data, indent = 2)

def save_csv(list_of_dicts,f):
	writer= csv.writer(f, delimiter=';')
	writer.writerow(["NAME","CITY","SALARY"])  #riga intestazione
	for p in list_of_dicts:
		writer.writerow( [ p["name"],p["city"],p["salary"] ])
	

def save(list_of_dicts, fname="data.txt"):
	"""
	# abbiamo bisogno di salvare PEOPLE su file
	# operazioni su file si fanno con with
	with apre e chiude il file
	save data in many formats depending on the filename extension
	"""
	
		
	with open(fname, "wb") as f:
		if fname.endswith(".json"):
			f.write(get_json(list_of_dicts))
		elif fname.endswith(".csv"):
			save_csv(list_of_dicts,f)
		else :	
			for p in list_of_dicts:
				f.write(get_person_str(p)+"\n")
	
	
def main_and_save(argv)	:
	PEOPLE = main()
	print("Lista parametri: {}".format(argv))
	if len(argv)>1:
		save(PEOPLE, fname=argv[1])
	else:	
		save(PEOPLE)
	
	
if __name__ == "__main__":
    main_and_save(sys.argv)