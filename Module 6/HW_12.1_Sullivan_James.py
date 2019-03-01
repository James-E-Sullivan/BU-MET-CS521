"""
HW 12.1
(The Triangle Class)
Design a class named Triangle that extends the GeometricObject class.
The Triangle class contains:

* Three float data fields named side1, side2, and side3 to denote the three
    sides of a triangle
* A constructor that creates a triangle with the specified side1, side2, and
    side3 with default values of 1.0.
* The accessor methods for all three data fields.
* A method named getArea() that returns the area of this triangle.
* A method named getPerimeter() that returns the perimeter of this triangle.
* A method named __str__() that returns a string description of the triangle.

For the formula to compute the area of a triangle, see Exercise 2.14:

s = (side1 + side2 + side3) / 2
area = sqrt(s(s - side1)(s - side2)(s - side3))

The __str__() method is implemented as follows:

return "Triangle: side1 = " + str(side1) + " side 2 = " +
    str(side2) + " side3 = " + str(side3)

Draw the UML diagrams for the classes Triangle and GeometricObject. Implement
the Triangle class. Write a test program that prompts the user to enter the
three sides of the triangle, a color, and 1 or 0 to indicate whether the
triangle is filled. The program should create a Triangle object with these
sides and set the color and filled properties using the input. The program
should display the triangle's area, perimeter, color, and True or False to
indicate whether the triangle is filled or not.
"""
import math


class GeometricObject:
    def __init__(self, color="green", filled=True):
        self.__color = color
        self.__filled = filled

    def getColor(self):
        return self.__color

    def setColor(self, color):
        self.__color = color

    def isFilled(self):
        return self.__filled

    def setFilled(self, filled):
        self.__fileed = filled

    def __str__(self):
        return "color: " + self.__color + " and filled: " + str(self.__filled)


class Triangle(GeometricObject):

    def __init__(self, side1=1.0, side2=1.0, side3=1.0):
        super().__init__()
        self.__side1 = side1
        self.__side2 = side2
        self.__side3 = side3

    def get_side1(self):
        return self.__side1

    def get_side2(self):
        return self.__side2

    def get_side3(self):
        return self.__side3

    def get_area(self):
        s = (self.__side1 + self.__side2 + self.__side3) / 2
        area = math.sqrt(
            s * (s - self.__side1) * (s - self.__side2) * (s - self.__side3)
        )
        return area

    def get_perimeter(self):
        return self.__side1 + self.__side2 + self.__side3

    def __str__(self):
        return "Triangle: side1 = " + str(self.__side1) + " side 2 = " + \
            str(self.__side2) + " side3 = " + str(self.__side3)


def test_Triangle_Class():

    while True:
        try:
            side_list = [float(side) for side in input(
                'Please enter the length of each side of a triangle,'
                ' separated by spaces: ').split()]

            color = input("Enter the triangle's color: ")
            filled = bool("Is the triangle filled? 1=Yes, 0=No")

            if len(side_list) is not 3:
                print('Incorrect amount of inputs. Try again.')
                continue
            else:
                break

        except ValueError:
            print('Could not convert input to float. Try again.')

    triangle1 = Triangle(side_list[0], side_list[1], side_list[2])

    triangle1.setColor(color)
    triangle1.setFilled(filled)

    print(triangle1.__str__())
    print('Area:', triangle1.get_area())
    print('Perimeter:', triangle1.get_perimeter())
    print('Color:', triangle1.getColor())
    print('Filled:', triangle1.isFilled())


test_Triangle_Class()
