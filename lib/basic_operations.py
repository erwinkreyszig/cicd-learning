# -*- coding: utf-8 -*-
import math


class BasicOperations:

    @staticmethod
    def add(*args):
        """Adds any number of arguments and returns the result"""
        for i in args:
            if type(i) != int:
                raise Exception
        if len(args) == 0:
            return 0
        elif len(args) == 1:
            return args[0]
        else:
            return sum(args)

    @staticmethod
    def subtract(val1, val2):
        """Subtracts the second argument from the first argument"""
        if type(val1) != int or type(val2) != int:
            raise Exception
        return val1 - val2

    @staticmethod
    def multiply(*args):
        """Multiplies any number of arguments and returns the result"""
        for i in args:
            if type(i) != int:
                raise Exception
        if len(args) == 0:
            return 0
        elif len(args) == 1:
            return args[0]
        else:
            return math.prod(args)

    @staticmethod
    def divide(val1, val2):
        """Divides an int number by another, then returns a tuple of quotient
        and remainder"""
        quotient = int(val1 / val2)
        remainder = int(val1 % val2)
        t = (quotient, remainder)
        return t


if __name__ == '__main__':
    operation = BasicOperations()
    print(operation.multiply(-4))
    print(operation.multiply(4, -3, -2))
    print(operation.multiply())
    print(operation.multiply(2, 4, 'a'))
