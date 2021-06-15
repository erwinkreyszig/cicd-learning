def add(val1, val2):
	"""Adds 2 int numbers and returns the result"""
	if type(val1) == int and type(val2) == int:
		result = val1 + val2
		return result
	else:
		return -1

def substract(val1, val2):
	if type(val1) == int and type(val2) == int:
		result = val1 - val2
		return result
	else:
		return -1
		
def multiply(val1, val2):
	for val in range(val2):
		result = val1 + val2
	return result

def test():
	print(add(1, 2))
	print(add(-1, -2))
	print(add(1, -1))

