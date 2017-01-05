# -*- coding: utf-8 -*-

import csv
import json

class BaseExporter(object):
    def __init__(self, f, debug = False):
        self.f = f
        self.debug = debug
        
    def do_export(self, rows):
        raise NotImplementedError("To be implemented in subclasses!")
        
        
        

class FileExporter(BaseExporter):

    def do_export(self, rows):
    
        for row in rows:
            output = "{}\n".format(row)
            if self.debug:
                print(output)
            else:
                self.f.write("{}\n".format(row))
            
            
            
class JsonExporter(BaseExporter):
    def do_export(self, rows):
        
        if self.debug:
            print(json.dumps(rows, indent=2))
        else:
            json.dump(rows, self.f, indent = 2)
        
 
class CsvExporter(BaseExporter):
    def do_export(self, rows):
        if self.debug:
            raise NotImplementedError("TODO")
    
        fieldnames = rows[0].keys()
        
        writer = csv.DictWriter(self.f, fieldnames = fieldnames, delimiter = ";")

        writer.writeheader()
        
        for row in rows:
            writer.writerow(row)
            
"""   
Un piccolo esempio..
         
BACKENDS_MAP = {
    "son" : JsonExporter,
    "csv" : CsvExporter
}

def apply_exortation_from_file(fname, data):
    ext = fname[-3:] #Leggi gli ultimi 3 caratteri!!
    xp_klass = BACKENDS_MAP.get(ext)
    
    xp = xp_klass(f)
    xp.do_export(data)
    
"""