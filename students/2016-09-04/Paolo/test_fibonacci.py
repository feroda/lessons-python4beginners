import pytest

import fibonacci

def test_fibonacci():
	print("Test Fibonacci 1 started")
	
	array = fibonacci.run(0, 5)
	
	assert array[0] == 0
	assert array[1] == 1
	assert array[2] == 1
	assert array[3] == 2
	assert array[4] == 3
	assert array[5] == 5
	
def test_exception():
	print("Test Fibonacci exception fired when start number is minor than zero")
	
	with pytest.raises(Exception):
		fibonacci.run(-1, 5)
		
def test_inputfirst_mustbe_number():
	with pytest.raises(TypeError):
		fibonacci.run("ciao", 5)
		
def test_inputend_mustbe_number():
	with pytest.raises(TypeError):
		fibonacci.run(0, "Ciao")