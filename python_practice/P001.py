# -*- coding: utf-8 -*-
"""write a method that tells whether a number is even or odd."""


def even_or_odd(val):
    """Returns True if the number is even, and False if odd."""
    if val % 2 == 0:
        return True
    else:
        return False


if __name__ == '__main__':
    # test even
    assert even_or_odd(6) == True
    # test odd
    assert even_or_odd(5) == False
    print('all tests passed')