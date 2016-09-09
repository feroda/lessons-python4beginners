# -*- coding: utf-8 -*-
#CON CLASSE
class DictList(dict):
    def get(k, default=None):   #OVERRIDE del metodo get della classe padre
        if not default:
            defalut = []
        return super(DictList, self).get(k,defalut) #SUPER richiama il metodo della classe padre -> OVERLOAD

city_map = DictList()
for p in PEOPLE:
    city = p["city"]
    city_map.get(city).append(p)
    
#ORDINAMENTO PER CHIAVE
PEOPLE.sort(key = lambda x: x["name"])  #ordina la lista PEOPLE per la chiave "name"


#SENZA CLASSE
city_map = {}
for p on PEOPLE:
    city = p["city"]
    city_map[city] = city_map.get(city, [])
    city_map[city].append(p)
    