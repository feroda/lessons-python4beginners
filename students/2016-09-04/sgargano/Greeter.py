class Greeter(object):
    
    
    def __init__(self, name):
        self.name = name
        
        
    def hello (self):
        print("Hello {}".format(self.name))
        print("Hello {0.name}".format(self))
        
        
luca = Greeter("Luca")
luca.hello()

simone = Greeter("Simone")
simone.hello()
        
        