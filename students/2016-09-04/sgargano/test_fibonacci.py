import pytest
from fibmio import fibonacci
def test_fib_ok_small():
    assert fib(0) == 0
	assert fib(1) == 1
	assert fib(2) == 1 
	assert fib(3) == 2
	
def test_fib_raise_if_string():
    with pytest.raises(TypeError):
	    fib("a")
		
def test_fib_raise_lt_zero():
   with pytest.raises(ValueError):
        fib(-1)
		
