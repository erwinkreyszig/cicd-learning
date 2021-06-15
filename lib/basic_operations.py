def add(val1, val2):
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
		

def test():
	print(add(1, 2))
	print(add(-1, -2))
	print(add(1, -1))

