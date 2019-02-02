'''
(Geography: estimate areas)
Find the GPS locations for Atlanta, Georgia; Orlando Florida;
Savannah, Georgia; and Charlotte, North Caroline from
www.gps-data-team.com/map/ and compute the estimated area enclosed by
these four cities.

***NOTE: THIS WEBSITE DOES NOT WORK PROPERLY***

(Hint: Use the formula in Programming Exercise 3.2 to compute the distance
between two cities. Divide the polygon into two triangles and use the
formula in Programming Exercise 2.14 to compute the area of a triangle)

Great Circle Distance - the distance between two points on the surface of a
sphere:

Let (x1, y1) and (x2, y2) be the geographical latitude and longitude of two
points. The great circle distance between the two points can be computed
using the following formula:

d = radius * arcCOS(sin(x1) * sin(x2) + cos(x1) * cos(x2) * cos(y1 - y2))

The average earth radius is 6,371.01 km. Note that you need to convert the
degrees into radians using the math.radians function, since Python trig
uses radians.

Area of a triangle:

s = (side1 + side2 + side3)/2
area = sqrt(s(s - side1) * (s - side2) * (s- side3))
'''

import math

# Adds city coordinates into a list structured [lat, long]
atlanta_coord = [33.7242700, -84.5785800]
orlando_coord = [28.4115300, -81.5250400]
savannah_coord = [32.0084900, -81.2143700]
charlotte_coord = [35.1336100, -80.9636300]


EARTH_RADIUS = 6371.01  # Earth's radius, in km


class City:

    def __init__(self, name):
        self.name = name
        self.degree_coordinates = []
        self.rad_coordinates = []

    def add_degree_coordinates(self, city_coord):
        self.degree_coordinates.append(city_coord)

    def add_rad_coordinates(self, city_coord):
        for coordinate in city_coord:
            self.rad_coordinates.append(math.radians(coordinate))


def greatCircleDistance(city_1_coord, city_2_coord):
    distance = EARTH_RADIUS * math.acos(
        (math.sin(city_1_coord[0]) * math.sin(city_2_coord[0])) +
        (math.cos(city_1_coord[0]) * math.cos(city_2_coord[0])
         * math.cos(city_1_coord[1] - city_2_coord[1]))
    )

    return distance


def areaOfTriangle(city_1_coord, city_2_coord, city_3_coord):

    side_1 = greatCircleDistance(city_1_coord, city_2_coord)
    side_2 = greatCircleDistance(city_1_coord, city_3_coord)
    side_3 = greatCircleDistance(city_2_coord, city_3_coord)

    s = ((side_1 + side_2 + side_3) / 2)

    area = math.sqrt(
        s * (s - side_1) * (s - side_2) * (s - side_3)
    )

    return area


Atlanta = City('Atlanta')
Atlanta.add_rad_coordinates(atlanta_coord)

Orlando = City('Orlando')
Orlando.add_rad_coordinates(orlando_coord)

Savannah = City('Savannah')
Savannah.add_rad_coordinates(savannah_coord)

Charlotte = City('Charlotte')
Charlotte.add_rad_coordinates(charlotte_coord)


triangle_1 = areaOfTriangle(
    Atlanta.rad_coordinates,
    Orlando.rad_coordinates,
    Savannah.rad_coordinates
)

triangle_2 = areaOfTriangle(
    Atlanta.rad_coordinates,
    Savannah.rad_coordinates,
    Charlotte.rad_coordinates
)

total_area = triangle_1 + triangle_2

print(total_area)
