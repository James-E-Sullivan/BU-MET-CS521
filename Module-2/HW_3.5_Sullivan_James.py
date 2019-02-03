'''
(Geometry: area of a regular polygon)
A regular polygon is an n-sided polygon in which all sides are of the same
length and all angles have the same degree (i.e., the polygon is both
equilateral and equiangular). The formula for computing the area of a
regular polygon is:

Area = (n * (s ** 2)) / (4 * tan(pi/n))

Here, s is the length of a side (*and n is number of sides*).
Write a program that prompts the user to enter the number of sides and their
length of a regular polygon and displays its area.
'''

import math

# Prompts user for number of sides and length of regular polygon
# Values stored in variables
number_of_sides, side_length = eval(input(
    'Enter the number of sides of a regular polygon, '
    'followed by the side length (separated by a comma): '))

# Calculates the area of a regular python, using the above variables
area = (number_of_sides * (side_length ** 2)) / \
       (4 * math.tan((math.pi / number_of_sides)))

print('The area of the polygon is: ', area)
