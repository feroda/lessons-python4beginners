# -*- coding: utf-8 -*-

import unittest
import sqlite3 as db
from GestDB import ObjGestDB

class TestGestioneDB(unittest.TestCase):
       
    def setUp(self):
        self.dbrows = [
            {"name": "Gianni", "city": "Napoli", "salary": 3000, "genfibo": 5,
            "conigli": [{"name": "coniglio1_Gianni", "age": 3}, {"name": "coniglio2_Gianni", "age": 8}, {"name": "coniglio3_Gianni", "age": 4}]},
            {"name": "Fabio", "city": "Ascoli", "salary": 300, "genfibo": 8,
            "conigli": [{"name": "coniglio1_Fabio", "age": 10}, {"name": "coniglio2_Fabio", "age": 6}]}
        ]


    def test_saveDB(self):
        gestidb = ObjGestDB("C:/DBPersone.db")
        
        self.assertTrue(gestidb.CreaDB())
        self.assertTrue(gestidb.RegistraDB(self.dbrows))
        
        gestidb.CloseDB()
        

if __name__ == '__main__':
    unittest.main()