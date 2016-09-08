# Esercizio successione di Fibonacci

def fib_from_string(_id):
    fib_serie = "0 1 1 2 3 5 8"
    int_id = int(_id)
    if int_id < 0:
        raise ValueError("ERR: indice negativo: {}" .format(int_id))
    return int(fib_serie.replace(" ", "")[int(int_id)])

def fib_from_list(_id):
    fib_serie = [0,1,1,2,3,5,8]
    int_id = int(_id)
    if _id < 0:
        raise ValueError("ERR: indice negativo: {}" .format(int_id))
    return int(fib_serie[int(int_id)])

def fib_from_algo(_id):
    # cast index from string to int
    int_id = int(_id)
    if _id < 0:
        raise ValueError("ERR: indice negativo: {}" .format(_id))

    fib_serie=[0,1,1]
    # Posso sostituire range con xrange
    for f in range(2, int_id):
        fib_serie.append(fib_serie[-1] + fib_serie[-2])
    print("DBG: fib_serie {}" .format(fib_serie))
    return int(fib_serie[int_id])

