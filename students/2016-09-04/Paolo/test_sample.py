def func(x):
	return x + 1
	
def test_answer():
	assert func(3) == 5
	
#Posso utilizzare anche il with facendo pytest.raises(TypeError): compose_hello(1)