# -*- coding: utf-8 -*-
def do_hello(name=u"mondo"):
    """
    Metodo che saluta
    :param str name: nome di chi salutare
    """
    print(u"Ciao {}!".format(name))

import this

if __name__ == "__main__":
    do_hello()