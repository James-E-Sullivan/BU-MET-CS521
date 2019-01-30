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
SECONDS_PER_YEAR = 60 * 60 * 24 * 365

# Calculate annual births, deaths, and immigrants per year in US
# Rounds to nearest integer
annualBirths = SECONDS_PER_YEAR // 7
annualDeaths = SECONDS_PER_YEAR // 13
annualImmigrants = SECONDS_PER_YEAR // 45

# Assigns annual population change to a variable
# Based on the annual births, deaths, and immigrants
annualPopulationChange = annualBirths - annualDeaths + annualImmigrants

# Current US population
startingPopulation = 312032486

# The current year
startingYear = 2019

def project_Population(currentPopulation, currentYear):
    '''
    currentPopulation: The population at the start of the projection
    currentYear: The year at the start of the projection

    Function will output the projected population for 5 years, starting with
    currentYear + 1.
    '''

    endYear = currentYear + 5

    while currentYear < endYear:

        yearPop = currentPopulation + annualPopulationChange
        print((currentYear + 1), 'Population:', yearPop)
        currentPopulation = yearPop
        currentYear += 1


project_Population(startingPopulation, startingYear)
