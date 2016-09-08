
# dictionary definition
#  1 - not sorted
#  2 - searching for key, not for index
# key : value
d = {1 : "SimoneC", 2 : 'Elena', 3 : 'Gianluca'}

# key : value
pianibaia = {'basso':'Aula Sirene', 'terra': 'Hall'}
stanze_per_piano = pianibaia
stanze_per_piano = {'basso':'Aula Sirene', 'terra': 'Hall', 'basso':'bagno'}

# fibonacci sequence
fib_d = {0:1, 1:1}

def fib(x):
    #doc string
    """
    calcola fibonacci con cache su dizionario

    Se trova il valore nel dizionario lo restituisce, altrimenti lo calcola, lo mette nel dizionario e lo restituisce

    :param x: indice di input richiesto
    :return: numero della sequenza di fibonacci
    """
    if x in (0,1):
        return fib_d[x]

    fib_pre = fib(x-1)
    fib_d[x-1] = fib_pre

    fib_prepre = fib(x-2)
    fib_d[x-2] = fib_prepre

    return fib_pre + fib_prepre

def fib_orig(x):
    if x in (0,1):
        return x
    return fib_orig(x-1) + fib_orig(x-2)

def fib_calcolato(x):
    choice = raw_input("Quale numero vuoi calcolare?")
fibo = fib(35)
