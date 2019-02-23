"""
HW 6.9
(Conversions between feet and meters)
Write a module that contains the following two functions:

# Converts from feet to meters
def footToMeter(foot):

# Converts from meters to feet
def meterToFoot(meter):

The formulas for the conversions are:

foot = meter / 0.305
meter = 0.305 * foot

Write a test program that invokes these functions to display the following
tables:

Feet    Meters  |   Meters  Feet
1.0     0.305   |   20.0    66.574
2.0     0.610   |   25.0    81.967
...
9.0     2.745   |   60.0    196.721
10.0    3.050   |   65.0    213.115
"""


# Converts from feet to meters
def footToMeter(foot):
    meter = 0.305 * foot
    return meter


def meterToFoot(meter):
    foot = meter / 0.305
    return foot


# Prints table headers
print('Feet    Meters  |   Meters  Feet')

# Prints formatted table of foot<-->meter conversions
for i in range(1, 11):

    foot1 = i
    meter1 = footToMeter(foot1)
    print(format(foot1, "<7.1f"), format(meter1, "<8.3f"), end="|   ")

    meter2 = (i * 5) + 15
    foot2 = meterToFoot(meter2)
    print(format(meter2, "<7.1f"), format(foot2, ".3f"))
