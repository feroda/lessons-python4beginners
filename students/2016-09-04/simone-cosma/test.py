import io
import csv

toCSV = [{'name':'bob','age':25,'weight':200},
         {'name':'jim','age':31,'weight':180}]
keys = toCSV[0].keys()
print keys
f = io.BytesIO()
dict_writer = csv.DictWriter(f, keys)
dict_writer.writeheader()
dict_writer.writerows(toCSV)

print f.getvalue()