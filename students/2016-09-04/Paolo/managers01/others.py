import json
import csv
import cStringIO as StringIO

from .base import BaseManager


class FileManager(BaseManager): #Il metodo do_export è implementato direttamente nella classe padre!!

    def get_output(self, rows): #Avere il get_output per ogni classe ci permette di mettere "if self.debug ecc." solo nella classe padre

        rv = u""
        for row in rows:
            rv += u"{}\n".format(row)
        return rv
        
    def _do_export(self, rows):

        self.f.write(self.get_output())


class JsonManager(BaseManager):

    def get_output(self, rows):

        return json.dumps(rows, indent=2)

    def _do_export(self, rows):

        json.dump(rows, self.f, indent=2)

    def _do_import(self):
        return json.load(self.f)


class CsvManager(BaseManager):

    def get_output(self, rows):
        """Output CSV in a fake file in memory."""

        #In realtà abbiamo importato cStringIO, che è nettamente più veloce del massimo StringIO. Si mette sempre "as StringIO".
        myfile = StringIO.StringIO() #Questo ha un metodo write(), ecc. E fondamentalmente mi tiene il file in ram senza scriverlo veramente su filesystem!!
        self.__perform(myfile, rows)
        myfile.seek(0) #Riporta il puntatore del file ad inizio file.
        return myfile.read()

    def __perform(self, myfile, rows):
        """
        Encapsulate writing csv data to file.
        Due to how csv library works this seems to be the
        best way to get csv data in string
        """

        fieldnames = rows[0].keys()
        writer = csv.DictWriter( myfile,
            fieldnames = fieldnames, delimiter = ";")

        writer.writeheader()
        map(writer.writerow, rows)

    
    def _do_export(self, rows):

        self.__perform(self.f, rows)

    def _do_import(self):

        reader = csv.DictReader(myfile)
        return list(reader)