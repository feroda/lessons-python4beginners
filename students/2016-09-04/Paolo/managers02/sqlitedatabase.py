import os
import sqlite3

class SqliteDatabase(object):
    def __init__(self, file_name):
        self.file_name = file_name
        
        self.conn = sqlite3.connect(file_name)
        self.conn.row_factory = sqlite3.Row

        cursor = self.conn.cursor()
        
        if not os.path.exists(file_name):
            cursor.execute("CREATE TABLE people (name VARCHAR(64), city VARCHAR(32), salary INTEGER);")
            
    def write(self, list):
        cursor = self.conn.cursor()
        
        for row in list:
            t = (row["name"], row["city"], row["salary"])
            cursor.execute('INSERT INTO people VALUES (?,?,?)', t)
            
    def read_all(self):
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM people")
        return cursor.fetchall()
        
    def commit(self):
        self.conn.commit()
        
    def close(self):
        self.conn.close()