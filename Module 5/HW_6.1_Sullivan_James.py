"""
HW 6.1
(Math: pentagonal numbers)
A pentagonal number is defined as n(3n - 1)/2 for n = 1, 2, ..., and so on.
So, the first few numbers are 1, 5, 12, 22, ... Write a function with the
following header that returns a pentagonal number:

def getPentagonalNumber(n):

Write a test program that uses this function to display the first 100
pentagonal numbers with 10 numbers on each line.
"""


def getPentagonalNumber(n):

    pentagonal_number = (n * ((3 * n) - 1)) / 2
    return pentagonal_number


for i in range(1, 100):

    if i % 10 == 0:
        print(int(getPentagonalNumber(i)))
    else:
        print(int(getPentagonalNumber(i)), end=' ')
