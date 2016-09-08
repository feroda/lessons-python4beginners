import json
import csv

class BaseExporter(object):
    def __init__(self, f, debug = False):
        self.f = f
        self.debug = debug
    def do_export(self, rows):
        raise NotImplementedError("Implementato nelle sottoclassi!")
    def do_import(self):
        raise NotImplementedError("Implementato nelle sottoclassi!")  
        
    
class DebugExporter(BaseExporter):
    def do_export(self, rows):
        for row in rows:
            print("{}".format(row))
            
xp = DebugExporter()
l2 = [1,2,3,4,10,200,30]
xp.do_export(rows=l2) #scrive ciascun elemento della lista separato da una riga vuota


class FileExporter(BaseExporter):
    def do_export(self, rows):
        for row in rows:
            output = "{}\n".format(row)
            if self.debug:
                print(output)
            else:
                f.write(output)
                
            
xp = Exporter()
l2 = [1,2,3,4,10,200,30]
with open("a.txt", "wb") as f
xp.do_export(rows=l2) #scrive ciascun elemento della lista separato da una riga vuota


class JsonExporter(BaseExporter):
    def do_export(self, rows):
            if self.debug:
                print(json.dump(rows, indent = 2))
            else:
                json.dump(rows, self.f, indent = 2)
    
    def do_import(self):
        return(json.dump(rows, self.f))
            

class CsvExporter(BaseExporter):
    def do_export(self, rows):
        fieldnames = row[0].keys()
        writer = csv.DictWriter(self.f, fieldnames = fieldnames, delimiter = ";")         
        writer.writeheader()
        for row in rows:
            if self.debug:
                print(writer.writerow(row))
            else:
                writer.writerow(row)
                
                
def apply_exportation(xp, fname, data):
    with open(fname, "wb") as f:
        xp.do_export(rows = data)