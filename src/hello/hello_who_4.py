# -*- coding: utf-8 -*-

# This is hello_who_4.py
import sys                            # <-- importo un modulo
import random
import time


def compose_hello(who, force=True):   # <-- valore di default
    """
    Get the hello message.

        :param str who: the person to say Hello
        :param bool force: force message for non-string input
 TODO       :type priority: integer or None
        :return: the message
        :rtype: str
        :raises TypeError: who is not a string
    """
    
    try:                                     # <-- gestione eccezioni `Duck Typing` 
        message = "Hello " + who + "!"
    except TypeError:                       # <-- eccezione specifica
    # except TypeError as e:                       # <-- eccezione specifica su parametro e
        print("[WARNING] Il parametro `who` dovrebbe essere una stringa")
        if force:                            # <-- controllo "if"
            message = "Hello {}!".format(who)
        else:
            raise                            # <-- solleva eccezione originale
            # raise e                        # <-- solleva la stessa eccezione, ma qui 
            # raise MyMessageError("dire ciao e' semplice")  # <-- solleva la tua eccezione
    return message


def get_random_names():
    return ['a','b','c']  # TODO


def hello_many(names):
    """
    Say hello many times in many modes
    
    """
    for name in names:
        print(compose_hello(name))

    print("\n# Ora li scrivo numerandoli, con pause")
    for i, name in enumerate(names, 1):
        print("[{:>2}] {}".format(i, name))  
        time.sleep(0.5)

    # Se si vuole modificare la lista durante l'iterazione
    # si raccomanda di iterare su una copia e si può fare
    # con l'operatore slice [:]
    for n in names[:]:
        if n[0] > 'l':
            names.remove(n)
            names.append(n)

    print("\n# In fondo quelli sopra la 'l': {}".format(names))

    print("\n# Ora svuoto names")
    while names:
        print(names.pop()) 

    print("\n# Finito")


def main(argv):  
    """
    Ask for names and say many hello.
    
    If the "random" parameter is passed then names are chosen randomly

        :param str argv: Parameters passed in command line
    """

    is_random = False
    if len(argv) > 1:
        is_random = argv[1] == "random"
        if not is_random:
            print("Usage: {0} [random]".format(argv))
            sys.exit(100)

    if is_random:
        names = get_random_names()
    else:
        names = []
        while True:
            x = raw_input("Give me a name [<enter>,_,BASTA to finish] ? ")
            if x.upper() not in ['', '_','BASTA']:
                names.append(x)
            else:
                break

    hello_many(names)

if __name__ == "__main__":
    main(sys.argv)

