import pytest

import fibonacci

def test_fibonacci():
	print("Test Fibonacci 1 started")
	
	array = fibonacci.run(0, 5)
	
	assert array[0] == 0