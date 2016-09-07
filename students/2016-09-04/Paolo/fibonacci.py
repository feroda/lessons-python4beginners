# -*- coding: utf-8 -*-


def run(first, end):
	next = 0
	second = 1
	array = []
	value = 0
	
	if first < 0:
		raise Exception("First number shoould be > 0")
	
	if isinstance(first,basestring):
		raise TypeError("First input variable should be a number!")
		
	if isinstance(end,basestring):
		raise TypeError("First input variable should be a number!")
	
	while value <= end:
		
		if value <= 1:
			next = value
			array.append(next)
		elif value > 1:
			next = first + second
			array.append(next)
			first = second
			second = next
			
		value += 1
	
	print(array)
	
	return array
		
if __name__ == "__main__":
	run(0,5)