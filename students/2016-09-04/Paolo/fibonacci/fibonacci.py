# -*- coding: utf-8 -*-

import exception_handler


def verify_exceptions(start, end):

	ex_handler = exception_handler.ExceptionHandler()
	
	ex_handler.verifyNumberIsNotNegative(start)
	ex_handler.verifyNumberIsNotAString(start)
	ex_handler.verifyNumberIsNotAString(end)
	ex_handler.isFirstNumberGreaterThanSecondNumber(start,end)

		

def fill_fibonacci_array(fibonacci_list, end):
	next = 0
	second = 1
	count = 0
	first = 0
	
	while count <= end:
		
		if count <= 1:
			fibonacci_list.append(count)
		elif count > 1:
			next = first + second
			fibonacci_list.append(next)
			first = second
			second = next
			
		count += 1
	

def run(start, end):
	fibonacci_list = []
	
	verify_exceptions(start,end)	
	fill_fibonacci_array(fibonacci_list, end)
	
	print(fibonacci_list)
	
	return fibonacci_list[start:]
		
if __name__ == "__main__":
	run(0,5)