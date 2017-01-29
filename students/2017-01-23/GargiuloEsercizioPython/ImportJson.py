# -*- coding: utf-8 -*-

"""
modulo di importazione di un file json in un DB
"""

import sqlite3 as db
import codecs
from GestDB import ObjGestDB
import json

def importJson():
    with codecs.open("C:/Persone.json", encoding="utf-8", mode="r") as f:
        db=json.load(f)
    
    gestidb = ObjGestDB("C:/DBPersone.db")
    
    try:
        if gestidb.CreaDB():
            gestidb.RegistraDB(db)
    except db.Error as e:
        print(u"si è verificato il seguente errore:" + e[0] )
    except:
        pass

    gestidb.CloseDB()  

if __name__ == "__main__":
    importJson()
