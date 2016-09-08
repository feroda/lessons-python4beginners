
import pytest
from myprogram import fib

def test_fib_ok_small():
    assert fib(3)==2
    assert fib(0)==0
    assert fib(1)==1
    assert fib(2)==1
    
def test_fib_raise_if_string():
    with pytest.raises(TypeError):
    fib("a")

def test_fib_raises_it_zero():
    with pytest.raises(ValueError):
    fib(-1)
    
    