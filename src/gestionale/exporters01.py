import json
import csv


# Esempio di preparazione dati

# people_fname = r"c:\Users\gigi\lessons-python4beginners\src\gestionale\people_fixture.json"
# with open(people_fname, "rb") as fpeople:
#     PEOPLE = json.load(fpeople)
# outfname = r"c:\Users\gigi\a.txt"


class DebugExporter(object):
    def do_export(self, f, rows):
        for row in rows:
            print("{}".format(row))
            
class Exporter(object):
    def do_export(self, f, rows):
        for row in rows:
            f.write("{}\n".format(row))

class JsonExporter(object):
    def do_export(self, f, rows):
        json.dump(rows, f, indent=2)


class CsvExporter(object):
    def do_export(self, f, rows):
        
        fieldnames = rows[0].keys()
        writer = csv.DictWriter(
            f, fieldnames = fieldnames, delimiter = ";")
        writer.writeheader()
        
        for row in rows:
            writer.writerow(row)


def apply_exportation(xp, fname, data):

    with open(fname, "wb") as f:
        xp.do_export(f, rows=data)
