class Greeter(object):  #classe che deriva dalla classe base object
	
	
	def __init__(self,name):  #è il costruttore di un oggetto, quando istanzio un oggetto viene chiamato tale oggetto
		self.name = name
		
		
	def hello(self): #self è l’oggetto stesso che viene passato come primo parametron dei metodi
		#print("hello {}".format(self.name))
		print("hello {0.name}".format(self)) #equivale alla istruzione di sopra

		
x = Greeter("Luca")
x.hello()