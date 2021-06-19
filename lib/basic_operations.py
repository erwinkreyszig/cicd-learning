# -*- coding: utf-8 -*-


def add(val1, val2):
    """Adds 2 int numbers and returns the result"""
    if type(val1) != int or type(val2) != int:
        raise Exception
    return val1 + val2


def subtract(val1, val2):
    """Subtracts the second argument from the first argument"""
    if type(val1) != int or type(val2) != int:
        raise Exception
    return val1 - val2


def multiply(val1, val2):
    """Multiplies 2 int numbers and returns the result"""
    return val1 * val2


def divide(val1, val2):
	"""Divides an int number by another, then returns a tuple of quotient and remainder"""
	quotient = int(val1 / val2)
	remainder = int(val1 % val2)
	t = (quotient, remainder) 
	return t


if __name__ == '__main__':
    print(multiply(2, 4))
    print(multiply(-4, -8))
    print(multiply(4, -9))
