# uso dizionario come cache per evitare di calcolare sempre
fib_d = {
    0: 0,
    1: 1,
}


def fib(x):
	"""
	Calcola fibonacci con cache su diizonario
	se trova il valore nel dizionario lo restituisce,
	altrimenti lo calcola, lo mette nel dizionario e lo restituisce
	raw_input funzione per passare parametro di input
	choice = raw_input("di quale num vuoi calcolare ? ")
	"""
	if x in fib_d:
		return fib_d[x]
	fib_pre = fib(x-1)
	fib_d[x-1] = fib_pre
	fib_prepre = fib(x-2)
	fib_d[x-2] = fib_prepre
	return fib_pre + fib_prepre

def fib_par():
	choice = raw_input("di quale num vuoi calcolare ? ")
	x = int(choice)
	if x in fib_d:
		return fib_d[x]
	fib_pre = fib(x-1)
	fib_d[x-1] = fib_pre
	fib_prepre = fib(x-2)
	fib_d[x-2] = fib_prepre
	return fib_pre + fib_prepre
	