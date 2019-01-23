'''
(Population Projection) The US Census Bureau projects population based on the
following assumptions:

One birth every 7 seconds
One death every 13 seconds
One new immigrant every 45 seconds

Write a program to display the population for each of the next five years.
Assume the current population is 312032486 and one year has 365 days.
Hint: in Python, you can use integer division operator // to perform division.
The result is an integer. For example, 5 // 4 is 1 (not 1.25) and 10 // 4 is 2.
'''

# Number of seconds in a 365-day year
seconds_per_year = 60 * 60 * 24 * 365

# Current US population
starting_pop = 312032486

# The current year
starting_year = 2019

def project_Population():

    current_pop = starting_pop
    current_year = starting_year
    years = 5
    i = 0

    annual_births = seconds_per_year / 7
    annual_deaths = seconds_per_year / 13
    annual_immigrants = seconds_per_year / 45

    while i < years:

        year_pop = current_pop + annual_births - annual_deaths + annual_immigrants
        print(str(current_year) + ' Population: ' + str(int(year_pop)))
        current_pop = year_pop
        current_year += 1
        i += 1

project_Population()