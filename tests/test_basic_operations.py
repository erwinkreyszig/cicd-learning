# -*- coding: utf-8 -*-
"""
Unit tests for the basic_operations library
"""


from lib.basic_operations import BasicOperations


class TestBasicOperations(object):

    def test_add(self):
        # testing no argument
        assert 0 == BasicOperations.add(0)
        # testing one argument
        assert -6 == BasicOperations.add(-6)
        # testing more than one argument
        assert 9 == BasicOperations.add(1, -1, 5, 4)
        # testing more than one string argument
        assert 'abcde' == BasicOperations.add('a', 'b', 'cde')
        # testing a non-integer argument
        ex = None
        try:
            BasicOperations.add(1, 'a', 5)
        except Exception as e:
            ex = e
        assert type(ex) == Exception

    def test_subtract(self):
        # testing positive arguments
        assert 1 == BasicOperations.subtract(3, 2)
        # testing negative arguments
        assert 1 == BasicOperations.subtract(-1, -2)
        # testing negative and positive arguments
        assert 2 == BasicOperations.subtract(1, -1)
        # testing a non-integer argument
        ex = None
        try:
            BasicOperations.subtract('a', 6)
        except Exception as e:
            ex = e
        assert type(ex) == Exception

    def test_multiply(self):
        # testing O or more arguments
        assert 0 == BasicOperations.multiply()
        # testing negative arguments
        assert -2 == BasicOperations.multiply(-2)
        # testing negative and positive arguments
        assert 24 == BasicOperations.multiply(3, 4, 2)
        # testing a non-integer argument
        ex = None
        try:
            BasicOperations.multiply('a', 6)
        except Exception as e:
            ex = e
        assert type(ex) == Exception

    def test_divide(self):
        # testing positive arguments
        assert (0, 2) == BasicOperations.divide(2, 5)
        # testing negative arguments
        assert (2, -1) == BasicOperations.divide(-5, -2)
        # testing negative and positive arguments
        assert (-2, 0) == BasicOperations.divide(8, -4)
        # testing a non-integer argument
        ex = None
        try:
            BasicOperations.divide('a', 6)
        except Exception as e:
            ex = e
        assert type(ex) == TypeError
