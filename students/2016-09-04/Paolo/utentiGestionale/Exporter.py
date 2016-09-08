# -*- coding: utf-8 -*-

import csv

class Exporter(object):

    def __init__(self, name):
        self.name = name

    def do_export(self, f, rows):
    
        for row in rows:
            f.write("{}\n".format(row))
            
            
            
class JsonExporter(object):
    def do_export(self, f, rows):
        json.dump(rows, f, indent = 2)
        
 
class CsvExporter(object):
    def do_export(self, f, rows):
    
        fieldnames = rows[0].keys()
        
        writer = csv.DictWriter(f, fieldnames = fieldnames, delimiter = ";")

        writer.writeheader()
        
        for row in rows:
            writer.writerow(row)