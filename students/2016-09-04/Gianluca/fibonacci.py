
def fib_from_string_semplice(x):
  s = "0112358"
  if x < 0:
    raise ValueError("Non accetta valori negativi") 
  try:
    return int(s[x])
  except IndexError:
    raise NotImplementedError("Non implementata")
    
def fib_from_string(x):
  stringa = "0112358"
  if type(x) == type(''):
    raise TypeError
  elif x < 0:
    raise ValueError("Non accetta valori negativi") 
  elif x > 6:
    raise NotImplementedError("Non implementata")
  else:
    return int(stringa[x])
  
def fib_from_lista(x):
  lista = [0,1,1,2,3,5,8]
  if type(x) == type(''):
    raise TypeError
  elif x < 0:
    raise ValueError("Non accetta valori negativi") 
  elif x > 6:
    return 0
  else:
    return lista[x]
  
def fib_algo(x):
  if type(x) == type(''):
    raise TypeError
  elif x < 0:
    raise ValueError 
  elif x == 0:
    return 0
  elif x == 1:
    return 1
  else:
    return fib_algo(x-1) + fib_algo(x-2)
  
def fib_algo2(x):
  fib_serie=[0,1]
  for i in range(1,x): # al posto di i e' possibile usare _ convenzione per una variabile che non usero' mai
    fib_serie.append = fib_serie(-1) + fib_serie(-2)
  return int(fib_serie(x))

fib_d = {
  0 : 0, 
  1 : 1
}
def fib_dict(x):
  """
  Calcola fibonacci con cache
  """
  if x in fib_d:
    return fib_d(x)
    
  fib_d[x-1], fib_d[x-2] = fib_dict(x-1), fib_dict(x-2)
  return fib_d[x-1] + fib_d[x-2]

  
fib = fib_dict

if __name__ == "__main__": #Necessario per non farlo eseguire quando viene fatto IMPORT 
  num = raw_imput("Che numero vuoi calcolare?")
  fib(int(num))
    
