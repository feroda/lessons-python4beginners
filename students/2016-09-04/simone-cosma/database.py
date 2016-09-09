import sqlite3
import os


class DBManager(object):

    def __init__(self, filename):
        self.filename = filename

    def _init_db(self):
        self._connect()
        cu = self.conn.cursor()
        cu.execute("CREATE TABLE people (name VARCHAR(64), city VARCHAR(32), salary INTEGER);")
        self.conn.commit()

    def _connect(self):
        self.conn = sqlite3.connect(self.filename)

    def connect(self):
        print(self.filename)
        # Initialize the db if does not exists
        if not os.path.exists(self.filename):
            self._init_db()
        else:
            self._connect()
        self.conn.row_factory = sqlite3.Row

    def save(self, rows):
        cu = self.conn.cursor()
    
        elements = [(e['name'], e['city'], e['salary']) for e in rows ]
        # Do this instead
        cu.executemany('INSERT INTO people VALUES (?,?,?)', elements)
        self.conn.commit()
    
    def load(self):
        cu = self.conn.cursor()
        cu.execute('SELECT name, city, salary FROM people')
        return cu.fetchall()
    
    def close(self):
        self.conn.close()