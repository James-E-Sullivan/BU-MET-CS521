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
secondsPerYear = 60 * 60 * 24 * 365

# Current US population
startingPopulation = 312032486

# The current year
startingYear = 2019

def project_Population(currentPopulation, currentYear):

    endYear = currentYear + 5

    annualBirths = secondsPerYear / 7
    annualDeaths = secondsPerYear / 13
    annualImmigrants = secondsPerYear / 45

    while currentYear < endYear:

        yearPop = currentPopulation + annualBirths - annualDeaths + annualImmigrants
        print(currentYear, 'Population:', int(yearPop))
        currentPopulation = yearPop
        currentYear += 1

project_Population(startingPopulation, startingYear)