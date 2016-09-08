import pytest
from fibonacci import fib

def test_fib_ok_small():
    assert fib(0) == 0
    assert fib(1) == 1
    assert fib(2) == 1
    assert fib(3) == 2
    assert fib(4) == 3

def test_fib_raise_if_string():
    with pytest.raises(TypeError):      # errore per stringa letterare
        fib("a")
    with pytest.raises(TypeError):      # errore per stringa numerica
        fib("1")

def test_fib_raises_lt_zero():
    with pytest.raises(ValueError):
        fib(-1)
