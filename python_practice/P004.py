# -*- coding: utf-8 -*-
"""ask for a number from the user then display a triangle using asterisks:
if the input was 4, print:
`xxxo`
`xxoo`
`xooo`
`oooo`
* the o's are supposed to be asterisks, and the x's are spaces"""


def triangle():
    number_from_user = int(input("Please type a number."))
    for i in range(number_from_user):
        for j in range(number_from_user - 1):
            print(" ", end='')
        for k in range(i + 1):
            print("*", end='')
        number_from_user -= 1
        print('')


if __name__ == '__main__':
    # test1
    triangle()
