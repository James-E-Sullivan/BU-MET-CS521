"""
HW 7.5
(Geometry: n-sided regular polygon)
An n-sided regular polygon's sides all have the same length and all of its
angles have the same degree (i.e., teh polygon is both equilateral and
equiangular). Design a class named 'RegularPolygon' that contains:

* A private int data field named 'n' that defines the number of sides in
    the polygon.
* A private float data field named side that stores the length of the side.
* A private float data field named x that defines the x-coordinate of the
    center of the polygon with default value 0.
* A private float data field named y that defines the y-coordinate of the
    center of the polygon with the default value 0.
* A constructor that creates a regular polygon with the specified n (default 3),
    side (default 1), x (default 0), and y (default 0).
* The accessor and mutator methods for all data fields.
* The method getPerimeter() that returns the perimeter of the polygon.
* The method getArea() that returns the area of the polygon. The formula for
    computing the area of a regular polygon is:

    Area = (n * s**2) / (4 * tan(pi/n))

Draw the UML diagram for the class, and then implement the class. Write a test
program that creates three RegularPolygon objects, created using
RegularPolygon(), RegularPolygon(6, 4), and RegularPolygon(10, 4, 5.6, 7.8).
For each object, display its perimeter and area.
"""
import math


class RegularPolygon:

    def __init__(self, n=3, side=1, x=0.0, y=0.0):
        self.__n = n
        self.__side = side
        self.__x = x
        self.__y = y

    # returns n, number of sides
    def get_n(self):
        return self.__n

    # sets n, number of sides
    def set_n(self, new_n):
        self.__n = new_n

    # returns side length
    def get_side(self):
        return self.__side

    # sets side length
    def set_side(self, new_side):
        self.__side = new_side

    # returns x value
    def get_x(self):
        return self.__x

    # sets x value
    def set_x(self, new_x):
        self.__x = new_x

    # returns y value
    def get_y(self):
        return self.__y

    # sets y value
    def set_y(self, new_y):
        self.__y = new_y

    # returns polygon perimeter, using side length and n
    def getPerimeter(self):
        perimeter = self.__side * self.__n
        return perimeter

    # returns polygon area, using side length and n
    def getArea(self):
        area = (self.__n * (self.__side**2)) /\
               (4 * math.tan(math.pi / self.__n))
        return area


def test_RegularPolygon():

    # Creates 3 polygon objects with different parameters
    polygon1 = RegularPolygon()
    polygon2 = RegularPolygon(6, 4)
    polygon3 = RegularPolygon(10, 4, 5.6, 7.8)

    # Prints perimeter and area of the three polygons
    print('Polygon 1 perimeter:', polygon1.getPerimeter())
    print('Polygon 1 area:', polygon1.getArea())
    print('Polygon 2 perimeter:', polygon2.getPerimeter())
    print('Polygon 2 area:', polygon2.getArea())
    print('Polygon 3 perimeter:', polygon3.getPerimeter())
    print('Polygon 3 area:', polygon3.getArea())


test_RegularPolygon()
