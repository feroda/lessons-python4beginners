# -*- coding: utf-8 -*-

# funzione che saluta
def do_hello(who):
    print (u"Ciao {}" .format(who))
    """
    Say the hello message.

    :param str who: the person who say hello
    """
    print (compose_hello("Mario", force=True))
    
def compose_hello(who, force=True):
    """
    Get the hello message
    :param str who: The person who say hello
    :param bool force: force message for non-string input
    :return: the message
    :raises TypeError: who is not a string
    """

    try: "Hello" + who + "!"
    except TypeError:
        print("[WARNING] Il parametro 'who' dovrebbe essere una stringa")
        if force:
            message = "Hello {}!".format(who)
        else:
            raise
            # raise e                          # <-- solleva eccezione originale
            # raise MyMessageError("dire ciao e' semplice")  # <-- solleva
    except Exception:
        print("Verificatasi eccezione non prevista")
    else:
        print("Nessuna eccezione")
    finally:
        print("Bye")

    return message


if __name__ == "__main__":
    do_hello("ciccio")