
# Capitolo 4 - una nuova speranza...

## Concludere ieri


```python
l = [1,2,3,4, 800, 40, 73, 8]
ll = [x*2 for x in l]
# ll = [2, 4, 6, 8, 1600, 80, 146, 16]

# list(enumerate(l))
{ k: k*2 for k in l }
ll.append("pippo")
zip(l, ll, ll, ll)

{ pippo: v for k,v,pippo in zip(l, ll, ll) }

x,y,z = 1,5,10
```




    {2: 2, 4: 4, 6: 6, 8: 8, 16: 16, 80: 80, 146: 146, 1600: 1600}



### Operatore "is"


```python
import copy
x = [10, 3, 9]
y = copy.copy(x)
print("\n# y = copy.copy(x)")
print("x is y? {}".format(x is y))
print("x == y? {}".format(x == y))
print(id(x), id(y))
```

    
    # y = copy.copy(x)
    x is y? False
    x == y? True
    (57176712L, 61642760L)
    


```python
# Verifica l'identità di un oggetto
x = False
print("x is False? {}".format(x is False))
print(id(x), id(False))

x = 10
print("\nx is 10? {}".format(x is 10))
print(id(x), id(10))

x = [10, 3, 9]
y = x
print("\n# y = x")
print("x is y? {}".format(x is y))
print(id(x), id(y))
      
import copy
x = [10, 3, 9]
y = copy.copy(x)
print("\n# y = copy.copy(x)")
print("x is y? {}".format(x is y))
print("x == y? {}".format(x == y))
print(id(x), id(y))
```

    x is False? True
    (505971624L, 505971624L)
    
    x is 10? True
    (6126144L, 6126144L)
    
    # y = x
    x is y? True
    (60189000L, 60189000L)
    
    # y = copy.copy(x)
    x is y? False
    x == y? True
    (58541768L, 60189064L)
    

### BONUS: stipendi random(!)


```python
import random

r = lambda : int(random.random()*3000)

# Uguale a
# def r():
#     return int(random.random()*3000)

PEOPLE = [
    {"name": "Luca", "city": "Fabriano", "salary": r()},
    {"name": "Simone", "city": "Fabriano", "salary": r()},
    {"name": "Elena", "city": "Mondavio", "salary":r()},
    {"name": "Gianluca", "city": "Senigallia", "salary": r()},
    {"name": "Monica", "city": "Roma", "salary": r()},
{"name": "Sonia", "city": "Bari", "salary": r()},
{"name": "Patrizia", "city": "Bari", "salary": r()},]

PEOPLE
```




    [{'city': 'Fabriano', 'name': 'Luca', 'salary': 587},
     {'city': 'Fabriano', 'name': 'Simone', 'salary': 59},
     {'city': 'Mondavio', 'name': 'Elena', 'salary': 1478},
     {'city': 'Senigallia', 'name': 'Gianluca', 'salary': 851},
     {'city': 'Roma', 'name': 'Monica', 'salary': 531},
     {'city': 'Bari', 'name': 'Sonia', 'salary': 479},
     {'city': 'Bari', 'name': 'Patrizia', 'salary': 2157}]



### Raggruppare gli elementi per città


```python
city_map = {}
for p in PEOPLE:
    city = p["city"]
    city_map[city] = city_map.get(city, [])
    city_map[city].append(p)
    
import pprint
pprint.pprint(city_map)
```

    {'Bari': [{'city': 'Bari', 'name': 'Sonia', 'salary': 479},
              {'city': 'Bari', 'name': 'Patrizia', 'salary': 2157}],
     'Fabriano': [{'city': 'Fabriano', 'name': 'Luca', 'salary': 587},
                  {'city': 'Fabriano', 'name': 'Simone', 'salary': 59}],
     'Mondavio': [{'city': 'Mondavio', 'name': 'Elena', 'salary': 1478}],
     'Roma': [{'city': 'Roma', 'name': 'Monica', 'salary': 531}],
     'Senigallia': [{'city': 'Senigallia', 'name': 'Gianluca', 'salary': 851}]}
    


```python
class DictList(dict):

     def get(self, k, default=None):
         if k not in self:
            self[k] = []
         return super(DictList, self).get(k, default)

     def __getitem__(self, k):
         if k not in self:
            # self[k] = []
            super(DictList, self).__setitem__(k, [])
            
         return super(DictList, self).__getitem__(k)
        
city_map = DictList()
l = city_map.get("pippo")
print(city_map)
```

    {'pippo': []}
    


