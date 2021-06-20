# -*- coding: utf-8 -*-


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
    def multiply(val1, val2):
        """Multiplies 2 int numbers and returns the result"""
        return val1 * val2

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
    print(operation.add(-4))
    print(operation.add(4, -9, -8))
    print(operation.add())
    print(operation.add(2, 4, 'a'))
