# uso dizionario come cache per evitare di calcolare sempre
PEOPLE = []

def main():
	"""
	devo far inserire name, city, salary come input e salvarli nel dizionario
	# 1.finche utente non smette.
    # 2.l'utente inserisce il nome 
         usa raw_input per chiedere le info all'utente 
    # 3.l'utente inserisce la città
    # 4.l'utente inserisce lo stipendio
    # 5.inserisci il dizionario con chiavi 
         'name','city','salary'
          nella lista PEOPLE = []
    PEOPLE.append(person_d)          
    
    # 6.STAMPA A VIDEO PEOPLE nel modo che ti piace
    # 7.ri-inizia da Step 1
    # FINE 
    
    #----BONUS-----
    #STEP 8.QUANDO L'UTENTE SMETTE --> SCRIVI I DATI IN UN FILE
    #     SE VUOI STEP 8.1 IN FOMRATO JSON
    #     SE VUOI STEP 8.2 IN FORMATO CSV
    #     SE VUOI STEP  8.3 IN FORMATO XML
    # STEP 9. FALLO ANCHE SE L 'UTENTE PREME CTRL+C O CTRL+Z
    

	"""
	cont = True
	while cont:
		cont = insert_person()
	stampa_lista()
	scrivi_file()

def insert_person():
	ret_val = False
	
	nome = get_input("Come ti chiami ? ")
	if nome :
		cit = get_input("Dove vivi ? ")
		if cit :
			salario = get_input("Quanto guadagni mensilmente ? ")
			try:
				salario = int(salario)
			except ValueError:
				print("Salario non valido")
				return False
			if salario :
				persona = {"name":nome , "city" : cit, "salary" : salario }
				PEOPLE.append(persona)
				ret_val = True
				#print(ret_val)
	
	return ret_val
		
def stampa_lista():
  print("Stampo la mia lista... ")
  for x in PEOPLE:
	print("Sig: {name} di {city} guadagna {salary}".format(**x) )

def get_input(msg):
	try:
		ret = raw_input(msg)
	except KeyboardInterrupt:
		ret =''
	return ret	
	
def scrivi_file():	
	print("Scrivo file... ")
	
if __name__ == "__main__":
    main()