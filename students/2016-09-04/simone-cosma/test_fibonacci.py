import pytest
import fibonacci


def test_zero():
    result = fibonacci.calculate(0)
    assert result == 0

def test_one():
    result = fibonacci.calculate(1)
    assert result == 1

def test_two():
    result = fibonacci.calculate(1)
    assert result == 1

def test_three():
    result = fibonacci.calculate(3)
    assert result == 2

def test_valid_number():
    result = fibonacci.calculate(6)
    assert result == 8

#def test_valid_very_big_number():
 #   result = fibonacci.calculate(100)
  #  assert result == 354224848179261915075


def test_string():
    with pytest.raises(TypeError):
        fibonacci.calculate('AAAA')

def test_negative_number():
    with pytest.raises(ValueError):
        fibonacci.calculate(-1)