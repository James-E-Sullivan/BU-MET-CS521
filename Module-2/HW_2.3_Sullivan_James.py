'''
(Convert feet into meters)
Write a program that reads a number in feet, converts it to meters,
and displays the result. One foot is 0.305 meters.
'''

imperialDistance = eval(input('Enter a value for feet: '))

metricDistance = imperialDistance * 0.305

print(imperialDistance, 'feet is', metricDistance, 'meters')
