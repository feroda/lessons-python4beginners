def fib_from_string(x):
    s = "0112358"
    if (x < 0 or x > 7):
	    print ("Valore non consentito")
    else:
        return int(s[x])
		
def fib_from_list(x):
    lista = [0, 1, 1, 2, 3, 5, 8]
    if (x < 0 or x > 7):
        print ("Valore non consentito")
    else:
	    return lista[x]

def fib_algo(x):
    if x == 0 or x == 1:
        return 1
    elif x < 0:
	    print ("Valore non consentito")
    else:
	    return fib_algo(x-1) + fib_algo(x-2)


fibString = fib_from_string
fibList = fib_from_list
fibAlgo = fib_algo

	
if __name__== "__main__":
	rv=fibString(-1)
	print("valore ottenuto {}".format(rv))
	rv=fibList(-1)
	print("valore ottenuto {}".format(rv))
	rv=fibAlgo(30)
	print("valore ottenuto {}".format(rv))
   