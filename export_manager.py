import types
import codecs
import json
import csv


class BaseExporter(object):
    
    def __init__(self, f=None):
        
        self._to_be_closed = True
        if f == None:
            self.f = self._open("exports.txt")
        elif isinstance(f, types.StringTypes):
            self.f = self._open(f)
        else:
            self.f = f
            self._to_be_closed = False
    
    def _open(self, fname):
        return codecs.open(fname, encoding="utf-8", mode="w+")

    def do_export(self, people):
        pass
    
    def get_exported_content(self):
        self.f.seek(0)
        return self.f.read()

class AllReprExporter(BaseExporter):
    
    def do_export(self, people):
        self.f.write(repr(people))

class LineByLineExporter(BaseExporter):
    
    def do_export(self, people):
        all_reprs = [ repr(x) for x in people ]
        self.f.writelines(all_reprs)

class JsonExporter(BaseExporter):
    
    def do_export(self, people):
        json.dump(people, self.f)


class CsvExporter(BaseExporter):
    
    def do_export(self, people):
        
        fieldnames = people[0].keys()
        writer = csv.DictWriter(
            self.f, fieldnames=fieldnames, delimiter=";")
        writer.writeheader()
        
        for row in people:
            writer.writerow(row)


class ExporterFactory(object):
    
    EXPORTERS_D = {
        "csv": CsvExporter,
        "json": JsonExporter,
        "lbl": LineByLineExporter,
        "all": AllReprExporter
    }

    @property
    def supported(self):
        return self.EXPORTERS_D.keys()

    def get_instance(self, backend, f=None):
        return self.EXPORTERS_D[backend](f)
