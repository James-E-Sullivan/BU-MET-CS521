'''
(Geometry: area of a pentagon)
Write a program that prompts the user to enter the length from the center of a
pentagon to a vertex and computes the area of the pentagon, as shown in the
following figure.

*Figure in book*

The formula for computing the area of a pentagon is:

***NOTE: THIS IS INCORRECT. THIS IS THE FORMULA FOR AREA OF A HEXAGON***

Area = ((3 * sqrt(3)) / 2) * (s ** 2)

where s is the length of a side.

The side can be computed using the formula:

s = 2r sin (PI/5)       where r is the length from the center of a pentagon
to a vertex.

Example:
    Enter the length from the center to a vertex: 5.5
    The area of the pentagon is 108.61
'''

import math

center_to_vertex = eval(input('Enter the length from the center of a pentagon'
                               ' to a vertex: '))

side_length = (2 * center_to_vertex) * (math.sin(math.pi / 5))

# Known issue: the provided formula is for the area of a hexagon
# Used math.pow() function instead of standard **.
hexagon_area = ((3 * math.sqrt(3)) / 2) * (math.pow(side_length, 2))

pentagon_area = (1/4) * math.sqrt(5 * (5 + (2 * math.sqrt(5)))) * (side_length ** 2)

print('Using the formula provided in the book, the area is: ', hexagon_area)
print('The area of the pentagon is: ', pentagon_area)