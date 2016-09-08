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

fib_dic = {0 : 1, 1 : 1}
        
def fib_from_dict(x):
    """
    Calcola fibonacci con cache su dizionario
    """
    if x in fib_dic:
        return fib_dic[x]
        
    fib_pre = fib_from_dict(x-1)
    fib_dic[x-1] = fib_pre
    fib_prepre = fib_from_dict(x-2)
    fib_dic[x-2] = fib_prepre
    
    return fib_pre + fib_prepre

fib = fib_from_dict
		
if __name__ == "__main__":
    pos_fib = raw_input("Posizione di fibonacci")
    max_fib = int(pos_fib)
    print(fib(max_fib))
	