```python
city_map = DictList()
for p in PEOPLE:
    city = p["city"]
    # city_map[city] = city_map.get(city, [])
    city_map.get(city).append(p)
    
import pprint
pprint.pprint(city_map)
```

    {'Bari': [{'city': 'Bari', 'name': 'Sonia', 'salary': 479},
              {'city': 'Bari', 'name': 'Patrizia', 'salary': 2157}],
     'Fabriano': [{'city': 'Fabriano', 'name': 'Luca', 'salary': 587},
                  {'city': 'Fabriano', 'name': 'Simone', 'salary': 59}],
     'Mondavio': [{'city': 'Mondavio', 'name': 'Elena', 'salary': 1478}],
     'Roma': [{'city': 'Roma', 'name': 'Monica', 'salary': 531}],
     'Senigallia': [{'city': 'Senigallia', 'name': 'Gianluca', 'salary': 851}]}
    

### BONUS: Ordinamento per chiave del dizionario


```python
# def get_name(x):
#    return (x["city"], x["name"]) 
# PEOPLE.sort(key=get_name)

PEOPLE.sort(key=lambda x: (x["city"], x["name"]))

PEOPLE
```




    [{'city': 'Bari', 'name': 'Patrizia', 'salary': 2157},
     {'city': 'Bari', 'name': 'Sonia', 'salary': 479},
     {'city': 'Fabriano', 'name': 'Luca', 'salary': 587},
     {'city': 'Fabriano', 'name': 'Simone', 'salary': 59},
     {'city': 'Mondavio', 'name': 'Elena', 'salary': 1478},
     {'city': 'Roma', 'name': 'Monica', 'salary': 531},
     {'city': 'Senigallia', 'name': 'Gianluca', 'salary': 851}]




```python
PEOPLE.sort(key=lambda x: x["salary"])
PEOPLE
```




    [{'city': 'Fabriano', 'name': 'Luca', 'salary': 3},
     {'city': 'Fabriano', 'name': 'Simone', 'salary': 10},
     {'city': 'Mondavio', 'name': 'Elena', 'salary': 15},
     {'city': 'Senigallia', 'name': 'Gianluca', 'salary': 15},
     {'city': 'Roma', 'name': 'Monica', 'salary': 20},
     {'city': 'Bari', 'name': 'Patrizia', 'salary': 20},
     {'city': 'Bari', 'name': 'Sonia', 'salary': 20}]



### Classi che prendono in input fname


```python
# v. gestionale/managers01/
```


```python
class BaseManager(object):
    def do_export(self, rows):
        self.__privateattr = "PRIVATO"
        print(u"Esporto qualcosa per te")
        rv = self._internal_do_export(rows)
        return rv
    
class FileManager(BaseManager):
    def _internal_do_export(self, rows):
        print(self.__privateattr)
        print(u"ti esporto")
        
class ExtraFileManager(FileManager):
    def _internal_do_export(self, rows):
        print(u"ti esporto extra")

        
mymanager = FileManager()
mymanager.do_export([1,2])
mymanger.__privateattr

```

    Esporto qualcosa per te
    


    ---------------------------------------------------------------------------

    AttributeError                            Traceback (most recent call last)

    <ipython-input-119-a9a4533ad29d> in <module>()
         17 
         18 mymanager = FileManager()
    ---> 19 mymanager.do_export([1,2])
         20 mymanger.__privateattr
    

    <ipython-input-119-a9a4533ad29d> in do_export(self, rows)
          3         self.__privateattr = "PRIVATO"
          4         print(u"Esporto qualcosa per te")
    ----> 5         rv = self._internal_do_export(rows)
          6         return rv
          7 
    

    <ipython-input-119-a9a4533ad29d> in _internal_do_export(self, rows)
          8 class FileManager(BaseManager):
          9     def _internal_do_export(self, rows):
    ---> 10         print(self.__privateattr)
         11         print(u"ti esporto")
         12 
    

    AttributeError: 'FileManager' object has no attribute '_FileManager__privateattr'


## DB-API


```python
# [PEP 249](https://www.python.org/dev/peps/pep-0249/)
# v. gestionale/managers02/db.py
```


