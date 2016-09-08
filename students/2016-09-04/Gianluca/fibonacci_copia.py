
def fib_from_string(x):
  stringa = "0112358"
  if x > 6 or x < 1:
    return 0
  else:
    return stringa(x)
  
def fib_from_lista(x):
  lista = [0,1,1,2,3,5,8]
  if x > 6 or x < 1:
    return 0
  else:
    return lista(x)
  
def fib_algo(x):
  if x == 0:
    return 1
  return fib_algo(x-1) + fib_algo(x-2)

fib = fib_from_string

if __name__ == "__main__":
    fib(0)
    
