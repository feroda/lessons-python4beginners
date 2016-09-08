# -*- coding: utf-8 -*-


class NegativeNumberException(Exception):
	pass
	
	def __init__(self, message):
		super(NegativeNumberException, self).__init__(message)
		
class InvalidNumberProvidedException(Exception):
	pass
	
	def __init__(self, message):
		super(InvalidNumberProvidedException, self).__init__(message)