import sqlite3
import os

from .base import BaseManager
from .decori import connectme, debugme

class BaseDBManager(BaseManager):


    def __init__(self, settings, debug=False):
        """Init with db settings and debug mode on/off."""

        self.settings = settings
        super(BaseDBManager, self).__init__(debug=debug)
        self.conn = None

    def close(self):
        self.conn.close()



class SqliteDBManager(BaseDBManager):

    def _init_db(self):

        self.conn = sqlite3.connect(self.settings["name"])
        cu = self.conn.cursor()
        cu.execute("CREATE TABLE people (name VARCHAR(64), city VARCHAR(32), salary INTEGER);")
        self.conn.commit()

    def connect(self):
        """Create a connection to DB."""

        # Initialize the db if does not exists
        # wARNING: lo fa sempre, meglio rendere pubblico il metodo init_db()
        if not os.path.exists(self.settings["name"]):
            self._init_db()
        else:
            self.conn = sqlite3.connect(self.settings["name"])

        self.conn.row_factory = sqlite3.Row

    def get_output(self, rows):
        return "Non sarebbe attendibile"

    @debugme(kind="export")
    @connectme
    def do_export(self, rows):

        cu = self.conn.cursor()

        # KO: Never do this -- insecure!
        # KO: for row in rows:
        # KO:     c.execute("INSERT INTO people VALUES ('{name}','{city}','{salary}')".format(**row))

        # Do this instead
        for row in rows:
            t = (row["name"], row["city"], row["salary"])
            c.execute('INSERT INTO people VALUES (?,?,?)', t)
        self.conn.commit()

    @connectme
    @debugme(kind="import")
    def do_import(self):

        cu = self.conn.cursor()
        cu.execute("SELECT * FROM people")
        return cu.fetchall()




