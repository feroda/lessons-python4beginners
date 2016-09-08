import pytest

from fibonacci import fib

def test_num():
    assert 0 == fib(0)
    assert 1 == fib(1)
    assert 1 == fib(1)
    assert 2 == fib(3)
    
def test_string():
    with pytest.raises(TypeError):
        fib("a")

def test_neg():
    with pytest.raises(ValueError):
        fib(-1) 