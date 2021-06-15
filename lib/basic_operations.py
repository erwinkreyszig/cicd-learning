def add(val1, val2):
	"""Adds 2 int numbers and returns the result"""
	if type(val1) == int and type(val2) == int:
		result = val1 + val2
		return result
	else:
		return -1

def substract(val1, val2):
	if type(val1) != int or type(val2) != int:
		raise Exception
	return val1 - val2

def multiply(val1, val2):
	for val in range(val2):
		result = val1 + val2
	return result

def test():
	assert 3 == add(1, 2)
	assert -3 == add(-1, -2)
	assert 0 == add(1, -1)

