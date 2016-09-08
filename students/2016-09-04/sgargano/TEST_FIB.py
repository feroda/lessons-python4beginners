import pytest
from myrogram import fibonacci
def test:fib_ok_small():
    assert fibonacci(0) == 0
	assert fibonacci(1) == 1
	assert fibonacci(2) == 1 
	assert fibonacci(3) == 2
	
def test_fib_raise_if_string():
    with pytest.raises(TypeError):
	    fibonacci("a")
		
def test_fib_raise_lt_zero():
   with pytest.raises(ValueError):
        fibonacci(-1)
		
def  assert fibonacci(3) == 2(n):
    if n == 1 or n==2:
        return 1
	else n == 0
	    return 0
	
return fibonacci(n-1)+fibonacci(n-2)