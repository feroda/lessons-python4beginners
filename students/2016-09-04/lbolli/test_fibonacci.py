import pytest
from fibonacci import *

def test_fib_from_string_fast_ok():
    assert fib_from_string(0) == 0
    assert fib_from_string(1) == 1
    assert fib_from_string(2) == 1
    assert fib_from_string(3) == 2
    assert fib_from_string(4) == 3 
    assert fib_from_string(5) == 5

def test_fib_all_raises_lt_zero():
    with pytest.raises(ValueError):
        fib_from_string(-1)
    with pytest.raises(ValueError):
        fib_from_list(-2)
    with pytest.raises(ValueError):
        fib_from_algo(-10)

