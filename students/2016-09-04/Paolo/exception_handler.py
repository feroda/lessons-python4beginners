# -*- coding: utf-8 -*-

import custom_exception

class ExceptionHandler:
		
	def verifyNumberIsNotNegative(self, number):
		if number < 0:
			raise custom_exception.NegativeNumberException("Provided number should be > 0")
			
	def verifyNumberIsNotAString(self, number):
		if isinstance(number,basestring):
			raise TypeError("Start input variable should be a number!")
			
	def isFirstNumberGreaterThanSecondNumber(self, first_number, second_number):
		if first_number > second_number:
			raise custom_exception.InvalidNumberProvidedException("Start cannot be > than end")