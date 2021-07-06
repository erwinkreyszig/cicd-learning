# -*- coding: utf-8 -*-


class BasicOperations:

    @staticmethod
    def add(*args):
        """Adds any number of arguments and returns the result"""
        # check first how many arguments was passed
        # if none, return zero
        # if one, return that
        # if more than one, get the type of the first one
        # then use this to check the type of the other arguments
        string = ""
        if len(args) == 0:
            return 0
        if len(args) == 1:
            return args[0]
        if type(args[0]) == str:
            for i in args:
                if type(i) != str:
                    raise Exception('You can\'t concatenate an integer to' +
                                    ' a string!')
                string += i
            return string
        else:
            for i in args:
                if type(i) != int:
                    raise Exception('You can\'t concatenate a string to' +
                                    ' an integer!')
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
            # TODO: return to this: return math.prod(args)
            # when version at circleci container is 3.8+is
            product = 1
            for x in args:
                product *= x
            return product

    @staticmethod
    def divide(val1, val2):
        """Divides an int number by another, then returns a tuple of quotient
        and remainder"""
        quotient = int(val1 / val2)
        remainder = int(val1 % val2)
        t = (quotient, remainder)
        return t

    @staticmethod
    def add_and_multiply(*args, op):
        """Depending on the keyword argument, adds or multiply any number of 
        arguments and returns the result"""
        if op == 'add':
            res = BasicOperations.add(*args)
        if op == 'multiply':
            if len(args) == 0:
                raise Exception
            res = BasicOperations.multiply(*args)
        return res

if __name__ == '__main__':
    print(BasicOperations.add_and_multiply('O chan ', 'and ', 'S chan', op='add'))
    print(BasicOperations.add_and_multiply(-5, -2, op='multiply'))
    print(BasicOperations.add_and_multiply(op='multiply'))
