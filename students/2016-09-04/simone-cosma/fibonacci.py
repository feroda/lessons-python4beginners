def _checkInput(index):
    if index < 0:
        raise ValueError("Indice negativo non supportato [{}]".format(index))
    elif type(index) != int:
        raise TypeError("Inserire un intero [tipo input {}]".format(type(index).__name__))

def fib_from_string(index):
    _checkInput(index)
    serie = "0 1 1 2 3 5 8".replace(" ", "")
    return int(serie[index])

def fib_from_list(index):
    _checkInput(index)
    serie = [0,1,1,2,3,5,8]
    return serie[index]

def fib_from_algo(index):
    _checkInput(index)
    current_number = current_index = 0
    base = 1

    while current_index < index:
        old_base = current_number
        current_number = current_number + base
        base = old_base
        current_index += 1
        pass
    
    return current_number
    
def recursion(index):
    if index <= 1:
        return index
    return recursion(index - 1) + recursion(index - 2)
    
def fib_from_recursion_func(index):
    _checkInput(index)    
    return recursion(index)


calculate = fib_from_recursion_func