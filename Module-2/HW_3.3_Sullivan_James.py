"""
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
"""


import math

# Adds city coordinates into a list structured [lat, long] for each city.
atlanta_coord = [33.7242700, -84.5785800]
orlando_coord = [28.4115300, -81.5250400]
savannah_coord = [32.0084900, -81.2143700]
charlotte_coord = [35.1336100, -80.9636300]


EARTH_RADIUS = 6371.01  # Earth's radius, in km


class City:
    """
    City class used to store and manipulate information about cities,
    and used to more easily reference the data.
    """

    def __init__(self, degree_coordinates):

        # New class objects must be instantiated with coordinates, in degrees.

        self.degree_coordinates = degree_coordinates

        # When a class is instantiated, coordinates are converted to
        # radians and stored in list self.rad_coordinates.
        self.rad_coordinates = []
        for coordinate in degree_coordinates:
            self.rad_coordinates.append(math.radians(coordinate))


def greatCircleDistance(city_1_coord, city_2_coord):
    """
    Function takes in lists of latitude and longitude coordinates
    for two cities. Coordinates must be in radians, not degrees.

    Distance between two cities calculated using the formula the
    Great Circle Distance Formula.

    Returns the distance between the two cities.
    """

    distance = EARTH_RADIUS * math.acos(
        (math.sin(city_1_coord[0]) * math.sin(city_2_coord[0])) +
        (math.cos(city_1_coord[0]) * math.cos(city_2_coord[0])
         * math.cos(city_1_coord[1] - city_2_coord[1]))
    )

    return distance


def areaOfTriangle(city_1_coord, city_2_coord, city_3_coord):
    """
    Function takes in lists of latitude and longitude coordinates
    for three cities. Coordinates must be in radians, not degrees.

    greatCircleDistance function used to get length of each side
    of a triangle.

    Returns the area of the triangle between the 3 cities.
    """

    side_1 = greatCircleDistance(city_1_coord, city_2_coord)
    side_2 = greatCircleDistance(city_1_coord, city_3_coord)
    side_3 = greatCircleDistance(city_2_coord, city_3_coord)

    s = ((side_1 + side_2 + side_3) / 2)

    area = math.sqrt(
        s * (s - side_1) * (s - side_2) * (s - side_3)
    )

    return area


# Instantiates City class objects for the four cities
# Adds name and coordinates, converted to radians.
Atlanta = City(atlanta_coord)
Orlando = City(orlando_coord)
Savannah = City(savannah_coord)
Charlotte = City(charlotte_coord)


# Computes area of 1st triangle
triangle_1 = areaOfTriangle(
    Atlanta.rad_coordinates,
    Orlando.rad_coordinates,
    Savannah.rad_coordinates
)

# Computes area of 2nd triangle
triangle_2 = areaOfTriangle(
    Atlanta.rad_coordinates,
    Savannah.rad_coordinates,
    Charlotte.rad_coordinates
)

# Adds areas of 2 triangles to find total area between the 4 cities
total_area = triangle_1 + triangle_2

print(total_area)