```python
class SqliteDBManager(object):
    
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

```


```python
row = PEOPLE[0]
print(row)
s = "ciao ('{name}','{city}','{salary}')"
s.format(**row)

s.format({'salary': 2157, 
          'city': 'Bari', 
          'name': 'Patrizia'})

s.format(name=row["name"], 
         city=row["city"], 
         salary=row["salary"])

```

    {'salary': 2157, 'city': 'Bari', 'name': 'Patrizia'}
    


    ---------------------------------------------------------------------------

    KeyError                                  Traceback (most recent call last)

    <ipython-input-124-654a68f527f7> in <module>()
          6 s.format({'salary': 2157, 
          7           'city': 'Bari',
    ----> 8           'name': 'Patrizia'})
          9 
         10 s.format(name=row["name"], 
    

    KeyError: 'name'


## Esercizio DB-API

1. Fai in modo che il tuo gestionale:
    * inizializzi un tabella PEOPLE su un database sqlite3
    * vi esporti i dati di PEOPLE
2. BONUS: Importa un file json (o altro) all'avvio del tuo programma in modo da precaricare un set di dati in PEOPLE

## Decoratori


```python
def wrappitto(f):
    print("Prima di eseguirti...")
    return f

@wrappitto
def hello(who="a chi?"):
    print("Ciao {}".format(who))

hello()
```

    Prima di eseguirti...
    Ciao a chi?
    


```python
# v. managers03/base.py , decori.py e db.py
```

## Profilazione del codice con i decoratori


```python
from functools import wraps 

def profileme(f):
    start = time.time()
    @wraps
    def wrapper(*args, **kw):
        return f(*args, **kw)
    stop = time.time()
    print("Tempo {} secondi".format(stop-start))
    return wrapper
```

#### v. anche modulo timeit

#### v. memory_profiler di terze parti

* https://pypi.python.org/pypi/memory_profiler
* pip install memory_profiler
* decoratore di funzione @profile

## Unicode, una croce sopra

### mettete sempre la u prima delle stringhe (u"")

v. unicode HowTO nelle references sotto


```python
(u"Papà" + "è")
```


    ---------------------------------------------------------------------------

    UnicodeDecodeError                        Traceback (most recent call last)

    <ipython-input-41-49a710a02967> in <module>()
    ----> 1 (u"Papà" + "è")
    

    UnicodeDecodeError: 'ascii' codec can't decode byte 0xc3 in position 0: ordinal not in range(128)


### Leggere e scrivere files con contenuti Unicode


```python
import codecs

f = codecs.open('unicode.rst', encoding='utf-8', mode='w+')
f.write(u'\u4500 blah blah blah\n')
f.seek(0)
print repr(f.readline()[:1])
f.close()

f = codecs.open('unicode.rst', encoding='utf-8')
for line in f:
    print repr(line)
    
```

    u'\u4500'
    u'\u4500 blah blah blah\n'
    
The most important tip is:

    Software should only work with Unicode strings internally, converting to a particular encoding on output.

```python

```

## Testare con Unittest


```python
# v. modulo unittest
```

## Multithread


```python
# v. modulo threading
```

## References python 2.7

* [IL Tutorial](https://docs.python.org/2.7/tutorial/)
    * [Coding Style](https://docs.python.org/2.7/tutorial/controlflow.html#intermezzo-coding-style)
* [Le funzioni builtins](https://docs.python.org/2.7/library/functions.html) (su ipython >>> ``help(__builtins__))``
* [Gli HowTo](https://docs.python.org/2.7/howto/index.html) (tra cui "Unicode HowTo" e "Idioms and Anti-Idioms in Python")
* [Tipi, operatori e comparazioni](https://docs.python.org/2.7/library/stdtypes.html)
* [String format mini-language](https://docs.python.org/2.7/library/string.html#formatspec)
* [DB-API 2.0 (PEP 249)](https://www.python.org/dev/peps/pep-0249/)
* [Scope delle variabili (blog)](http://www.saltycrane.com/blog/2008/01/python-variable-scope-notes/)
* [Test con PyTest](http://doc.pytest.org/)


```python
phrase = "happy-python-hacking!"
the_end = u" ".join([s.capitalize() for s in phrase.split("-")])

```


```python

```
