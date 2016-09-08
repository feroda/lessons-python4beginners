PEOPLE = [] 

def StampaAnag():
  for x in PEOPLE:
    print("Nome: {name}, Citta': {city}, Stipendio: {salary}".format(**x))
    
def fun_chiedi():
  person_d = {}
  nome = raw_input("Quale e' il nome? ")
  citta = raw_input("La citta'? ")
  stipendio = raw_input("Lo stipendio? ")  
  person_d["name"] = nome
  person_d["city"] = citta
  person_d["salary"] = stipendio
  PEOPLE.append(person_d)
  StampaAnag()
  print("\n")
  continua = raw_input("Si desidera inserire altre persone (S/N)? ")
  if continua in ("S","s"):
    return "S"
  else:
    return "N"
    
def main():
  risp = "S"
  while risp == "S":
    risp = fun_chiedi()
    
if __name__ == "__main__":
  main()

