# -*- coding: utf-8 -*-


def run(first, end):
	next = 0
	second = 1
	array = []
	value = 0
	
	while value <= end:
		
		if value <= 1:
			next = value
			print(next)
			array.append(next)
		elif value > 1:
			next = first + second
			print(next)
			array.append(next)
			first = second
			second = next
			
		value += 1
	
	print(array)
	
	return array
		
if __name__ == "__main__":
	run(0,5)