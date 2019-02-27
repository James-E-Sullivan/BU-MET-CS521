"""
HW 7.1
(The Rectangle class)
Following the example of the Circle class in Section 7.2, design a class
named 'Rectangle' to represent a rectangle. The class contains:

* Two data fields named 'width' and 'height'
* A constructor that creates a rectangle with the specified width and height.
    - The default values are 1 and 2 for the width and height, respectively
* A method named 'getArea()' that returns the area of this rectangle
* A method named 'getPerimeter()' that returns the perimeter

Draw the UML diagram for the class, then implement the class. Write a test
program that creates two Rectangle objects - one with width 4 and height 40,
and the other with width 3.5 and height 35.7. Display the width, height, area,
and perimeter of each rectangle in this order.
"""


class Rectangle:

    def __init__(self, width=1, height=2):
        self.__width = width
        self.__height = height

    def getWidth(self):
        return self.__width

    def getHeight(self):
        return self.__height

    def getArea(self):
        return self.__width * self.__height

    def getPerimeter(self):
        perimeter = (2 * self.__width) + (2 * self.__height)
        return perimeter


def test_Rectangle_class():

    rectangle1 = Rectangle(4, 40)
    rectangle2 = Rectangle(3.5, 35.7)

    print('rectangle1')
    print('Width: ', rectangle1.getWidth(), '\n'
          'Height: ', rectangle1.getHeight(), '\n'
          'Area: ', rectangle1.getArea(), '\n'
          'Perimeter: ', rectangle1.getPerimeter(), '\n')

    print('rectangle2')
    print('Width: ', rectangle2.getWidth(), '\n'
          'Height: ', rectangle2.getHeight(), '\n'
          'Area: ', rectangle2.getArea(), '\n'
          'Perimeter: ', rectangle2.getPerimeter())


test_Rectangle_class()
