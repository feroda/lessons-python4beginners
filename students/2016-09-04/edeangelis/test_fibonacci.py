import pytest

from fibonacci import succ_fib

def test_fib_small():
    assert succ_fib(0) == 0
    assert succ_fib(1) == 1
    assert succ_fib(2) == 1
    assert succ_fib(3) == 2

def test_fib_raise_if_string():
    with pytest.raises(TypeError):
        succ_fib("a")
		
def test_fib_raise_if_zero():
    with pytest.raises(ValueError):
        succ_fib(-1)