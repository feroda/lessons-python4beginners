# -*- coding: utf-8 -*-

# This is hello_who_3.py
import sys                            # <-- importo un modulo


def compose_hello(who, force=False):   # <-- valore di default
    """
    Get the hello message.

        :param str who: the person to say Hello
        :param bool force: force message for non-string input
        :return: the message
        :rtype: str
        :raises ValueError: who is not a string
    """
    
    try:                                     # <-- gestione eccezioni `Duck Typing` 
        message = "Hello " + who + "!"
    except TypeError:                       # <-- eccezione specifica
    # except ValueError as e:                       # <-- eccezione specifica su parametro e
        print("[WARNING] Il parametro `who` dovrebbe essere una stringa")
        if force:                            # <-- controllo "if"
            message = "Hello {}!".format(who)
        else:
            raise                            # <-- solleva eccezione originale
            # raise e                        # <-- solleva la stessa eccezione, ma qui 
            # raise MyMessageError("dire ciao e' semplice")  # <-- solleva la tua eccezione
    return message


def hello(who='world'):               # <-- valore di default
    """
    Say the hello message.

        :param str who: The person to say Hello
    """
    print(compose_hello(who))
    

if __name__ == "__main__":
    hello("mamma")


