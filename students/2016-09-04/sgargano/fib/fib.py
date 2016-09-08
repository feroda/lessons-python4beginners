
lista = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89,144]

 
def fib_from_string(x):
    
    if x < 0 :
       raise ValueError("indice negativo ({})  non funziona".format(x))
    elif x <= 6:
        s = "0112358"
        return int(s[x])
    else:
        raise NotImplementedError(
        "Non sono stato capace da 7 in su")
		
def fib_from_list(x):
    if x < 0:
         raise ValueError("indice negativo ({})  non funziona".format(x))
    return lista[x]

def fib_algo(x):
    if x < 0:
        raise ValueError("indice negativo ({})  non funziona".format(x))
    elif x == 0 or x == 1:
        return x
    else:
	    return fib_algo(x-1) + fib_algo(x-2)

def fib_algo_lb(i):
    fib_serie = [0, 1]
    print("range ={}".format(range(1,i)))
    for f in range(1,i):
        fib_serie.append(fib_serie[-1] + fib_serie[-2])
    print(fib_serie)
    return int(fib_serie[i])


def liste_sonia():
    l2= [1, 2,3 , 4]
    l3 =[]
    for x in l2:
        l3.append(x*2)


def prova_listCOMP():
    l2=[1,2,3,4,7,9,70,80,6,44]
    l3 = [x*2 for x in l2]
    print ("Prova {}".format(l3))
    l3 = [x*2 for x in l2 if x>10]
    print ("Prova {}".format(l3))

fib = fib_algo_lb	
if __name__== "__main__":
	rv=fib()
	print("valore ottenuto {}".format(rv))

   