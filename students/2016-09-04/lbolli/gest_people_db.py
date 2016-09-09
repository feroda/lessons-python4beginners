import json
import sqlite3

def main():
    f = open('lbolli.json', 'r')
    stringa = f.read()
    lista = json.loads(stringa)

    print(lista)

    conn = sqlite3.connect('lbolli.sqlite')
    cu = conn.cursor()
    str_sql = u'CREATE TABLE IF NOT EXISTS people (name VARCHAR(100), city VARCHAR(100), salary INTEGER, annual INTEGER)'
    print(str_sql)
    cu.execute(str_sql)

    str_sql = u"INSERT INTO people (name, city, salary, annual) VALUES ('{}', '{}', {}, {})"
    for l in lista:
        #for k, v in l.intems(): # altra possibilità di iterare sul dizionario
        t = list(l[k] for k in ("name", "city", "salary", "annual"))
        str_sql2 = str_sql.format(t[0], t[1], t[2], t[3])
        print(str_sql2)
        cu.execute(str_sql2)

    conn.commit()
    conn.close()


if __name__ == "__main__" :
	main()

