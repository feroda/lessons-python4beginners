# -*- coding: utf-8 -*-

def double_list(input_list):
    double_list = [x*2 for x in input_list]
    print(double_list)
    
def double_dict(input_list):
    my_dict = {k: k*2 for k in list} #Posso anche fare k: v for k,v in enumerate(list)
    print(my_dict)

if __name__ == "__main__":
    list = [1, 2, 3, 4]
    double_list(list)
    double_dict(list)