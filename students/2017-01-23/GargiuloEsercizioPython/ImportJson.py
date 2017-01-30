# -*- coding: utf-8 -*-

"""
modulo di importazione di un file json in un DB
"""

import sqlite3 as db
import codecs
from GestDB import ObjGestDB
import json

def importJson():

    # vedi ExportJson sul C:/
    with codecs.open("C:/Persone.json", encoding="utf-8", mode="r") as f:
        db=json.load(f)
    
    gestidb = ObjGestDB("C:/DBPersone.db")
    
    try:
        if gestidb.CreaDB():
            gestidb.RegistraDB(db)
    except db.Error as e:
        # WAS: print(u"si è verificato il seguente errore:" + e[0] )
        # devi usare la formattazione di una stringa che converte il valore in stringa
        print(u"si è verificato il seguente errore: {}".format(e))
    except:
        pass

    gestidb.CloseDB()  

if __name__ == "__main__":
    importJson()
