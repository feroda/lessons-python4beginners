import decimal
import types

import fibo

class Person(dict):
    
    def __setitem__(self, key, value):
        
        if key == "salary" and not isinstance(value, decimal.Decimal):
            value = decimal.Decimal(str(self["salary"]))
        
        elif key == "genfibo" and not isinstance(value, types.IntType):
            value = int(value)
        
        super(Person, self).__setitem__(key, value)

    def calc_rabbits(self):
        return fibo.calc_fibo(self["genfibo"])
    
    def calc_monthly_salary(self):
        return self["salary"] / 12