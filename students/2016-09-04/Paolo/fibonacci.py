# -*- coding: utf-8 -*-


def verify_exceptions(start, end):
	
	if isinstance(start,basestring):
		raise TypeError("Start input variable should be a number!")
		
	if isinstance(end,basestring):
		raise TypeError("First input variable should be a number!")
		
	if start < 0:
		raise Exception("Start number shoould be > 0")
		
	if start > end:
		raise Exception("Start cannot be > than end")

def run(start, end):
	next = 0
	second = 1
	array = []
	value = 0
	first = 0
	
	verify_exceptions(start,end)
	
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
	
	return array[start:]
		
if __name__ == "__main__":
	run(0,5)