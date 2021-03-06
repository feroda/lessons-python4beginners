# -*- coding: utf-8 -*-

import sqlite3
import os

from base import BaseManager

class BaseDBManager(BaseManager):


    def __init__(self, settings, debug=False):
        """Init with db settings and debug mode on/off."""

        self.settings = settings #Settings nella sua idea � un dizionario.
        super(BaseDBManager, self).__init__(debug=debug)
        self.conn = None

    def close(self):
        self.conn.close()

    def do_export(self, rows):

        self.debug_export(rows)
        self.connect()
        self._do_export(rows)
        self.close()

    def do_import(self):

        self.connect()
        rows = self._do_import()
        self.close()
        self.debug_import(rows)



class SqliteDBManager(BaseDBManager):

    def _init_db(self):
        self._connect()
        cu = self.conn.cursor()
        cu.execute("CREATE TABLE people (name VARCHAR(64), city VARCHAR(32), salary INTEGER);")
        self.conn.commit()
        
    def _connect(self): #Mettiamo la connessione qu� cos� che non devo ripeterla nella classe, per� sconsigliamo a chi mi usa da fuori di usare questo metodo
        self.conn = sqlite3.connect(self.settings["name"])

    def connect(self):
        """Create a connection to DB."""

        # Initialize the db if does not exists
        # WARNING: lo fa sempre, meglio rendere pubblico il metodo init_db()
        if not os.path.exists(self.settings["name"]):
            self._init_db()
        else:
            self._connect()

        self.conn.row_factory = sqlite3.Row #Questo serve per fare in modo che i record restituiti dalla fetchAll siano sottoforma di dizionario con chiave.

    def get_output(self, rows):
        return "Non sarebbe attendibile"

    def _do_export(self, rows):

        cu = self.conn.cursor()

        # KO: Never do this -- insecure!
        # KO: for row in rows:
        # KO:     c.execute("INSERT INTO people VALUES ('{name}','{city}','{salary}')".format(**row))

        # Do this instead
        for row in rows:
            t = list((row[k] for k in (row["name"], row["city"], row["salary"])))
            cu.execute('INSERT INTO people VALUES (?,?,?)', t) #Il QUOTING deve farlo la libreria e non noi se no � un macello!!
        self.conn.commit()

    def _do_import(self):

        cu = self.conn.cursor()
        cu.execute("SELECT * FROM people")
        return cu.fetchall()