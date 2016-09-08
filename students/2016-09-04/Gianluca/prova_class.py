
class Greeter(object):
	def __init__(self, name="no name"):
		#Invocato quando instanzio l'oggetto (name è il parametro passato)
		self.name = name #proprieta
	def hello(self): #metodo
		#print("HELLO {}".format(self.name))
		print("HELLO {0.name}".format(self))
		
x = Greeter("Gianluca")
x.hello()
