import json
import csv

class BaseExporter(object):
	def __init__(sefl, f, debug=False):
		self.f = f
		self.debug = debug
	def do_export(self, rows):
		raise NotImplementedError("Implementeta nelle sotto classi")
	def do_import(self):
		raise NotImplementedError("Implementeta nelle sotto classi")
	# return super(BaseExporter, self).__getitem__ => Per chiamare il metodo della classe originale 

class DebugExporter(BaseExporter):
	def do_export(self, rows):
		for row in rows:
			print("{}\n".format(row))

class FileExporter(BaseExporter):
	def do_export(self, rows):
		for row in rows:
			if self.debug:
				print("{}\n".format(row))
			else:
				self.f.write("{}\n".format(row))

class JsonExporter(BaseExporter):
	def do_export(self, rows):
		if self.debug:
			json.dumps(rows)
		else:
			json.dump(rows,f)
	def do_import(self):
		json.load(self.f)

class CSVExporter(BaseExporter):
	def do_export(self, rows):
		fieldnames = rows[0].keys() 
		if self.debug:
			print(fieldnames)
		else:
			writer = csv.DictWriter(sef.f, fieldnames = fieldnames, delimiter = ";")
			writer.writeheader()
		for row in rows:
			if self.debug:
				print(row)
			else:
				writer.writerow(row)

def set_export(xp,fname,data):
	if fname.finsh
l2 = [1,2,4,6,100,200,30]
xp = Exporter()
with open(r"c:\tmp.txt")
	xp.do_export(None, l2)