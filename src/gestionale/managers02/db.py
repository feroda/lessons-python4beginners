import sqlite3
import os

from .base import BaseManager

class BaseDBManager(BaseManager):


    def __init__(self, settings, debug=False):
        """Init with db settings and debug mode on/off."""

        self.settings = settings
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

    def _connect(self):
        self.conn = sqlite3.connect(self.settings["name"])

    def connect(self):
        """Create a connection to DB."""

        # Initialize the db if does not exists
        if not os.path.exists(self.settings["name"]):
            self._init_db()
        else:
            self._connect()

        self.conn.row_factory = sqlite3.Row

    def get_output(self, rows):
        return "Non sarebbe attendibile"

    def _do_export(self, rows):

        cu = self.conn.cursor()

        # KO: Never do this -- insecure!
        # KO: for row in rows:
        # KO:     c.execute("INSERT INTO people VALUES ('{name}','{city}','{salary}')".format(**row))

        # Do this instead
        for row in rows:
            t = (row["name"], row["city"], row["salary"])
            cu.execute('INSERT INTO people VALUES (?,?,?)', t)
        self.conn.commit()

    def _do_import(self):

        cu = self.conn.cursor()
        cu.execute("SELECT * FROM people")
        return cu.fetchall()