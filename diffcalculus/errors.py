"""
Contains all the Exceptions.
"""

class BaseError(Exception):
	""" Invalid Base, esp. for logarithmic functions."""
	pass

class ExponentError(Exception):
	""" Invalid Exponent, esp. for exponential functions."""
	pass

class FunctionError(Exception):
	""" Invalid Function for Differentiation, Substitution."""
	pass

class OperationError(Exception):
	""" Invalid Operation between different functions for Differentiation,
		Substitution.
	"""
	pass

class ParameterError(Exception):
	""" Invalid Parameters passed to a Function."""
	pass