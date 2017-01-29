# -*- coding: utf-8 -*-

"""
modulo di gestione DB
"""

import sqlite3 as db

class ObjGestDB(object):
    
    conn = None
    def __init__(self,fname):
        global conn
        conn = db.connect(fname)
 
    def CloseDB(self):
        global conn
        conn.close()
    
    def CreaDB(self):
        #return true/false
        global conn
        cu = conn.cursor()
        
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
            raise db.Error(u"Si è verificato un errore nella creazione della tabella PERSONE !!!")
            return False

        try:
            cu.execute("CREATE TABLE CONIGLI (name_person VARCHAR(32), name VARCHAR(32), age INTEGER)")
        except db.Error:
            raise db.Error(u"Si è verificato un errore nella creazione della tabella CONIGLI !!!")
            return False
        return True    

    def RegistraDB(self,rows):
        global conn
        cu = conn.cursor()
        
        try:
            for row in rows:
                t = (row["name"], row["city"], row["salary"],row["genfibo"])
                cu.execute('INSERT INTO PERSONE VALUES (?,?,?,?)', t)
                for rowchild in row["conigli"]:
                    c = (row["name"],rowchild["name"], rowchild["age"])
                    cu.execute('INSERT INTO CONIGLI VALUES (?,?,?)', c) 
        except db.Error:
            raise db.Error(u"Si è verificato un errore nell'inserimento del Record !!!") 
            conn.rollback()
            return False
        
        conn.commit()
        return True

        


