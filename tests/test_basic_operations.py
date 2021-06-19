# -*- coding: utf-8 -*-
"""
Unit tests for the basic_operations library
"""


from src.lib.basic_operations import add, subtract


class TestBasicOperations(object):

    def test_add(self):
        assert 3 == add(1, 2)
        assert -3 == add(-1, -2)
        assert 0 == add(1, -1)

    def test_subtract(self):
        assert 1 == subtract(3, 2)
        assert 1 == subtract(-1, -2)
        assert 2 == subtract(1, -1)
