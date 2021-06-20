# -*- coding: utf-8 -*-
"""
Unit tests for the basic_operations library
"""


from lib.basic_operations import add, subtract


class TestBasicOperations(object):

    def test_add(self):
        # testing method with no argument
        assert 0 == add()
        # testing method with one argument
        assert -5 == add(-5)
        # testing method with more than one argument
        assert 12 == add(11, -1, 2)
        # initialize a variable to store the caught exception later
        ex = None
        try:
            # this is the code that will result in an exception
            add(2, 'a')
        except Exception as e:
            # when an exception happens, exception will be put in
            # the vaiable e, then put it in ex so it can be used
            # outside the try-catch
            ex = e
        # test if the exception that happened is of Exception type
        assert type(ex) == Exception

    def test_subtract(self):
        assert 1 == subtract(3, 2)
        assert 1 == subtract(-1, -2)
        assert 2 == subtract(1, -1)


if __name__ == '__main__':
    test = TestBasicOperations()
    test.test_add()
