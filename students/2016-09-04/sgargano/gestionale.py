PEOPLE = []
def main():
    want_continue = True
    while want_continue:
        name = raw_input("Nome?")
        city = raw_input("City?")
        salary = int(raw_input("Salary?"))
        
        PEOPLE.append({
            'name': name,'city':city,'salary':salary })
        print ("Hai inserito")
        for p in PEOPLE:
            print("Nome:{name}, City: {city}, Stipendio: {salary}".format(**p))
 #       choice = raw_input("Vuoi continuare [y/n] ") or "Y"
 
        a = raw_input("Vuoi continuare [y/n] ").upper()
        want_continue = a not in ["N","NO"]
        # oopure want_continue = a != "N"
 #        if(choice.upper[0]=="N")
 #            choice = False
            
if __name__== "__main__":
    main()
