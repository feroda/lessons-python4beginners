

def main():
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
    
    

PEOPLE =[]

def main():
    scelta = True 
    while scelta:
    
        nome = raw_input("Nome? ")
        citta = raw_input("Cognome? ")
        salario = raw_input("Salario? ")
        d = { "name": nome , "city": citta , "salary": salario }
        PEOPLE.append(d)
    
        scelta = raw_input("Continui o no? ")
        if scelta.lower() in ('n','no'):
            scelta = False
    
        for x in PEOPLE:
            print(x)
        #    print("Nome: {name}".format(name=x["name"])
            print("Nome: {name}".format(**x)
            
c = raw_input("\nInserisci [NOME/1 / CITTA/2 / SALARIO/3 ] ? ")
 
    
    