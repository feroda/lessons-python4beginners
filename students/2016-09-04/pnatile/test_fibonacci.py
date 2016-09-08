import pytest

from fib import dofib


def test_fib_ok():
    assert dofib(0) == 0
    assert dofib(1) == 1
    assert dofib(2) == 1
    assert dofib(3) == 2

def test_fib_raise_if_string():
    with pytest.raises(TypeError):
        dofib("a")
  
def test_fib_raise_lt_zero():
    with pytest.raises(ValueError):  #with content manager che serve a wrappare quello che avviene intorno 
         dofib(-1)
