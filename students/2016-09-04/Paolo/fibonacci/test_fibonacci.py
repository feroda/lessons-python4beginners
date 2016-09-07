import pytest

import fibonacci
import custom_exception

def test_fibonacci():
	print("Test Fibonacci 1 started")
	
	array = fibonacci.run(0, 5)
	
	assert array[0] == 0
	assert array[1] == 1
	assert array[2] == 1
	assert array[3] == 2
	assert array[4] == 3
	assert array[5] == 5
	
def test_exception_when_start_is_negative():
	print("Test Fibonacci exception fired when start number is minor than zero")
	
	with pytest.raises(custom_exception.NegativeNumberException):
		fibonacci.run(-1, 5)
		
def test_input_start_must_be_number():
	with pytest.raises(TypeError):
		fibonacci.run("ciao", 5)
		
def test_input_end_must_be_number():
	with pytest.raises(TypeError):
		fibonacci.run(0, "Ciao")
		
		
def test_start_cannot_be_more_than_end():
	with pytest.raises(custom_exception.InvalidNumberProvidedException):
		fibonacci.run(7,5)