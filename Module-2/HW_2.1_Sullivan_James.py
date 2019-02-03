'''
(Convert Celsius to Fahrenheit)
Write a program that reads a Celsius degree from the console and converts it
to Fahrenheit and displays the result. The formula for the conversion is as
follows:

fahrenheit = (9/5) * celsius + 32
'''

celsiusTemp = eval(input('Enter a degree in Celsius: '))

fahrenheitTemp = (9/5) * celsiusTemp + 32

print(celsiusTemp, 'Celsius is', fahrenheitTemp, 'Fahrenheit')
