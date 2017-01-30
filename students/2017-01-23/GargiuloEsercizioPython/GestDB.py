# -*- coding: utf-8 -*-

"""
modulo di gestione DB
"""

import sqlite3 as db

class ObjGestDB(object):
    """
    Incapsula la logica di interazione con il database.

    In questo caso si tratta di un database sqlite.
    """
    
    conn = None
    def __init__(self,fname):
        # questo non è corretto per prendere l'attributo di classe proprio sopra
        # l'__init__. Penso che fosse questa la tua intenzione. O forse no dato che 
        # se istanziato 2 volte connette 2 volte al db.
        # WAS: global conn
        # WAS: conn = db.connect(fname)
        if ObjGestDB.conn is None:
            ObjGestDB.conn = db.connect(fname)
 
    def CloseDB(self):
        ObjGestDB.conn.close()
        ObjGestDB.conn = None  # almeno siamo sicuri che una nuova __init__ funzioni

    def CreaDB(self):
        """
        Crea l'intero db da 0.

        :return: True/False
        """
        
        cu = ObjGestDB.conn.cursor()
        
        #Cancellazione preventiva delle tabelle se queste dovessero essere già presenti !!
        try:
            cu.execute("DROP TABLE PERSONE")
        except:
            pass    
        
        try:
            cu.execute("DROP TABLE CONIGLI")
        except:
            pass        
        
        try:
            cu.execute("CREATE TABLE PERSONE (name VARCHAR(32), city VARCHAR(32), salary INTEGER, genfibo INTEGER)")
        except db.Error:
            # errore: se fai la raise il flusso di esecuzione si interrompe,
            # quindi non arriverai mai alla "return False"
            # puoi decidere di fare una print e poi il "return False"
            raise db.Error(u"Si è verificato un errore nella creazione della tabella PERSONE !!!")
            return False

        try:
            cu.execute("CREATE TABLE CONIGLI (name_person VARCHAR(32), name VARCHAR(32), age INTEGER)")
        except db.Error:
            # stessa cosa
            raise db.Error(u"Si è verificato un errore nella creazione della tabella CONIGLI !!!")
            return False
        return True    


    def RegistraDB(self, rows):
        
        cu = ObjGestDB.conn.cursor()
        
        try:
            # NOTA DB: la DB-API supportata dal modulo sqlite3 supporta l'esecuzione ottimizzata
            # di più query con la execute_many()
            # Questo va un po' oltre il corso, ma comunque ti suggerisco di dargli un'occhiata
            # https://docs.python.org/2/library/sqlite3.html#sqlite3.Cursor.executemany
            for row in rows:
                t = (row["name"], row["city"], row["salary"],row["genfibo"])
                cu.execute('INSERT INTO PERSONE VALUES (?,?,?,?)', t)
                for rowchild in row["conigli"]:
                    c = (row["name"],rowchild["name"], rowchild["age"])
                    cu.execute('INSERT INTO CONIGLI VALUES (?,?,?)', c) 
        except db.Error:
            # ERRORE: qui non farai quindi nemmeno mai il rollback se si verifica un db.Error :(
            raise db.Error(u"Si è verificato un errore nell'inserimento del Record !!!") 
            ObjGestDB.conn.rollback()
            return False
        
        ObjGestDB.conn.commit()
        return True

        


