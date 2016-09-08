import json
import csv


class BaseManager(object):

    def __init__(self, f, debug=False):
        self.f = f
        self.debug = debug

    def do_export(self, rows):
        raise NotImplementedError("To be implemented in subclasses")

    def do_import(self):
        raise NotImplementedError("To be implemented in subclasses")


class DebugManager(BaseManager):

    def do_export(self, rows):
        for row in rows:
            print("{}".format(row))
            

class FileManager(BaseManager):

    def do_export(self, rows):

        for row in rows:
            output = "{}\n".format(row)
            if self.debug:
                print(output)
            else:
                self.f.write(output)


class JsonManager(BaseManager):

    def do_export(self, rows):

        if self.debug:
            print(json.dumps(rows, indent=2))
        else:
            json.dump(rows, self.f, indent=2)

    def do_import(self):
        return json.load(self.f)


class CsvManager(BaseManager):

    def do_export(self, rows):

        if self.debug:
            raise NotImplementedError("TODO")
        else:
            fieldnames = rows[0].keys()
            writer = csv.DictWriter(
                self.f, fieldnames = fieldnames, delimiter = ";")
            writer.writeheader()
            
            for row in rows:
                writer.writerow(row)

        

