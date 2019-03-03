"""
HW 7.7
(Algebra: 2x2 linear equations) Design a class named LinearEquation for a 2x2
system of linear equations:

    ax + by = e             x = (ed - bf) / (ad - bc)
    cx + dy = f             y = (af - ec) / (Ad - bc)

The class contains:
* The private data fields, a, b, c, d, e, and f with get methods.
* A constructor with the arguments for a, b, c, d, e, and f.
* Six get methods for a, b, c, d, e, and f.
* A method named isSolvable() that returns true if (ad - bc) is not 0.
* The methods getX() and getY() that return the solution for the equation.

Draw the UML diagram for the class, then implement the class. Write a test
program that prompts the user to enter a, b, c, d, e, and f and displays
the result. If (ad - bc) is 0, report that "The equation has no solution."
See Exercise 4.3 for sample runs.
"""


class LinearEquation:

    def __init__(self, a, b, c, d, e, f):
        self.__a = a
        self.__b = b
        self.__c = c
        self.__d = d
        self.__e = e
        self.__f = f

    def get_a(self):
        return self.__a

    def get_b(self):
        return self.__b

    def get_c(self):
        return self.__c

    def get_d(self):
        return self.__d

    def get_e(self):
        return self.__e

    def get_f(self):
        return self.__f

    def isSolvable(self):
        if (self.__a * self.__d) - (self.__b * self.__c) is not 0:
            return True
        else:
            return False

    def getX(self):
        if self.isSolvable() is True:
            x = ((self.__e * self.__d) - (self.__b * self.__f)) / \
                ((self.__a * self.__d) - (self.__b * self.__c))
            return x
        else:
            print('The equation has no solution')

    def getY(self):
        if self.isSolvable() is True:
            y = ((self.__a * self.__f) - (self.__e * self.__c)) / \
                ((self.__a * self.__d) - (self.__b * self.__c))
            return y
        else:
            print('The equation has no solution')


def test_LinearEquation():

    # Assigns values to equation1
    equation1 = LinearEquation(9, 4, 3, -5, -6, -21)
    print('equation1: ')

    # Checks if equation1 is solvable, displays x & y if it is
    if equation1.isSolvable():
        print('x is', equation1.getX())
        print('y is', equation1.getY())
    else:
        print('The equation has no solution')

    # Prints blank line between outputs of the two equations
    print('')

    # Assigns values to equation2
    equation2 = LinearEquation(1, 2, 2, 4, 4, 5)
    print('equation2: ')

    # Checks if equation1 is solvable, displays x & y if it is
    if equation2.isSolvable():
        print('x is', equation2.getX())
        print('y is', equation2.getY())
    else:
        print('The equation has no solution')


test_LinearEquation()
