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

# City coordinates, listed in latitude and longitude
atlanta_lat, atlanta_long = 33.7242700, -84.5785800
orlando_lat, orlando_long = 28.4115300, -81.5250400
savannah_lat, savannah_long = 32.0084900, -81.2143700
charlotte_lat, charlotte_long = 35.1336100, -80.9636300

# Adds city coordinates into a list structured [lat, long]
atlanta_coord = [atlanta_lat, atlanta_long]
orlando_coord = [orlando_lat, orlando_long]
savannah_coord = [savannah_lat, savannah_long]
charlotte_coord = [charlotte_lat, charlotte_long]

EARTH_RADIUS = 6371.01  # Earth's radius, in km

'''
distance_atlanta_orlando = EARTH_RADIUS * math.acos(
    (math.sin(atlanta_lat) * math.sin(orlando_lat)) +
    (math.cos(atlanta_lat) * math.cos(orlando_lat)
     * math.cos(atlanta_long - orlando_long))
)
'''

def greatCircleDistance(city_1_coord, city_2_coord):

    distance = EARTH_RADIUS * math.acos(
        (math.sin(city_1_coord[0]) * math.sin(city_2_coord[0])) +
        (math.cos(city_1_coord[0]) * math.cos(city_2_coord[0])
         * math.cos(city_1_coord[1] - city_2_coord[1]))
    )

    return distance

print(greatCircleDistance(atlanta_coord, orlando_coord))


