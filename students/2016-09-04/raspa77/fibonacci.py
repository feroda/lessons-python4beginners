# -*- coding: utf-8 -*-

def do_hello():
    print(u"ciao RASPA !")
    tot = 1 + 1
    print(tot)
	
def fib_from_string(x):
    s = "0112358"
    if x < 0 or x > 6: 
        raise ValueError("Valore non ammesso {}".format(x)) 
	else:
        return int(s[x])
		
def fib_from_list(x):
    l = [0,1,1,2,3,5,8]
    if x < 0 or x > 6:
        raise ValueError("Valore non ammesso {}".format(x)) 
    else:
        return l[x]
		
def fib_from_algo(x):
    if x < 0:
        raise ValueError("Valore non ammesso {}".format(x))
    elif x == 0 or x == 1:
        return x
    else:
        return fib_from_algo(x - 1) + fib_from_algo(x - 2)

fib = fib_from_string
		
if __name__ == "__main__":
    print(fib(7))
	