# -*- coding: utf-8 -*-
"""Swap the values of two variables."""


def swap_variables(val1, val2):
    """Returns swapped variables."""
    val = val1
    val1 = val2
    val2 = val
    return (val1, val2)


if __name__ == '__main__':
    # test1
    assert swap_variables(3, 6) == (6, 3)
    # test2
    assert swap_variables(-5, -10) == (-10, -5)
    print('all tests passed')